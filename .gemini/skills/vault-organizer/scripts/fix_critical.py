import os
import shutil

VAULT_ROOT = r"C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"

# 1. MOVES (Map: Source -> Destination)
MOVES = {
    r"03_APRENDIZADO\Cursos_Ativos\DeFi_Journey\MATERIAL_ORIGINAL\TEMPLATE_MODULO_PADRAO.md": r"04_RECURSOS\TEMPLATES\TEMPLATE_Modulo_Padrao.md",
    r"03_APRENDIZADO\Cursos_Ativos\DeFi_Journey\_BACKUP_15AUG2025\SISTEMA_CONTINUIDADE\TEMPLATE_SESSION_STARTER.md": r"04_RECURSOS\TEMPLATES\TEMPLATE_Session_Starter.md"
}

# 2. RENAMES (Map: Old Path -> New Name (just filename))
RENAMES = {
    r"01_CONHECIMENTO\Tecnologia\Inteligencia_Artificial\Claude_Code_Templates_Repositorio.md": "TEMPLATE_Claude_Code_Repositorio.md",
    r"03_APRENDIZADO\Alan_Nicolas_Universe\Alan_Nicolas_Academia_Lendaria\vida_lendaria\Cursos_TEMPLATE-ESTRUTURA-CURSO.md": "TEMPLATE_Estrutura_Curso.md"
}

def run_fixes():
    print("# RELATÓRIO DE CORREÇÃO (GUARDIAN LEVEL 2)")
    print("-" * 50)
    
    # 1. Execute Moves
    print("\n## 1. Mover Arquivos (Localização)")
    for src_rel, dest_rel in MOVES.items():
        src = os.path.join(VAULT_ROOT, src_rel)
        dest = os.path.join(VAULT_ROOT, dest_rel)
        
        if os.path.exists(src):
            try:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.move(src, dest)
                print(f"✅ MOVIDO:\n   De: {src_rel}\n   Para: {dest_rel}")
            except Exception as e:
                print(f"❌ ERRO ao mover {src_rel}: {e}")
        else:
            print(f"⚠️ ARQUIVO NÃO ENCONTRADO: {src_rel}")

    # 2. Execute Renames
    print("\n## 2. Renomear Arquivos (Nomenclatura)")
    for old_rel, new_name in RENAMES.items():
        old_path = os.path.join(VAULT_ROOT, old_rel)
        dir_name = os.path.dirname(old_path)
        new_path = os.path.join(dir_name, new_name)
        
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"✅ RENOMEADO:\n   De: {os.path.basename(old_rel)}\n   Para: {new_name}")
            except Exception as e:
                print(f"❌ ERRO ao renomear {old_rel}: {e}")
        else:
            print(f"⚠️ ARQUIVO NÃO ENCONTRADO: {old_rel}")

if __name__ == "__main__":
    run_fixes()
