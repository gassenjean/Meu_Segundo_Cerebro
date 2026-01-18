# 🚧 GUIA: Edge Cases & Limitações das Skills Antigravity

**Responsável:** Antigravity (Gemini)
**Versão:** 1.0
**Ultima Atualização:** 18/JAN/2026

---

## 🎯 Objetivo

Documentar cenários de borda (edge cases), limitações conhecidas e comportamentos inesperados das skills automatizadas para evitar surpresas.

---

## 🏗️ Limitações Gerais do Sistema

### 1. Sistema de Arquivos (Windows)

* **Limite de Caminho (MAX_PATH):** O Windows tem um limite histórico de 260 caracteres.
  * **Risco:** Se o vault tiver caminhos muito profundos (`01_CONHECIMENTO/Categoria/Sub/Topico/..../arquivo.md`), scripts Python podem falhar ao tentar abrir/mover.
  * **Sintoma:** `FileNotFoundError` mesmo o arquivo existindo.
  * **Workaround:** Mantenha nomes de pastas concisos e estrutura rasa (max 4-5 níveis).

* **Caracteres Especiais:**
  * **Risco:** Arquivos com 🤔, ç, ã, ou caracteres reservados (`:`, `?`) vindos de downloads.
  * **Comportamento:** `vault-organizer` tenta sanitizar, mas pode falhar se o encoding do terminal não for UTF-8.
  * **Workaround:** Renomeie manualmente arquivos com nomes "exóticos" antes de rodar automações.

* **Arquivos em Uso (Lock):**
  * **Risco:** Tentar organizar um PDF que está aberto no Acrobat Reader.
  * **Comportamento:** `PermissionError`. A skill vai pular o arquivo e avisar no log.
  * **Solução:** Feche os arquivos antes de rodar `vault-organizer`.

### 2. Git & Controle de Versão

* **Repo Sujo (Dirty State):**
  * **Cenário:** Você editou 50 arquivos mas não deu commit, e roda `vault-organizer`.
  * **Risco:** Se a skill fizer algo errado, o `git stash` ou `git checkout` vai ser uma bagunça para restaurar.
  * **Regra de Ouro:** **Sempre commite (ou stash) antes de rodar automações massivas.**

---

## 🧹 Edge Cases: vault-organizer

### Caso 1: Arquivos Ambíguos

* **Cenario:** Um PDF chamado `Relatorio_Financeiro_2025.pdf`.
* **Dúvida:** É `02_PROJETOS/Financeiro` ou `01_CONHECIMENTO/Financas`?
* **Comportamento Atual:** A IA tenta adivinhar pelo contexto do nome. Se falhar, pode cair em `04_RECURSOS/Arquivos` ou ficar na raiz.
* **Solução:** Mova manualmente arquivos sensíveis ao contexto. A skill é boa para "limpeza grossa" (livros, imagens, zips), não para organização semântica fina.

### Caso 2: Pastas como Arquivos

* **Cenario:** Uma pasta chamada `Backup.zip` (sim, pasta com nome de arquivo).
* **Comportamento:** O script verifica `os.path.isfile()`. Se for pasta, ele ignora. Não espere que ele mova pastas inteiras, apenas arquivos.

---

## 📊 Edge Cases: status-updater

### Caso 1: Vazio ou Markdown Quebrado

* **Cenario:** `STATUS_VAULT.md` está vazio ou alguém apagou os comentários mágicos `<!-- status:start -->`.
* **Comportamento:** O script não encontrará onde injetar o texto. Pode criar um novo bloco no final ou falhar silenciosamente.
* **Solução:** Sempre mantenha a estrutura base do `STATUS_VAULT.md`. Se quebrar, restaure o backup ou copie do template.

### Caso 2: Métricas Distorcidas

* **Cenario:** Você copiou a pasta `node_modules` para dentro de um projeto (milhares de arquivos pequenos).
* **Comportamento:** O contador de "Total Arquivos" vai explodir (de 2.000 para 50.000).
* **Solução:** O script deve ignorar pastas ocultas e comuns (`node_modules`, `.git`), mas fique atento a pastas de dados massivos não padronizadas.

---

## 📝 Edge Cases: session-logger

### Caso 1: Conflito de Agentes (Race Condition)

* **Cenario:** Claude e Gemini tentam escrever no `SESSION_LOG.md` ao mesmo tempo (raro, mas possível em sync de arquivos).
* **Comportamento:** Conflito de git ou arquivo corrompido.
* **Solução:** O `SESSION_LOG.md` deve ser tratado como um "livro de visitas". Um assina por vez.

---

## 🛑 Quando NÃO usar Skills Antigravity

Evite automações quando:

1. **Refatoração Estrutural:** Vai renomear pastas raiz (`01_CONHECIMENTO` -> `Bibiloteca`). Faça na mão ou com script dedicado.
2. **Dados Sensíveis:** Arquivos com senhas ou chaves privadas que não deveriam ser lidos/movidos por scripts genéricos.
3. **Sem Backup:** Se seu Git quebrou e você não tem backup, não rode scripts que movem arquivos.

---

**Fim do Guia**
