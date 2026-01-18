import os
import shutil
import re
import datetime

# --- CONFIGURAÇÃO ---
VAULT_ROOT = r"C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"
CATEGORIES = {
    "01_CONHECIMENTO": ["pdf", "epub", "mobi", "doc", "docx", "txt"],
    "02_PROJETOS": ["png", "jpg", "jpeg", "gif", "svg"],  # Imagens geralmente vão para assets de projetos
    "03_APRENDIZADO": ["mp4", "mp3", "wav"],             # Mídia de aulas
    "04_RECURSOS": ["zip", "rar", "7z", "json", "yaml"], # Recursos/Templates
    "05_PESSOAL": []                                     # Notas pessoais (difícil automatizar só por extensão)
}

# Regex para datas (tentativa de identificar datas em formatos variados)
DATE_REGEX = re.compile(r'(\d{2})[-_/\.]?(\d{2})[-_/\.]?(\d{2,4})')

def get_timestamp():
    return datetime.datetime.now().strftime("%d%b%Y").upper()

def normalize_name(name):
    """
    Aplica padrões de nomenclatura:
    1. Troca espaços por underscores
    2. Remove caracteres especiais
    3. Tenta aplicar CamelCase (capitaliza primeira letra de cada palavra)
    """
    name_no_ext, ext = os.path.splitext(name)
    
    # Substituir espaços e hífens por underscores (exceto hífens de versão/data se estiverem bem padronizados, mas vamos simplificar)
    clean_name = re.sub(r'[\s\-]+', '_', name_no_ext)
    
    # Remover caracteres não permitidos
    clean_name = re.sub(r'[^\w_]', '', clean_name)
    
    # CamelCase: Split por underscore, capitalizar cada parte, juntar
    parts = clean_name.split('_')
    camel_parts = [p.capitalize() for p in parts if p]
    final_name = '_'.join(camel_parts)
    
    # Limite de 60 caracteres (truncar se necessário, mantendo hash ou algo único seria ideal, mas vamos truncar)
    if len(final_name) > 60:
        final_name = final_name[:60]
    
    return f"{final_name}{ext}"

def identify_category(filename):
    """Identifica a categoria baseada na extensão ou nome."""
    ext = filename.split('.')[-1].lower() if '.' in filename else ""
    
    # Lógica simples por extensão
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
            
    # Lógica por palavras-chave no nome
    filename_lower = filename.lower()
    if "projeto" in filename_lower or "briefing" in filename_lower:
        return "02_PROJETOS"
    if "curso" in filename_lower or "aula" in filename_lower:
        return "03_APRENDIZADO"
    if "template" in filename_lower:
        return "04_RECURSOS"
    if "ideia" in filename_lower or "pessoal" in filename_lower:
        return "05_PESSOAL"
        
    # Default para Inbox ou Conhecimento se for texto/markdown não classificado
    return "01_CONHECIMENTO" # Fallback padrão segudo

def scan_and_organize(root_path):
    report = []
    actions = []
    
    report.append(f"# Relatório Vault Organizer - {get_timestamp()}")
    report.append("")
    report.append("## Ações Realizadas")
    report.append("")
    
    # Scan apenas na RAIZ (para não bagunçar pastas já organizadas)
    # ou scan recursivo em pastas específicas de "Inbox" se existissem.
    # Vamos focar na RAIZ para segurança inicial conforme prompt "impar arquivos da raiz".
    files_to_process = [f for f in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, f))]
    
    # Ignorar arquivos do sistema/config
    ignore_list = ["SESSION_LOG.md", "PC_SYNC_LOG.md", "STATUS_VAULT.md", "CLAUDE.md", ".gitignore", ".gitattributes"]
    
    count_moved = 0
    
    for file in files_to_process:
        if file in ignore_list or file.startswith("."):
            continue
            
        original_path = os.path.join(root_path, file)
        
        # 1. Identificar Categoria
        category = identify_category(file)
        target_dir = os.path.join(root_path, category)
        
        # Se 02_PROJETOS ou 03_APRENDIZADO, talvez precisasse de subpasta, 
        # mas vamos mover para a raiz da categoria para o usuário refinar depois (automação segura)
        # OU criar uma pasta "Inbox_Organizer" dentro da categoria.
        target_dir = os.path.join(target_dir, "Inbox_Organizer")
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        # 2. Renomear
        new_name = normalize_name(file)
        new_path = os.path.join(target_dir, new_name)
        
        # Evitar sobrescrever
        if os.path.exists(new_path):
            base, ext = os.path.splitext(new_name)
            new_name = f"{base}_{get_timestamp()}{ext}"
            new_path = os.path.join(target_dir, new_name)
            
        # 3. Mover
        try:
            shutil.move(original_path, new_path)
            actions.append(f"1. ✅ {file} → {category}/Inbox_Organizer/{new_name}")
            count_moved += 1
            
            # 4. Atualizar MOC (Simulado - append no MOC da categoria se existir)
            moc_path = os.path.join(root_path, category, f"_MOC_{category.split('_')[1].capitalize()}.md")
            # Tentar nome padrão MOC se o specífico não existir
            if not os.path.exists(moc_path):
                 # Tenta encontrar qualquer arquivo que comece com _MOC na pasta
                 mocs = [f for f in os.listdir(os.path.join(root_path, category)) if f.startswith("_MOC") and f.endswith(".md")]
                 if mocs:
                     moc_path = os.path.join(root_path, category, mocs[0])
            
            if os.path.exists(moc_path):
                with open(moc_path, "a", encoding="utf-8") as f:
                    f.write(f"\n- [[{new_path}|{new_name}]] - Organizado automaticamente em {get_timestamp()}")
                # report actions update
        except Exception as e:
            actions.append(f"1. ❌ Erro ao mover {file}: {str(e)}")

    if count_moved == 0:
        report.append("Nenhum arquivo solto encontrado na raiz para organizar.")
    else:
        report.extend(actions)
        
    report.append("")
    report.append(f"**Total processado:** {count_moved} arquivos.")
    
    # Salvar relatório
    report_content = "\n".join(report)
    print(report_content) # Para o stdout do agente ver
    
    # Opcional: Salvar em arquivo de log
    with open(os.path.join(root_path, f"RELATORIO_ORGANIZER_{get_timestamp()}.md"), "w", encoding="utf-8") as f:
        f.write(report_content)

if __name__ == "__main__":
    scan_and_organize(VAULT_ROOT)
