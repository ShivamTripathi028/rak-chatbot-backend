import os
from pathlib import Path
import config  # Import your existing config to find the right folder automatically

def delete_specific_files(filename_to_delete="index.md", dry_run=True):
    """
    Scans the data directory and deletes specific files.
    
    Args:
        filename_to_delete (str): The specific filename to hunt for (e.g., 'index.md').
        dry_run (bool): If True, only prints what would happen. If False, actually deletes.
    """
    root_path = Path(config.DATA_DIRECTORY)
    
    if not root_path.exists():
        print(f"❌ Error: Data directory not found at: {root_path}")
        return

    print(f"🔍 Scanning '{root_path}' for files named '{filename_to_delete}'...")
    
    # Find all matching files recursively
    found_files = list(root_path.rglob(filename_to_delete))
    
    if not found_files:
        print(f"✅ No '{filename_to_delete}' files found.")
        return

    print(f"⚠️  Found {len(found_files)} files.")
    
    if dry_run:
        print("\n--- DRY RUN MODE (No files will be deleted) ---")
        for file_path in found_files:
            print(f"Would delete: {file_path}")
        print(f"\nExample content of the first file found ({found_files[0].name}):")
        try:
            with open(found_files[0], 'r', encoding='utf-8') as f:
                print(f"---\n{f.read().strip()}\n---")
        except:
            print("(Could not read file content)")
        print(f"\nTotal files to delete: {len(found_files)}")
        print("To actually delete these files, set 'DRY_RUN = False' in the script.")
    else:
        print("\n--- DELETING FILES ---")
        deleted_count = 0
        for file_path in found_files:
            try:
                os.remove(file_path)
                print(f"🗑️  Deleted: {file_path}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Error deleting {file_path}: {e}")
        
        print(f"\n✅ Operation Complete. Deleted {deleted_count} files.")

if __name__ == "__main__":
    # ---------------- CONFIGURATION ----------------
    # Set this to False ONLY when you are ready to delete
    DRY_RUN = False 
    # -----------------------------------------------
    
    delete_specific_files("index.md", dry_run=DRY_RUN)