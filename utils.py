# utils.py
import logging
from pathlib import Path
from langchain_community.docstore.document import Document
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_product_categories(data_dir: str) -> list[str]:
    """
    Scans the data directory to find all subdirectories, which represent product categories.
    
    Args:
        data_dir: The path to the root data directory.

    Returns:
        A sorted list of category names, with a global option first.
    """
    root_path = Path(data_dir)
    categories = ["All Categories (Global DB)"] 
    if root_path.exists() and root_path.is_dir():
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'): 
                categories.append(item.name)
    return sorted(list(set(categories)))

def load_and_parse_single_readme_file_with_metadata(filepath_str: str, root_dir_str: str, top_level_folder_name: str) -> list[Document]:
    """
    Loads a single README.md file, parses it, and enriches the documents with metadata.

    Args:
        filepath_str: The string path to the README file.
        root_dir_str: The string path to the root data directory (for creating relative paths).
        top_level_folder_name: The name of the category folder.

    Returns:
        A list of LangChain Document objects, or an empty list if an error occurs.
    """
    filepath = Path(filepath_str)
    root_path = Path(root_dir_str)
    processed_docs = []
    
    try:
        loader = UnstructuredMarkdownLoader(str(filepath))
        docs_from_file = loader.load()
    except Exception as e:
        logging.error(f"    Error loading/parsing {filepath.name} in {top_level_folder_name}: {e}")
        return []

    if not docs_from_file:
        return []
        
    for doc in docs_from_file:
        if not hasattr(doc, 'metadata') or doc.metadata is None:
            doc.metadata = {}
        try:
            # Create a relative path from the data directory root
            relative_p_to_readme = filepath.resolve().relative_to(root_path.resolve())
            doc.metadata["relative_path"] = str(relative_p_to_readme).replace("\\", "/")
        except ValueError:
            # Fallback if the file is not within the root_path for some reason
            doc.metadata["relative_path"] = str(filepath.resolve()).replace("\\", "/")
        
        doc.metadata["top_level_folder"] = top_level_folder_name
        processed_docs.append(doc)
        
    return processed_docs