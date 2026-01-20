import os
import re
import datetime

# --- CONFIGURAÇÃO ---
VAULT_ROOT = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro"
TARGET_DIR_REL = r"01_CONHECIMENTO"
LOG_DIR = r"00_SISTEMA\RELATORIOS"

def normalize_name(name):
    """
    Aplica padrões de nomenclatura:
    1. Troca espaços por underscores
    2. Remove caracteres especiais (exceto _ e - e .)
    3. Tenta aplicar CamelCase
    """
    name_no_ext, ext = os.path.splitext(name)
    
    # Substituir espaços e hífens por underscores
    clean_name = re.sub(r'[\s\-]+', '_', name_no_ext)
    
    # Remover caracteres não permitidos 
    clean_name = re.sub(r'[^\w_]', '', clean_name)
    
    # CamelCase
    parts = clean_name.split('_')
    camel_parts = [p.capitalize() for p in parts if p]
    final_name = '_'.join(camel_parts)
    
    if len(final_name) > 60:
        final_name = final_name[:60]
    
    return f"{final_name}{ext}"

def batch_rename_recursive(root_path, target_rel_path):
    full_target_path = os.path.join(root_path, target_rel_path)
    report = []
    renamed_count = 0
    errors_count = 0
    
    timestamp = datetime.datetime.now().strftime("%d%b%Y_%H%M").upper()
    report.append(f"# RELATÓRIO BATCH RENAME: {target_rel_path}")
    report.append(f"**Data:** {timestamp}")
    report.append("")
    report.append("## Mudanças Realizadas")
    report.append("")
    
    # Caminhar recursivamente
    for dirpath, dirnames, filenames in os.walk(full_target_path):
        # Renomear arquivos
        for filename in filenames:
            if filename.startswith("."): continue # Ignorar ocultos
            
            # Verificar se precisa renomear (tem espaço ou chars ruins)
            if " " in filename or "-" in filename or len(filename) > 60:
                 pass # Candidato a rename
            else:
                 # Se já parece "ok" (sem espaços), vamos checar se camelcase/limpeza muda algo
                 pass

            new_name = normalize_name(filename)
            
            if new_name != filename:
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_name)
                
                # Evitar conflito
                if os.path.exists(new_file_path):
                     report.append(f"- ⚠️ SKIPPED (Conflito): `{filename}` -> `{new_name}` (Arquivo já existe)")
                     continue
                
                try:
                    os.rename(old_file_path, new_file_path)
                    report.append(f"- ✅ `{filename}` -> `{new_name}`")
                    renamed_count += 1
                except Exception as e:
                    report.append(f"- ❌ ERRO: `{filename}`: {str(e)}")
                    errors_count += 1

    report.append("")
    report.append(f"**Total Renomeados:** {renamed_count}")
    report.append(f"**Total Erros:** {errors_count}")

    # Salvar relatório
    report_file = os.path.join(root_path, LOG_DIR, f"RELATORIO_RENAME_{target_rel_path}_{timestamp}.md")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    print(f"Relatório salvo em: {report_file}")
    print(f"Total renomeados: {renamed_count}")

if __name__ == "__main__":
    batch_rename_recursive(VAULT_ROOT, TARGET_DIR_REL)
