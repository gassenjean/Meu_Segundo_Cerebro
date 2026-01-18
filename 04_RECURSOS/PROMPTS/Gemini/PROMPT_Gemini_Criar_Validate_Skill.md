# PROMPT: Criar Skill Antigravity - validate

**Para:** Gemini 3 Pro (Antigravity)
**Data:** 18/JAN/2026
**Prioridade:** MÁXIMA (Skill #1 do Top 4)
**Contexto:** Fase 7.4 - Sistemas Bi-IA

---

## 🎯 OBJETIVO

Criar a skill `validate` que atua como **Guardião do Sistema de Arquivos**.
Seu objetivo principal é garantir que **nenhum arquivo fora do padrão permaneça no sistema** e que **todo novo arquivo seja automaticamente indexado** no MOC correto.

---

## 📋 ESPECIFICAÇÕES DA SKILL

### Metadados

- **Nome:** `validate`
- **Triggers:**
  - "validar [arquivo]"
  - "validate [file]"
  - "check [file]"
  - "verificar regras"
- **Versão:** 1.0

### 🔧 Funcionalidades Obrigatórias

#### 1. Validação de Nomenclatura (Regex)

- Verificar se o nome segue `NOMENCLATURA.md` (CamelCase, Sem espaços, DDMMMYYYY).
- **Erro:** "nome errado.md" -> **Sugestão:** "Nome_Correto.md".
- **Erro:** "2025-01-01.md" -> **Sugestão:** "01JAN2025.md".

#### 2. Validação de Localização (Path)

- Verificar se pastas pais existem e são válidas (00-05).
- Alertar se arquivo estiver na Raiz (exceto allowlist).

#### 3. 🧠 Atualização Automática de MOCs (Killer Feature)

- **Lógica Inteligente:**
  1. Identificar a categoria do arquivo (ex: `01_CONHECIMENTO/Tecnologia`).
  2. Encontrar o MOC mais relevante nessa pasta (ex: `_MOC_Tecnologia.md` ou `MOC_Tech.md`).
     - Procurar arquivos começando com `MOC_` ou `_MOC_` na mesma pasta ou na pasta pai.
  3. Verificar se o arquivo já está linkado no MOC.
  4. Se não estiver, **ADICIONAR** link automaticamente.
     - Onde adicionar? No final da lista de links ou numa seção "Novos".
     - **Safety:** Não quebrar a estrutura do MOC. Inserir de forma segura (append safe).

#### 4. Estrutura Interna

- Verificar H1 único.
- Verificar Frontmatter (se aplicável).

### 🛠️ Workflow de Uso

1. **Usuário cria arquivo:** `01_CONHECIMENTO/IA/Novo_Conceito.md`
2. **Usuário comando:** "validar Novo_Conceito.md"
3. **Skill roda:**
   - Checa nome: OK.
   - Checa local: OK.
   - Checa MOC: `_MOC_IA.md` encontrado.
   - Ação: Adiciona `[[Novo_Conceito]]` (se faltar).
   - Retorno: "✅ Arquivo validado e indexado em _MOC_IA.md"

---

## 💻 REQUISITOS TÉCNICOS

- **Script:** `scripts/validate.py`
- **Argumentos:** Aceitar caminho do arquivo como argumento (parseado do prompt).
  - Se nenhum arquivo especificado, rodar validação no último arquivo modificado (smart detection).
- **MOC Update:**
  - Ler conteúdo do MOC.
  - Verificar existência da string `[[Nome_Arquivo]]`.
  - Append formatado: `- [[Nome_Arquivo]]` na seção apropriada ou fim do arquivo.

## 🛡️ SAFETY

- **MOC Backup:** Antes de editar qualquer MOC, criar `.bak`.
- **Read-Only Mode (opcional):** Flag para apenas verificar sem alterar MOCs.

---

## ✅ CHECKLIST DE ENTREGA

- [ ] Estrutura `.gemini/skills/validate/`
- [ ] Script `validate.py` robusto
- [ ] Detecção de argumentos (nome do arquivo)
- [ ] Lógica de MOC Updates funcionando
- [ ] Teste com arquivo fictício

---
**FIM DO PROMPT**
