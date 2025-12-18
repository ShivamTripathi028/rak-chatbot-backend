import logging
import re
import html
from pathlib import Path
import frontmatter
from langchain_core.documents import Document
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_product_categories(data_dir: str) -> list[str]:
    root_path = Path(data_dir)
    categories = ["All Categories (Global DB)"] 
    if root_path.exists() and root_path.is_dir():
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'): 
                categories.append(item.name)
    return sorted(list(set(categories)))

def html_table_to_markdown(table_html):
    try:
        soup = BeautifulSoup(table_html, "html.parser")
        headers = []
        thead = soup.find('thead')
        if thead:
            rows = thead.find_all('tr')
            header_cells = rows[0].find_all(['th', 'td']) if rows else thead.find_all(['th', 'td'])
            for cell in header_cells:
                headers.append(" ".join(cell.get_text(separator=" ", strip=True).split()))

        tbody = soup.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
        else:
            all_rows = soup.find_all('tr')
            if thead:
                rows = [r for r in all_rows if r.parent.name != 'thead']
            else:
                rows = all_rows

        if not rows and not headers: return ""

        grid = []
        occupied = {} 
        for r_idx, row in enumerate(rows):
            grid_row = []
            c_idx = 0
            cells = row.find_all(["td", "th"])
            if not cells and not occupied: continue

            cell_iterator = iter(cells)
            while True:
                if (r_idx, c_idx) in occupied:
                    grid_row.append(occupied[(r_idx, c_idx)])
                    c_idx += 1
                    continue
                try:
                    cell = next(cell_iterator)
                except StopIteration:
                    break
                
                text = " ".join(cell.get_text(separator=" ", strip=True).split())
                try: rowspan = int(cell.get("rowspan", 1))
                except: rowspan = 1
                try: colspan = int(cell.get("colspan", 1))
                except: colspan = 1

                for _ in range(colspan):
                    grid_row.append(text)
                if rowspan > 1:
                    for r in range(1, rowspan):
                        for c in range(colspan):
                            occupied[(r_idx + r, c_idx + c)] = text
                c_idx += colspan
            grid.append(grid_row)

        # Remove redundant header rows caused by flattening
        cleaned_grid = []
        if grid:
            skip_indices = set()
            for i in range(len(grid) - 1):
                curr, next_r = grid[i], grid[i+1]
                if curr and next_r and len(curr) > 0 and len(next_r) > 0:
                    if curr[0] == next_r[0] and curr[-1] == "" and next_r[-1] != "":
                        skip_indices.add(i)
            for i, row in enumerate(grid):
                if i not in skip_indices:
                    cleaned_grid.append(row)
        else:
            cleaned_grid = grid

        max_cols = 0
        if cleaned_grid: max_cols = max(len(r) for r in cleaned_grid)
        if headers: max_cols = max(max_cols, len(headers))

        md_lines = []
        if headers:
            headers.extend([""] * (max_cols - len(headers)))
            md_lines.append("| " + " | ".join(headers) + " |")
            md_lines.append("| " + " | ".join(["---"] * max_cols) + " |")
        
        for row in cleaned_grid:
            row.extend([""] * (max_cols - len(row)))
            md_lines.append("| " + " | ".join(row) + " |")

        return "\n".join(md_lines)
    except Exception as e:
        logging.error(f"Table conversion error: {e}")
        return table_html

def split_large_markdown_tables(content: str, max_rows=10) -> str:
    """
    Splits tables > 10 rows. Repeats headers. 
    Keeps chunks small enough for BGE-Base (1500 chars).
    """
    lines = content.split('\n')
    new_lines = []
    
    table_buffer = []
    inside_table = False
    
    for line in lines:
        if line.strip().startswith('|'):
            inside_table = True
            table_buffer.append(line)
        else:
            if inside_table:
                if len(table_buffer) > (max_rows + 2): 
                    header = table_buffer[0]
                    separator = table_buffer[1]
                    data_rows = table_buffer[2:]
                    for i in range(0, len(data_rows), max_rows):
                        chunk = data_rows[i : i + max_rows]
                        new_lines.append(header)
                        new_lines.append(separator)
                        new_lines.extend(chunk)
                        new_lines.append("\n")
                else:
                    new_lines.extend(table_buffer)
                inside_table = False
                table_buffer = []
            
            new_lines.append(line)
            
    if inside_table and table_buffer:
        new_lines.extend(table_buffer)

    return "\n".join(new_lines)

def clean_rak_content(content: str) -> str:
    content = re.sub(r"^import Rk.*$", "", content, flags=re.MULTILINE)
    
    table_pattern = re.compile(r'<table.*?>.*?</table>', re.DOTALL | re.IGNORECASE)
    content = table_pattern.sub(lambda match: "\n" + html_table_to_markdown(match.group(0)) + "\n", content)

    img_pattern = r'<RkImage\s+[^>]*caption="([^"]+)"[^>]*\/>'
    content = re.sub(img_pattern, r'\n> **Image:** \1\n', content)
    content = re.sub(r'<RkImage[^>]*\/>', "", content)
    content = re.sub(r'<RkCertificationIcons[^>]*\/>', "", content)
    content = re.sub(r'<RkBottomNav[^>]*\/>', "", content)

    content = re.sub(r"<b>(.*?)</b>", r"**\1**", content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.IGNORECASE)
    content = html.unescape(content)
    
    fluff_patterns = [r"Thank you for choosing.*?product\.", r"To help you get started.*?product\.", r"🎉"]
    for pattern in fluff_patterns:
        content = re.sub(pattern, "", content, flags=re.IGNORECASE | re.DOTALL)

    # Aggressive table splitting for BGE-Base size limits
    content = split_large_markdown_tables(content, max_rows=10)

    return content.strip()

def load_and_parse_file(filepath_str: str, root_dir_str: str, top_level_folder_name: str) -> list[Document]:
    filepath = Path(filepath_str)
    try:
        post = frontmatter.load(filepath)
        raw_content = post.content
        file_metadata = post.metadata
        
        cleaned_text = clean_rak_content(raw_content)

        if len(cleaned_text) < 10: return []

        if "title" not in file_metadata:
            h1_match = re.search(r'^#\s+(.*)$', raw_content, re.MULTILINE)
            if h1_match:
                file_metadata["title"] = h1_match.group(1)
            else:
                file_metadata["title"] = filepath.stem.replace("-", " ").title()

        final_metadata = {
            "source": str(filepath.name),
            "relative_path": str(filepath.resolve().relative_to(Path(root_dir_str).resolve())).replace("\\", "/"),
            "category": top_level_folder_name,
            "title": file_metadata.get("title", "Unknown"),
            "keywords": ", ".join(file_metadata.get("keywords", [])) if isinstance(file_metadata.get("keywords"), list) else ""
        }
        return [Document(page_content=cleaned_text, metadata=final_metadata)]

    except Exception as e:
        logging.error(f"Error loading {filepath.name}: {e}")
        return []