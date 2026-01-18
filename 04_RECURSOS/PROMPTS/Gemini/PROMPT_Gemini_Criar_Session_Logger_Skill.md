# PROMPT PARA GEMINI: Criar Skill "Session Logger"

**Para:** Gemini 3 Pro (Antigravity)
**Tarefa:** Criar terceira Antigravity Skill - Automação de SESSION_LOG.md (Comunicação Bi-IA)
**Prioridade:** ⭐⭐⭐⭐ ALTA

---

## CONTEXTO

Você (Gemini) vai criar a **terceira e última skill do protótipo** do sistema bi-IA. Esta skill é uma conversão da skill Claude Code `/sync` para automação executável.

**Diferença fundamental:**
- **Claude `/sync`** = Conhecimento (analisa sessão e atualiza SESSION_LOG.md manualmente)
- **Antigravity `session-logger`** = Automação (detecta mudanças e atualiza automaticamente)

**Sistema Bi-IA:**
- Claude Code + Antigravity/Gemini trabalham no mesmo vault
- SESSION_LOG.md é o canal de comunicação bidirecional
- Cada agente lê o que o outro fez
- Evita conflitos e garante continuidade

---

## OBJETIVO

Criar skill `session-logger` que **automaticamente:**

1. Detecta mudanças na sessão atual (arquivos criados/modificados)
2. Identifica o agente ativo (Claude ou Gemini)
3. Gera entrada no SESSION_LOG.md com:
   - Timestamp (DD/MMM/YYYY HH:MM)
   - Ações realizadas
   - Arquivos modificados
   - Estado do vault
   - Mensagem para o outro agente (se necessário)
4. Insere entrada no topo da seção "ÚLTIMAS MUDANÇAS"
5. Mantém formatação e estrutura original
6. Cria backup antes de atualizar

---

## ESTRUTURA DA SKILL

Criar em: `.gemini/skills/session-logger/`

```
.gemini/skills/session-logger/
├── skill.md           # Metadados + Descrição
├── scripts/
│   ├── logger.py     # Script principal
│   └── detector.py   # Detecção de mudanças (se necessário)
└── resources/
    └── template.md   # Template entrada SESSION_LOG (se necessário)
```

---

## CONTEÚDO: skill.md

```markdown
---
name: session-logger
description: Atualiza SESSION_LOG.md automaticamente com ações da sessão (comunicação bi-IA)
version: 1.0
triggers:
  - "sync"
  - "atualizar session log"
  - "registrar sessão"
  - "session log"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Session Logger

Automação inteligente que atualiza `SESSION_LOG.md` com ações da sessão atual, facilitando a comunicação entre Claude Code e Antigravity/Gemini.

## Funcionalidades

- ✅ Detecta mudanças na sessão (arquivos criados/modificados)
- ✅ Identifica agente ativo (Claude ou Gemini)
- ✅ Gera entrada com timestamp
- ✅ Lista ações e arquivos modificados
- ✅ Mantém formatação original
- ✅ Cria backup automático
- ✅ Preserva histórico completo

## Como Usar

**Linguagem Natural:**
- "Sync"
- "Atualizar session log"
- "Registrar sessão"
- "Salvar estado para o outro agente"

**Comando Explícito:**
- `/session-logger` (executa registro da sessão)

## Workflow

1. **Scan:** Detecta mudanças via git status (ou timestamp de arquivos)
2. **Análise:** Identifica ações significativas
3. **Template:** Gera entrada seguindo formato padrão
4. **Update:** Insere no topo de SESSION_LOG.md
5. **Backup:** Cria cópia de segurança
6. **Relatório:** Confirma ações registradas

## Template de Entrada

**Para Gemini (Antigravity):**
```markdown
## 🟢 Antigravity/Gemini - DD/MMM/YYYY (HH:MM) - TÍTULO

### Trabalho Realizado

**1. [Categoria de Trabalho]**

* ✅ [Ação específica 1]
* ✅ [Ação específica 2]

**2. [Outra Categoria]**

* ✅ [Ação específica 3]

### Arquivos Criados/Modificados

* `caminho/arquivo1.md` - Descrição
* `caminho/arquivo2.md` - Descrição

### Status

* ✅ [Tarefas concluídas]
* ⏳ [Tarefas em andamento]

### Mensagem para Claude Code

> [Mensagem se necessário, ou "Nenhuma ação necessária"]

---
```

**Para Claude (Claude Code):**
```markdown
## 🔵 Claude Code - DD/MMM/YYYY (HH:MM) - TÍTULO

### Trabalho Realizado

[Mesmo formato que Gemini, mas com cor azul 🔵]

---
```

## Script

Executa `scripts/logger.py` que implementa toda lógica automaticamente.
```

---

## CONTEÚDO: scripts/logger.py

**Requisitos do script:**

1. **Funções principais:**
   ```python
   def detect_agent():
       """Detecta qual agente está ativo (Claude ou Gemini)"""
       # Pode usar variável de ambiente, prompt do usuário, ou heurística

   def detect_changes(vault_root):
       """Detecta arquivos criados/modificados na sessão"""
       # Opção 1: git status (se git disponível)
       # Opção 2: comparar timestamps com início da sessão
       # Opção 3: perguntar ao usuário

   def categorize_actions(files_changed):
       """Categoriza ações baseado nos arquivos modificados"""
       # Exemplo: Se modificou .gemini/skills/ → "Criação de Skills"

   def generate_session_entry(agent, actions, files, summary):
       """Gera entrada markdown seguindo template"""

   def insert_entry(session_log_path, entry):
       """Insere entrada no topo da seção ÚLTIMAS MUDANÇAS"""

   def create_backup(file_path):
       """Cria backup com timestamp"""
   ```

2. **Detecção de Agente:**
   ```python
   def detect_agent():
       """
       Detecta qual agente está ativo.

       Opções:
       1. Variável de ambiente (CLAUDE_CODE=1 ou ANTIGRAVITY=1)
       2. Prompt do usuário (perguntar)
       3. Heurística (processo em execução)

       Retorna: "Claude Code" ou "Antigravity/Gemini"
       """
       # Implementação simplificada: perguntar ou usar env var
   ```

3. **Detecção de Mudanças:**
   ```python
   def detect_changes(vault_root):
       """
       Detecta arquivos criados/modificados.

       Opção 1 (Preferencial): git status
       ```
       git status --short
       M  arquivo_modificado.md
       A  arquivo_criado.md
       ```

       Opção 2: Comparar timestamps
       - Salvar timestamp ao iniciar skill
       - Comparar com timestamp de arquivos

       Retorna: lista de (arquivo, status)
       """
   ```

4. **Categorização de Ações:**
   ```python
   def categorize_actions(files_changed):
       """
       Categoriza ações baseado nos arquivos.

       Exemplos:
       - Se modificou .gemini/skills/ → "Criação de Skills Antigravity"
       - Se modificou 00_SISTEMA/PROTOCOLOS/ → "Criação de Protocolos"
       - Se modificou STATUS_VAULT.md → "Atualização de Status"
       - Se modificou múltiplos .md em 01_CONHECIMENTO → "Migração de Conhecimento"

       Retorna: dict de {categoria: [ações]}
       """
   ```

5. **Template de Entrada:**
   ```python
   def generate_session_entry(agent, categorized_actions, files, message_to_other="Nenhuma ação necessária"):
       """
       Gera entrada markdown.

       Estrutura:
       - Header: ## 🟢/🔵 [Agent] - DD/MMM/YYYY (HH:MM) - TÍTULO
       - Trabalho Realizado (por categoria)
       - Arquivos Criados/Modificados
       - Status (opcional)
       - Mensagem para o outro agente
       - Separador ---
       """
       now = datetime.datetime.now()
       date_str = now.strftime("%d/%b/%Y (%H:%M)").upper()

       # PT-BR months
       months = {"JAN": "JAN", "FEB": "FEV", ...}

       # Emoji baseado no agente
       emoji = "🟢" if agent == "Antigravity/Gemini" else "🔵"

       # Gerar título automático baseado em ações principais
       title = generate_title(categorized_actions)

       entry = f"## {emoji} {agent} - {date_str} - {title}\n\n"
       entry += "### Trabalho Realizado\n\n"

       for category, actions in categorized_actions.items():
           entry += f"**{category}**\n\n"
           for action in actions:
               entry += f"* ✅ {action}\n"
           entry += "\n"

       if files:
           entry += "### Arquivos Criados/Modificados\n\n"
           for file, description in files:
               entry += f"* `{file}` - {description}\n"
           entry += "\n"

       entry += "### Mensagem para " + ("Claude Code" if agent == "Antigravity/Gemini" else "Antigravity/Gemini") + "\n\n"
       entry += f"> {message_to_other}\n\n"
       entry += "---\n"

       return entry
   ```

6. **Inserção no SESSION_LOG.md:**
   ```python
   def insert_entry(session_log_path, entry):
       """
       Insere entrada no topo da seção ÚLTIMAS MUDANÇAS.

       Passos:
       1. Ler arquivo atual
       2. Localizar seção ## 📅 HISTÓRICO ou similar
       3. Inserir nova entrada APÓS o header (no topo)
       4. Manter últimas 20 entradas (apagar antigas se > 20)
       5. Escrever arquivo atualizado
       """
       with open(session_log_path, 'r', encoding='utf-8') as f:
           content = f.read()

       # Localizar seção de histórico (pode variar)
       # Padrão: Procurar por último "---" antes de novo entry
       # Ou procurar por header específico

       # Inserir entrada no topo
       # ...

       with open(session_log_path, 'w', encoding='utf-8') as f:
           f.write(updated_content)
   ```

7. **Workflow Principal:**
   ```python
   def main():
       print("🔄 Iniciando Session Logger...")

       # 1. Detectar agente
       agent = detect_agent()
       print(f"🤖 Agente: {agent}")

       # 2. Detectar mudanças
       changes = detect_changes(VAULT_ROOT)
       print(f"📂 Mudanças detectadas: {len(changes)} arquivos")

       if not changes:
           print("ℹ️ Nenhuma mudança significativa detectada.")
           response = input("Deseja registrar uma entrada vazia? (s/n): ")
           if response.lower() != 's':
               return

       # 3. Categorizar ações
       categorized = categorize_actions(changes)

       # 4. Perguntar se há mensagem para outro agente
       message = input("Mensagem para o outro agente (Enter para pular): ").strip()
       if not message:
           message = "Nenhuma ação necessária"

       # 5. Gerar entrada
       entry = generate_session_entry(agent, categorized, changes, message)

       # 6. Mostrar preview
       print("\n" + "="*60)
       print("PREVIEW DA ENTRADA:")
       print("="*60)
       print(entry)
       print("="*60)

       # 7. Confirmar
       confirm = input("\nConfirmar atualização? (s/n): ")
       if confirm.lower() != 's':
           print("❌ Cancelado.")
           return

       # 8. Backup
       backup_file = create_backup(SESSION_LOG_PATH)
       print(f"💾 Backup: {backup_file.name}")

       # 9. Inserir entrada
       insert_entry(SESSION_LOG_PATH, entry)

       print("✅ SESSION_LOG.md atualizado com sucesso!")
   ```

8. **Safety:**
   - Backup antes de atualizar
   - Confirmação do usuário (preview)
   - Verificação de encoding UTF-8
   - Preservação de formatação
   - Não sobrescrever mensagens do outro agente

9. **Output:**
   ```markdown
   🔄 Iniciando Session Logger...
   🤖 Agente: Antigravity/Gemini
   📂 Mudanças detectadas: 3 arquivos

   ========================
   PREVIEW DA ENTRADA:
   ========================
   ## 🟢 Antigravity/Gemini - 18/JAN/2026 (15:30) - Skills Antigravity Criadas

   ### Trabalho Realizado

   **Criação de Skills Antigravity**

   * ✅ vault-organizer criada
   * ✅ status-updater criada

   ### Arquivos Criados/Modificados

   * `.gemini/skills/vault-organizer/skill.md` - Skill #1
   * `.gemini/skills/status-updater/skill.md` - Skill #2

   ### Mensagem para Claude Code

   > Skills prontas para validação!

   ---
   ========================

   Confirmar atualização? (s/n): s
   💾 Backup: SESSION_LOG.bak_20260118_153045
   ✅ SESSION_LOG.md atualizado com sucesso!
   ```

---

## ARQUIVOS DE REFERÊNCIA

**OBRIGATÓRIO ler antes de criar a skill:**

1. `SESSION_LOG.md` - Estrutura completa do arquivo a atualizar
2. `.claude/commands/sync.md` - Skill original (referência)
3. `00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md` - Protocolo bi-IA
4. `.gemini/skills/vault-organizer/` - Skill #1 (padrão)
5. `.gemini/skills/status-updater/` - Skill #2 (padrão)

**Opcional (contexto):**
- `00_SISTEMA/CHECKPOINTS/CHECKPOINT_18JAN2026_Antigravity_Skills_Integration.md`

---

## CHECKLIST DE VALIDAÇÃO

Antes de finalizar, verificar:

- [ ] Estrutura de pastas criada (skill.md + scripts/)
- [ ] skill.md completo (metadados + descrição + triggers)
- [ ] Script Python funcional e testado
- [ ] Detecção de agente implementada
- [ ] Detecção de mudanças implementada (git ou timestamps)
- [ ] Categorização de ações implementada
- [ ] Template de entrada gerado corretamente
- [ ] Inserção no topo do SESSION_LOG.md funcional
- [ ] Formatação markdown preservada
- [ ] Backup criado antes de atualizar
- [ ] Preview + confirmação implementados
- [ ] Testado em nova conversa (zero contexto)
- [ ] Ativação via "sync" funciona
- [ ] Meses em PT-BR

---

## TESTE FINAL

**Criar nova conversa no Antigravity e testar:**

1. Criar arquivo de teste: `teste_session.md`
2. Dizer: "Sync"
3. Verificar se:
   - Skill ativa automaticamente
   - Detecta mudanças (teste_session.md criado)
   - Gera preview da entrada
   - Solicita confirmação
   - Cria backup
   - Atualiza SESSION_LOG.md no topo
   - Formatação preservada
4. Ler SESSION_LOG.md e validar entrada

---

## ENTREGA

**Salvar skill em:**
`.gemini/skills/session-logger/`

**Atualizar SESSION_LOG.md com:**
- Skill criada e testada
- Exemplos de uso
- Conclusão da Fase 2 (3 de 3 skills protótipo)

**Avisar Claude Code** que skill está pronta para validação!

---

**Skill #3 de 7 - Última do protótipo! 🎉🚀**
