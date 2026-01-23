
import os
import re

ROOT_DIR = r"c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"
MOC_DIR = os.path.join(ROOT_DIR, "03_APRENDIZADO")

def sanitize_filename(name):
    original_name = name
    # Remove file extension for processing
    base, ext = os.path.splitext(name)
    
    # 1. Parentheses to underscore or remove if empty
    base = re.sub(r'\s*\([^)]*\)', '', base) # Remove content in parens if it looks like metadata, or just parens?
    # User said: "Parênteses () -> remover ou substituir por underscore"
    # Let's simple remove parens chars and content? Or just chars?
    # "Parênteses () -> remover ou substituir por underscore". A safe bet is replacing " (" with "_" and ")" with ""
    # But files often have (1).md
    # Let's try to be smart. Replace `(` and `)` with `_` then clean up double `__`.
    base = base.replace('(', '_').replace(')', '_')
    base = base.replace('[', '_').replace(']', '_')
    
    # 2. Emojis - Removes anything not ASCII or standard latin chars? 
    # Use regex for non-alphanumeric (allowing underscore, dot, hyphen)
    # Be careful with accents (pt-BR).
    # Regex to keep: a-zA-Z0-9, accents, _, -
    # Remove emojis is tricky without specific library, but we can whitelist chars.
    # Whitelist: \w (alphanumeric+underscore), \s (space - to be replaced), -, .
    # Unicode ranges for Latin-1 Supplement (Accents): \u00C0-\u00FF
    
    # Replace spaces with underscore
    base = base.replace(' ', '_')
    
    # Replace invalid chars with empty or underscore
    # Remove emojis by keeping only safe ranges.
    # This regex matches anything NOT in allowed set.
    # Allowed: a-z, A-Z, 0-9, _, -, ., accented chars
    # base = re.sub(r'[^\w\-\.]', '', base) # This is too aggressive for accents if not handled by \w depending on locale
    # Let's rely on string replacement of specific bad chars user mentioned, and maybe a generic "non-ascii and non-latin" remover?
    
    # Specific cleanup for emojis: output chars > 255?
    new_base = ""
    for char in base:
        if ord(char) > 255: # Simplistic emoji detection (and some math symbols). Valid accents are usually < 255 (Latin-1)
            continue
        new_base += char
    base = new_base

    # Cleanup multiple underscores
    base = re.sub(r'_+', '_', base)
    # Remove leading/trailing underscores
    base = base.strip('_')
    
    if not base: # If filename became empty
        base = "Untitled"

    new_name = base + ext
    return new_name

def rename_mocs():
    print(f"Scanning {MOC_DIR} for MOCs...")
    if not os.path.exists(MOC_DIR):
        print("Directory not found!")
        return

    count = 0
    for filename in os.listdir(MOC_DIR):
        if filename.startswith("MOC_") and filename.endswith(".md"):
            # Rename to _MOC_
            new_name = "_" + filename
            print(f"Renaming MOC: {filename} -> {new_name}")
            try:
                os.rename(os.path.join(MOC_DIR, filename), os.path.join(MOC_DIR, new_name))
                count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
    print(f"Renamed {count} MOCs.")

def clean_special_chars():
    print(f"Scanning {ROOT_DIR} for special chars...")
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # process files
        for filename in files:
            if filename == "NOMENCLATURA.md" or filename == "SESSION_LOG.md": continue
            
            new_name = sanitize_filename(filename)
            if new_name != filename:
                # Check conflicts
                if os.path.exists(os.path.join(root, new_name)):
                    print(f"Skipping conflict: {filename} -> {new_name}")
                    continue
                
                print(f"Renaming: {filename} -> {new_name}")
                try:
                    os.rename(os.path.join(root, filename), os.path.join(root, new_name))
                    count += 1
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")
    
    print(f"Cleaned {count} files.")

if __name__ == "__main__":
    clean_special_chars()
    rename_mocs()
