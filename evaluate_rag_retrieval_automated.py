# evaluate_rag_retrieval_automated.py
import json
import logging
import pandas as pd
import torch
import config
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
try:
    from langchain_huggingface import HuggingFaceCrossEncoder
except ImportError:
    from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker

logging.basicConfig(filename=config.EVAL_LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s', filemode='w')

def get_embedding_model_eval():
    device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Eval running on: {device}")
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME, 
        model_kwargs={'device': device},
        encode_kwargs={'normalize_embeddings': True}
    )

def check_sources(retrieved_docs, expected_paths):
    if not retrieved_docs: return False
    retrieved = {d.metadata.get("relative_path", "").replace("\\", "/") for d in retrieved_docs}
    expected = {p.replace("\\", "/") for p in expected_paths}
    for r in retrieved:
        for e in expected:
            if e in r: return True
    return False

def run_eval(dataset, embedding_func):
    results = []
    # Test specific high-capacity configs for BGE-M3
    configs = [(15, 7), (20, 10)] 
    
    for init_k, final_k in configs:
        print(f"Testing K={init_k} -> {final_k}")
        hits = 0
        total = 0
        
        # Group by category to load DB once per cat
        by_cat = {}
        for item in dataset:
            cat = item["category"]
            if cat not in by_cat: by_cat[cat] = []
            by_cat[cat].append(item)
            
        for cat, items in by_cat.items():
            db_name = config.GLOBAL_DB_NAME if cat == "All Categories (Global DB)" else f"{cat.lower().replace(' ', '_').replace('-', '_')}_db"
            db_path = config.CHROMA_BASE_PERSIST_DIR / db_name
            if not db_path.exists(): continue
            
            vector_store = Chroma(persist_directory=str(db_path), embedding_function=embedding_func)
            
            # Setup Retriever
            base = vector_store.as_retriever(search_kwargs={"k": init_k})
            reranker = HuggingFaceCrossEncoder(model_name=config.BEST_RERANKER_MODEL, model_kwargs={'device': 'cpu'})
            compressor = CrossEncoderReranker(model=reranker, top_n=final_k)
            retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base)
            
            for item in items:
                total += 1
                try:
                    docs = retriever.invoke(item["query"])
                    if check_sources(docs, item["expected_source_paths"]):
                        hits += 1
                except: pass

        acc = (hits/total * 100) if total else 0
        print(f"Accuracy: {acc:.2f}%")
        results.append({"init_k": init_k, "final_k": final_k, "accuracy": acc})
        
    pd.DataFrame(results).to_csv(config.EVAL_RESULTS_CSV, index=False)

if __name__ == "__main__":
    with open(config.EVAL_DATASET_JSON, 'r') as f: data = json.load(f)
    embed = get_embedding_model_eval()
    run_eval(data, embed)