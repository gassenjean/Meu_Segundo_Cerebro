import os
import re
import datetime
import argparse

# Configurações
VAULT_ROOT = os.getcwd()
REPORT_DIR = os.path.join(VAULT_ROOT, "00_SISTEMA", "RELATORIOS")
ALLOWED_ROOT_FILES = [
    "CLAUDE.md",
    "SESSION_LOG.md",
    "PC_SYNC_LOG.md",
    "STATUS_VAULT.md",
    ".gitignore",
    ".ds_store",
    "desktop.ini"
]
IGNORED_DIRS = {".git", ".obsidian", ".gemini", ".claude", ".vscode", ".idea", "node_modules"}

# Cores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_all_md_files():
    md_files = []
    file_map = {} # Nome -> Caminho Completo
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Ignorar diretórios ocultos/sistema
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith('.')]
        
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
                file_map[file] = full_path
    return md_files, file_map

def check_root_hygiene():
    errors = []
    files_in_root = [f for f in os.listdir(VAULT_ROOT) if os.path.isfile(os.path.join(VAULT_ROOT, f))]
    for f in files_in_root:
        if f.lower() not in [af.lower() for af in ALLOWED_ROOT_FILES] and not f.startswith('.'):
             # Permitir backups temporários se seguirem algum padrão? Não, ser rígido.
             # Mas ignorar arquivos de backup criados por nossas skills (.bak)
             if not f.endswith(".bak") and "backup" not in f.lower():
                 errors.append(f)
    return errors

def check_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Ler apenas os primeiros bytes/linhas para performance
            first_line = f.readline().strip()
            return first_line == "---"
    except:
        return False

def extract_h1(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("# "):
                    return line.strip()[2:]
    except:
        pass
    return None

def extract_links(file_path):
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex básico para [[link]] ou [[link|text]]
            matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', content)
            links.extend(matches)
    except:
        pass
    return links

def run_linter():
    print(f"{YELLOW}Iniciando Architect Linter...{RESET}")
    
    md_files, file_map = get_all_md_files()
    
    issues = {
        "root_hygiene": [],
        "missing_frontmatter": [],
        "h1_duplicates": {}, # H1 -> [files]
        "broken_links": {} # File -> [links]
    }

    # 1. Root Hygiene
    issues["root_hygiene"] = check_root_hygiene()

    # Scan files
    h1_cache = {} # H1 -> File
    
    count = 0
    total = len(md_files)
    
    for file_path in md_files:
        rel_path = os.path.relpath(file_path, VAULT_ROOT)
        count += 1
        if count % 100 == 0:
            print(f"Processando {count}/{total}...")

        # 2. Frontmatter
        if not check_frontmatter(file_path):
            issues["missing_frontmatter"].append(rel_path)

        # 3. H1 Duplicates
        h1 = extract_h1(file_path)
        if h1:
            if h1 in h1_cache:
                if h1 not in issues["h1_duplicates"]:
                    issues["h1_duplicates"][h1] = [h1_cache[h1]]
                issues["h1_duplicates"][h1].append(rel_path)
            else:
                h1_cache[h1] = rel_path

        # 4. Broken Links
        links = extract_links(file_path)
        for link in links:
            # Simplificação: assume que [[Nome do Arquivo]] busca 'Nome do Arquivo.md'
            # Obsdian resolve links de forma complexa (path relativo, shortest path)
            # Vamos checar se existe ALGUM arquivo com esse nome no vault
            target_name = link.split('#')[0].split('^')[0] # Remove ancora
            if not target_name.strip(): continue # Link vazio ou só ancora

            target_file_md = target_name if target_name.endswith('.md') else f"{target_name}.md"
            
            # Check simples: existe no map?
            if target_file_md not in file_map:
                # Tentar case-insensitive e variações é muito caro aqui, vamos assumir exato por enquanto
                # Melhor: vamos checar case-insensitive no map
                found = False
                for k in file_map:
                    if k.lower() == target_file_md.lower():
                        found = True
                        break
                
                if not found:
                    if rel_path not in issues["broken_links"]:
                        issues["broken_links"][rel_path] = []
                    issues["broken_links"][rel_path].append(link)

    # Gerar Relatório
    timestamp = datetime.datetime.now().strftime("%d%b%Y").upper()
    report_filename = f"ARCHITECT_LINTER_RELATORIO_{timestamp}.md"
    report_path = os.path.join(REPORT_DIR, report_filename)
    
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Relatório Architect Linter - {timestamp}\n\n")
        f.write(f"**Data:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write(f"**Arquivos Analisados:** {total}\n\n")
        
        f.write("## 1. 🧹 Root Hygiene\n")
        if issues["root_hygiene"]:
            f.write(f"🔴 **{len(issues['root_hygiene'])} arquivos indevidos na raiz:**\n")
            for item in issues["root_hygiene"]:
                f.write(f"- `{item}`\n")
        else:
            f.write("🟢 Raiz limpa.\n")
        
        f.write("\n## 2. 📑 Frontmatter Ausente\n")
        if issues["missing_frontmatter"]:
            f.write(f"🟡 **{len(issues['missing_frontmatter'])} arquivos sem frontmatter:**\n")
            # Limitando lista
            for item in issues["missing_frontmatter"][:50]:
                 f.write(f"- `{item}`\n")
            if len(issues["missing_frontmatter"]) > 50:
                f.write(f"- ... e mais {len(issues['missing_frontmatter']) - 50}\n")
        else:
            f.write("🟢 Todos arquivos possuem frontmatter.\n")
            
        f.write("\n## 3. 👯 H1 Duplicados\n")
        if issues["h1_duplicates"]:
            f.write(f"🔴 **{len(issues['h1_duplicates'])} títulos duplicados:**\n")
            for h1, files in issues["h1_duplicates"].items():
                f.write(f"- **'{h1}'** aparece em:\n")
                for file in files:
                    f.write(f"  - `{file}`\n")
        else:
            f.write("🟢 Títulos H1 únicos.\n")

        f.write("\n## 4. 🔗 Links Quebrados (Estimativa)\n")
        count_broken = sum(len(v) for v in issues["broken_links"].values())
        if issues["broken_links"]:
            f.write(f"🟠 **{count_broken} links potencialmente quebrados:**\n")
            for file, links in list(issues["broken_links"].items())[:50]:
                 f.write(f"- Em `{file}`:\n")
                 for l in links[:5]:
                     f.write(f"  - `[[{l}]]`\n")
                 if len(links) > 5:
                     f.write(f"  - ... (+{len(links)-5})\n")
        else:
            f.write("🟢 Links internos parecem saudáveis.\n")

    print(f"\n{GREEN}Auditoria concluída!{RESET}")
    print(f"Relatório gerado em: {report_path}")
    
    # Resumo console
    print("\n=== RESUMO ===")
    print(f"File System: {len(issues['root_hygiene'])} issues")
    print(f"Frontmatter: {len(issues['missing_frontmatter'])} issues")
    print(f"H1 Duplicates: {len(issues['h1_duplicates'])} issues")
    print(f"Broken Links: {count_broken} issues")

def main():
    parser = argparse.ArgumentParser(description="Architect Linter")
    parser.add_argument("command", choices=["run"], help="Comando a executar")
    args = parser.parse_args()
    
    if args.command == "run":
        run_linter()

if __name__ == "__main__":
    main()
