# PROMPT: Criar Skill Antigravity - mapa

**Para:** Gemini 3 Pro (Antigravity)
**Data:** 18/JAN/2026
**Prioridade:** MÁXIMA (Skill #2 do Top 4)
**Contexto:** Fase 7.4 - Sistemas Bi-IA

---

## 🎯 OBJETIVO

Criar a skill `mapa` que gera um **índice completo e atualizado do Vault**.
O objetivo é criar um arquivo único (`INDICE_VAULT_COMPLETO.md`) que represente a estrutura do vault, permitindo que a IA entenda onde estão os arquivos sem precisar fazer `list_dir` recursivos caros ou ler milhares de arquivos.

---

## 📋 ESPECIFICAÇÕES DA SKILL

### Metadados

- **Nome:** `mapa`
- **Triggers:**
  - "mapa"
  - "índice"
  - "gerar indice"
  - "update index"
- **Versão:** 1.0

### 🔧 Funcionalidades Obrigatórias

#### 1. Mapeamento Recursivo

- Percorrer todo o vault a partir da raiz.
- **Ignorar:** `.git`, `.obsidian`, `.claude`, `.gemini`, `node_modules`, `.trash`, `.venv`, `__pycache__`.
- **Ignorar:** Arquivos de imagem/binários (focar em `.md`, `.txt`, `.py`).

#### 2. Extração de Metadados (Leve)

- Para cada arquivo `.md`, ler a **primeira linha não vazia** (assumindo ser o Título H1).
- Se começar com `#`, usar o texto como descrição.
- Se não, usar o nome do arquivo.

#### 3. Geração de Árvore Markdown

- Gerar uma lista indentada representando a estrutura de pastas.
- Exemplo:

  ```markdown
  - 📂 01_CONHECIMENTO
    - 📂 IA
      - 📄 [[Conceitos_Basicos.md]] - Conceitos Básicos de IA
  ```

- **Links:** Usar WikiLinks `[[Arquivo]]`.

#### 4. Output Fixo

- **Arquivo Alvo:** `00_SISTEMA/INDICE_VAULT_COMPLETO.md` (Verificar se a pasta `00_SISTEMA` existe, se não, criar).
- **Sobrescrever:** Sempre gerar um novo arquivo limpo.

---

## 💻 REQUISITOS TÉCNICOS

- **Script:** `scripts/indexer.py` (ou `mapa.py`)
- **Performance:** Deve ser rápido. Ler apenas a primeira linha de cada arquivo.
- **Formatação:**
  - Cabeçalho com Data/Hora da geração.
  - Estatísticas: Total Arquivos, Total Pastas.

## 🛡️ SAFETY

- Não deletar arquivos (exceto o próprio índice anterior).
- Tratar erros de encoding ao ler arquivos (utf-8, fallback cp1252).

---

## ✅ CHECKLIST DE ENTREGA

- [ ] Estrutura `.gemini/skills/mapa/`
- [ ] Script `mapa.py`
- [ ] Teste de geração
- [ ] Verificar se o output é um Markdown válido e navegável

---
**FIM DO PROMPT**
