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

# --- LLM Configuration (for rak_chatbot.py) ---
OPENROUTER_MODEL_NAME = "deepseek/deepseek-r1-0528:free" # Or your preferred OpenRouter model
# Optional: These are sent to OpenRouter for analytics and identifying your app.
SITE_URL = "http://localhost:8501" 
SITE_TITLE = "RAKwireless Support Chatbot"


# --- RAG Pipeline Parameters ---
BEST_INITIAL_K = 20
BEST_FINAL_K = 7
BEST_RERANKER_MODEL = "BAAI/bge-reranker-large"

# --- Database & Data Processing Parameters (for build_databases.py) ---
# The size of text chunks for the vector store.
CHUNK_SIZE = 1000
# The overlap between consecutive text chunks.
CHUNK_OVERLAP = 350
# The name for the global database that contains all categories.
GLOBAL_DB_NAME = "all_rak_global_db"  # <-- THIS LINE WAS MISSING. IT IS NOW FIXED.
# Number of CPU cores to use for parallel data processing.
MAX_WORKERS_DATA_PROCESSING = os.cpu_count()