# PROMPT PARA GEMINI: Criar Skill "Status Updater"

**Para:** Gemini 3 Pro (Antigravity)
**Tarefa:** Criar segunda Antigravity Skill - Automação de Atualização de STATUS_VAULT.md
**Prioridade:** ⭐⭐⭐⭐ ALTA

---

## CONTEXTO

Você (Gemini) vai criar a **segunda skill Antigravity** do sistema bi-IA. Esta skill é uma conversão da skill Claude Code `/atualizar-status` para automação executável.

**Diferença fundamental:**
- **Claude `/atualizar-status`** = Conhecimento (lê STATUS_VAULT.md e atualiza manualmente)
- **Antigravity `status-updater`** = Automação (coleta métricas e atualiza automaticamente)

---

## OBJETIVO

Criar skill `status-updater` que **automaticamente:**

1. Coleta métricas do vault (arquivos, projetos, MOCs, comandos, etc)
2. Calcula progresso baseado em:
   - Fases implementadas (1-7)
   - Estrutura criada vs pendente
   - Conteúdo migrado
3. Atualiza STATUS_VAULT.md com:
   - Estatísticas atualizadas
   - Nova entrada no histórico
   - Progresso recalculado
4. Gera relatório de mudanças
5. Mantém formatação e estrutura original

---

## ESTRUTURA DA SKILL

Criar em: `.gemini/skills/status-updater/`

```
.gemini/skills/status-updater/
├── skill.md           # Metadados + Descrição
├── scripts/
│   ├── updater.py    # Script principal
│   └── metrics.py    # Coleta de métricas (se necessário)
└── resources/
    └── template.md   # Template entrada histórico (se necessário)
```

---

## CONTEÚDO: skill.md

```markdown
---
name: status-updater
description: Atualiza STATUS_VAULT.md automaticamente com métricas e progresso
version: 1.0
triggers:
  - "atualizar status"
  - "update vault status"
  - "status vault"
  - "atualizar progresso"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Status Updater

Automação inteligente que atualiza `STATUS_VAULT.md` com métricas coletadas automaticamente do vault.

## Funcionalidades

- ✅ Coleta métricas do vault (arquivos, projetos, MOCs)
- ✅ Calcula progresso por fase (1-7)
- ✅ Atualiza estatísticas automaticamente
- ✅ Adiciona entrada no histórico com timestamp
- ✅ Mantém formatação original
- ✅ Gera relatório de mudanças

## Como Usar

**Linguagem Natural:**
- "Atualize o status do vault"
- "Atualizar progresso"
- "Status vault update"
- "Gerar relatório de progresso"

**Comando Explícito:**
- `/status-updater` (executa update completo)

## Workflow

1. **Scan:** Coleta métricas do vault (arquivos, pastas, MOCs, comandos)
2. **Análise:** Calcula progresso por fase e geral
3. **Update:** Atualiza seções de STATUS_VAULT.md
4. **Histórico:** Adiciona nova entrada com timestamp
5. **Relatório:** Gera resumo de mudanças

## Métricas Coletadas

**Estrutura:**
- Total de arquivos
- Projetos ativos (02_PROJETOS/)
- Cursos ativos (03_APRENDIZADO/)
- MOCs criados (00_SISTEMA/MOCs/)
- Templates (04_RECURSOS/TEMPLATES/)
- Checklists, Prompts, Guias

**Comandos:**
- Skills Claude (.claude/skills/)
- Skills Antigravity (.gemini/skills/)
- Total de comandos disponíveis

**Progresso:**
- Fase 1-7 (% baseado em critérios)
- Progresso geral calculado

## Script

Executa `scripts/updater.py` que implementa toda lógica automaticamente.
```

---

## CONTEÚDO: scripts/updater.py

**Requisitos do script:**

1. **Funções principais:**
   ```python
   def collect_metrics(vault_root):
       """Coleta todas métricas do vault"""

   def calculate_progress():
       """Calcula progresso por fase e geral"""

   def update_statistics(metrics):
       """Atualiza seção de estatísticas no STATUS_VAULT.md"""

   def add_history_entry(summary):
       """Adiciona nova entrada no histórico com timestamp"""

   def generate_report(old_metrics, new_metrics):
       """Gera relatório de mudanças"""

   def preserve_formatting(content):
       """Mantém formatação markdown original"""
   ```

2. **Métricas a coletar:**

   ```python
   metrics = {
       # Arquivos e Pastas
       "total_files": count_all_files(vault_root),
       "total_folders": count_folders(vault_root),

       # Projetos
       "projetos_ativos": count_projects("02_PROJETOS"),

       # Aprendizado
       "cursos_ativos": count_courses("03_APRENDIZADO"),

       # Conhecimento
       "areas_conhecimento": count_areas("01_CONHECIMENTO"),

       # Sistema
       "mocs_total": count_mocs("00_SISTEMA/MOCs"),
       "mocs_categoria": count_category_mocs(),

       # Recursos
       "templates": count_files("04_RECURSOS/TEMPLATES"),
       "prompts": count_files("04_RECURSOS/PROMPTS"),
       "checklists": count_files("04_RECURSOS/CHECKLISTS"),
       "guias": count_files("04_RECURSOS/GUIAS"),

       # Comandos e Skills
       "skills_claude": count_skills(".claude/skills"),
       "skills_gemini": count_skills(".gemini/skills"),
       "comandos_total": count_commands(),

       # Progresso
       "fases": {
           1: calculate_phase_progress(1),  # Aprendizado
           2: calculate_phase_progress(2),  # Estrutura Base
           3: calculate_phase_progress(3),  # Gemini CLI
           4: calculate_phase_progress(4),  # Migração
           5: calculate_phase_progress(5),  # Automação
           6: calculate_phase_progress(6),  # Arquitetura
           7: calculate_phase_progress(7),  # Manutenção
       }
   }
   ```

3. **Cálculo de progresso:**

   ```python
   def calculate_phase_progress(phase_number):
       """
       Calcula progresso de cada fase baseado em critérios.

       Fase 1 (Aprendizado): 100% se cursos estruturados
       Fase 2 (Estrutura Base): 100% se pastas 00-05 criadas
       Fase 3 (Gemini CLI): 100% se .gemini/ configurado
       Fase 4 (Migração): % baseado em conteúdo migrado
       Fase 5 (Automação): % baseado em skills criadas
       Fase 6 (Arquitetura): 100% se guidelines criados
       Fase 7 (Manutenção): % baseado em limpeza e organização
       """

   def calculate_overall_progress(phases):
       """Calcula progresso geral (média ponderada das fases)"""
   ```

4. **Atualização do STATUS_VAULT.md:**

   ```python
   def update_status_vault(metrics):
       """
       Atualiza STATUS_VAULT.md mantendo estrutura original.

       Seções a atualizar:
       1. VISÃO GERAL → Versão, Status Geral, Progresso
       2. ESTATÍSTICAS → Todos os contadores
       3. HISTÓRICO → Nova entrada no topo com:
          - Data/Hora atual (DDMMMYYYY HH:MM)
          - Resumo do que mudou
          - Métricas destacadas
          - Próximos passos (se houver)
       """

       # LER arquivo atual
       with open("STATUS_VAULT.md", "r", encoding="utf-8") as f:
           content = f.read()

       # ATUALIZAR seções específicas (regex ou string replace)
       # Manter formatação markdown original

       # ADICIONAR entrada no histórico (no topo da seção)
       history_entry = generate_history_entry(metrics)

       # ESCREVER arquivo atualizado
       with open("STATUS_VAULT.md", "w", encoding="utf-8") as f:
           f.write(updated_content)
   ```

5. **Template de entrada no histórico:**

   ```markdown
   ### DD/MMM/YYYY (HH:MM) - ATUALIZAÇÃO AUTOMÁTICA

   **Métricas Atualizadas:**

   - 📁 Total de arquivos: XXX (↑ YYY desde última atualização)
   - 📂 Projetos ativos: X
   - 📚 Cursos ativos: X
   - 🗂️ MOCs: X
   - 🤖 Skills: X Claude + X Gemini = X total

   **Progresso:**

   - Fase 1-7: [barra de progresso visual]
   - Geral: XX% (↑ Y% desde última atualização)

   **Mudanças Detectadas:**

   - [Lista de mudanças significativas]

   ---
   ```

6. **Safety:**
   - Backup de STATUS_VAULT.md antes de atualizar
   - Validação de formatação markdown
   - Rollback se erro
   - Não sobrescrever seções manuais (preservar)

7. **Output:**
   ```markdown
   # Relatório Status Updater - 18/JAN/2026 HH:MM

   ## Resumo
   - Métricas coletadas: 15
   - Seções atualizadas: 3
   - Entrada histórico: Adicionada
   - Backup: STATUS_VAULT_backup_18JAN2026_HHMM.md

   ## Mudanças Detectadas

   ### Arquivos
   - Total: 1847 → 1850 (+3)

   ### Skills
   - Gemini: 3 → 4 (+1 - status-updater criada)

   ### Progresso
   - Fase 5 (Automação): 33% → 66% (+33%)
   - Geral: 92% → 94% (+2%)

   ## STATUS_VAULT.md Atualizado

   ✅ Histórico: Nova entrada adicionada
   ✅ Estatísticas: Contadores atualizados
   ✅ Progresso: Barras de progresso atualizadas
   ```

---

## ARQUIVOS DE REFERÊNCIA

**OBRIGATÓRIO ler antes de criar a skill:**

1. `STATUS_VAULT.md` - Estrutura completa do arquivo a atualizar
2. `.claude/commands/atualizar-status.md` - Skill original (referência)
3. `00_SISTEMA/PROTOCOLOS/PROTOCOLO_DIVISAO_SKILLS_Claude_Antigravity.md` - Como criar skills Antigravity
4. `.gemini/skills/vault-organizer/` - Skill #1 como referência

**Opcional (contexto):**
- `00_SISTEMA/CHECKPOINTS/CHECKPOINT_18JAN2026_Antigravity_Skills_Integration.md`
- `00_SISTEMA/ANALISES/ANALISE_Antigravity_Skills_Integracao_Sistema_BiIA.md`

---

## CHECKLIST DE VALIDAÇÃO

Antes de finalizar, verificar:

- [ ] Estrutura de pastas criada (skill.md + scripts/)
- [ ] skill.md completo (metadados + descrição + triggers)
- [ ] Script Python funcional e testado
- [ ] Coleta de métricas implementada (15+ métricas)
- [ ] Cálculo de progresso implementado (7 fases)
- [ ] Atualização de STATUS_VAULT.md funcional
- [ ] Entrada no histórico gerada corretamente
- [ ] Formatação markdown preservada
- [ ] Backup criado antes de atualizar
- [ ] Testado em nova conversa (zero contexto)
- [ ] Ativação via linguagem natural funciona
- [ ] Relatório de mudanças gerado

---

## TESTE FINAL

**Criar nova conversa no Antigravity e testar:**

1. Dizer: "Atualize o status do vault"
2. Verificar se:
   - Skill ativa automaticamente
   - Métricas são coletadas corretamente
   - STATUS_VAULT.md é atualizado
   - Histórico recebe nova entrada
   - Backup é criado
   - Relatório é gerado
3. Validar se formatação original foi preservada

---

## ENTREGA

**Salvar skill em:**
`.gemini/skills/status-updater/`

**Atualizar SESSION_LOG.md com:**
- Skill criada e testada
- Exemplos de uso
- Próximos passos (skill #3: session-logger)

**Avisar Claude Code** que skill está pronta para validação!

---

**Skill #2 de 7 - Vamos nessa! 🚀**