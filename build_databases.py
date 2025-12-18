import os
import shutil
import time 
import logging
import psutil
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

import torch
import config
from utils import load_and_parse_file

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_optimal_batch_size():
    """Calculates optimal batch size. BGE-Base is lighter, we can be aggressive."""
    total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    if total_ram_gb >= 16: return 256
    elif total_ram_gb >= 8: return 128
    else: return 64

def process_file_wrapper(args):
    file_path, root_dir, category = args
    return load_and_parse_file(file_path, root_dir, category)

def chunk_documents(documents):
    # 1. Structural Split (Extracts H1-H3 into Metadata)
    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    
    # 2. Size Split
    # We add H4 and H5 to separators to ensure we don't slice a sub-header 
    # away from its content if possible.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=[
            "\n```",   # Priority 1: Keep code blocks whole
            "\n#### ", # Priority 2: Split at H4 headers (Keep them with content)
            "\n##### ",# Priority 3: Split at H5 headers
            "\n:::",   # Priority 4: Admonitions
            "\n\n",    # Priority 5: Paragraphs
            "\n", 
            ". ", 
            " ", 
            ""
        ]
    )

    final_chunks = []
    for doc in documents:
        # Split by Header (H1-H3)
        header_splits = markdown_splitter.split_text(doc.page_content)
        
        # Split by Size (Respecting H4-H5 boundaries)
        recursive_splits = text_splitter.split_documents(header_splits)
        
        for split in recursive_splits:
            split.metadata.update(doc.metadata)
            
            # --- METADATA STAMPING (Context Injection) ---
            # We explicitly add the hierarchy back into the text so the 
            # embedding model "sees" the context even if the chunk is small.
            context_prefixes = []
            
            # Product Title
            if "title" in split.metadata:
                context_prefixes.append(f"Product: {split.metadata['title']}")
            
            # Hierarchical Headers
            if "Header 1" in split.metadata:
                context_prefixes.append(f"Section: {split.metadata['Header 1']}")
            if "Header 2" in split.metadata:
                context_prefixes.append(f"Subsection: {split.metadata['Header 2']}")
            if "Header 3" in split.metadata:
                context_prefixes.append(f"Topic: {split.metadata['Header 3']}")
            
            # Prepend context string to the content
            if context_prefixes:
                context_str = " | ".join(context_prefixes)
                split.page_content = f"{context_str}\n\n{split.page_content}"
            
            final_chunks.append(split)
            
    return final_chunks

if __name__ == "__main__":
    start_time = time.time()
    
    if os.path.exists(config.CHROMA_BASE_PERSIST_DIR):
        shutil.rmtree(config.CHROMA_BASE_PERSIST_DIR)
    os.makedirs(config.CHROMA_BASE_PERSIST_DIR, exist_ok=True)

    root_path = Path(config.DATA_DIRECTORY)
    all_files = []
    
    for f in root_path.glob("*.md"):
        all_files.append((str(f), str(root_path), "Global"))
        
    for category_dir in [x for x in root_path.iterdir() if x.is_dir()]:
        if category_dir.name.startswith('.'): continue
        for f in category_dir.rglob("*.md"):
            all_files.append((str(f), str(root_path), category_dir.name))

    print(f"📂 Found {len(all_files)} Markdown files.")

    print(f"⚙️  Processing files using {os.cpu_count()} CPU cores...")
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        results = list(tqdm(executor.map(process_file_wrapper, all_files), total=len(all_files)))

    raw_docs = [item for sublist in results for item in sublist]
    
    print("✂️  Chunking documents...")
    docs_by_category = {}
    all_global_docs = []
    
    for doc in raw_docs:
        cat = doc.metadata.get("category", "Global")
        if cat not in docs_by_category: docs_by_category[cat] = []
        docs_by_category[cat].append(doc)
        all_global_docs.append(doc)

    chunks_by_category = {}
    for cat, docs in docs_by_category.items():
        chunks_by_category[cat] = chunk_documents(docs)
    
    global_chunks = chunk_documents(all_global_docs)

    print(f"🚀 Initializing {config.EMBEDDING_MODEL_NAME}...")
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"   Using device: {device.upper()}")
        
    embedding_func = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={'device': device},
        encode_kwargs={'normalize_embeddings': True}
    )

    BATCH_SIZE = get_optimal_batch_size()
    print(f"⚡ Calculated Optimal Batch Size: {BATCH_SIZE}")
    print("💾 Creating Vector Databases...")
    
    def create_db(chunks, folder_name):
        if not chunks: return
        persist_path = config.CHROMA_BASE_PERSIST_DIR / folder_name
        vectordb = Chroma(persist_directory=str(persist_path), embedding_function=embedding_func)
        for i in tqdm(range(0, len(chunks), BATCH_SIZE), desc=folder_name, leave=False):
            batch = chunks[i:i + BATCH_SIZE]
            vectordb.add_documents(batch)
            
    for cat, chunks in chunks_by_category.items():
        db_name = f"{cat.lower().replace(' ', '_').replace('-', '_')}_db"
        create_db(chunks, db_name)

    print(f"   -> Building '{config.GLOBAL_DB_NAME}' ({len(global_chunks)} chunks)...")
    create_db(global_chunks, config.GLOBAL_DB_NAME)

    print(f"\n✅ Done! Total time: {time.time() - start_time:.2f} seconds.")