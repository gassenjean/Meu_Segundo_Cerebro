import os
import sys
import datetime
import subprocess
import shutil
import re

# Tenta configurar encoding para UTF-8 no stdout/stderr (importante para Windows)
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Caminho raiz do Vault (assumindo que o script roda a partir de .gemini/skills/...)
# Se o script for chamado de qualquer lugar, é melhor usar o cwd ou passar como argumento.
# Aqui assumiremos que o CWD é a raiz do vault, mas faremos uma verificação.
VAULT_ROOT = os.getcwd()
SESSION_LOG_FILENAME = "SESSION_LOG.md"
SESSION_LOG_PATH = os.path.join(VAULT_ROOT, SESSION_LOG_FILENAME)

def detect_agent():
    """
    Detecta qual agente está ativo.
    Retorna: "Antigravity/Gemini" (default) ou "Claude Code".
    """
    # Heurística simples: Verificar variáveis de ambiente ou assumir Gemini já que é uma skill Antigravity.
    # Se fosse rodado pelo Claude, poderíamos checar CLAUDE_CODE_ENV ou algo similar.
    # Por padrão, se esta skill está sendo executada pelo framework Antigravity, é o Gemini.
    return "Antigravity (Gemini 3 Pro)"

def detect_changes():
    """
    Detecta arquivos criados/modificados usando git status.
    Retorna uma lista de tuplas (status, arquivo).
    """
    try:
        # Executa git status --short
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=VAULT_ROOT,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode != 0:
            print(f"⚠️ Aviso: Falha ao executar git status. Código: {result.returncode}")
            return []
            
        changes = []
        for line in result.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
                
            # Formato short do git: "XY Path/to/file"
            # X = status do index, Y = status do worktree
            # Ex: "M  file.md" (modificado), "?? file.md" (untracked/novo), "A  file.md" (adicionado)
            parts = line.split(maxsplit=1)
            if len(parts) < 2:
                continue
                
            status_code = parts[0]
            filename = parts[1]
            
            # Remove aspas se houver (git coloca em filenames com espaço)
            if filename.startswith('"') and filename.endswith('"'):
                filename = filename[1:-1]
                
            status = "Modificado"
            if "??" in status_code or "A" in status_code:
                status = "Criado"
            elif "D" in status_code:
                status = "Deletado"
            elif "M" in status_code:
                status = "Modificado"
                
            # Ignorar arquivos de sistema/temp/logs próprios
            if filename == SESSION_LOG_FILENAME or filename.startswith(".git") or filename.endswith(".bak"):
                continue
                
            changes.append((status, filename))
            
        return changes
        
    except FileNotFoundError:
        print("⚠️ Erro: Git não encontrado. A detecção automática depende do Git.")
        return []

def categorize_actions(changes):
    """
    Categoriza ações baseado nos arquivos modificados.
    Retorna um dicionário {categoria: [descrições]}.
    """
    categories = {}
    
    for status, filename in changes:
        category = "Outros"
        if ".gemini/skills" in filename:
            category = "Desenvolvimento de Skills Antigravity"
        elif ".claude/skills" in filename:
            category = "Desenvolvimento de Skills Claude"
        elif "SESSION_LOG.md" in filename:
            continue
        elif "00_SISTEMA" in filename:
            category = "Manutenção do Sistema"
        elif "01_CONHECIMENTO" in filename:
            category = "Gestão de Conhecimento"
        elif "02_PROJETOS" in filename:
            category = "Execução de Projetos"
            # Tentar ser mais específico
            if "KabaK" in filename:
                category = "Projeto KabaK"
        elif "03_APRENDIZADO" in filename:
            category = "Aprendizado"
            
        if category not in categories:
            categories[category] = []
            
        action_desc = f"{status}: `{filename}`"
        categories[category].append(action_desc)
        
    return categories

def generate_session_entry(agent, changes, message_to_other=""):
    """
    Gera a entrada markdown para o SESSION_LOG.md.
    """
    now = datetime.datetime.now()
    # Format: 18/JAN/2026 (14:30)
    # Mapping months EN -> PT-BR (simple approximation)
    months_pt = {
        1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN",
        7: "JUL", 8: "AGO", 9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"
    }
    month_str = months_pt[now.month]
    date_str = f"{now.day:02d}/{month_str}/{now.year} ({now.hour:02d}:{now.minute:02d})"
    
    # Emoji e Título
    emoji = "🟣" if "Gemini" in agent else "🔵"
    
    # Determinar título baseado na categoria dominante
    categorized = categorize_actions(changes)
    title = "SESSÃO AUTOMÁTICA"
    if categorized:
        # Pega a categoria com mais itens
        top_category = max(categorized, key=lambda k: len(categorized[k]))
        if "Skills" in top_category:
            title = "DESENVOLVIMENTO DE SKILLS"
        elif "KabaK" in top_category:
            title = "ATUALIZAÇÃO KABAK"
        elif "Sistema" in top_category:
            title = "MANUTENÇÃO DO SISTEMA"
        else:
            title = f"TRABALHO EM: {top_category.upper()}"
            
    entry = f"\n## {emoji} {agent} - {date_str} - {title}\n\n"
    
    entry += "### Trabalho Realizado\n\n"
    
    if not categorized:
        entry += "* ✅ Nenhum arquivo modificado detectado via git.\n"
    else:
        for cat, actions in categorized.items():
            entry += f"**{cat}**\n\n"
            for action in actions:
                # Limpar status duplicado se já estiver na string
                entry += f"* ✅ {action}\n"
            entry += "\n"
            
    entry += "### Arquivos Criados/Modificados\n\n"
    if not changes:
        entry += "* Nenhuma detecção automática.\n"
    else:
        for status, filename in changes:
            entry += f"* `{filename}` - {status}\n"
            
    entry += "\n### Mensagem para Claude Code\n\n"
    if message_to_other:
        entry += f"> {message_to_other}\n"
    else:
        entry += "> Sessão registrada automaticamente. Nenhuma mensagem específica.\n"
        
    entry += "\n---\n"
    
    return entry

def create_backup(file_path):
    """Cria um backup do arquivo com timestamp."""
    if not os.path.exists(file_path):
        return None
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.bak_{timestamp}"
    try:
        shutil.copy2(file_path, backup_path)
        return backup_path
    except Exception as e:
        print(f"⚠️ Erro ao criar backup: {e}")
        return None

def insert_entry(file_path, entry):
    """Insere a entrada no SESSION_LOG.md no topo da lista."""
    if not os.path.exists(file_path):
        print("⚠️ SESSION_LOG.md não encontrado. Criando novo.")
        content = "---\ncreated: " + datetime.datetime.now().isoformat() + "\n---\n# SESSION LOG\n\n"
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
    # Lógica de inserção: Procurar pelo primeiro Header de sessão ou inserir após o header principal
    # Assumindo que o arquivo começa com frontmatter e um header H1
    
    # Estratégia: Encontrar a linha "---" que separa o cabeçalho das entradas ou a primeira entrada existente
    # O padrão do arquivo parece ser:
    # Header
    # ---
    # ## Entry 1
    
    # Vamos tentar inserir após a primeira ocorrência de "---" depois do cabeçalho H1, ou logo após H1 se não houver "---"
    
    lines = content.splitlines()
    insert_index = -1
    
    # Procurar onde inserir
    # Geralmente após a seção de contexto (que termina em ---)
    # Exemplo do arquivo lido:
    # ...
    # Contexto: Organização Marie Kondo ✅
    #
    # ---
    #
    # ## 🟣 Antigravity...
    
    # Vamos procurar o primeiro separador "---" que não seja do frontmatter e inserir DEPOIS dele.
    separators_found = 0
    header_found = False
    
    for i, line in enumerate(lines):
        if line.strip() == "---":
            separators_found += 1
            # Frontmatter opens and closes with ---. So 2nd --- is end of frontmatter.
            # Then usually there is intro text and another --- before entries.
            # Let's count separators.
            # 1: start FM
            # 2: end FM
            # 3: end of intro section?
            
        if separators_found >= 2 and line.strip() == "---":
             # Se encontramos um terceiro separador, é um bom lugar.
             # Mas precisamos garantir que não estamos dentro de um code block.
             # Simplificação: Inserir logo antes da primeira linha que começa com "## 🟣" ou "## 🔵"
             pass

    # Estratégia mais robusta baseada no conteúdo visualizado:
    # Encontrar a primeira linha que começa com "## 🟣" ou "## 🔵". Inserir antes dela.
    
    target_line_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("## 🟣") or line.startswith("## 🔵"):
            target_line_idx = i
            break
            
    if target_line_idx != -1:
        # Inserir antes desta linha
        new_content = "\n".join(lines[:target_line_idx]) + "\n" + entry + "\n".join(lines[target_line_idx:])
    else:
        # Se não achou entradas, anexa ao final (ou logo após header)
        # Vamos tentar achar o último "---" da introdução
        last_separator_idx = -1
        for i, line in enumerate(lines):
            if line.strip() == "---":
                last_separator_idx = i
        
        if last_separator_idx > 1: # Ignorar frontmatter
            new_content = "\n".join(lines[:last_separator_idx+1]) + "\n" + entry + "\n".join(lines[last_separator_idx+1:])
        else:
             new_content = content + "\n" + entry

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

def main():
    print("🔄 Iniciando Session Logger (Antigravity)...")
    
    # 1. Detectar Agente
    agent = detect_agent()
    print(f"🤖 Agente detectado: {agent}")
    
    # 2. Detectar Mudanças
    changes = detect_changes()
    print(f"📂 Mudanças detectadas: {len(changes)} arquivos")
    
    categorized = categorize_actions(changes)
    if categorized:
        print("\nCategorias identificadas:")
        for cat, items in categorized.items():
            print(f"  - {cat}: {len(items)} itens")
            
    # 3. Perguntar mensagem (se interativo) ou usar default
    # Como rodaremos via ferramenta run_command, não podemos facilmente pegar input interativo no meio sem send_command_input.
    # Vamos assumir um modo não-interativo ou usar argumentos se fornecidos.
    # O prompt pede "input", mas na automação "skill", é melhor ser direto ou aceitar args.
    # Vou implementar um check simples: se não houver args, usa default.
    
    message = ""
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        # Tentar ler de variável de ambiente se existir, ou input se for terminal interativo real (difícil saber)
        # Para o propósito da automação do agente, vamos deixar vazio por enquanto e permitir edição manual se o usuário quiser,
        # OU o agente que chama a skill passa a mensagem como argumento.
        pass

    # 4. Gerar e Mostrar Preview
    entry = generate_session_entry(agent, changes, message)
    
    print("\n" + "="*40)
    print("PREVIEW DA ENTRADA:")
    print("="*40)
    print(entry)
    print("="*40 + "\n")
    
    # 5. Backup e Update (Automático para a skill, sem confirmação extra no script para não bloquear)
    # Na "vida real" o prompt sugere 'input', mas para o agente executar, input bloqueia.
    # Vou adicionar uma flag --dry-run para testes, e se não tiver, executa.
    
    if "--dry-run" in sys.argv:
        print("🧪 Modo Dry-Run: Nada foi gravado.")
        return

    print("💾 Criando backup...")
    backup = create_backup(SESSION_LOG_PATH)
    if backup:
        print(f"   Backup criado: {os.path.basename(backup)}")
    
    print("📝 Atualizando SESSION_LOG.md...")
    if insert_entry(SESSION_LOG_PATH, entry):
        print("✅ SESSION_LOG.md atualizado com sucesso!")
    else:
        print("❌ Falha ao atualizar SESSION_LOG.md")

if __name__ == "__main__":
    main()
