# main.py
import os
import logging
import asyncio
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
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain_core.documents import Document

# --- OPTIMIZED CPU RERANKER (FlashRank) ---
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank

# --- OpenAI Raw Client ---
from openai import AsyncOpenAI

# --- Setup ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Dynamic CORS ---
allowed_origins_env = os.getenv("ALLOWED_ORIGINS")
if allowed_origins_env:
    ALLOWED_ORIGINS = [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]
else:
    ALLOWED_ORIGINS = ["http://localhost:8080", "http://localhost:5173", "https://rak-knowledge-hub.rak-internal.net"]

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

    # 2. Load Embedding Model
    logging.info(f"Loading Embedding Model: {config.EMBEDDING_MODEL_NAME}")
    ml_models["embedding_model"] = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME, 
        model_kwargs={'device': device_type}, 
        encode_kwargs={'normalize_embeddings': True}
    )
    
    # 3. Load Optimized Reranker (FlashRank)
    logging.info("Loading Optimized CPU Reranker (FlashRank)...")
    
    # --- FIX: Removed 'cache_dir' as it causes Pydantic validation error ---
    ml_models["reranker_model"] = FlashrankRerank(
        model="ms-marco-MiniLM-L-12-v2", 
        top_n=config.BEST_FINAL_K
    )
    
    # 4. Load OpenAI Client
    api_key = os.getenv("OPENAI_API_KEY")
    ml_models["openai_client"] = AsyncOpenAI(api_key=api_key)
    
    logging.info(f"AsyncOpenAI Client initialized for model: {config.OPENAI_MODEL_NAME}")
    
    # 5. Load Retrievers
    categories = get_product_categories(config.DATA_DIRECTORY)
    retrievers = {}
    embedding_func = ml_models["embedding_model"]
    reranker = ml_models["reranker_model"]
    
    logging.info("Building retrievers for categories...")
    
    for category_name in categories:
        db_name = config.GLOBAL_DB_NAME if category_name == "All Categories (Global DB)" else f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
        db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
        
        if not db_path.exists():
            continue
            
        vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_func)
        
        # Base Retriever (MMR for diversity)
        base_retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": config.BEST_INITIAL_K, 
                "fetch_k": 60,
                "lambda_mult": 0.25
            } 
        )
        
        # Final Retriever (FlashRank for precision)
        final_retriever = ContextualCompressionRetriever(
            base_compressor=reranker, 
            base_retriever=base_retriever
        )
        
        retrievers[category_name] = final_retriever
        
    logging.info(f"Retrievers loaded for {len(retrievers)} categories.")
    ml_models["retrievers"] = retrievers
    logging.info("--- All models loaded and optimized ---")
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
    """
    Checks if a document belongs to an EOL product by analyzing its path.
    Handles paths like 'WisDuo/RAK4270-Module/...' by treating hyphens as separators.
    """
    doc_path = doc.metadata.get("relative_path", "")
    if not doc_path: return False
    
    # Normalize path: replace hyphens/underscores with slashes to tokenize effectively
    # e.g., "RAK4270-Module" -> "RAK4270/Module"
    normalized_path = doc_path.replace("-", "/").replace("_", "/")
    
    path_components = set(p.lower() for p in normalized_path.split('/'))
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
    client: AsyncOpenAI = ml_models.get("openai_client")

    if not retriever or not client:
        return {"error": "Model not available."}

    # --- STEP 2A: Contextual Query Rewriting ---
    final_search_query = query
    previous_messages = request.chat_history[:-1]
    has_prior_user_context = any(msg.role == 'user' for msg in previous_messages)

    if has_prior_user_context:
        logging.info("PHASE 2A: Rewriting query based on history...")
        history_str = ""
        for msg in previous_messages:
            role = "User" if msg.role == "user" else "Assistant"
            history_str += f"{role}: {msg.content}\n"
            
        rewrite_messages = [
            {"role": "system", "content": "Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question."},
            {"role": "user", "content": f"Chat History:\n{history_str}\nFollow Up Input: {query}\nStandalone question:"}
        ]
        
        try:
            rewrite_response = await client.chat.completions.create(
                model=config.OPENAI_MODEL_NAME, 
                messages=rewrite_messages,
                temperature=1 
            )
            final_search_query = rewrite_response.choices[0].message.content.strip()
            logging.info(f"PHASE 2A: Rewritten Query: '{final_search_query}'")
        except Exception as e:
            logging.error(f"Rewriting failed: {e}. Using original.")
    else:
        logging.info("PHASE 2A: First user question detected. Skipping rewrite.")

    # --- STEP 2B: Retrieval ---
    logging.info(f"PHASE 2B: Searching DB with: '{final_search_query}'")
    retrieval_start = datetime.now()
    
    loop = asyncio.get_running_loop()
    
    # Run retrieval in thread pool
    retrieved_docs = await loop.run_in_executor(None, retriever.invoke, final_search_query)
    
    logging.info(f"PHASE 2B: Found {len(retrieved_docs)} docs. Took: {(datetime.now() - retrieval_start).total_seconds():.2f}s.")

    # --- DEBUGGING: Print INITIAL Sources ---
    logging.info("--- RETRIEVED SOURCES (RAW from DB) ---")
    for i, doc in enumerate(retrieved_docs):
        path = doc.metadata.get('relative_path', 'Unknown Source')
        logging.info(f"  [Raw {i+1}]: {path}")
    logging.info("---------------------------------------")

    # --- EOL & Suggestion Logic ---
    mentioned_eol_products = get_eol_products_from_query(final_search_query) 
    is_suggestion_query = not mentioned_eol_products
    context_is_all_eol = False
    
    if is_suggestion_query:
        # FILTER: Remove EOL docs unless they are the only ones left
        active_docs = [doc for doc in retrieved_docs if not is_document_eol(doc)]
        
        if not active_docs and retrieved_docs:
            final_docs = retrieved_docs
            context_is_all_eol = True
        else:
            final_docs = active_docs
    else:
        final_docs = retrieved_docs

    # --- DEBUGGING: Print FINAL Context Docs ---
    # This block verifies what actually gets sent to the LLM after EOL filtering
    logging.info(f"--- FINAL CONTEXT DOCS PASSED TO LLM ({len(final_docs)}) ---")
    for i, doc in enumerate(final_docs):
        path = doc.metadata.get('relative_path', 'Unknown Source')
        logging.info(f"  [Context {i+1}]: {path}")
    logging.info("-------------------------------------------------------")

    async def stream_llm_response():
        # --- System Prompt ---
        system_prompt_base = """You are a helpful, friendly, and knowledgeable RAKwireless product support specialist.

CORE RESPONSIBILITIES:
1. Answer the user's question **directly and authoritatively** using the provided context. **Do not** use phrases like "Based on the documents," "It appears," or "I only have information about."
2. Provide the answer without hedging. Only state that information is missing if the context is completely irrelevant or insufficient to answer the specific question.
3. Use Markdown formatting (bold key terms, bullet points) to make answers readable.

FORMATTING RULES:
- **Technical Specs:** If the user asks to compare technical specifications, use a Markdown Table.
- **Scenarios/Advice:** If the user asks for "which is better for X" or "use cases", prefer using **bullet points** or **text explanations**.
- **Check History:** If a comparison table for these products was ALREADY provided, **DO NOT** generate the table again.
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
        
        messages = [{"role": "system", "content": system_prompt}]
        
        if request.chat_history:
            for msg in request.chat_history[:-1]:
                messages.append({"role": msg.role, "content": msg.content})
        
        messages.append({"role": "user", "content": human_prompt})
        
        logging.info(f"PHASE 3: Streaming LLM response via Raw Client...")
        llm_start_time = datetime.now()

        try:
            stream = await client.chat.completions.create(
                model=config.OPENAI_MODEL_NAME,
                messages=messages,
                temperature=1.0 if "nano" in config.OPENAI_MODEL_NAME.lower() else 0.0,
                stream=True 
            )

            # Yield empty space to flush headers
            yield " " 

            async for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
                    
        except Exception as e:
            logging.error(f"Error during OpenAI stream: {e}")
            yield f"Error: {str(e)}"
        
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