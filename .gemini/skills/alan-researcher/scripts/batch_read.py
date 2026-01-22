import os
import sys
import fnmatch

# Configuração
VAULT_ROOT = r"c:/Users/gasse/OneDrive/Meu_Segundo_Cerebro"
SEARCH_DIRS = [
    os.path.join(VAULT_ROOT, "03_APRENDIZADO", "Alan_Nicolas_Universe"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "WORKFLOWS"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "PROMPTS"),
    os.path.join(VAULT_ROOT, "01_CONHECIMENTO", "IA_e_Tecnologia")
]

# Configuração dos Temas (Filtros de Busca)
THEMES = {
    "mentalidade": {
        "keywords": ["mentalidade", "mindset", "princípio", "filosofia", "herói", "vilão", "vida lendária", "sobre mim"],
        "output": "TEMP_AGREGADO_MENTALIDADE.md"
    },
    "automacao": {
        "keywords": ["n8n", "agente", "workflow", "script", "python", "api", "claude code", "automação"],
        "output": "TEMP_AGREGADO_AUTOMACAO.md"
    },
    "negocios": {
        "keywords": ["5c", "sistema", "gestão", "pkm", "segundo cérebro", "obsidian", "organização"],
        "output": "TEMP_AGREGADO_NEGOCIOS.md"
    },
    "glossario": {
        "keywords": ["glossário", "definição", "termo", "conceito", "significa", "scaffolding", "janela de contexto", "atomicidade", "zettelkasten", "moc", "pkm", "5c", "mindset"],
        "output": "TEMP_AGREGADO_GLOSSARIO.md"
    },
    "prompts_raw": {
        "keywords": ["prompt", "prompts", "sdr", "clone", "aurora", "atena", "vendedor"],
        "output": "TEMP_AGREGADO_PROMPTS_RAW.md"
    }
}

def aggregate_content(theme_key):
    if theme_key not in THEMES:
        print(f"❌ Tema '{theme_key}' não encontrado. Opções: {list(THEMES.keys())}")
        return

    config = THEMES[theme_key]
    params = config["keywords"]
    output_filename = config["output"]
    output_path = os.path.join(VAULT_ROOT, "02_PROJETOS", "Estudo_Alan_Nicolas", "WIKI", output_filename)
    
    print(f"📚 Iniciando agregação para tema: {theme_key.upper()}...")
    print(f"🔍 Buscando termos: {params}")

    aggregated_content = []
    files_found = 0
    total_chars = 0

    # Header
    aggregated_content.append(f"# ARQUIVO AGREGADO: {theme_key.upper()}")
    aggregated_content.append(f"Gerado para extração profunda via Gemini.\n---\n")

    seen_files = set()

    for search_dir in SEARCH_DIRS:
        if not os.path.exists(search_dir):
            continue

        for root, _, files in os.walk(search_dir):
            for file in files:
                if not file.endswith(".md"):
                    continue
                
                # Evitar duplicatas se pastas se sobrepõem
                if file in seen_files:
                    continue

                full_path = os.path.join(root, file)
                
                # Lógica de Match (Nome ou Conteúdo)
                should_include = False
                file_lower = file.lower()
                
                # 1. Match no nome do arquivo (Peso alto)
                for kw in params:
                    if kw in file_lower:
                        should_include = True
                        break
                
                # 2. Se não match nome, ler conteúdo (apenas se arquivo pequeno < 50KB para performance)
                if not should_include:
                    try:
                        if os.path.getsize(full_path) < 50000:
                            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content_snippet = f.read(2000).lower() # Lê apenas início
                                for kw in params:
                                    if kw in content_snippet:
                                        should_include = True
                                        break
                    except:
                        pass

                if should_include:
                    try:
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                            aggregated_content.append(f"\n\n# 📄 FONTE: {file}\nCaminho: {full_path}\n---\n")
                            aggregated_content.append(content)
                            files_found += 1
                            total_chars += len(content)
                            seen_files.add(file)
                            print(f"   ✅ Adicionado: {file}")
                    except Exception as e:
                        print(f"   ❌ Erro ao ler {file}: {e}")

    # Salvar
    if files_found > 0:
        with open(output_path, "w", encoding="utf-8") as out:
            out.write("".join(aggregated_content))
        print(f"\n✅ Agregação concluída!")
        print(f"📂 Arquivos processados: {files_found}")
        print(f"📝 Total caracteres: {total_chars}")
        print(f"💾 Salvo em: {output_path}")
    else:
        print("⚠️ Nenhum arquivo encontrado para este tema.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python batch_read.py <tema>")
        sys.exit(1)
    
    theme = sys.argv[1].lower()
    aggregate_content(theme)
