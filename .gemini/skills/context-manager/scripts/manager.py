import argparse
import os
import sys
import re

# Cores ANSI
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

VAULT_ROOT = os.getcwd()

# Definição dos Modos
MODES = {
    "work": {
        "title": "WORK MODE",
        "path": "02_PROJETOS",
        "moc": "02_PROJETOS/_MOC_Projetos.md",
        "desc": "Foco total na execução de PROJETOS.",
        "tools": ["/status-updater", "/kabak-agent"]
    },
    "learn": {
        "title": "LEARNING MODE",
        "path": "03_APRENDIZADO",
        "moc": "03_APRENDIZADO/_MOC_Aprendizado.md",
        "desc": "Foco em absorção de conteúdo e cursos.",
        "tools": ["/notebook-lm", "/flashcards"]
    },
    "knowledge": {
        "title": "KNOWLEDGE MODE",
        "path": "01_CONHECIMENTO",
        "moc": "01_CONHECIMENTO/_MOC_Conhecimento.md",
        "desc": "Gestão de notas, Zettelkasten e Inbox.",
        "tools": ["/mapa", "/search", "/vault-organizer"]
    },
    "system": {
        "title": "SYSTEM MODE",
        "path": "00_SISTEMA",
        "moc": "00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md",
        "desc": "Manutenção, limpeza e arquitetura do Vault.",
        "tools": ["/validate", "/architect-linter", "/session-log-archiver"]
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner(mode_key):
    mode = MODES[mode_key]
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}   {mode['title']}   {RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{YELLOW}>> {mode['desc']}{RESET}\n")

def read_status_vault():
    status_path = os.path.join(VAULT_ROOT, "STATUS_VAULT.md")
    if not os.path.exists(status_path):
        return None
    
    try:
        with open(status_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Tentar extrair uma seção relevante de status geral, se houver
            # Por enquanto, apenas retorna as primeiras linhas relevantes como resumo
            lines = [line.strip() for line in content.splitlines() if line.strip()]
            return lines[:5] # Retorna as primeiras 5 linhas não vazias
    except Exception as e:
        return [f"Erro ao ler STATUS_VAULT.md: {e}"]

def read_moc_snippet(moc_rel_path):
    moc_path = os.path.join(VAULT_ROOT, moc_rel_path)
    # Tentar encontrar o arquivo caso o nome varie ligeiramente (case insensitive, etc)
    if not os.path.exists(moc_path):
        # Fallback: tentar listar diretório e achar arquivo MOC_*.md
        directory = os.path.dirname(moc_path)
        if os.path.exists(directory):
            files = os.listdir(directory)
            for f in files:
                if f.upper().startswith("MOC_") or f.upper().startswith("_MOC_"):
                    moc_path = os.path.join(directory, f)
                    break
        else:
             return [f"{RED}MOC não encontrado: {moc_rel_path}{RESET}"]

    if not os.path.exists(moc_path):
        return [f"{RED}MOC não encontrado: {moc_rel_path}{RESET}"]

    try:
        with open(moc_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
            snippet = []
            count = 0
            # Tenta pegar seções de "Em Andamento" ou "Prioridades"
            capture = False
            for line in lines:
                if "Andamento" in line or "Prioridade" in line or "Ongoing" in line or "Current" in line:
                    capture = True
                
                if capture:
                    snippet.append(line)
                    count += 1
                
                if count >= 10: # Limite de linhas
                    break
            
            if not snippet:
                # Se não achou seção específica, pega o início
                snippet = lines[:10]
            
            return snippet
    except Exception as e:
        return [f"Erro ao ler MOC: {e}"]

def set_mode(mode_key):
    if mode_key not in MODES:
        print(f"{RED}Modo inválido: {mode_key}{RESET}")
        print(f"Modos disponíveis: {', '.join(MODES.keys())}")
        return

    clear_screen()
    print_banner(mode_key)

    # 1. Status Geral do Vault
    print(f"{BOLD}📊 Status Geral (STATUS_VAULT.md):{RESET}")
    status_lines = read_status_vault()
    if status_lines:
        for line in status_lines:
            print(f"  {line}")
    else:
        print(f"  {YELLOW}STATUS_VAULT.md não encontrado.{RESET}")
    print("-" * 40)

    # 2. Contexto Específico (MOC)
    moc_path = MODES[mode_key]['moc']
    print(f"{BOLD}📑 Contexto Atual ({os.path.basename(moc_path)}):{RESET}")
    moc_content = read_moc_snippet(moc_path)
    if moc_content:
        for line in moc_content:
            print(f"  {line}")
    print("-" * 40)

    # 3. Ferramentas Recomendadas
    print(f"{BOLD}🛠️ Ferramentas Sugeridas:{RESET}")
    for tool in MODES[mode_key]['tools']:
        print(f"  {GREEN}→ {tool}{RESET}")
    print("\n")

def main():
    parser = argparse.ArgumentParser(description="Context Manager para Antigravity")
    subparsers = parser.add_subparsers(dest="command", help="Comando a executar")

    # Comando: set
    set_parser = subparsers.add_parser("set", help="Define o modo de foco")
    set_parser.add_argument("mode", choices=MODES.keys(), help="Modo desejado")

    # Comando: status
    subparsers.add_parser("status", help="Exibe status do contexto atual")

    args = parser.parse_args()

    if args.command == "set":
        set_mode(args.mode)
    elif args.command == "status":
        # Por enquanto, status requer argumento, vamos assumir 'system' ou ler de um state file futuro
        # Para simplificar agora, pedimos para rodar set novamente ou implementamos persistence depois.
        print(f"{YELLOW}Para ver o status, use 'context-manager set <mode>' novamente.{RESET}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
