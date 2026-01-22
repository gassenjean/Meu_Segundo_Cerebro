import os
import re
from datetime import datetime

# Configuração de Caminhos
VAULT_ROOT = r"c:/Users/gasse/OneDrive/Meu_Segundo_Cerebro"
TARGET_PATHS = [
    os.path.join(VAULT_ROOT, "03_APRENDIZADO", "Alan_Nicolas_Universe"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "WORKFLOWS"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "PROMPTS"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "Glossarios"),
    os.path.join(VAULT_ROOT, "01_CONHECIMENTO", "IA_e_Tecnologia")
]
OUTPUT_FILE = os.path.join(VAULT_ROOT, "02_PROJETOS", "Estudo_Alan_Nicolas", "CONHECIMENTO_CONSOLIDADO.md")

def extract_key_concepts(content):
    """Extrai blocos semânticos importantes baseados em headers e keywords."""
    concepts = []
    
    # Regex para capturar headers importantes
    patterns = [
        r"(?i)^#+\s*.*(princípio|regra|lei|definição|conceito).*",
        r"(?i)^#+\s*.*(workflow|fluxo|processo).*",
        r"(?i)^#+\s*.*(prompt|instrução).*"
    ]
    
    lines = content.split('\n')
    capture = False
    buffer = []
    
    for line in lines:
        # Verifica se linha é um header de interesse
        is_header = any(re.match(p, line) for p in patterns)
        
        if is_header:
            if buffer:
                concepts.append("\n".join(buffer))
                buffer = []
            capture = True
            buffer.append(line)
        elif capture:
            if line.startswith("#") and not is_header: # Outro header parou a captura
                capture = False
                if buffer:
                    concepts.append("\n".join(buffer))
                    buffer = []
            else:
                buffer.append(line)
                
    if buffer:
        concepts.append("\n".join(buffer))
        
    return concepts

def index_vault():
    print(f"🚀 Iniciando Indexação Profunda do Universo Alan Nicolas...")
    print(f"📅 Data: {datetime.now().isoformat()}")
    
    knowledge_base = []
    
    file_count = 0
    concept_count = 0
    
    # Header do Arquivo Consolidado
    knowledge_base.append(f"# 🧠 CONHECIMENTO CONSOLIDADO: ALAN NICOLAS")
    knowledge_base.append(f"**Gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    knowledge_base.append(f"**Fonte:** Indexação Local Profunda")
    knowledge_base.append(f"---\n")

    for path in TARGET_PATHS:
        if not os.path.exists(path):
            continue
            
        category_name = os.path.basename(path)
        knowledge_base.append(f"## 📂 Categoria: {category_name}\n")
        
        for root, _, files in os.walk(path):
            for file in files:
                if not file.endswith(".md"):
                    continue
                    
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        
                        # Filtro Básico: Tem algo do Alan?
                        if "alan" in content.lower() or "lendária" in content.lower() or "5c" in content.lower() or "agente" in content.lower():
                            
                            concepts = extract_key_concepts(content)
                            
                            if concepts:
                                file_count += 1
                                link = f"[[{file[:-3]}]]" # Wikilink
                                knowledge_base.append(f"### 📄 Fonte: {link}")
                                
                                for concept in concepts:
                                    clean_concept = concept.strip()
                                    if len(clean_concept) > 50: # Evitar lixo
                                        knowledge_base.append(clean_concept)
                                        knowledge_base.append("\n---\n")
                                        concept_count += 1
                                        
                except Exception as e:
                    print(f"❌ Erro ao ler {file}: {e}")

    # Salvar Resultado
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(knowledge_base))
        
    print(f"\n✅ Indexação concluída!")
    print(f"📄 Arquivos processados: {file_count}")
    print(f"💡 Conceitos extraídos: {concept_count}")
    print(f"💾 Salvo em: {OUTPUT_FILE}")

if __name__ == "__main__":
    index_vault()
