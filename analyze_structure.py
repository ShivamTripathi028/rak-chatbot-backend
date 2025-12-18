import os
import re
from pathlib import Path

# Configuration
TARGET_DIR = "./product-categories"
# This should match the chunk size you plan to use in config.py
TARGET_CHUNK_SIZE = 1000 
# Output report file name
REPORT_FILE = "structure_analysis_report.txt"

def analyze_file_structure(file_path):
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Check for Code Blocks > Chunk Size
        # Finds ``` ... ``` blocks
        code_blocks = re.finditer(r'```[\s\S]*?```', content)
        for i, match in enumerate(code_blocks):
            length = len(match.group(0))
            if length > TARGET_CHUNK_SIZE:
                issues.append(f"Huge Code Block ({length} chars)")

        # 2. Check for Admonitions > Chunk Size
        # Finds ::: ... ::: blocks (Docusaurus specific)
        admonitions = re.finditer(r':::[a-zA-Z]+[\s\S]*?:::', content)
        for i, match in enumerate(admonitions):
            length = len(match.group(0))
            if length > TARGET_CHUNK_SIZE:
                # Get the type (tip, warning, etc)
                type_match = re.match(r':::([a-zA-Z]+)', match.group(0))
                type_name = type_match.group(1) if type_match else "Unknown"
                issues.append(f"Huge Admonition '{type_name}' ({length} chars)")

        # 3. Check for Markdown Tables > Chunk Size
        # Finds standard markdown tables
        # Looks for lines starting with | followed by lines with | and -
        tables = re.finditer(r'(\|.*\|\n\|[-:| ]+\|\n(\|.*\|\n)+)', content)
        for i, match in enumerate(tables):
            length = len(match.group(0))
            if length > TARGET_CHUNK_SIZE:
                issues.append(f"Huge Table ({length} chars)")

        # 4. Check for Long Sections (Wall of Text)
        # Splits by headers and checks the length of the content in between
        header_pattern = r'(^|\n)#{1,4}\s' # Matches H1 to H4
        splits = re.split(header_pattern, content)
        
        for section in splits:
            if len(section) > (TARGET_CHUNK_SIZE * 2): # If a section is 2x chunk size
                # Check if it's just code/tables (already caught) or actual text
                clean_sec = re.sub(r'```[\s\S]*?```', '', section) # Remove code
                if len(clean_sec) > (TARGET_CHUNK_SIZE * 2):
                    issues.append(f"Wall of Text (Section size: {len(section)} chars)")
                    break # Just report one per file to reduce noise

    except Exception as e:
        return [f"Error reading file: {str(e)}"]

    return issues

def main():
    # Helper to print to console and write to file simultaneously
    def log(msg):
        print(msg)
        f.write(msg + "\n")

    print(f"Writing report to: {REPORT_FILE} ...")
    
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        log(f"--- Analyzing Content Structure Risks in: {TARGET_DIR} ---")
        log(f"Threshold: Structures larger than {TARGET_CHUNK_SIZE} characters will be flagged.\n")
        
        files_with_issues = 0
        
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    file_issues = analyze_file_structure(file_path)
                    
                    if file_issues:
                        files_with_issues += 1
                        # Format output
                        short_name = os.path.join(os.path.basename(os.path.dirname(file_path)), file)
                        log(f"📄 {short_name}")
                        for issue in file_issues:
                            log(f"   ⚠️  {issue}")
                        log("")

        if files_with_issues == 0:
            log("✅ No structural risks found! Your data fits nicely into the chunk size.")
        else:
            log(f"found {files_with_issues} files with potential chunking risks.")
            
    print(f"Done! Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    main()