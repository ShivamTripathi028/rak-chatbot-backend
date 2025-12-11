# main.py
import os
import logging
from datetime import datetime
from contextlib import asynccontextmanager
from typing import Dict, List, Literal, Set
import re

# --- FIX FOR TOKENIZERS WARNING ---
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from dotenv import load_dotenv
import torch 

# --- Local Imports ---
import config
from utils import get_product_categories

# --- LangChain Components ---
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

try:
    from langchain_huggingface import HuggingFaceCrossEncoder
except ImportError:
    from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from langchain_chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain.retrievers.multi_query import MultiQueryRetriever

# --- LangChain Core ---
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.documents import Document
from langchain_core.caches import BaseCache
from langchain_core.callbacks import Callbacks
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Fix Pydantic/LangChain integration issue
ChatOpenAI.model_rebuild()

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Dynamic CORS ---
allowed_origins_env = os.getenv("ALLOWED_ORIGINS")
if allowed_origins_env:
    ALLOWED_ORIGINS = [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]
    logging.info(f"CORS: Loaded allowed origins from env: {ALLOWED_ORIGINS}")
else:
    ALLOWED_ORIGINS = ["http://localhost:8080", "http://localhost:5173", "https://rak-knowledge-hub.vercel.app"]
    logging.warning(f"CORS: 'ALLOWED_ORIGINS' env var not set. Using defaults: {ALLOWED_ORIGINS}")

class ChatMessage(BaseModel):
    role: Literal['user', 'assistant']
    content: str

class ChatRequest(BaseModel):
    query: str
    category: str
    chat_history: List[ChatMessage]

ml_models: Dict[str, any] = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("--- Server starting up: Loading all models... ---")
    
    # 1. Hardware Detection
    if torch.cuda.is_available():
        device_type = "cuda"
        logging.info("Hardware acceleration: NVIDIA CUDA detected.")
    elif torch.backends.mps.is_available():
        device_type = "mps"
        logging.info("Hardware acceleration: Apple Metal (MPS) detected.")
    else:
        device_type = "cpu"
        logging.info("Hardware acceleration: None. Using CPU.")

    # 2. Load Embedding & Reranker
    ml_models["embedding_model"] = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME, 
        model_kwargs={'device': device_type}, 
        encode_kwargs={'normalize_embeddings': True}
    )
    
    ml_models["reranker_model"] = HuggingFaceCrossEncoder(
        model_name=config.BEST_RERANKER_MODEL, 
        model_kwargs={'device': 'cpu'} 
    )
    
    # 3. Load Main LLM
    model_name = config.OPENAI_MODEL_NAME
    # Reasoning models (gpt-5-nano, o1) require temperature=1
    temp_val = 1 if ("nano" in model_name or "gpt-5" in model_name or "o1" in model_name) else 0.1
    ml_models["llm"] = ChatOpenAI(model=model_name, temperature=temp_val)
    
    logging.info(f"LLM loaded: {model_name}")
    
    # 4. Load Retrievers
    categories = get_product_categories(config.DATA_DIRECTORY)
    retrievers = {}
    embedding_func = ml_models["embedding_model"]
    reranker = ml_models["reranker_model"]
    # Use the main LLM for query generation
    query_gen_llm = ml_models["llm"] 
    
    for category_name in categories:
        db_name = config.GLOBAL_DB_NAME if category_name == "All Categories (Global DB)" else f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
        db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
        
        if not db_path.exists():
            continue
            
        vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_func)
        
        # A. MMR Retrieval (Diversity Focus)
        base_retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": config.BEST_INITIAL_K, # e.g., 30
                "fetch_k": 50,             # Look at top 200 candidates
                "lambda_mult": 0.25         # High diversity to catch comparison docs
            } 
        )
        
        # B. Multi-Query Expansion
        multi_query_retriever = MultiQueryRetriever.from_llm(
            retriever=base_retriever,
            llm=query_gen_llm,
            include_original=True
        )

        # C. Re-ranking
        compressor = CrossEncoderReranker(model=reranker, top_n=config.BEST_FINAL_K)
        final_retriever = ContextualCompressionRetriever(
            base_compressor=compressor, 
            base_retriever=multi_query_retriever
        )
        
        retrievers[category_name] = final_retriever
        logging.info(f"Retriever constructed for '{category_name}'.")
        
    ml_models["retrievers"] = retrievers
    logging.info("--- All models loaded ---")
    yield
    ml_models.clear()

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root(): return {"status": "RAK Chatbot API is running."}

# --- Helper Functions ---
def get_eol_products_from_query(query: str) -> List[str]:
    mentioned_eol_products = []
    for product in config.EOL_PRODUCTS:
        pattern = r'\b' + re.escape(product) + r'\b'
        if re.search(pattern, query, re.IGNORECASE):
            mentioned_eol_products.append(product)
    return mentioned_eol_products

def is_document_eol(doc: Document) -> bool:
    doc_path = doc.metadata.get("relative_path", "")
    if not doc_path: return False
    path_components = set(p.lower() for p in doc_path.split('/'))
    eol_products_lower = set(p.lower() for p in config.EOL_PRODUCTS)
    return not path_components.isdisjoint(eol_products_lower)

def extract_product_names_from_docs(docs: List[Document]) -> Set[str]:
    product_names = set()
    for doc in docs:
        path = doc.metadata.get("relative_path", "")
        parts = path.split('/')
        if len(parts) > 2:
            product_name = parts[-2]
            if "RAK" in product_name or "Wis" in product_name:
                product_names.add(product_name)
    return product_names

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    start_time = datetime.now()
    logging.info(f"PHASE 1: Query: '{request.query}'")

    query = request.query
    retriever = ml_models.get("retrievers", {}).get(request.category)
    llm = ml_models.get("llm")

    if not retriever or not llm:
        return {"error": "Model not available."}

    # --- STEP 2A: Contextual Query Rewriting ---
    final_search_query = query
    
    if request.chat_history:
        logging.info("PHASE 2A: Rewriting query based on history...")
        history_str = ""
        # Convert history to string, skipping the very last user message (which is current 'query')
        for msg in request.chat_history[:-1]:
            role = "User" if msg.role == "user" else "Assistant"
            history_str += f"{role}: {msg.content}\n"
            
        if history_str:
            rewrite_prompt = ChatPromptTemplate.from_template(
                """Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question.
                Chat History:
                {history}
                Follow Up Input: {question}
                Standalone question:"""
            )
            # Use the main LLM for rewriting now
            rewriter_chain = rewrite_prompt | llm | StrOutputParser()
            try:
                final_search_query = rewriter_chain.invoke({"history": history_str, "question": query})
                logging.info(f"PHASE 2A: Rewritten Query: '{final_search_query}'")
            except Exception as e:
                logging.error(f"Rewriting failed: {e}. Using original.")

    # --- STEP 2B: Retrieval (Using Rewritten Query) ---
    logging.info(f"PHASE 2B: Searching DB with: '{final_search_query}'")
    retrieval_start = datetime.now()
    retrieved_docs = retriever.invoke(final_search_query) 
    logging.info(f"PHASE 2B: Found {len(retrieved_docs)} docs. Took: {(datetime.now() - retrieval_start).total_seconds():.2f}s.")

    # --- DIAGNOSTIC: Log Docs ---
    for i, doc in enumerate(retrieved_docs):
        path = doc.metadata.get('relative_path', 'N/A')
        logging.info(f"Doc [{i+1}]: {path}")

    # --- EOL & Suggestion Logic ---
    mentioned_eol_products = get_eol_products_from_query(final_search_query) # Check against rewritten query
    is_suggestion_query = not mentioned_eol_products
    context_is_all_eol = False
    
    if is_suggestion_query:
        active_docs = [doc for doc in retrieved_docs if not is_document_eol(doc)]
        if not active_docs and retrieved_docs:
            final_docs = retrieved_docs
            context_is_all_eol = True
        else:
            final_docs = active_docs
    else:
        final_docs = retrieved_docs

    async def stream_llm_response():
        # --- System Prompt ---
        system_prompt_base = """You are a helpful, friendly, and knowledgeable RAKwireless product support specialist.

CORE RESPONSIBILITIES:
1. Answer based ONLY on the provided context.
2. If the context is missing info, politely admit it.
3. Use Markdown formatting to make answers readable (bold key terms, use bullet points).

FORMATTING RULES:
- If the user asks for a COMPARISON between two or more products, you MUST format the result as a Markdown Table.
- Example Table structure: | Feature | Product A | Product B |
"""
        system_prompt = system_prompt_base

        if mentioned_eol_products:
            product_list_str = f"the {', '.join(mentioned_eol_products)}"
            verb = "is" if len(mentioned_eol_products) == 1 else "are"
            eol_instruction = f"IMPORTANT: You MUST start your response with the exact phrase '**Please be aware that {product_list_str} {verb} an End-of-Life (EOL) product.**' before providing the detailed answer from the context."
            system_prompt = f"{eol_instruction}\n\n{system_prompt_base}"
        elif context_is_all_eol:
            eol_instruction = "IMPORTANT: You MUST start your response with the exact phrase '**Please note, the most relevant options I found are End-of-Life (EOL) products, which are no longer recommended for new designs.**' before providing the suggestion from the context."
            system_prompt = f"{eol_instruction}\n\n{system_prompt_base}"
        elif is_suggestion_query and final_docs:
            allowed_products = extract_product_names_from_docs(final_docs)
            if allowed_products:
                allowed_products_str = ", ".join(sorted(list(allowed_products)))
                suggestion_instruction = f"CRITICAL RULE: The user wants a suggestion. Base your answer ONLY on the context provided. You can only recommend products from this list: **{allowed_products_str}**. Do not mention any other RAK product names."
                system_prompt = f"{suggestion_instruction}\n\n{system_prompt_base}"

        context = "\n\n".join([doc.page_content for doc in final_docs])
        human_prompt = f"Context Documents:\n------------------\n{context}\n------------------\nUser's Question: {query}\nHelpful and Accurate Answer:"
        
        # --- HISTORY INJECTION ---
        messages = [SystemMessage(content=system_prompt)]
        
        if request.chat_history:
            for msg in request.chat_history[:-1]:
                if msg.role == 'user':
                    messages.append(HumanMessage(content=msg.content))
                elif msg.role == 'assistant':
                    messages.append(AIMessage(content=msg.content))
        
        messages.append(HumanMessage(content=human_prompt))
        
        logging.info(f"PHASE 3: Streaming LLM response...")
        llm_start_time = datetime.now()

        for chunk in llm.stream(messages):
            if chunk.content:
                yield chunk.content
        
        logging.info(f"PHASE 3: Stream complete. Took: {(datetime.now() - llm_start_time).total_seconds():.2f}s.")
        logging.info(f"PHASE 4: Done. Total time: {(datetime.now() - start_time).total_seconds():.2f}s.")

    return StreamingResponse(
        stream_llm_response(), 
        media_type="text/plain", 
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Content-Type-Options": "nosniff"
        }
    )