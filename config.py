import os
from pathlib import Path

# --- Core Directories ---
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIRECTORY = BASE_DIR / "product-categories"
CHROMA_BASE_PERSIST_DIR = BASE_DIR / "new_rak_category_dbs"

# --- Logging ---
EVAL_LOG_FILE = BASE_DIR / 'automated_evaluation_log.txt'
CHATBOT_LOG_FILE = BASE_DIR / 'rak_chatbot_ui.log'
EVAL_DATASET_JSON = BASE_DIR / "evaluation_dataset.json"
EVAL_RESULTS_CSV = BASE_DIR / "automated_evaluation_results.csv"

# --- Model Configuration ---
# BGE-Base: Fast, standard 512 token context.
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"
OPENAI_MODEL_NAME = "gpt-4.1-nano-2025-04-14"

# --- RAG Pipeline Parameters ---
# Reduced to 1500 to fit BGE-Base's 512 token limit safely.
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 300

# Retrieval Settings
BEST_INITIAL_K = 20  # Increased K to retrieve more small chunks
BEST_FINAL_K = 7
BEST_RERANKER_MODEL = "BAAI/bge-reranker-base" 

# --- System ---
GLOBAL_DB_NAME = "all_rak_global_db"
MAX_WORKERS_DATA_PROCESSING = os.cpu_count() 

# --- EOL Products List ---
EOL_PRODUCTS = [
    'RAK7240', 'RAK7289', 'RAK7249', 'RAK7258', 'RAK7268', 'RAK10701-P',
    'RAK7243', 'RAK7243C', 'RAK7244', 'RAK7244C', 'RAK7246G',
    'RAK4200', 'RAK4260', 'RAK4270', 'RAK4600',
    'RAK811', 'RAK813', 'RAK811-D', 'RAK4200-D', 'RAK4260-D', 'RAK4270-D', 'RAK4600-D', 'RAK4200-E', 'RAK4260-E',
    'RAK831', 'RAK833',
    'RAK2245 Stamp', 'RAK2245 Pi HAT', 'RAK2247',
    'RAK5005-O', 'RAK1910', 'RAK2171',
    'RAK7200', 'RAK7204', 'RAK612', 'RAK7201', 'RAK2011', 'RAK2013',
    "RAK815", "RAK7205", "RAK5205", "RAKBox-GW-4B", "RAKBox-GW-4S", "RAK8212"
]