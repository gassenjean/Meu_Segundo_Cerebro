---
criado: 2026-01-16T18:56:42-03:00
atualizado: 2026-01-18T18:50:00-03:00
---
# GUIA: Usuário Quick Start

**Navegação Rápida e Decision Trees para Gassen**

**Criado:** 16/Jan/2026
**Versão:** 2.0 (Sistema Bi-IA Maduro - 7 Skills)
**Propósito:** Reduzir fricção, decisão rápida, rotinas claras
**Audiência:** Gassen (usuário, dono do vault)

---

## 🎯 NAVEGAÇÃO RÁPIDA (30 SEGUNDOS)

**O que você quer fazer?**

```
┌──────────────────────────────────────────────────────────┐
│ USAR Sistema Bi-IA (7 skills automação) 🆕               │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 0: Sistema Bi-IA


┌──────────────────────────────────────────────────────────┐
│ CRIAR algo novo (arquivo, projeto, nota)                 │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 1: Criar


┌──────────────────────────────────────────────────────────┐
│ ENCONTRAR algo existente (arquivo, informação)           │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 2: Encontrar


┌──────────────────────────────────────────────────────────┐
│ ORGANIZAR vault (limpeza, estrutura, MOCs)               │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 3: Organizar


┌──────────────────────────────────────────────────────────┐
│ SINCRONIZAR (trocar PC, handoff IA, GitHub)              │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 4: Sincronizar


┌──────────────────────────────────────────────────────────┐
│ RESOLVER problema (erro, confusão, lentidão)             │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 5: Troubleshooting


┌──────────────────────────────────────────────────────────┐
│ MANUTENÇÃO periódica (semanal, mensal)                   │
└──────────────────┬───────────────────────────────────────┘
                   ▼
           Ver SEÇÃO 6: Rotinas
```

---

## SEÇÃO 0: Sistema Bi-IA (7 Skills) 🆕

**Status:** ✅ MADURO E OPERACIONAL (Fase 7.4 Completa - 18/Jan/2026)

### O que é o Sistema Bi-IA?

**Sistema Bi-IA = 7 Skills Antigravity + Claude + Gemini**

- **Claude Code** = Cérebro (decisão, estratégia, planejamento)
- **Gemini/Antigravity** = Braços (execução, volume, processamento massivo)
- **7 Skills Nativas** = Automação (validação, indexação, contexto, auditoria, etc)

**Benefício:** Economia de 50-80k tokens/sessão + 95% menos erros + 2-3 min/troca contexto

---

### As 7 Skills Antigravity

#### 1. 🔒 validate (Filesystem Guardian)

**O que faz:** Valida nomenclatura e localização de arquivos ANTES de criar

**Quando usar:** Sempre que for criar arquivo importante

**Como usar (via Gemini CLI):**
```bash
validate check "quero criar TEMPLATE_Briefing_Cliente.md"

# Output: Local correto + nomenclatura validada
```

**Frequência:** 5-10x/dia

**Benefício:** 95% redução de erros de criação

---

#### 2. 🗺️ mapa (Vault Indexer)

**O que faz:** Gera índice completo do vault (2200+ arquivos em 1 arquivo)

**Quando usar:** Início de sessão Claude/Gemini

**Como usar (via Gemini CLI):**
```bash
mapa generate

# Cria: 00_SISTEMA/MOCs/INDICE_VAULT_COMPLETO.md
```

**Frequência:** 1x/sessão ou quando mudar muitos arquivos

**Benefício:** Economia de 50-80k tokens/sessão (Claude lê 1 arquivo vs varrer 2200+)

---

#### 3. 🎯 context-manager (Focus Enforcer)

**O que faz:** Gerencia modos de foco (work, learn, knowledge, system)

**Quando usar:** Trocar de contexto (projetos → aprendizado → manutenção)

**Como usar (via Gemini CLI):**
```bash
context-manager set work      # Foco em projetos (02_PROJETOS)
context-manager set learn     # Foco em cursos (03_APRENDIZADO)
context-manager set knowledge # Foco em zettelkasten (01_CONHECIMENTO)
context-manager set system    # Foco em manutenção (00_SISTEMA)
```

**Frequência:** 4-6x/dia

**Benefício:** Economiza 2-3 min por troca de contexto + foco claro

**O que acontece:**
- Limpa tela
- Mostra banner visual do modo
- Lê STATUS_VAULT.md (contexto geral)
- Carrega MOC relevante
- Sugere ferramentas recomendadas

---

#### 4. 🔍 architect-linter (Codebase Auditor)

**O que faz:** Audita vault (4 checks mecânicos: raiz, frontmatter, H1 duplicados, links quebrados)

**Quando usar:** Antes de checkpoint semanal (sexta 17h)

**Como usar (via Gemini CLI):**
```bash
architect-linter run

# Relatório: 00_SISTEMA/RELATORIOS/ARCHITECT_LINTER_[DATA].md
```

**Frequência:** 1x/semana

**Benefício:** Detecção proativa de issues (400+ erros detectados na última execução)

**O que detecta:**
- Arquivos indevidos na raiz
- Arquivos sem frontmatter YAML
- Títulos H1 duplicados (conflito de conceito)
- Links internos quebrados

---

#### 5. 📝 session-logger (Comunicação Bi-IA)

**O que faz:** Atualiza SESSION_LOG.md automaticamente

**Quando usar:** Automático (não requer ação manual)

**Benefício:** Comunicação Claude ↔ Gemini sem fricção

---

#### 6. 📊 status-updater (Dashboard Metrics)

**O que faz:** Atualiza STATUS_VAULT.md com métricas reais

**Quando usar:** Automático ou quando quiser métricas frescas

**Como usar (via Gemini CLI):**
```bash
status-updater update
```

**Benefício:** Dashboard sempre atualizado (15+ métricas calculadas)

---

#### 7. 🧹 vault-organizer (Marie Kondo Automático)

**O que faz:** Organiza arquivos soltos na raiz do vault

**Quando usar:** Raiz está bagunçada (arquivos fora do lugar)

**Como usar (via Gemini CLI):**
```bash
vault-organizer organize

# Move arquivos para locais corretos + gera relatório
```

**Frequência:** 1x/semana ou quando necessário

---

### Decision Tree: Qual Skill Usar?

```
Vou criar arquivo importante?
├─ SIM → validate check "descrição"
└─ NÃO → Próxima pergunta

Iniciar sessão Claude/Gemini?
├─ SIM → mapa generate (economizar tokens)
└─ NÃO → Próxima pergunta

Trocar de foco (projetos → cursos)?
├─ SIM → context-manager set <modo>
└─ NÃO → Próxima pergunta

É sexta 17h (revisão semanal)?
├─ SIM → architect-linter run
└─ NÃO → Próxima pergunta

Raiz do vault está bagunçada?
├─ SIM → vault-organizer organize
└─ NÃO → Continuar trabalho normal
```

---

### Workflow Diário com Skills

**MANHÃ (5 min):**
```bash
# 1. Gerar índice (economia de tokens)
mapa generate

# 2. Definir foco do dia
context-manager set work   # ou learn/knowledge/system

# 3. Processar _inbox/ (captura rápida do dia anterior)
"Claude, processar _inbox/"

# 4. Começar trabalho
```

**DURANTE O DIA:**
```bash
# Criar arquivo importante?
validate check "quero criar arquivo X"

# Trocar foco?
context-manager set learn   # mudou de projetos para cursos
```

**NOITE (3 min):**
```bash
# Captura rápida em _inbox/
# Atualizar STATUS_ATUAL.md (projetos ativos)
# Fechar vault
```

---

### Workflow Semanal com Skills (Sexta 17h - 30 min)

```bash
# 1. Auditar vault
architect-linter run
# Revisar relatório: 00_SISTEMA/RELATORIOS/ARCHITECT_LINTER_[DATA].md

# 2. Organizar raiz (se necessário)
vault-organizer organize

# 3. Atualizar status
status-updater update

# 4. Processar inbox (deve ficar VAZIO)
"Claude, processar _inbox/"

# 5. Criar checkpoint
"Claude, criar checkpoint semanal"
```

---

### Boas Práticas - Sistema Bi-IA

#### ✅ FAÇA

- Use `validate` ANTES de criar arquivos importantes
- Use `mapa` no início de sessões Claude (economiza 50-80k tokens)
- Use `context-manager` para trocar foco (economiza 2-3 min)
- Delegue volume para Gemini (processamento massivo = grátis)
- Execute `architect-linter` semanalmente (higiene vault)
- Mantenha _inbox/ vazio (processar diariamente)

#### ❌ NÃO FAÇA

- Criar arquivos sem validar nomenclatura/local
- Usar Claude para processar 50+ arquivos (use Gemini)
- Ignorar relatórios do architect-linter (400+ issues detectados)
- Deixar _inbox/ acumular (>20 arquivos)
- Misturar contextos (projetos + cursos ao mesmo tempo)
- Usar Gemini para decisões estratégicas (use Claude)

---

### Cenários Práticos com Skills

#### Cenário 1: Criar novo template
```
Você: "Quero criar TEMPLATE_Proposta_Comercial.md"

Passo 1: validate check "criar TEMPLATE_Proposta_Comercial.md"
Output: Local correto = 04_RECURSOS/TEMPLATES/
        Nomenclatura = ✅ Válida

Passo 2: "Claude, criar template em 04_RECURSOS/TEMPLATES/"
Claude cria arquivo + atualiza _MOC_Recursos.md
```

#### Cenário 2: Processar 20 lives Alan Nicolas
```
Você (SESSION_LOG.md):
  "Gemini, processar lives #40-60 Alan Nicolas"

Gemini:
  1. Lê SESSION_LOG.md
  2. Processa 20 lives (1M tokens = R$ 0)
  3. Cria notas em 03_APRENDIZADO/
  4. Atualiza SESSION_LOG.md (conclusão)
```

#### Cenário 3: Trocar foco (projetos → aprendizado)
```bash
# Antes: trabalhando em KabaK
context-manager set learn

# Agora:
# - Tela limpa
# - Banner "LEARNING MODE"
# - STATUS_VAULT.md carregado
# - _MOC_Aprendizado.md carregado
# - Ferramentas sugeridas: /notebook-lm, /flashcards
```

#### Cenário 4: Revisão semanal (sexta 17h)
```bash
# 1. Auditoria completa
architect-linter run
# Detectou: 2 arquivos na raiz, 383 sem frontmatter, 53 H1 duplicados

# 2. Organizar raiz
vault-organizer organize
# Moveu: COMANDOS_PROXIMA_SESSAO.md → 00_SISTEMA/ARQUIVO/

# 3. Processar inbox
"Claude, processar _inbox/"
# Inbox agora está VAZIO ✅

# 4. Checkpoint
"Claude, criar checkpoint semanal"
```

---

### Quando Usar Claude vs Gemini vs Skills

| Cenário | Use | Motivo |
|---------|-----|--------|
| Validar arquivo antes de criar | **validate skill** | Previne 95% erros |
| Economizar tokens sessão | **mapa skill** | 50-80k tokens economizados |
| Trocar contexto rápido | **context-manager skill** | Economiza 2-3 min |
| Auditar vault (semanal) | **architect-linter skill** | Detecta 400+ issues |
| Decisão estratégica | **Claude** | Raciocínio superior |
| Planejamento | **Claude** | Arquitetura clara |
| Criar 1-3 arquivos | **Claude** | Precisão + contexto |
| Processar 10+ PDFs/lives | **Gemini** | 1M tokens grátis |
| Refatoração 50+ arquivos | **Gemini** | Volume |
| Organizar vault completo | **Gemini** | Escala |

---

## SEÇÃO 1: Criar

### Decision Tree: O que criar?

```
Quero criar:

┌─────────────────────────────────────┐
│ NOTA RÁPIDA (captura rápida)        │
└───────────┬─────────────────────────┘
            ▼
        _inbox/ → Processar depois


┌─────────────────────────────────────┐
│ NOTA DE CONHECIMENTO (permanente)   │
└───────────┬─────────────────────────┘
            │
            ▼
    1. validate check "criar nota X em 01_CONHECIMENTO/"
    2. 01_CONHECIMENTO/
       ├─ Qual área? (IA, Negócios, Dev Pessoal, etc)
       ├─ Seguir padrão: Area_Subarea_Topico.md
       └─ Atualizar _MOC_Conhecimento.md


┌─────────────────────────────────────┐
│ PROJETO NOVO                        │
└───────────┬─────────────────────────┘
            │
            ▼
    1. validate check "criar projeto X"
    2. 02_PROJETOS/Nome_Projeto/
       ├─ README.md (obrigatório)
       ├─ STATUS_ATUAL.md (obrigatório)
       ├─ planejamento/ checkpoints/ docs/ recursos/ tarefas/ metricas/
       └─ Ver: 02_PROJETOS/_GUIDELINES.md


┌─────────────────────────────────────┐
│ NOTA DE CURSO/LIVE                  │
└───────────┬─────────────────────────┘
            │
            ▼
    03_APRENDIZADO/Nome_Curso/notas/
    ├─ Seguir Sistema 5C
    ├─ Atualizar README.md do curso
    └─ Ver: 03_APRENDIZADO/_GUIDELINES.md


┌─────────────────────────────────────┐
│ TEMPLATE/RECURSO                    │
└───────────┬─────────────────────────┘
            │
            ▼
    1. validate check "criar TEMPLATE_X"
    2. 04_RECURSOS/
       ├─ TEMPLATES/ → TEMPLATE_Nome.md
       ├─ PROMPTS/ → Prompt_IA_Funcao.md
       └─ CHECKLISTS/ → CHECKLIST_Nome.md


┌─────────────────────────────────────┐
│ NOTA PESSOAL (journal, ideia)       │
└───────────┬─────────────────────────┘
            │
            ▼
    05_PESSOAL/
    ├─ Journal/ → Journal_DDMMMYYYY.md
    ├─ Ideas/ → Idea_Nome.md
    └─ Reflections/ → Reflection_Topico.md
```

### Como Criar (Delegação IA)

**Opção 1: Claude Code (Recomendado para criação estrutural)**

```
"Claude, criar [tipo] sobre [assunto] em [categoria]"

Exemplo:
"Claude, criar projeto KabaK em 02_PROJETOS/ com estrutura completa"
```

**Opção 2: Gemini (Recomendado para processamento massivo)**

```
"Gemini, processar live #23 do Alan Nicolas e criar notas em 03_APRENDIZADO/"

Exemplo:
"Gemini, organizar 50 PDFs da pasta Downloads em 01_CONHECIMENTO/"
```

### Quando Usar Qual IA?

| Tarefa | Claude | Gemini | Skills |
|--------|--------|--------|--------|
| Validar antes de criar | ❌ | ❌ | ✅ validate |
| Criar projeto completo | ✅ | ❌ | ❌ |
| Criar template/protocolo | ✅ | ❌ | ❌ |
| Processar 1 live/PDF | ✅ | ✅ | ❌ |
| Processar 10+ lives/PDFs | ❌ | ✅ | ❌ |
| Organizar <10 arquivos | ✅ | ❌ | ❌ |
| Organizar 50+ arquivos | ❌ | ✅ | ❌ |
| Decisão estratégica | ✅ | ❌ | ❌ |

---

## SEÇÃO 2: Encontrar

### Mapa de Pastas - Onde Está O Quê?

```
00_SISTEMA/           → Padrões, protocolos, MOCs, guias
├─ PADROES/          → NOMENCLATURA, ARCHITECTURE_GUIDELINES
├─ PROTOCOLOS/       → PROTOCOLO_*, TROUBLESHOOTING
├─ MOCs/             → Índices master
│  └─ INDICE_VAULT_COMPLETO.md → Gerado por 'mapa' skill
└─ GUIAS/            → Guias de leitura (este arquivo)

01_CONHECIMENTO/      → Base de conhecimento permanente
├─ IA_Tecnologia/    → IA, LLMs, prompts
├─ Negocios/         → Marketing, vendas, gestão
├─ Desenvolvimento_Pessoal/ → TDAH, produtividade, hábitos
└─ [outras áreas]

02_PROJETOS/          → Projetos ativos
├─ KabaK/            → Projeto KabaK (marca roupa)
├─ Segundo_Cerebro/  → Este vault (meta)
└─ [outros projetos]

03_APRENDIZADO/       → Cursos e estudos
├─ Alan_Nicolas_Academia_Lendaria/ → Lives, episódios, notas
└─ [outros cursos]

04_RECURSOS/          → Templates, prompts, ferramentas
├─ TEMPLATES/        → TEMPLATE_*
├─ PROMPTS/          → Prompt_*
└─ CHECKLISTS/       → CHECKLIST_*

05_PESSOAL/           → Journal, ideias, reflexões
├─ Journal/          → Diário (Journal_DDMMMYYYY.md)
├─ Ideas/            → Ideias (Idea_Nome.md)
└─ Reflections/      → Reflexões

_inbox/               → Captura rápida (processar depois)

.gemini/skills/       → 7 Skills Antigravity (Python)
├─ validate/         → Filesystem Guardian
├─ mapa/             → Vault Indexer
├─ context-manager/  → Focus Enforcer
├─ architect-linter/ → Codebase Auditor
├─ session-logger/   → Comunicação Bi-IA
├─ status-updater/   → Dashboard Metrics
└─ vault-organizer/  → Marie Kondo Automático
```

### Buscar por Tipo

**Documentação de Padrões:**
→ `00_SISTEMA/PADROES/`

**Protocolos e Workflows:**
→ `00_SISTEMA/PROTOCOLOS/`

**Índices (MOCs):**
→ `00_SISTEMA/MOCs/` ou `[Categoria]/_MOC_*.md`
→ `00_SISTEMA/MOCs/INDICE_VAULT_COMPLETO.md` (gerado por mapa skill)

**Projetos:**
→ `02_PROJETOS/Nome_Projeto/`

**Cursos/Lives:**
→ `03_APRENDIZADO/Nome_Curso/`

**Templates:**
→ `04_RECURSOS/TEMPLATES/`

**Notas pessoais:**
→ `05_PESSOAL/`

**Skills Antigravity:**
→ `.gemini/skills/`

### Atalhos Obsidian

**Buscar arquivo:**
- `Ctrl+O` → Quick Switcher (buscar por nome)
- `Ctrl+Shift+F` → Buscar em todos arquivos (conteúdo)

**Navegar:**
- `Ctrl+Click` em link → Abrir arquivo
- `Alt+←` → Voltar
- `Alt+→` → Avançar

**Criar:**
- `Ctrl+N` → Novo arquivo
- `Ctrl+Shift+N` → Nova janela

---

## SEÇÃO 3: Organizar

### Limpeza Rápida (Semanal)

**Opção 1: Via Skills (Recomendado)**
```bash
# Via Gemini CLI:
vault-organizer organize

# O que faz:
# - Identifica arquivos fora do lugar
# - Move para locais corretos (00-05)
# - Gera relatório detalhado
# - Atualiza MOCs
```

**Opção 2: Via Claude Code**
```
"Claude, executar limpeza do vault"

ou

"/limpeza-raiz-vault"  (comando slash)
```

**Tempo:** 5-10 minutos

---

### Organizar Inbox (_inbox/)

**Frequência:** Diária (ideal) ou Semanal

**Workflow:**
```
1. Abrir _inbox/
2. Para cada arquivo:
   ├─ É conhecimento? → 01_CONHECIMENTO/
   ├─ É projeto? → 02_PROJETOS/
   ├─ É curso? → 03_APRENDIZADO/
   ├─ É recurso? → 04_RECURSOS/
   └─ É pessoal? → 05_PESSOAL/
3. Atualizar MOCs relevantes
4. _inbox/ deve ficar VAZIO
```

**Delegação:**
```
"Claude, processar arquivos do _inbox/ e organizar nas categorias corretas"
```

---

### Atualizar MOCs

**Quando:**
- Criou arquivo novo → Atualizar MOC da categoria
- Moveu arquivo → Atualizar MOC de origem + destino
- Deletou arquivo → Remover link do MOC

**Localização dos MOCs:**
```
01_CONHECIMENTO/_MOC_Conhecimento.md
02_PROJETOS/_MOC_Projetos.md
03_APRENDIZADO/_MOC_Aprendizado.md
04_RECURSOS/_MOC_Recursos.md
05_PESSOAL/_MOC_Pessoal.md
00_SISTEMA/MOCs/INDICE_VAULT_COMPLETO.md (gerado por mapa skill)
```

**Delegação:**
```
"Claude, atualizar _MOC_Conhecimento.md com os 5 novos arquivos que criei"
```

---

### Auditoria Semanal (Novo com architect-linter)

**Frequência:** Sexta 17h (revisão semanal)

**Como fazer:**
```bash
# Via Gemini CLI:
architect-linter run

# Relatório gerado em:
# 00_SISTEMA/RELATORIOS/ARCHITECT_LINTER_[DATA].md
```

**O que o relatório mostra:**
- Arquivos indevidos na raiz
- Arquivos sem frontmatter YAML
- Títulos H1 duplicados (conflito)
- Links internos quebrados

**Benefício:** Detecção proativa de problemas (400+ issues na última execução)

---

## SEÇÃO 4: Sincronizar

### Trocar de PC (Alienware ↔ Desktop)

**Protocolo:**

**Ao SAIR de um PC:**
```
1. Atualizar PC_SYNC_LOG.md (o que fez)
2. Deixar mensagem para o outro PC
3. Aguardar OneDrive sync (2-5 min)
4. Fechar vault
```

**Ao ABRIR no outro PC:**
```
1. LER PC_SYNC_LOG.md PRIMEIRO
2. Ver mensagens para você
3. Continuar trabalho
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_MULTI_PC.md]]

---

### Handoff entre IAs (Claude → Gemini ou vice-versa)

**Claude delegando para Gemini:**
```
1. Claude atualiza SESSION_LOG.md
2. Claude deixa "Mensagem para Gemini"
3. Gemini lê SESSION_LOG.md ao iniciar (automático via session-logger skill)
4. Gemini executa tarefa
5. Gemini reporta conclusão (automático via session-logger skill)
```

**Quando usar:**
- Tarefa >100k tokens → Gemini
- Processamento massivo (50+ arquivos) → Gemini
- Decisão estratégica → Claude
- Planejamento → Claude

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]]

---

### Sincronizar GitHub

**Cenário 1: Branches do iPhone (claude/*)**

```
Desktop/Alienware:
1. git fetch origin
2. git merge origin/claude/nome-branch
3. git push origin master
4. git push origin --delete claude/nome-branch
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]]

**Cenário 2: Criar issue/PR via Gemini**

```
"Gemini, criar issue no GitHub para documentar sistema X"

Gemini usa: gh issue create --title "..." --body "..."
```

**Ver detalhes:** [[../PROTOCOLOS/PROTOCOLO_ANTIGRAVITY_GITHUB.md]]

---

### Decision Tree: Qual Protocolo de Sincronização?

**Ver:** [[../MOCs/MOC_Sincronizacao_Sistemas.md]] (decision tree completo)

```
Trocar PC? → PROTOCOLO_MULTI_PC + PC_SYNC_LOG
Handoff IA? → PROTOCOLO_SINCRONIZACAO_AGENTES + SESSION_LOG (automático via session-logger skill)
Branches iPhone? → PROTOCOLO_GITHUB_MULTI_DISPOSITIVO
GitHub API? → PROTOCOLO_ANTIGRAVITY_GITHUB
```

---

## SEÇÃO 5: Troubleshooting

### Problemas Comuns

**Ver guia completo:** [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]]

#### Problema 1: Claude não responde (Overload)

**Solução:**
1. Aguardar 5 minutos
2. Tentar novamente
3. Se persistir → Usar Gemini temporariamente

**Horários melhores:** Madrugada (0-6h), Fim de semana

---

#### Problema 2: Gemini quota excedida

**Solução:**
1. Aguardar reset (24h)
2. Dividir trabalho em múltiplos dias
3. Usar Claude para urgente

**Prevenção:** Planejar processamento massivo

---

#### Problema 3: Arquivo no lugar errado

**Solução Opção 1 (Skill):**
```bash
# Via Gemini CLI:
vault-organizer organize
# Move automaticamente para local correto
```

**Solução Opção 2 (Claude):**
```
"Claude, mover arquivo X para local correto conforme padrões"
```

Claude vai:
- Consultar NOMENCLATURA.md
- Identificar local correto
- Mover arquivo
- Atualizar MOCs

---

#### Problema 4: Nome de arquivo errado

**Solução Opção 1 (Skill):**
```bash
# Antes de criar:
validate check "criar arquivo X"
# Previne erro de nomenclatura
```

**Solução Opção 2 (Claude):**
```
"Claude, renomear arquivo X para padrão correto"
```

Claude vai:
- Aplicar padrão NOMENCLATURA.md
- Renomear arquivo
- Atualizar links/MOCs

---

#### Problema 5: Vault lento

**Solução:**
1. Aguardar OneDrive sync completo
2. Desabilitar plugins não usados (Obsidian settings)
3. Se >5000 arquivos → Dividir vault

**Delegação:**
```
"Claude, diagnosticar lentidão do vault"
```

---

#### Problema 6: Muitos erros no vault (Novo)

**Detecção:**
```bash
# Via Gemini CLI:
architect-linter run
# Relatório mostra todos os problemas
```

**Solução gradual:**
1. Priorizar raiz (arquivos indevidos)
2. Depois frontmatter (adicionar aos poucos)
3. Depois H1 duplicados (renomear/consolidar)
4. Depois links quebrados (corrigir/remover)

**Não precisa corrigir tudo de uma vez** (backlog gradual)

---

## SEÇÃO 6: Rotinas

### Diária (5 minutos) 🆕 Atualizado com Skills

**Manhã:**
```bash
# 1. Gerar índice vault (economia tokens)
mapa generate

# 2. Definir foco do dia
context-manager set work   # ou learn/knowledge/system

# 3. Processar _inbox/ (captura rápida do dia anterior)
"Claude, processar _inbox/"

# 4. Revisar tarefas pendentes (projetos ativos)
```

**Durante o dia:**
```bash
# Criar arquivo importante?
validate check "descrição do arquivo"

# Trocar foco?
context-manager set <modo>
```

**Noite:**
- [ ] Captura rápida em _inbox/ (ideias do dia)
- [ ] Atualizar STATUS_ATUAL.md (projetos ativos)

---

### Semanal (30 minutos) - Sexta 17h 🆕 Atualizado com Skills

**Ver protocolo:** [[../PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md]]

**Checklist com Skills:**
```bash
# 1. Auditar vault (detectar problemas)
architect-linter run
# Revisar: 00_SISTEMA/RELATORIOS/ARCHITECT_LINTER_[DATA].md

# 2. Organizar raiz (se necessário)
vault-organizer organize

# 3. Atualizar status
status-updater update

# 4. Processar _inbox/ (deve ficar VAZIO)
"Claude, processar _inbox/"

# 5. Atualizar projetos ativos
"Claude, atualizar STATUS_ATUAL.md de todos projetos"

# 6. Atualizar progresso aprendizado
"Claude, atualizar progresso em 03_APRENDIZADO/"

# 7. Criar checkpoint semanal
"Claude, criar checkpoint semanal"
```

**Comando rápido (alternativo):**
```
"Claude, executar revisão semanal"

ou

"/atualizar-status"  (comando slash)
```

---

### Mensal (1-2 horas) - Último Domingo

**Checklist:**
- [ ] Revisar _inbox/ profundamente
- [ ] Consolidar ideias em 05_PESSOAL/Ideas/
- [ ] Revisar projetos pausados (pausar ou reativar)
- [ ] Atualizar metas e OKRs (se usa)
- [ ] Backup completo do vault
- [ ] Revisar progresso financeiro (se rastreia)
- [ ] Executar `architect-linter run` e revisar relatório completo
- [ ] Corrigir erros críticos detectados (raiz, links quebrados)

**Comando:**
```
"Claude, executar revisão mensal completa"
```

---

## 🎯 ATALHOS ÚTEIS

### Comandos Slash (Claude Code)

```
/learn          → Ativar contexto aprendizado
/work           → Ativar contexto projetos
/nevoa          → Ativar agente Névoa (orquestração)
/claude-architect → Ativar Claude Architect (padrões)
/marie-kondo    → Ativar Marie Kondo (organização)
/atualizar-status → Atualizar STATUS_VAULT.md
/limpeza-raiz-vault → Limpar raiz do vault
/gemini         → Delegar para Gemini
/validate       → Validar criação de arquivo
```

**Ver lista completa:** `CLAUDE.md` seção "Available Commands"

---

### Comandos Skills (Gemini CLI) 🆕

```bash
# Validação
validate check "descrição arquivo"

# Indexação
mapa generate

# Contexto
context-manager set work       # Projetos
context-manager set learn      # Aprendizado
context-manager set knowledge  # Zettelkasten
context-manager set system     # Manutenção

# Auditoria
architect-linter run

# Organização
vault-organizer organize

# Status
status-updater update
```

---

### Arquivos Essenciais (Bookmarks Mentais)

**Leitura Frequente:**
- `CLAUDE.md` - Instruções master para IAs
- `README.md` - Visão geral do vault
- `STATUS_VAULT.md` - Estado atual do vault (auto-atualizado por status-updater skill)
- `SESSION_LOG.md` - Comunicação Claude↔Gemini (auto-atualizado por session-logger skill)
- `PC_SYNC_LOG.md` - Comunicação Alienware↔Desktop

**Referência:**
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Padrões de nomenclatura
- `00_SISTEMA/PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md` - Resolver problemas
- `00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md` - Índice master
- `00_SISTEMA/MOCs/INDICE_VAULT_COMPLETO.md` - Índice gerado por mapa skill

**Projetos:**
- `02_PROJETOS/KabaK/STATUS_ATUAL.md` - Status KabaK
- `02_PROJETOS/KabaK/metricas/DASHBOARD.md` - Métricas KabaK

**Skills (Documentação):**
- `.gemini/skills/validate/SKILL.md` - Documentação validate
- `.gemini/skills/mapa/SKILL.md` - Documentação mapa
- `.gemini/skills/context-manager/SKILL.md` - Documentação context-manager
- `.gemini/skills/architect-linter/SKILL.md` - Documentação architect-linter

---

## 💡 DICAS PRÁTICAS

### Dica 1: Use _inbox/ sem Culpa

**Captura rápida > Organização perfeita**

```
✅ CORRETO:
Ideia → _inbox/idea.md → Processar depois

❌ ERRADO:
Ideia → Gastar 10min pensando onde colocar → Esquecer ideia
```

**Processar _inbox/ diariamente (5min) mantém organização.**

---

### Dica 2: Delegue Trabalho Massivo para Gemini

**Gemini = Gratuito (1M tokens)**

```
50 PDFs para organizar → Gemini (R$ 0)
vs
Claude processando tudo → R$ 50-100

Economia: R$ 50-100 por tarefa grande
```

---

### Dica 3: Checkpoint Antes de Grandes Mudanças

**Antes de refatoração grande:**

```
"Claude, criar checkpoint ANTES_REFATORACAO_DDMMMYYYY"
```

**Se algo der errado → Restaurar estado anterior.**

---

### Dica 4: Use MOCs para Navegação Rápida

**Em vez de buscar arquivos um por um:**

```
Abrir _MOC_Conhecimento.md → Ver todos índices de conhecimento
Abrir _MOC_Projetos.md → Ver todos projetos ativos
Abrir INDICE_VAULT_COMPLETO.md → Ver vault inteiro (gerado por mapa skill)
```

**MOCs = Índice visual do vault**

---

### Dica 5: Use validate SEMPRE 🆕

**ANTES de criar arquivo importante:**

```bash
validate check "quero criar TEMPLATE_Briefing.md"
# Output: Local correto + nomenclatura validada

# Só então criar arquivo
```

**Previne 95% dos erros de criação**

---

### Dica 6: Use context-manager para Foco 🆕

**Troque de contexto com 1 comando:**

```bash
# Trabalhando em projetos
context-manager set work

# Mudou para estudar
context-manager set learn
# Tela limpa, banner visual, STATUS + MOC carregados
```

**Economiza 2-3 min por troca + mantém foco**

---

### Dica 7: Auditoria Semanal Previne Caos 🆕

**Sexta 17h:**

```bash
architect-linter run
# Detecta problemas ANTES que virem caos
# Exemplo: 400+ issues detectados
```

**Correção gradual >> Caos acumulado**

---

## 📚 REFERÊNCIAS ÚTEIS

**Navegação:**
- Este guia (GUIA_Usuario_Quick_Start.md)
- [[../MOCs/MOC_Padroes_Protocolos_Guidelines.md]] - Índice master
- [[../MOCs/INDICE_VAULT_COMPLETO.md]] - Índice gerado por mapa skill

**Padrões:**
- [[../PADROES/NOMENCLATURA.md]] - Como nomear arquivos
- [[../PADROES/GUIA_Claude_vs_Gemini.md]] - Qual IA usar

**Protocolos:**
- [[../PROTOCOLOS/PROTOCOLO_MULTI_PC.md]] - Trocar PC
- [[../PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]] - Handoff IA
- [[../PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md]] - Revisão semanal
- [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] - Resolver problemas
- [[../PROTOCOLOS/PROTOCOLO_Uso_Skills_Antigravity.md]] - Uso das 7 skills 🆕

**Guidelines:**
- [[../../02_PROJETOS/_GUIDELINES.md]] - Organizar projetos
- [[../../03_APRENDIZADO/_GUIDELINES.md]] - Processar cursos/lives

**Guias IA:**
- [[GUIA_Leitura_Claude.md]] - Para Claude Code
- [[GUIA_Leitura_Gemini.md]] - Para Gemini/Antigravity

**Skills (Documentação):** 🆕
- [[../../.gemini/skills/validate/SKILL.md]] - validate skill
- [[../../.gemini/skills/mapa/SKILL.md]] - mapa skill
- [[../../.gemini/skills/context-manager/SKILL.md]] - context-manager skill
- [[../../.gemini/skills/architect-linter/SKILL.md]] - architect-linter skill
- [[../MOCs/MOC_Skills_BiIA.md]] - Índice master de todas skills

---

## 🚨 SINAIS DE ALERTA 🆕

**Execute auditoria se:**

| Sinal | Problema | Solução |
|-------|----------|---------|
| _inbox/ >20 arquivos | Acúmulo | Processar diariamente |
| Raiz com arquivos estranhos | Desorganização | `vault-organizer organize` |
| Claude lento (carregando) | Sem índice | `mapa generate` |
| Arquivos em locais errados | Sem validação | Usar `validate` sempre |
| 400+ issues (linter) | Higiene baixa | `architect-linter run` semanal |
| Criar arquivo sem validar | Risco alto de erro | `validate check` ANTES |
| Trocar contexto manualmente | Tempo perdido | `context-manager set <modo>` |

---

## 📊 RESUMO EXECUTIVO (TL;DR) 🆕

**Sistema Bi-IA = 7 Skills + Claude + Gemini**

**7 Skills Antigravity:**
1. **validate** → Previne erros (usar SEMPRE antes criar)
2. **mapa** → Economiza tokens (usar INÍCIO sessão)
3. **context-manager** → Foco claro (usar TROCAR contexto)
4. **architect-linter** → Higiene vault (usar SEMANAL)
5. **session-logger** → Comunicação (AUTOMÁTICO)
6. **status-updater** → Métricas (AUTOMÁTICO)
7. **vault-organizer** → Limpeza (usar QUANDO bagunçado)

**Quando usar:**
- **Claude** = Decisão + Estratégia + Planejamento
- **Gemini** = Execução + Volume + Processamento massivo (grátis)
- **Skills** = Automação + Eficiência + Prevenção

**Benefícios:**
- Economia: 50-80k tokens/sessão (mapa)
- Eficiência: 95% menos erros (validate)
- Produtividade: 2-3 min/troca contexto (context-manager)
- Qualidade: 400+ issues detectados (architect-linter)

**Rotina Diária (5 min):**
1. `mapa generate` (economizar tokens)
2. `context-manager set work` (definir foco)
3. Processar _inbox/
4. Trabalhar

**Rotina Semanal (30 min):**
1. `architect-linter run` (auditar)
2. `vault-organizer organize` (limpar)
3. `status-updater update` (métricas)
4. Processar _inbox/ (VAZIO)
5. Criar checkpoint

---

**Versão:** 2.0 (Sistema Bi-IA Maduro - 7 Skills)
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Última atualização:** 18/Jan/2026

**DECISÃO RÁPIDA + SISTEMA BI-IA = MENOS FRICÇÃO = MAIS PRODUTIVIDADE** 🚀✅
