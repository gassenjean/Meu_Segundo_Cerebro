import os
import sys
import re
import glob
import shutil
import datetime

# --- CONFIG ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
IGNORED_DIRS = ['.git', '.obsidian', '.claude', '.gemini', 'node_modules', '.trash', '.venv']

def log(message, level="INFO"):
    print(f"[{level}] {message}")

def get_last_modified_file():
    """Finds the last modified markdown file in the vault."""
    last_file = None
    last_time = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            if file.endswith('.md') and not file.startswith('SESSION_LOG') and not file.startswith('PC_SYNC_LOG'):
                path = os.path.join(root, file)
                mtime = os.path.getmtime(path)
                if mtime > last_time:
                    last_time = mtime
                    last_file = path
    return last_file

def validate_nomenclature(filename):
    """Checks if filename follows conventions."""
    issues = []
    name, ext = os.path.splitext(filename)
    
    # 1. Spaces
    if " " in name:
        issues.append("Contém espaços (Use CamelCase ou underscore)")
    
    # 2. Invalid chars
    if re.search(r'[<>:"/\\|?*]', name):
        issues.append("Caracteres inválidos")
        
    # 3. Bad implementation of dates (quick check)
    # Check for YYYY-MM-DD (bad) vs DDMMMYYYY (good)
    if re.search(r'\d{4}-\d{2}-\d{2}', name):
         issues.append("Formato de data incorreto (Use DDMMMYYYY)")

    # 4. Starting with lowercase (convention preference, mostly)
    if name[0].islower() and not name.startswith('_'): # Exclude utility files
         issues.append("Começa com minúscula (Preferência: CamelCase)")
         
    return issues

def validate_location(filepath):
    """Checks if file is in a valid location."""
    issues = []
    relpath = os.path.relpath(filepath, ROOT_DIR)
    
    # Check root
    if os.path.dirname(relpath) == '':
        allowed_root = ['SESSION_LOG.md', 'PC_SYNC_LOG.md', 'README.md', 'LICENSE', 'CLAUDE.md', 'STATUS_VAULT.md']
        if os.path.basename(filepath) not in allowed_root:
            issues.append(f"Arquivo na raiz do vault ({relpath})")
            
    return issues

def find_best_moc(directory):
    """Finds the most likely MOC file in the given directory."""
    files = os.listdir(directory)
    mocs = [f for f in files if f.endswith('.md') and ('MOC_' in f or '_MOC' in f)]
    
    if not mocs:
        return None
        
    # Heuristic 1: Match Directory Name
    dir_name = os.path.basename(directory)
    for moc in mocs:
        if dir_name.lower() in moc.lower():
            return os.path.join(directory, moc)
            
    # Heuristic 2: Return the one strictly starting with MOC_ or _MOC_
    priority = [f for f in mocs if f.startswith('MOC_') or f.startswith('_MOC_')]
    if priority:
        return os.path.join(directory, priority[0])
        
    return None

def update_moc(filepath, moc_path):
    """Appends file link to MOC if missing."""
    filename = os.path.basename(filepath)
    name_no_ext = os.path.splitext(filename)[0]
    
    try:
        with open(moc_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if f"[[{name_no_ext}]]" in content or f"[[{filename}]]" in content:
            log(f"Já indexado em: {os.path.basename(moc_path)}", "INFO")
            return False
            
        # Backup
        shutil.copy2(moc_path, moc_path + ".bak")
        
        # Append
        # Try to find a good place (end of file for now)
        new_entry = f"\n- [[{name_no_ext}]]"
        
        with open(moc_path, 'a', encoding='utf-8') as f:
            f.write(new_entry)
            
        log(f"🔗 Adicionado ao MOC: {os.path.basename(moc_path)}", "SUCCESS")
        return True
        
    except Exception as e:
        log(f"Erro ao atualizar MOC: {e}", "ERROR")
        return False

def main():
    target_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    target_path = ""
    
    if target_arg and target_arg != "{file_path}": # Handle placeholder from skill.md
        # Try relative path first
        if os.path.exists(target_arg):
             target_path = os.path.abspath(target_arg)
        elif os.path.exists(os.path.join(ROOT_DIR, target_arg)):
             target_path = os.path.join(ROOT_DIR, target_arg)
        else:
            log(f"Arquivo não encontrado: {target_arg}", "ERROR")
            return
            
    else:
        log("Nenhum arquivo especificado. Buscando o último modificado...", "INFO")
        target_path = get_last_modified_file()
        if not target_path:
            log("Nenhum arquivo markdown encontrado.", "ERROR")
            return
            
    log(f"🔍 Validando: {os.path.basename(target_path)}", "INFO")
    
    # 1. Check Rules
    nom_issues = validate_nomenclature(os.path.basename(target_path))
    loc_issues = validate_location(target_path)
    
    valid = True
    if nom_issues:
        valid = False
        log("❌ Erros de Nomenclatura:", "ERROR")
        for i in nom_issues: print(f"  - {i}")
        
    if loc_issues:
        valid = False
        log("❌ Erros de Localização:", "ERROR")
        for i in loc_issues: print(f"  - {i}")
        
    if valid:
        log("✅ Arquivo Válido!", "SUCCESS")
        
        # 2. Update MOC
        # Only update MOC if file is valid? Yes, good practice.
        parent_dir = os.path.dirname(target_path)
        moc_path = find_best_moc(parent_dir)
        
        if moc_path:
            # Don't link MOC to itself
            if os.path.abspath(moc_path) != os.path.abspath(target_path):
                 update_moc(target_path, moc_path)
        else:
            log("ℹ️ Nenhum MOC encontrado na pasta pai para indexação automática.", "WARNING")
            
    else:
        log("⚠️ Corrija os erros acima antes de indexar.", "WARNING")

if __name__ == "__main__":
    main()
