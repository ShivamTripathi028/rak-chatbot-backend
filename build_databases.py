# build_databases.py
import os
import shutil
import time 
import logging
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

# build_databases.py

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading required NLTK resource 'punkt'...")
    nltk.download('punkt')

# ...

# --- Local Imports ---
import config
from utils import load_and_parse_single_readme_file_with_metadata

# --- LangChain Components ---
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_single_category_for_db(category_folder_path_str: str, root_dir_str: str):
    """Processes all README.md files in a single category folder."""
    category_folder_path = Path(category_folder_path_str)
    category_name = category_folder_path.name
    logging.info(f"  [Worker] Processing category: {category_name}")
    category_documents = []
    readme_files_in_category = list(category_folder_path.rglob("README.md"))
    for readme_filepath in readme_files_in_category:
        if ".DS_Store" in str(readme_filepath) or "._" in readme_filepath.name:
            continue
        docs = load_and_parse_single_readme_file_with_metadata(
            str(readme_filepath), root_dir_str, category_name
        )
        category_documents.extend(docs)
    logging.info(f"  [Worker] Finished category: {category_name}. Found {len(category_documents)} document sections.")
    return category_name, category_documents

def chunk_documents_for_db(documents: list[Document], category_name_for_log: str):
    """Splits a list of documents into smaller chunks."""
    if not documents:
        logging.warning(f"No documents to chunk for {category_name_for_log}.")
        return []
    logging.info(f"\nChunking {len(documents)} document sections for '{category_name_for_log}'...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", "## ", "### ", "#### ", ". ", "? ", "! ", " ", ""],
        length_function=len,
        is_separator_regex=False,
    )
    chunked_documents = text_splitter.split_documents(documents)
    logging.info(f"Successfully split into {len(chunked_documents)} chunks for '{category_name_for_log}'.")
    return chunked_documents

def build_and_persist_db(chunks_to_embed: list[Document], db_persist_path: str, embedding_func, db_name_for_log: str):
    """Builds and persists a ChromaDB vector store."""
    if not chunks_to_embed:
        logging.warning(f"No chunks to embed for DB: {db_name_for_log} at {db_persist_path}. Skipping.")
        return

    if os.path.exists(db_persist_path):
        logging.info(f"Deleting existing DB at {db_persist_path} to rebuild for {db_name_for_log}.")
        shutil.rmtree(db_persist_path)
    
    os.makedirs(db_persist_path, exist_ok=True)

    logging.info(f"Creating new vector store for '{db_name_for_log}' in: {db_persist_path}")
    logging.info(f"Embedding {len(chunks_to_embed)} chunks with {config.EMBEDDING_MODEL_NAME}. This will take time...")
    start_embed_time = time.time()
    try:
        Chroma.from_documents(
            documents=chunks_to_embed,
            embedding=embedding_func,
            persist_directory=db_persist_path
        )
        end_embed_time = time.time()
        logging.info(f"DB for '{db_name_for_log}' created. Embedding took {end_embed_time - start_embed_time:.2f} seconds.")
    except Exception as e:
        logging.error(f"ERROR creating DB for '{db_name_for_log}': {e}", exc_info=True)

if __name__ == "__main__":
    overall_start_time = time.time()
    logging.info("--- Starting Pre-Build of All Vector Databases ---")

    if not os.path.exists(config.DATA_DIRECTORY):
        logging.error(f"ERROR: Data directory '{config.DATA_DIRECTORY}' not found. Cannot build databases.")
        exit()

    if os.path.exists(config.CHROMA_BASE_PERSIST_DIR):
        logging.info(f"Deleting old base DB directory: {config.CHROMA_BASE_PERSIST_DIR}")
        shutil.rmtree(config.CHROMA_BASE_PERSIST_DIR)
    os.makedirs(config.CHROMA_BASE_PERSIST_DIR, exist_ok=True)
    
    logging.info(f"Initializing embedding model: {config.EMBEDDING_MODEL_NAME}...")
    model_kwargs_embed = {'device': 'cpu'} 
    encode_kwargs_embed = {'normalize_embeddings': True} 
    embedding_function = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs=model_kwargs_embed,
        encode_kwargs=encode_kwargs_embed
    )
    logging.info("Embedding model initialized.")

    root_path = Path(config.DATA_DIRECTORY).resolve()
    all_documents_for_global_db = [] 
    category_specific_documents = {} 

    root_readme_path = root_path / "README.md"
    if root_readme_path.is_file():
        logging.info(f"\nProcessing root README: {root_readme_path.name}")
        docs_root = load_and_parse_single_readme_file_with_metadata(
            str(root_readme_path), str(root_path), "_root_"
        )
        all_documents_for_global_db.extend(docs_root)
        logging.info(f"Found {len(docs_root)} document sections in root README.")

    subfolders = [item for item in root_path.iterdir() if item.is_dir() and not item.name.startswith('.')]
    
    if subfolders:
        logging.info(f"\nStarting parallel processing for {len(subfolders)} categories...")
        with ProcessPoolExecutor(max_workers=config.MAX_WORKERS_DATA_PROCESSING) as executor:
            future_to_folder = {
                executor.submit(process_single_category_for_db, str(folder_path), str(root_path)): folder_path 
                for folder_path in subfolders
            }
            for future in as_completed(future_to_folder):
                original_folder_path = future_to_folder[future]
                try:
                    category_name, docs_for_category = future.result()
                    category_specific_documents[category_name] = docs_for_category
                    all_documents_for_global_db.extend(docs_for_category) 
                except Exception as exc:
                    logging.error(f"Category {original_folder_path.name} generated an exception: {exc}", exc_info=True)
        logging.info("Parallel category document loading complete.")
    
    for category_name, docs_list in category_specific_documents.items():
        logging.info(f"\n--- Building DB for Category: {category_name} ---")
        db_name_sanitized = f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
        category_db_persist_path = str(config.CHROMA_BASE_PERSIST_DIR / db_name_sanitized)
        chunks_for_category = chunk_documents_for_db(docs_list, category_name)
        build_and_persist_db(chunks_for_category, category_db_persist_path, embedding_function, category_name)

    if all_documents_for_global_db:
        logging.info("\n--- Building Global DB ('All Categories') ---")
        global_db_persist_path = str(config.CHROMA_BASE_PERSIST_DIR / config.GLOBAL_DB_NAME)
        chunks_for_global = chunk_documents_for_db(all_documents_for_global_db, "Global (All Categories)")
        build_and_persist_db(chunks_for_global, global_db_persist_path, embedding_function, "Global (All Categories)")
    else:
        logging.warning("\nNo documents found to build the Global DB.")
    
    overall_end_time = time.time()
    logging.info(f"\n--- All Vector Database Pre-Builds Complete in {overall_end_time - overall_start_time:.2f} seconds ---")