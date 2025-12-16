# utils.py
import logging
import re
from pathlib import Path
from langchain_community.docstore.document import Document

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_product_categories(data_dir: str) -> list[str]:
    """
    Scans the data directory to find all subdirectories, which represent product categories.
    """
    root_path = Path(data_dir)
    categories = ["All Categories (Global DB)"] 
    if root_path.exists() and root_path.is_dir():
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'): 
                categories.append(item.name)
    return sorted(list(set(categories)))

def clean_and_filter_text(text: str) -> str:
    """
    1. Removes Docusaurus specific imports and components.
    2. Returns the cleaned text.
    """
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # --- FILTERS ---
        
        # 1. Skip Docusaurus Imports
        if stripped_line.startswith("import ") and ("@site" in stripped_line or "Redirection" in stripped_line):
            continue
            
        # 2. Skip Redirection Components (The "Useless" files)
        if stripped_line.startswith("<RkRedirect"):
            continue
            
        # 3. Skip Bottom Navigation components
        if stripped_line.startswith("<RkBottomNav"):
            continue

        # 4. Skip Frontmatter markers (optional, but keeps things clean)
        # We generally want to keep the text inside, but if you want to strip metadata blocks:
        # if stripped_line == "---": continue 

        cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines).strip()

def load_and_parse_single_readme_file_with_metadata(filepath_str: str, root_dir_str: str, top_level_folder_name: str) -> list[Document]:
    """
    Loads a markdown file, cleans it, and ONLY returns it if it has valid content.
    """
    filepath = Path(filepath_str)
    root_path = Path(root_dir_str)
    
    try:
        # 1. Read file directly (Fastest method)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            raw_text = f.read()
            
        # 2. Clean the content
        cleaned_text = clean_and_filter_text(raw_text)
        
        # 3. INTELLIGENT FILTERING
        # If the file was just a redirect or imports, cleaned_text will be empty or just whitespace.
        # We check if there are at least 10 characters of real content.
        if len(cleaned_text) < 10:
            # This logs silently so you don't spam the terminal, or you can enable it to see what's skipped
            # logging.info(f"Skipping empty/redirect file: {filepath.name}")
            return []

        # 4. Create Metadata
        metadata = {}
        try:
            relative_p_to_readme = filepath.resolve().relative_to(root_path.resolve())
            metadata["relative_path"] = str(relative_p_to_readme).replace("\\", "/")
        except ValueError:
            metadata["relative_path"] = str(filepath.resolve()).replace("\\", "/")
        
        metadata["top_level_folder"] = top_level_folder_name
        
        # 5. Return the document
        return [Document(page_content=cleaned_text, metadata=metadata)]

    except Exception as e:
        logging.error(f"    Error loading/parsing {filepath.name} in {top_level_folder_name}: {e}")
        return []