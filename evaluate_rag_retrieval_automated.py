# evaluate_rag_retrieval_automated.py
import os
import json
import time
import logging
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any

# --- Local Imports ---
import config

# --- LangChain Components ---
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker

# --- Logging Setup ---
logging.basicConfig(filename=config.EVAL_LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

# --- Evaluation Core Functions ---
def load_evaluation_dataset(filepath: str) -> List[Dict[str, Any]]:
    """Loads the evaluation dataset from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        logging.info(f"Successfully loaded {len(dataset)} evaluation items from {filepath}")
        return dataset
    except FileNotFoundError:
        logging.error(f"CRITICAL: Evaluation dataset file not found at: {filepath}")
        return []
    except json.JSONDecodeError:
        logging.error(f"CRITICAL: Error decoding JSON from {filepath}")
        return []

def get_embedding_model_eval(model_name: str = config.EMBEDDING_MODEL_NAME):
    logging.info(f"Initializing embedding model: {model_name}...")
    model_kwargs = {'device': 'cpu'} 
    encode_kwargs = {'normalize_embeddings': True} 
    embedding_function = HuggingFaceEmbeddings(
        model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
    )
    logging.info("Embedding model initialized.")
    return embedding_function

def load_vector_store_for_category_eval(category_name: str, embedding_function):
    if category_name == "All Categories (Global DB)": 
        db_name = config.GLOBAL_DB_NAME
    else:
        db_name = f"{category_name.lower().replace(' ', '_').replace('-', '_')}_db"
    db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
    
    if not (db_path.exists() and db_path.is_dir() and any(db_path.iterdir())):
        logging.error(f"Vector store for '{category_name}' not found at {db_path}. Pre-build required.")
        return None 
        
    logging.info(f"Loading vector store for: {category_name} from {db_path}")
    try:
        vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_function)
        logging.info(f"Vector store for '{category_name}' loaded.")
        return vector_store
    except Exception as e:
        logging.error(f"Error loading vector store for '{category_name}': {e}", exc_info=True)
        return None

def get_retrieval_components_eval(vector_store, initial_k, reranker_model_name, final_k):
    logging.info(f"Setting up retrieval: initial_k={initial_k}, reranker='{reranker_model_name}', final_k={final_k}")
    base_retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": initial_k})
    
    if reranker_model_name:
        try:
            cross_encoder = HuggingFaceCrossEncoder(model_name=reranker_model_name, model_kwargs={'device': 'cpu', 'max_length': 512})
            compressor = CrossEncoderReranker(model=cross_encoder, top_n=final_k)
            compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever)
            logging.info("Base and Compression retrievers initialized.")
            return base_retriever, compression_retriever
        except Exception as e:
            logging.error(f"Failed to initialize reranker '{reranker_model_name}': {e}", exc_info=True)
            return base_retriever, None
    else:
        logging.info("Base retriever initialized (no re-ranker).")
        return base_retriever, None

def check_sources(retrieved_docs: List[Document], expected_paths: List[str]) -> bool:
    """Checks if any retrieved document's path matches an expected path."""
    if not retrieved_docs: return False
    retrieved_paths = {doc.metadata.get("relative_path", "").replace("\\", "/") for doc in retrieved_docs}
    expected_paths_normalized = {path.replace("\\", "/") for path in expected_paths}
    
    for r_path in retrieved_paths:
        for e_path in expected_paths_normalized:
            if e_path in r_path:
                return True
    return False

def run_single_evaluation_iteration(embedding_model_name_param, initial_k_param, reranker_model_name_param, final_k_param, eval_dataset, embedding_func):
    logging.info(f"--- Starting Evaluation Iteration ---")
    logging.info(f"Params: Embedding='{embedding_model_name_param}', InitialK={initial_k_param}, "
                 f"ReRanker='{reranker_model_name_param}', FinalK={final_k_param}")

    if not embedding_func:
        logging.error("Embedding function not initialized. Skipping iteration.")
        return {"error": "Embedding function not initialized"}

    total_queries, base_retriever_hits, final_retriever_hits = 0, 0, 0
    queries_by_category = {}
    for item in eval_dataset:
        cat = item["category"]
        if cat not in queries_by_category: queries_by_category[cat] = []
        queries_by_category[cat].append(item)

    for category, queries_in_category in queries_by_category.items():
        logging.info(f"\nEvaluating Category: {category}")
        vector_store = load_vector_store_for_category_eval(category, embedding_func)
        if not vector_store:
            logging.warning(f"Skipping category {category} due to vector store loading error.")
            total_queries += len(queries_in_category)
            continue

        base_retriever, compression_retriever = get_retrieval_components_eval(
            vector_store, initial_k_param, reranker_model_name_param, final_k_param
        )
        if not base_retriever: 
            logging.warning(f"Skipping category {category} due to retriever init error.")
            total_queries += len(queries_in_category)
            continue
            
        for eval_item in queries_in_category:
            total_queries += 1
            query = eval_item["query"]
            expected_sources = eval_item["expected_source_paths"]
            
            base_retrieved_docs = base_retriever.invoke(query)
            if check_sources(base_retrieved_docs, expected_sources):
                base_retriever_hits += 1
            
            final_docs_for_metric = compression_retriever.invoke(query) if compression_retriever else base_retrieved_docs

            if check_sources(final_docs_for_metric, expected_sources):
                final_retriever_hits += 1

    base_hit_rate = (base_retriever_hits / total_queries) * 100 if total_queries > 0 else 0
    final_hit_rate = (final_retriever_hits / total_queries) * 100 if total_queries > 0 else 0
    
    current_run_results = {
        "embedding_model": embedding_model_name_param,
        "initial_k": initial_k_param,
        "reranker_model": reranker_model_name_param if reranker_model_name_param else "None",
        "final_k": final_k_param if reranker_model_name_param else "N/A",
        "total_queries": total_queries,
        "base_retriever_hits": base_retriever_hits,
        "base_hit_rate": f"{base_hit_rate:.2f}",
        "final_retriever_hits": final_retriever_hits,
        "final_hit_rate": f"{final_hit_rate:.2f}"
    }
    logging.info(f"--- Iteration Summary ---")
    logging.info(f"{current_run_results}")
    return current_run_results

if __name__ == "__main__":
    print("Starting Automated RAG Retrieval Evaluation Script...")
    logging.info("================ AUTOMATED EVALUATION SCRIPT STARTED ================")

    EVALUATION_DATASET = load_evaluation_dataset(config.EVAL_DATASET_JSON)
    embedding_function_global = get_embedding_model_eval()

    if not embedding_function_global or not EVALUATION_DATASET:
        print("CRITICAL: Prerequisite failed (Embedding model or Dataset not loaded). Exiting.")
        logging.critical("CRITICAL: Prerequisite failed (Embedding model or Dataset not loaded). Exiting.")
        exit()

    param_grid = {
        "initial_k_values": [15, 20],
        "reranker_setups": [
            {"name": None, "final_k_values": [0]}, 
            {"name": config.RERANKER_MODEL_BASE, "final_k_values": [3, 5]},
            {"name": config.RERANKER_MODEL_LARGE, "final_k_values": [3, 5, 7]},
        ]
    }
    
    all_run_results = []
    for ik in param_grid["initial_k_values"]:
        for reranker_setup in param_grid["reranker_setups"]:
            reranker_name = reranker_setup["name"]
            for fk in reranker_setup["final_k_values"]:
                if reranker_name and fk > ik:
                    logging.warning(f"Skipping invalid combo: final_k ({fk}) > initial_k ({ik})")
                    continue
                
                print(f"\nRunning Iteration: k={ik}, reranker='{reranker_name}', final_k={fk if reranker_name else 'N/A'}")
                iteration_results = run_single_evaluation_iteration(
                    embedding_model_name_param=config.EMBEDDING_MODEL_NAME,
                    initial_k_param=ik,
                    reranker_model_name_param=reranker_name,
                    final_k_param=fk,
                    eval_dataset=EVALUATION_DATASET,
                    embedding_func=embedding_function_global
                )
                all_run_results.append(iteration_results)
                time.sleep(1)

    print("\n\n--- ALL AUTOMATED EVALUATION ITERATIONS COMPLETE ---")
    
    if not all_run_results:
        print("No evaluation results to display.")
    else:
        results_df = pd.DataFrame(all_run_results)
        results_df.to_csv(config.EVAL_RESULTS_CSV, index=False)
        print(f"\nFull results saved to {config.EVAL_RESULTS_CSV}")
        logging.info(f"Full results saved to {config.EVAL_RESULTS_CSV}")
        
        # Display results using the dedicated script
        try:
            from display_results_table import display_csv_as_table
            print("\nDisplaying results summary:")
            display_csv_as_table(config.EVAL_RESULTS_CSV)
        except ImportError:
            print("\nCould not import display_results_table. Please run it manually.")
            print("\nResults Summary Table:")
            print(results_df.to_string(index=False))