import os
import logging
import asyncio
from datetime import datetime
from contextlib import asynccontextmanager
from typing import Dict, List, Literal, Set
import re

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from dotenv import load_dotenv
import torch 

import config
from utils import get_product_categories

from langchain_huggingface import HuggingFaceEmbeddings
try:
    from langchain_huggingface import HuggingFaceCrossEncoder
except ImportError:
    from langchain_community.cross_encoders import HuggingFaceCrossEncoder

from langchain_chroma import Chroma
# Explicit imports to prevent Pylance errors
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.cross_encoder import CrossEncoderReranker
from langchain_core.documents import Document
from openai import AsyncOpenAI

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ALLOWED_ORIGINS = ["*"] 

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
    
    if torch.cuda.is_available(): device_type = "cuda"
    elif torch.backends.mps.is_available(): device_type = "mps"
    else: device_type = "cpu"
    logging.info(f"Using Device: {device_type}")

    ml_models["embedding_model"] = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME, 
        model_kwargs={'device': device_type}, 
        encode_kwargs={'normalize_embeddings': True}
    )
    
    logging.info(f"Loading Reranker: {config.BEST_RERANKER_MODEL}")
    ml_models["reranker_model"] = HuggingFaceCrossEncoder(
        model_name=config.BEST_RERANKER_MODEL, 
        model_kwargs={'device': "cpu"} 
    )
    
    ml_models["openai_client"] = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    categories = get_product_categories(config.DATA_DIRECTORY)
    retrievers = {}
    embedding_func = ml_models["embedding_model"]
    reranker = ml_models["reranker_model"]
    
    for category_name in categories:
        db_name = config.GLOBAL_DB_NAME if category_name == "All Categories (Global DB)" else f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
        db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
        
        if not db_path.exists(): continue
            
        vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_func)
        
        base_retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": config.BEST_INITIAL_K, "fetch_k": 50, "lambda_mult": 0.25} 
        )
        
        compressor = CrossEncoderReranker(model=reranker, top_n=config.BEST_FINAL_K)
        final_retriever = ContextualCompressionRetriever(
            base_compressor=compressor, 
            base_retriever=base_retriever
        )
        
        retrievers[category_name] = final_retriever
        
    ml_models["retrievers"] = retrievers
    logging.info("--- Models loaded ---")
    yield
    ml_models.clear()

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root(): return {"status": "RAK Chatbot API is running."}

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
    normalized_path = doc_path.replace("-", "/").replace("_", "/")
    path_components = set(p.lower() for p in normalized_path.split('/'))
    eol_products_lower = set(p.lower() for p in config.EOL_PRODUCTS)
    return not path_components.isdisjoint(eol_products_lower)

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    start_time = datetime.now()
    query = request.query
    retriever = ml_models.get("retrievers", {}).get(request.category)
    client: AsyncOpenAI = ml_models.get("openai_client")

    if not retriever or not client: return {"error": "Model not available."}

    loop = asyncio.get_running_loop()
    retrieved_docs = await loop.run_in_executor(None, retriever.invoke, query)

    mentioned_eol_products = get_eol_products_from_query(query) 
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
        context_text = "\n\n".join([f"[Source: {d.metadata.get('title', 'Doc')}]\n{d.page_content}" for d in final_docs])
        
        system_prompt = "You are a RAKwireless expert support agent. Answer based ONLY on the context."
        
        if mentioned_eol_products:
             system_prompt += f"\nWARNING: The user asked about EOL products: {', '.join(mentioned_eol_products)}. Warn them first."
        elif context_is_all_eol:
             system_prompt += "\nWARNING: All retrieved products are End-of-Life. Warn the user."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
        ]
        
        try:
            temp = 1.0 if "nano" in config.OPENAI_MODEL_NAME.lower() else 0.1
            stream = await client.chat.completions.create(
                model=config.OPENAI_MODEL_NAME,
                messages=messages,
                temperature=temp,
                stream=True 
            )
            yield " " 
            async for chunk in stream:
                content = chunk.choices[0].delta.content
                if content: yield content
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(stream_llm_response(), media_type="text/plain")