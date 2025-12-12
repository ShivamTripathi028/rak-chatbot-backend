# config.py
import os
from pathlib import Path

# --- Core Directories and Paths ---
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIRECTORY = BASE_DIR / "rak-products"
CHROMA_BASE_PERSIST_DIR = BASE_DIR / "new_rak_category_dbs"

# --- Logging Configuration ---
EVAL_LOG_FILE = BASE_DIR / 'automated_evaluation_log.txt'
CHATBOT_LOG_FILE = BASE_DIR / 'rak_chatbot_ui.log'

# --- Evaluation and Results Files ---
EVAL_DATASET_JSON = BASE_DIR / "evaluation_dataset.json"
EVAL_RESULTS_CSV = BASE_DIR / "automated_evaluation_results.csv"

# --- Model Configuration ---
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

# --- LLM Configuration (OPTIMIZED) ---
# Switched to gpt-4o-mini for <5s response times. 
# It is significantly faster and cheaper than gpt-4o/gpt-5-nano.
OPENAI_MODEL_NAME = "gpt-5-nano-2025-08-07"

# --- RAG Pipeline Parameters (OPTIMIZED) ---
# Reduced 'Initial K' prevents the Reranker from processing too many documents.
# Switched to 'bge-reranker-base'. 'Large' is too slow for CPU inference.
BEST_INITIAL_K = 25 
BEST_FINAL_K = 8
BEST_RERANKER_MODEL = "BAAI/bge-reranker-base"

# --- Database & Data Processing Parameters ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 350
GLOBAL_DB_NAME = "all_rak_global_db"
MAX_WORKERS_DATA_PROCESSING = os.cpu_count()

# --- End of Life (EOL) Product List ---
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