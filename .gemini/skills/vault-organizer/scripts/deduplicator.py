import os
import hashlib
import shutil
import datetime
import sys
from pathlib import Path

# Configuração
VAULT_ROOT = r"C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TRASH_DIR = os.path.join(VAULT_ROOT, "00_SISTEMA", "TRASH_DUPLICATES", TIMESTAMP)
REPORT_FILE = os.path.join(VAULT_ROOT, "00_SISTEMA", "RELATORIOS", f"RELATORIO_DEDUPLICACAO_{TIMESTAMP}.md")

# Pastas a ignorar
IGNORE_DIRS = {".git", ".gemini", ".claude", ".obsidian", "TRASH_DUPLICATES", "$RECYCLE.BIN", "System Volume Information"}

def calculate_hash(file_path, chunk_size=8192):
    """Calcula SHA256 do arquivo."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
        return None

def score_path(file_path):
    """
    Atribui uma pontuação ao caminho. Menor pontuação = Melhor candidato a manter.
    """
    path_str = str(file_path)
    score = 0
    
    # 1. Preferência por pastas raiz numeradas (Menor é melhor, mas todas são boas)
    if "00_SISTEMA" in path_str: score -= 50
    elif "01_CONHECIMENTO" in path_str: score -= 40
    elif "04_RECURSOS" in path_str: score -= 30 # Templates e recursos devem ser canonicos
    elif "02_PROJETOS" in path_str: score -= 20
    elif "03_APRENDIZADO" in path_str: score -= 10
    elif "05_PESSOAL" in path_str: score -= 10
    
    # 2. Penalizar pastas de backup ou confusas
    if "Alan_Nicolas_Universe" in path_str: score += 100
    if "Alan_Vault_Original" in path_str: score += 100
    if "Vault_Original" in path_str: score += 100
    if "_BACKUP" in path_str.upper(): score += 200
    if "Arquivo_Antigo" in path_str: score += 150
    if "Lixeira" in path_str: score += 200
    if "temp" in path_str.lower(): score += 50
    
    # 3. Preferência de Nomenclatura
    filename = os.path.basename(path_str)
    if " " in filename: score += 10 # Penaliza espaços
    if filename.count("_") > 0: score -= 5 # Prefere underscores
    
    # Preferir "IA" sobre "Inteligencia_Artificial" na pasta (Convenção curta)
    # Mas se o arquivo estiver em "Inteligencia_Artificial" ele ganha pontos se não tiver "Alan_Nicolas..."
    # Vamos deixar neutro ou levemente penalizar caminhos muito longos
    
    # 4. Caminhos mais curtos tendem a ser melhores (menos subpastas desnecessárias)
    score += len(file_path.parts) * 2
    
    return score

def find_duplicates(root_path):
    """Varre o vault e encontra duplicatas por hash."""
    hashes = {}
    print(f"🔍 Varrendo {root_path}...")
    
    for root, dirs, files in os.walk(root_path):
        # Filtrar diretórios ignorados
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        
        for file in files:
            if not file.endswith(".md"): # Focar em MD por enquanto, mas pode ser removido
                continue
                
            full_path = Path(os.path.join(root, file))
            file_hash = calculate_hash(full_path)
            
            if file_hash:
                if file_hash not in hashes:
                    hashes[file_hash] = []
                hashes[file_hash].append(full_path)
                
    # Filtrar apenas hashes com > 1 arquivo
    duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
    return duplicates

def process_duplicates(duplicates, dry_run=True):
    """Processa as duplicatas identicadas."""
    actions = []
    stats = {"kept": 0, "trashed": 0, "bytes_saved": 0}
    
    if not dry_run and not os.path.exists(TRASH_DIR):
        os.makedirs(TRASH_DIR)
        
    for file_hash, paths in duplicates.items():
        # Ordenar caminhos pelo score (menor score = vencedor)
        paths.sort(key=score_path)
        
        winner = paths[0]
        losers = paths[1:]
        
        actions.append(f"### Grupo Hash: {file_hash[:8]}...")
        actions.append(f"- 🏆 **MANTER:** `{winner}` (Score: {score_path(winner)})")
        
        for loser in losers:
            actions.append(f"- 🗑️ **LIXO:** `{loser}` (Score: {score_path(loser)})")
            
            file_size = os.path.getsize(loser)
            stats["bytes_saved"] += file_size
            stats["trashed"] += 1
            
            if not dry_run:
                try:
                    # Estrutura no lixo para evitar colisão
                    # TRASH/Timestamp/Drive/Path/To/File
                    # Simplificado: TRASH/Timestamp/Hash_Filename
                    
                    # Vamos manter a estrutura relativa para facilitar restore
                    rel_path = loser.relative_to(VAULT_ROOT)
                    dest_path = os.path.join(TRASH_DIR, rel_path)
                    
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.move(str(loser), dest_path)
                    # actions.append(f"  - ✅ Movido para TRASH")
                except Exception as e:
                    actions.append(f"  - ❌ Erro ao mover: {e}")
            
    stats["kept"] = len(duplicates)
    return actions, stats

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("🚨 MODO DE APLICAÇÃO ATIVO - Arquivos serão movidos para TRASH!")
    else:
        dry_run = True
        print("🧪 MODO DRY-RUN (Simulação) - Use --apply para executar.")

    duplicates = find_duplicates(VAULT_ROOT)
    print(f"📦 Encontrados {len(duplicates)} grupos de duplicatas.")
    
    actions, stats = process_duplicates(duplicates, dry_run=dry_run)
    
    # Gerar Relatório
    report_content = [
        f"# Relatório de Deduplicação - {TIMESTAMP}",
        f"",
        f"- **Modo:** {'Simulação (Dry Run)' if dry_run else 'Execução Real'}",
        f"- **Grupos Duplicados:** {len(duplicates)}",
        f"- **Arquivos para Lixo:** {stats['trashed']}",
        f"- **Espaço Recuperável:** {stats['bytes_saved'] / 1024 / 1024:.2f} MB",
        f"- **Pasta de Lixo:** `{TRASH_DIR}`" if not dry_run else "- **Pasta de Lixo (Prevista):** .../TRASH_DUPLICATES/...",
        f"",
        "## Detalhes",
        ""
    ]
    report_content.extend(actions)
    
    # Garantir diretório de relatórios
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_content))
        
    print(f"📄 Relatório gerado em: {REPORT_FILE}")
    print("\nResumo:")
    print(f"Grupos: {len(duplicates)} | Arquivos Lixo: {stats['trashed']}")

if __name__ == "__main__":
    main()
