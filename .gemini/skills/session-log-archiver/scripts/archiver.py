
import os
import sys
import shutil
import re
from datetime import datetime

# Configuração
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SESSION_LOG_PATH = os.path.join(ROOT_DIR, "SESSION_LOG.md")
LOGS_DIR = os.path.join(ROOT_DIR, "00_SISTEMA", "LOGS")
BACKUP_EXT = ".bak"
KEEP_ENTRIES = 5

def log(message: str, level: str = "INFO"):
    """Função de log padronizada com emojis."""
    emojis = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌"}
    print(f"{emojis.get(level, '')} [{level}] {message}")

def create_backup(file_path: str) -> str:
    """Cria backup antes de modificar arquivo."""
    try:
        if os.path.exists(file_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{file_path}{BACKUP_EXT}_{timestamp}"
            shutil.copy2(file_path, backup_path)
            log(f"Backup criado: {os.path.basename(backup_path)}", "INFO")
            return backup_path
        return ""
    except Exception as e:
        log(f"Erro ao criar backup: {e}", "ERROR")
        return ""

def parse_session_log(content):
    """Parse session log into header and entries."""
    lines = content.splitlines(keepends=True)
    
    # Regex para identificar entradas
    # Suporta: 18/JAN/2026 e 17/01/2026
    entry_pattern = re.compile(r'^## (?:🟣|🔵) .+? - (\d{2}/(?:[A-Z]{3}|\d{2})/\d{4})')
    
    entries = []
    entry_starts = []
    
    # Encontrar linhas de início
    for i, line in enumerate(lines):
        if entry_pattern.match(line):
            entry_starts.append(i)
            
    if not entry_starts:
        return "".join(lines), []

    # Header é tudo antes da primeira entrada
    header = "".join(lines[:entry_starts[0]])
    
    # Mapping for normalization
    month_map = {
        '01': 'JAN', '02': 'FEV', '03': 'MAR', '04': 'ABR', '05': 'MAI', '06': 'JUN',
        '07': 'JUL', '08': 'AGO', '09': 'SET', '10': 'OUT', '11': 'NOV', '12': 'DEZ'
    }
    
    # Construir entradas
    for i in range(len(entry_starts)):
        start_idx = entry_starts[i]
        end_idx = entry_starts[i+1] if i + 1 < len(entry_starts) else len(lines)
        
        entry_text = "".join(lines[start_idx:end_idx])
        match = entry_pattern.match(lines[start_idx])
        date_str = match.group(1) if match else "UNKNOWN"
        
        # Extrair Mês e Ano
        try:
            day, month_raw, year = date_str.split('/')
            month = month_map.get(month_raw, month_raw) # Normalize if numeric
        except ValueError:
            month, year = "UNKNOWN", "UNKNOWN"
            
        entries.append({
            'text': entry_text,
            'date': date_str,
            'month': month,
            'year': year
        })
        
    return header, entries

def get_archive_path(month, year):
    """Retorna o caminho do arquivo de arquivo para o mês/ano."""
    filename = f"SESSION_LOG_ARQUIVO_{month}_{year}.md"
    return os.path.join(LOGS_DIR, filename)

def update_archive_file(filepath, new_entries):
    """Atualiza (ou cria) o arquivo de arquivo com novas entradas."""
    # Ensure dir exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    header_template = """---
criado: {created_date}
atualizado: {updated_date}
tags:
  - log-archive
  - session-history
periodo: {month}/{year}
---

# SESSION LOG - Arquivo {month}/{year}

**Total de entradas:** {total_count}
**Período:** {start_date} a {end_date}

---

"""
    existing_content = ""
    total_entries = 0
    start_date = "N/A"
    
    # Novas entradas (que são mais recentes que as que estão no arquivo, 
    # se o arquivo for antigo, mas neste caso estamos tirando do BOTTOM do main log,
    # que são as mais antigas DO MAIN LOG.
    # Mas se o arquivo de arquivo já tem Jan 1-10, e estamos arquivando Jan 11-15...
    # Espera. O Log principal é RevChron (Newest Top).
    # Então o bottom (archive candidates) são os OLDEST do log principal.
    # Ex: Log tem Jan 30, Jan 29 ... Jan 1.
    # Keep top 10. Archive Jan 20...Jan 1.
    # Archive tem Jan 20 (top) ... Jan 1 (bottom).
    # Se já existe arquivo com Jan 5...Jan 1.
    # E agora arquivamos Jan 10...Jan 6.
    # Jan 10 é NEWER que Jan 5.
    # Então Jan 10 deve ir ACIMA de Jan 5.
    # O arquivo resultante deve ser RevChron.
    # Então INSERIMOS no topo do corpo.*/
    
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Tentar separar header e corpo
        # Procurar o último '---'
        parts = content.split('---')
        if len(parts) >= 3:
            # Assumindo Frontmatter (--- ... ---) e Header Separator (---)
            # Geralmente o template tem 3 '---'.
            # 1. Start yaml, 2. End yaml, 3. Header separator
            # Vamos achar onde o conteudo começa
            # Uma heurística segura é achar o último '---' seguido de quebra de linha
            last_separator_idx = content.rfind('\n---')
            if last_separator_idx != -1:
                display_header = content[:last_separator_idx+5] # Inclui o \n---\n
                body = content[last_separator_idx+5:].lstrip()
            else:
                display_header = content # Fallback
                body = ""
        else:
             display_header = content
             body = ""
             
        # Contar entradas existentes (aprox)
        entry_pattern = re.compile(r'^## (?:🟣|🔵)', re.MULTILINE)
        total_entries = len(entry_pattern.findall(body))
    else:
        # Criar novo
        # Pegar data da primeira entrada (a mais antiga deste lote)
        # As entradas passadas para esta função são um slice da lista original.
        # A lista original estava RevChron (Newest First).
        # Então new_entries[0] é a mais recente deste lote.
        # new_entries[-1] é a mais antiga deste lote.
        display_header = "" # Será gerado
        body = ""
        total_entries = 0

    # Adicionar novas entradas no TOPO do corpo (para manter RevChron)
    # new_entries maintenance order?
    # Eles vêm do slice [30:] do log principal.
    # O log principal é RevChron.
    # Então new_entries[0] é mais novo que new_entries[1].
    # Está correto concatená-los: entry0 + entry1 + entry2...
    # E colocar esse bloco ANTES do body existente.
    
    new_block = "".join([e['text'] for e in new_entries])
    final_body = new_block + "\n" + body
    
    total_entries += len(new_entries)
    
    # Atualizar Header
    # Mês e Ano pegamos do primeiro entry do lote (assumindo arquivo por mês)
    month = new_entries[0]['month']
    year = new_entries[0]['year']
    
    # Calcular datas min/max para o header é complexo parsar tudo, vamos usar current stats
    # Simplesmente atualizando metadata básica
    
    final_header = header_template.format(
        created_date=current_date, # Ajustar se novo? Não vamos complicar parsing de yaml agora
        updated_date=current_date,
        month=month,
        year=year,
        total_count=total_entries,
        start_date="Ver log", # Placeholder para não parsar tudo
        end_date="Ver log"
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_header + final_body)
        
    return os.path.basename(filepath), len(new_entries)


def main():
    log("Iniciando session-log-archiver...", "INFO")
    
    if not os.path.exists(SESSION_LOG_PATH):
        log(f"Arquivo não encontrado: {SESSION_LOG_PATH}", "ERROR")
        sys.exit(1)
        
    # 1. Ler e Parsear
    with open(SESSION_LOG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    header, entries = parse_session_log(content)
    total_entries = len(entries)
    
    log(f"Total de entradas encontradas: {total_entries}", "INFO")
    
    if total_entries <= KEEP_ENTRIES:
        log(f"SESSION_LOG.md já está enxuto ({total_entries} entradas). Limite é {KEEP_ENTRIES}.", "SUCCESS")
        return
        
    log(f"Iniciando arquivamento de {total_entries - KEEP_ENTRIES} entradas antigas...", "WARN")
    
    # 2. Backup
    backup_file = create_backup(SESSION_LOG_PATH)
    if not backup_file:
        sys.exit(1)
        
    # 3. Separar
    keep_entries = entries[:KEEP_ENTRIES]
    archive_entries = entries[KEEP_ENTRIES:]
    
    # 4. Agrupar por arquivo destino (Mês/Ano)
    grouped_archives = {}
    for entry in archive_entries:
        key = (entry['month'], entry['year'])
        if key not in grouped_archives:
            grouped_archives[key] = []
        grouped_archives[key].append(entry)
        
    # 5. Escrever Arquivos de Arquivo
    created_files = []
    for (month, year), batch in grouped_archives.items():
        if month == "UNKNOWN":
            log("Encontradas entradas com data desconhecida. Arquivando em UNKNOWN.", "WARN")
            
        filepath = get_archive_path(month, year)
        fname, count = update_archive_file(filepath, batch)
        created_files.append(f"{fname} ({count} entradas)")
        
    # 6. Reescrever SESSION_LOG.md
    log("Atualizando SESSION_LOG.md...", "INFO")
    
    # Adicionar nota de arquivamento no header
    # Procurar onde inserir a nota. Geralmente logo após o título ou na mensagem.
    # Vamos inserir um Append no Header original se ele tiver metadados.
    # Ou simplesmente concatenar.
    
    new_content = header + "".join([e['text'] for e in keep_entries])
    
    with open(SESSION_LOG_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    # 7. Relatório Final
    report = f"""
📦 SESSION LOG ARQUIVAMENTO CONCLUÍDO

📋 Estatísticas:
   - Total anterior: {total_entries}
   - Mantidas: {len(keep_entries)}
   - Arquivadas: {len(archive_entries)}

📁 Arquivos Atualizados:
   {chr(10).join(['   - ' + f for f in created_files])}

💾 Backup: 
   - {os.path.basename(backup_file)}

✅ SESSION_LOG.md otimizado com sucesso!
"""
    log(report, "SUCCESS")

if __name__ == "__main__":
    main()
