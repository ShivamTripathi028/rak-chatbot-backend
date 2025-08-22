# main.py
import os
import logging
from contextlib import asynccontextmanager
from typing import Dict

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
from langchain.schema import BaseRetriever

# Load environment variables from .env file at the start
load_dotenv()

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Environment Variable for Production CORS ---
# This allows us to securely specify which frontend URL can connect to our API.
# It defaults to a common local dev port if not set.
FRONTEND_URL = "https://talk-to-rak.netlify.app"

# --- Pydantic Models for API validation ---
class ChatRequest(BaseModel):
    query: str
    category: str

# This dictionary will hold our loaded models and retrievers
ml_models: Dict[str, any] = {}

# --- FastAPI Lifespan Manager (loads models on startup) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP CODE ---
    logging.info("--- Server starting up: Loading all models... ---")
    
    ml_models["embedding_model"] = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    logging.info("Embedding model loaded.")

    ml_models["reranker_model"] = HuggingFaceCrossEncoder(
        model_name=config.BEST_RERANKER_MODEL, model_kwargs={'device': 'cpu'}
    )
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
    
    # --- SHUTDOWN CODE ---
    ml_models.clear()
    logging.info("--- Server shutting down: Models cleared. ---")


# --- Initialize FastAPI App ---
app = FastAPI(lifespan=lifespan)

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:8080", "http://localhost:8888"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"status": "RAK Chatbot API is running."}

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    query = request.query
    category = request.category

    retriever = ml_models.get("retrievers", {}).get(category)
    llm = ml_models.get("llm")

    if not retriever or not llm:
        return {"error": f"Model or retriever for category '{category}' not available."}

    retrieved_docs = retriever.invoke(query)

    async def stream_llm_response():
        system_prompt = """You are a helpful, friendly, and knowledgeable RAKwireless product support specialist.
Your primary goal is to accurately answer user questions based ONLY on the information found in the context documents provided below. When responding:
1. Carefully read the user's question and all provided context documents.
2. **DO NOT** mention the context or documents in your answer. Simply provide the information as if you know it.
3. If the context does **NOT** contain information to answer the question, politely state that you couldn't find the specific details in the available documentation."""
        
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        human_prompt = f"""Context Documents:\n------------------\n{context}\n------------------\nUser's Question: {query}\nHelpful and Accurate Answer:"""
        
        messages = [SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)]
        
        for chunk in llm.stream(messages):
            yield chunk.content

    return StreamingResponse(stream_llm_response(), media_type="text/event-stream")