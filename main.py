# main.py
import os
import logging
from datetime import datetime
from contextlib import asynccontextmanager
from typing import Dict, List, Literal, Set
import re # Import the regular expression module

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from dotenv import load_dotenv

# --- Local Imports from your project ---
import config
from custom_llm import OpenRouterChatModel
from utils import get_product_categories

# --- LangChain Components ---
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.documents import Document
from langchain.schema import BaseRetriever

# --- (Setup, models, lifespan, CORS, etc. remain unchanged) ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")

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
    # This is unchanged
    logging.info("--- Server starting up: Loading all models... ---")
    ml_models["embedding_model"] = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME, model_kwargs={'device': 'cpu'}, encode_kwargs={'normalize_embeddings': True})
    logging.info("Embedding model loaded.")
    ml_models["reranker_model"] = HuggingFaceCrossEncoder(model_name=config.BEST_RERANKER_MODEL, model_kwargs={'device': 'cpu'})
    logging.info("Reranker model loaded.")
    ml_models["llm"] = OpenRouterChatModel(model_name=config.OPENROUTER_MODEL_NAME)
    logging.info("LLM loaded.")
    categories = get_product_categories(config.DATA_DIRECTORY)
    retrievers = {}
    embedding_func = ml_models["embedding_model"]
    reranker = ml_models["reranker_model"]
    for category_name in categories:
        db_name = config.GLOBAL_DB_NAME if category_name == "All Categories (Global DB)" else f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
        db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
        if not db_path.exists():
            logging.warning(f"Database for category '{category_name}' not found at {db_path}. Skipping.")
            continue
        vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_func)
        base_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": config.BEST_INITIAL_K})
        compressor = CrossEncoderReranker(model=reranker, top_n=config.BEST_FINAL_K)
        final_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever)
        retrievers[category_name] = final_retriever
        logging.info(f"Retriever for '{category_name}' created successfully.")
    ml_models["retrievers"] = retrievers
    logging.info("--- All models and retrievers loaded. Server is ready. ---")
    yield
    ml_models.clear()
    logging.info("--- Server shutting down: Models cleared. ---")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:8080", "http://localhost:5173", "http://localhost:8888", "https://rak-knowledge-hub.vercel.app/"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "RAK Chatbot API is running."}

# --- CORRECTED HELPER FUNCTIONS ---
def get_eol_products_from_query(query: str) -> List[str]:
    """
    Finds EOL product names in the query using exact, whole-word matching.
    """
    mentioned_eol_products = []
    for product in config.EOL_PRODUCTS:
        # Use regex with word boundaries (\b) for a precise match
        # re.escape handles product names with special characters
        pattern = r'\b' + re.escape(product) + r'\b'
        if re.search(pattern, query, re.IGNORECASE):
            mentioned_eol_products.append(product)
    return mentioned_eol_products

def is_document_eol(doc: Document) -> bool:
    """
    Checks if a document's path contains an exact EOL product name component.
    """
    doc_path = doc.metadata.get("relative_path", "")
    if not doc_path:
        return False
    
    # Split the path into parts (e.g., ['WisGate', 'RAK7289-V2', 'Overview', 'README.md'])
    path_components = set(p.lower() for p in doc_path.split('/'))
    eol_products_lower = set(p.lower() for p in config.EOL_PRODUCTS)
    
    # Check for any intersection between the two sets
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
    # This entire function is now correct and does not need to be changed.
    # The fix is in the helper functions it calls.
    start_time = datetime.now()
    logging.info(f"PHASE 1: Received new user query at {start_time.isoformat()}. Query: '{request.query}'")

    query = request.query
    retriever = ml_models.get("retrievers", {}).get(request.category)
    llm = ml_models.get("llm")

    if not retriever or not llm:
        return {"error": f"Model or retriever for category '{request.category}' not available."}

    logging.info(f"PHASE 2: Starting data extraction from knowledge base...")
    retrieval_start_time = datetime.now()
    retrieved_docs = retriever.invoke(query)
    retrieval_end_time = datetime.now()
    logging.info(f"PHASE 2: Data extraction complete. Took: {(retrieval_end_time - retrieval_start_time).total_seconds():.2f}s. Found {len(retrieved_docs)} documents.")

    logging.info("--- DIAGNOSTIC: Inspecting retrieved document metadata and FULL content ---")
    for i, doc in enumerate(retrieved_docs):
        path = doc.metadata.get('relative_path', 'N/A')
        is_eol = is_document_eol(doc)
        log_message = (
            f"\n----- Document [{i+1}/{len(retrieved_docs)}] -----\n"
            f"  Path    : {path}\n"
            f"  Is EOL? : {is_eol}\n"
            f"  Content :\n{doc.page_content}\n"
            f"----- End Document [{i+1}/{len(retrieved_docs)}] -----"
        )
        logging.info(log_message)
    logging.info("--- END DIAGNOSTIC ---")
    
    mentioned_eol_products = get_eol_products_from_query(query)
    is_suggestion_query = not mentioned_eol_products
    context_is_all_eol = False
    
    if is_suggestion_query:
        active_docs = [doc for doc in retrieved_docs if not is_document_eol(doc)]
        if not active_docs and retrieved_docs:
            logging.warning("No active products found in retrieved docs. Falling back to EOL suggestions.")
            final_docs = retrieved_docs
            context_is_all_eol = True
        else:
            final_docs = active_docs
    else:
        final_docs = retrieved_docs

    async def stream_llm_response():
        try:
            system_prompt_base = """You are a helpful, friendly, and knowledgeable RAKwireless product support specialist. Your primary goal is to accurately answer user questions based ONLY on the information found in the context documents provided below. If the context does not contain information to answer the question, politely state that you couldn't find the specific details in the available documentation."""
            
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
            
            messages = [SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)]
            
            logging.info(f"PHASE 3: Passing data to LLM and starting response stream...")
            llm_start_time = datetime.now()

            for chunk in llm.stream(messages):
                yield chunk.content
            
            llm_end_time = datetime.now()
            logging.info(f"PHASE 3: LLM stream generation complete. Took: {(llm_end_time - llm_start_time).total_seconds():.2f}s.")

        finally:
            end_time = datetime.now()
            logging.info(f"PHASE 4: Full response streamed to UI. Total request time: {(end_time - start_time).total_seconds():.2f}s.")

    return StreamingResponse(stream_llm_response(), media_type="text/event-stream")