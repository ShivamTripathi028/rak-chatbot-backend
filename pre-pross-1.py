import os
import re
import html
from bs4 import BeautifulSoup

# Configuration: Directory to scan
TARGET_DIR = "./product-categories" 

def clean_imports(content):
    """
    Removes Docusaurus/React specific import lines.
    """
    content = re.sub(r"^import Rk.*$", "", content, flags=re.MULTILINE)
    return content

def convert_html_links(content):
    """
    Converts HTML links <a href="url">text</a> to Markdown [text](url).
    """
    # Pattern matches <a ... href="..." ...>Text</a>
    # Capture group 1: URL
    # Capture group 2: Link Text
    link_pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>(.*?)</a>'
    return re.sub(link_pattern, r'[\2](\1)', content, flags=re.IGNORECASE)

def process_certifications(content):
    """
    Finds <RkCertificationIcons ... /> tags.
    Extracts the certification type and URL, converting them to a Markdown list.
    """
    pattern = r'<RkCertificationIcons\s+certifications=\{([\[\s\S]*?\])\}\s*\/>'

    def replace_cert(match):
        raw_data = match.group(1)
        certs = re.findall(r"['\"](\w+)['\"]\s*:\s*['\"]([^'\"]+)['\"]", raw_data)

        if not certs:
            return ""

        md_lines = ["\n### Certifications"]
        for c_type, url in certs:
            md_lines.append(f"- **{c_type.upper()}:** {url}")

        return "\n".join(md_lines) + "\n"

    return re.sub(pattern, replace_cert, content)

def process_images(content):
    """
    Finds <RkImage ... /> tags.
    Replaces them with their caption to preserve context for the LLM.
    """
    pattern = r'<RkImage\s+[^>]*caption="([^"]+)"[^>]*\/>'
    
    def replacement(match):
        caption = match.group(1)
        return f"\n> **Image:** {caption}\n"

    content = re.sub(pattern, replacement, content)
    content = re.sub(r'<RkImage[^>]*\/>', "", content)
    content = re.sub(r'<RkCertificationIcons[^>]*\/>', "", content) # Cleanup if process_certifications didn't catch it
    content = re.sub(r'<RkBottomNav[^>]*\/>', "", content)
    
    return content

def clean_html_formatting(content):
    """
    Cleans leftover HTML tags and entities from the Markdown text.
    """
    # 1. Convert Bold tags
    content = re.sub(r"<b>(.*?)</b>", r"**\1**", content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r"<strong>(.*?)</strong>", r"**\1**", content, flags=re.IGNORECASE | re.DOTALL)

    # 2. Convert Italic tags
    content = re.sub(r"<i>(.*?)</i>", r"*\1*", content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r"<em>(.*?)</em>", r"*\1*", content, flags=re.IGNORECASE | re.DOTALL)

    # 3. Convert Break tags to newlines
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.IGNORECASE)

    # 4. Decode HTML entities
    content = html.unescape(content)

    return content

def html_table_to_markdown(table_html):
    """
    Robustly converts HTML tables to Markdown.
    """
    soup = BeautifulSoup(table_html, "html.parser")
    
    headers = []
    thead = soup.find('thead')
    if thead:
        header_rows = thead.find_all('tr')
        if header_rows:
            for cell in header_rows[0].find_all(['th', 'td']):
                headers.append(" ".join(cell.get_text(separator=" ", strip=True).split()))
        else:
            for cell in thead.find_all(['th', 'td']):
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

    if not rows and not headers:
        return ""

    grid = []
    occupied = {} 

    for r_idx, row in enumerate(rows):
        grid_row = []
        c_idx = 0
        
        cells = row.find_all(["td", "th"])
        if not cells and not occupied:
            continue

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

    max_cols = 0
    if grid: max_cols = max(len(r) for r in grid)
    if headers: max_cols = max(max_cols, len(headers))

    # Pad Body Rows
    for row in grid:
        if len(row) < max_cols:
            row.extend([""] * (max_cols - len(row)))
            
    # Pad Header Row
    if headers:
        if len(headers) < max_cols:
            headers.extend([""] * (max_cols - len(headers)))
    elif grid:
        headers = grid[0]
        grid = grid[1:]

    # Remove redundant rows caused by flattening
    cleaned_grid = []
    if grid:
        skip_indices = set()
        for i in range(len(grid) - 1):
            curr_row = grid[i]
            next_row = grid[i+1]
            if curr_row[0] == next_row[0]:
                if curr_row[-1] == "" and next_row[-1] != "":
                    skip_indices.add(i)

        for i, row in enumerate(grid):
            if i not in skip_indices:
                cleaned_grid.append(row)
    else:
        cleaned_grid = grid

    md_lines = []
    md_lines.append("| " + " | ".join(headers) + " |")
    md_lines.append("| " + " | ".join(["---"] * max_cols) + " |")
    for row in cleaned_grid:
        md_lines.append("| " + " | ".join(row) + " |")

    return "\n".join(md_lines)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Clean Imports
        content = clean_imports(content)

        # 2. Flatten HTML Tables to Markdown
        table_pattern = re.compile(r'<table.*?>.*?</table>', re.DOTALL | re.IGNORECASE)
        def table_replacer(match):
            return "\n" + html_table_to_markdown(match.group(0)) + "\n"
        content = table_pattern.sub(table_replacer, content)

        # 3. Convert Certifications
        content = process_certifications(content)

        # 4. Process Images
        content = process_images(content)

        # 5. Clean HTML Links (NEW)
        content = convert_html_links(content)

        # 6. Clean General HTML Formatting
        content = clean_html_formatting(content)

        # 7. Collapse excessive newlines
        content = re.sub(r'\n{3,}', '\n\n', content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Processed: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    print(f"Scanning directory: {TARGET_DIR}")
    count = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)
                count += 1
    print(f"Finished processing {count} files.")

if __name__ == "__main__":
    main()