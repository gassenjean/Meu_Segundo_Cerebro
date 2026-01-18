import os
import datetime

# --- CONFIG ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
OUTPUT_FILE = os.path.join(ROOT_DIR, "00_SISTEMA", "INDICE_VAULT_COMPLETO.md")

IGNORED_DIRS = {
    '.git', '.obsidian', '.claude', '.gemini', 'node_modules', 
    '.trash', '.venv', '__pycache__', '.idea', '.vscode'
}

IGNORED_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.pdf', '.exe', 
    '.dll', '.zip', '.rar', '.db', '.pyc', '.css' 
    # .css excluded from map to reduce noise? Maybe keep checks simple.
    # Keeping only text-heavy files makes map more useful for knowledge retrieval.
}

def log(message):
    print(f"[MAPA] {message}")

def get_h1_title(filepath):
    """Extracts the first H1 header from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i in range(20): # Only check first 20 lines
                line = f.readline()
                if not line: break
                stripped = line.strip()
                if stripped.startswith('# '):
                    return stripped[2:].strip()
                # If we find text required but no H1 yet, maybe file has no H1?
                # Keep searching a bit.
    except UnicodeDecodeError:
        try:
            # Fallback for weird encodings
            with open(filepath, 'r', encoding='latin-1') as f:
                for i in range(20):
                    line = f.readline()
                    if not line: break
                    if line.strip().startswith('# '):
                        return line.strip()[2:].strip()
        except:
            return None
    except Exception:
        return None
    return None

def process_directory(current_path, level, lines, stats):
    """Recursively processes directories and files."""
    try:
        items = os.listdir(current_path)
    except PermissionError:
        return

    # Sort: Folders first, then Files. Alphabetical within each.
    dirs = []
    files = []
    
    for item in items:
        full_path = os.path.join(current_path, item)
        if os.path.isdir(full_path):
            if item not in IGNORED_DIRS and not item.startswith('.'):
                dirs.append(item)
        else:
            _, ext = os.path.splitext(item)
            if ext.lower() not in IGNORED_EXTENSIONS and item != "INDICE_VAULT_COMPLETO.md":
                files.append(item)
                
    dirs.sort()
    files.sort()
    
    # Indentation
    indent = "  " * level
    
    # Process Directories
    for d in dirs:
        lines.append(f"{indent}- 📂 **{d}**")
        stats['folders'] += 1
        process_directory(os.path.join(current_path, d), level + 1, lines, stats)
        
    # Process Files
    for f in files:
        full_path = os.path.join(current_path, f)
        title = ""
        if f.endswith('.md'):
            h1 = get_h1_title(full_path)
            if h1:
                title = f" — *{h1}*"
        
        name_no_ext = os.path.splitext(f)[0]
        # Use WikiLink Format
        lines.append(f"{indent}- 📄 [[{name_no_ext}]] {title}")
        stats['files'] += 1

def main():
    start_time = datetime.datetime.now()
    log(f"Iniciando mapeamento em: {ROOT_DIR}")
    
    if not os.path.exists(os.path.dirname(OUTPUT_FILE)):
        os.makedirs(os.path.dirname(OUTPUT_FILE))
        
    lines = []
    lines.append(f"# 🗺️ Índice Completo do Vault")
    lines.append(f"**Gerado em:** {start_time.strftime('%d/%m/%Y %H:%M:%S')}")
    lines.append(f"**Autor:** Antigravity (Skill Mapa)")
    lines.append(f"\n---\n")
    
    stats = {'files': 0, 'folders': 0}
    
    process_directory(ROOT_DIR, 0, lines, stats)
    
    # Add stats to header (by prepending or just appending info? appending is fine)
    # Actually, let's insert stats after header.
    stats_text = f"**Total Arquivos:** {stats['files']} | **Total Pastas:** {stats['folders']}\n"
    lines.insert(4, stats_text)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    log(f"Mapa gerado com sucesso!")
    log(f"Arquivo: {OUTPUT_FILE}")
    log(f"Arquivos: {stats['files']}, Pastas: {stats['folders']}")

if __name__ == "__main__":
    main()
