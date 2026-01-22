import os
import sys

# Caminhos base para busca (ajustar conforme estrutura do usuário)
# Usando caminho relativo ao CWD se possível, ou absoluto
VAULT_ROOT = r"c:/Users/gasse/OneDrive/Meu_Segundo_Cerebro"
SEARCH_PATHS = [
    os.path.join(VAULT_ROOT, "03_APRENDIZADO", "Alan_Nicolas_Universe"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "WORKFLOWS"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "PROMPTS"),
    os.path.join(VAULT_ROOT, "04_RECURSOS", "Glossarios"),
    os.path.join(VAULT_ROOT, "01_CONHECIMENTO", "IA_e_Tecnologia")
]

def search_files(query):
    # Tratamento simples de query
    query_terms = query.lower().split()
    results = []

    print(f"🔎 Pesquisando por '{query}' no Universo Alan Nicolas...\n")
    print(f"Diretórios alvo: {len(SEARCH_PATHS)}")

    for search_path in SEARCH_PATHS:
        if not os.path.exists(search_path):
            continue

        for root, _, files in os.walk(search_path):
            for file in files:
                if not file.endswith(".md"):
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        content_lower = content.lower()
                        name_lower = file.lower()

                        score = 0
                        
                        match_count = 0
                        for term in query_terms:
                            if term in name_lower:
                                score += 10
                                match_count += 1
                            elif term in content_lower:
                                score += 1
                                match_count += 1
                        
                        if "alan" in content_lower or "lendária" in content_lower or "5c" in content_lower:
                             score += 2

                        if match_count >= len(query_terms) * 0.6:
                            results.append({
                                "path": file_path,
                                "name": file,
                                "score": score,
                                "preview": content[:200].replace("\n", " ") + "..."
                            })
                except Exception as e:
                    continue

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:10]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python search_alan.py <termo de busca>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    hits = search_files(query)

    if not hits:
        print("❌ Nenhum resultado encontrado no contexto local.")
    else:
        print(f"✅ Encontrados {len(hits)} documentos relevantes:\n")
        for i, hit in enumerate(hits):
            print(f"{i+1}. [{hit['name']}] (Score: {hit['score']})")
            print(f"   Path: {hit['path']}")
            print(f"   Preview: {hit['preview']}\n")
