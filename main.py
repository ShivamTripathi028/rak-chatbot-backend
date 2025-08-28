 # main.py
import os
import logging
from contextlib import asynccontextmanager
from typing import Dict, List, Literal

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



# --- (Load env, logging, constants, and Pydantic models - No changes here) ---
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

# --- (lifespan function for model loading is unchanged) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This entire function is unchanged from the last working version
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
# --- (CORS and root endpoint are unchanged) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:8080", "http://localhost:5173", "http://localhost:8888"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"status": "RAK Chatbot API is running."}

def get_eol_products_from_query(query: str) -> List[str]:
    """
    Identifies which specific EOL products are mentioned in the user's query.
    Returns a list of the matched EOL product names.
    """
    query_lower = query.lower()
    mentioned_eol_products = [
        p for p in config.EOL_PRODUCTS
        if f" {p.lower()} " in f" {query_lower} " or \
           query_lower.startswith(f"{p.lower()} ") or \
           query_lower.endswith(f" {p.lower()}") or \
           query_lower == p.lower()
    ]
    return mentioned_eol_products

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    query = request.query
    category = request.category
    chat_history = request.chat_history
    retriever = ml_models.get("retrievers", {}).get(category)
    llm = ml_models.get("llm")

    if not retriever or not llm:
        return {"error": f"Model or retriever for category '{category}' not available."}

    retrieved_docs = retriever.invoke(query)

    async def stream_llm_response():
        history_string = "\n".join([f"{msg.role}: {msg.content}" for msg in chat_history])
        
        mentioned_eol_products = get_eol_products_from_query(query)
        
        system_prompt_base = """You are a helpful, friendly, and knowledgeable RAKwireless product support specialist.
Your primary goal is to accurately answer user questions based ONLY on the information found in the context documents provided below. Use the chat history to understand follow-up questions. When responding:
1. Carefully read the user's question, chat history, and all provided context documents.
2. **DO NOT** mention the context or documents in your answer. Simply provide the information as if you know it.
3. If the context does **NOT** contain information to answer the question, politely state that you couldn't find the specific details in the available documentation.
Formatting Guidelines:
- Use **bold** to emphasize key terms, product names, or important details.
- Use *italics* for minor emphasis.
- Use bullet points or numbered lists when explaining multiple steps, features, or comparisons.
- Use short paragraphs for readability.
- If explaining a process, present it in a **step-by-step format**.
- Always keep a clear, professional, and user-friendly tone."""

        if mentioned_eol_products:
            if len(mentioned_eol_products) == 1:
                product_list_str = f"the {mentioned_eol_products[0]}"
                verb = "is"
            else:
                product_list_str = f"the {', '.join(mentioned_eol_products[:-1])} and {mentioned_eol_products[-1]}"
                verb = "are"
            eol_instruction = f"IMPORTANT INSTRUCTION: The product(s) {product_list_str} {verb} End-of-Life (EOL). You MUST start your response with the exact phrase '**Please be aware that {product_list_str} {verb} an End-of-Life (EOL) product.**' before providing the detailed answer."
            system_prompt = f"{eol_instruction}\n\n{system_prompt_base}"
        else:
            system_prompt = system_prompt_base
        
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        human_prompt = f"""Chat History:\n------------------\n{history_string}\n------------------\nContext Documents:\n------------------\n{context}\n------------------\nUser's Question: {query}\nHelpful and Accurate Answer:"""
        
        messages = [SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)]
        
        for chunk in llm.stream(messages):
            yield chunk.content

    return StreamingResponse(stream_llm_response(), media_type="text/event-stream")