---
created: 2026-01-24T21:13
updated: 2026-01-24T23:07
---
# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

---

## LEI SUPREMA

**`00_SISTEMA/VAULT_CONSTITUTION.md`** - Constituição do Segundo Cérebro

Todas as ações no vault DEVEM seguir a Constituição. Ela define:

- 3 Leis Fundamentais (Fluidez, Atomicidade, Contexto)
- Método 5C (Consumir→Capturar→Conectar→Criar→Compartilhar)
- Método MAPA (Mapear→Atomizar→Programar→Ativar)
- Hierarquia de Comando (Gassen→Névoa→Gerentes→Guardian)
- Sistema de Permissões 1-2-3

---

## PROTOCOLO OBRIGATÓRIO

**ANTES DE CRIAR QUALQUER ARQUIVO:**

1. **SEGUIR:** `00_SISTEMA/VAULT_CONSTITUTION.md` (LEI SUPREMA)
2. **LER:** `00_SISTEMA/PADROES/NOMENCLATURA.md` (OBRIGATÓRIO)
3. **CONSULTAR:** MOC relevante da categoria
4. **VALIDAR:** Localização e nomenclatura
5. **SÓ ENTÃO:** Criar arquivo(s)

**ZERO EXCEÇÕES.** Este é um sistema PKM com padrões rigorosos.

---

## 📡 SINCRONIZAÇÃO - Iniciar Sessão

### Bi-IA System (Claude + Gemini)

**CRÍTICO - Ler nesta ordem:**
1. **`.bi-ia/state.json`** - Estado compartilhado (NOVO - OBRIGATÓRIO)
2. `SESSION_LOG.md` (raiz) - Histórico e contexto
3. `PC_SYNC_LOG.md` (raiz) - Sync Alienware ↔ Desktop Casa

**Verificar em state.json:**
- `pendingTasks` onde `to: "claude"` → Executar ANTES de novas tarefas
- `errors` → Resolver se houver
- `rules` → Seguir sempre

**Protocolos completos:**
- `.bi-ia/PROTOCOLO_BI_IA_SYNC.md` (NOVO - Comunicação automática)
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md`
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md`

---

## 📂 Repository Overview

**Meu_Segundo_Cerebro** - Sistema PKM Híbrido

**Owner:** Gassen Jean Bou Karim
**System:** Alan Nicolas + Névoa 3.0
**Status:** ✅ Fase 4/5 Completa
**Version:** 2.0.76
**Agentes:** 9 especializados

### Estrutura

```text
00_SISTEMA/      → Governança (Constituição, MOCs, Padrões, Protocolos)
  ├── MOCs/      → Índices unificados
  ├── PADROES/   → Nomenclatura, guias, manuais
  ├── PROTOCOLOS/→ Como fazer as coisas
  ├── planejamento/ → Planos ativos 2026
  ├── _config/   → Scripts, automação
  └── ARQUIVO/   → Histórico (checkpoints, logs)
01_CONHECIMENTO/ → Base de conhecimento permanente
02_PROJETOS/     → Projetos ativos (6)
03_APRENDIZADO/  → Cursos
04_RECURSOS/     → Templates, prompts, checklists, agentes
05_PESSOAL/      → Notas privadas
99_ARQUIVO/      → Cold storage
```

### Agentes (7)

**Plataforma:** Claude Architect, Gemini Guardian
**Domínio:** Névoa, Coach (TDAH), Pedro (Tráfego), Alan (IA), Lucas (DeFi), Marie Kondo

---

## 📖 Guias (Progressive Disclosure)

**IMPORTANTE:** Ler apenas o necessário para economizar tokens.

- `00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md` - O que ler (Claude)
- `00_SISTEMA/GUIAS/GUIA_Leitura_Gemini.md` - O que ler (Gemini)
- `00_SISTEMA/GUIAS/GUIA_Usuario_Quick_Start.md` - Navegação rápida
- `00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md` - Índice (29 docs)

**Economia:** 40-50% tokens (Progressive Disclosure)

---

## 🎯 Core Principles

### 1. Standards Are Law
**Documentos críticos:**
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Naming (OBRIGATÓRIO)
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - File creation (OBRIGATÓRIO)

**NO EXCEPTIONS.**

### 2. MOCs = Organizational Layer
3 níveis: MOC Master → Category MOCs → Specific MOCs
**Sempre atualizar MOCs ao criar/mover arquivos.**

### 3. Naming Conventions
```
MOC_Name.md          → System MOC
_MOC_Name.md         → Category MOC (underscore!)
TEMPLATE_Type.md     → Template
PROTOCOLO_Name.md    → Protocol
STATUS_Name.md       → Status
CHECKPOINT_18JAN2026.md → Snapshot (DDMMMYYYY)
```

**Regras:** UPPERCASE prefixos | CamelCase hierarquia | Underscores (NO spaces) | <60 chars

### 4. Estruturas Padrão
**Curso:** README.md, notas/, recursos/
**Projeto:** README.md, STATUS_ATUAL.md, planejamento/, checkpoints/, docs/, recursos/, tarefas/, metricas/

---

## 🚀 Comandos Disponíveis (15 total)

### Core Agents

| Comando | Função |
| ------- | ------ |
| `/nevoa` | Orquestrador central |
| `/claude-architect` | Qualidade e padrões |
| `/marie-kondo` | Organização + limpeza raiz |

### Domain Agents

| Comando | Função |
| ------- | ------ |
| `/coach` | TDAH & Produtividade (absorveu /elena) |
| `/alan` | IA & Automação (absorveu /alan-vault) |
| `/pedro` | Tráfego pago |
| `/lucas` | DeFi |
| `/kabak-agent` | Projeto KabaK |

### Essential Tools

| Comando | Função |
| ------- | ------ |
| `/validate` | Validação de arquivos |
| `/mapa` | Índice inteligente |
| `/gemini` | Delegação Gemini |
| `/ultra-think` | Análise profunda |
| `/sync` | Sincronização Bi-IA |

### Context

| Comando | Função |
| ------- | ------ |
| `/learn` | Modo aprendizado |
| `/work` | Modo projetos |

### Regras Permanentes

- **Limite:** Máximo 15 comandos (adicionar = remover outro)
- **Workflows:** Apenas para Gemini/Antigravity (10 ativos)
- **Skills:** Apenas funcionalidades complexas (4 ativas)
- **Revisão:** Trimestral para remover não utilizados

---

## 📋 Workflow: Criar Arquivos

**RESUMO (Ver protocolo completo):**
1. Ler PROTOCOLO_CRIACAO_ARQUIVOS.md
2. Ler NOMENCLATURA.md
3. Consultar MOC categoria
4. Validar localização
5. Criar arquivo(s)
6. Atualizar MOC

**Use `/validate` antes de criar!**

**Protocolo detalhado:** `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md`

---

## 📍 File Locations (Quick Reference)

| Tipo | Localização | Prefixo |
|:-----|:------------|:--------|
| Templates | `04_RECURSOS/TEMPLATES/` | `TEMPLATE_` |
| Prompts | `04_RECURSOS/PROMPTS/` | (varia) |
| Checklists | `04_RECURSOS/CHECKLISTS/` | `CHECKLIST_` |
| Category MOC | Pasta categoria | `_MOC_` |
| System MOC | `00_SISTEMA/MOCs/` | `MOC_` |
| Protocolos | `00_SISTEMA/PROTOCOLOS/` | `PROTOCOLO_` |
| Planos | `00_SISTEMA/planejamento/` | `PLANO_` |

---

## ⚠️ Erros Comuns (Top 5)

1. ❌ Criar sem ler padrões → ✅ Ler NOMENCLATURA.md primeiro
2. ❌ Templates fora de 04_RECURSOS/ → ✅ Sempre em 04_RECURSOS/TEMPLATES/
3. ❌ Espaços em nomes → ✅ Usar underscores
4. ❌ Esquecer atualizar MOCs → ✅ Sempre atualizar MOC relevante
5. ❌ Prefixo errado (INDEX_ vs MOC_) → ✅ Consultar NOMENCLATURA.md

---

## 📝 Regras de Linting Markdown (OBRIGATÓRIO)

**Acordo Bi-IA - Sempre seguir:**

| Regra | Errado | Correto |
| ----- | ------ | ------- |
| MD040 | ` ``` ` (sem linguagem) | ` ```text `, ` ```bash `, ` ```json ` |
| MD036 | `**Título**` isolado | `### Título` |
| MD026 | `### Título:` | `### Título` |
| MD060 | `\|Texto\|` | `\| Texto \|` |
| MD022 | Header sem linha vazia | Linha vazia antes/depois de headers |
| MD032 | Lista sem linha vazia | Linha vazia antes/depois de listas |
| MD004 | Misturar `*` e `-` | Usar apenas `-` em listas |

**Checklist antes de salvar .md:**

- [ ] Code blocks têm linguagem especificada?
- [ ] Títulos usam `###` e não `**negrito**`?
- [ ] Tabelas têm espaços nas pipes?
- [ ] Headers têm linha vazia antes/depois?

---

## 🤖 Bi-IA System

**Claude Code (você):** Estratégia, arquitetura, decisões críticas, gestão vault
**Gemini 3 Pro (Antigravity):** Execução, bulk operations, processamento longo (1M tokens, free tier)

**Config:** `.gemini/GEMINI.md`
**Protocolo:** `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO.md`

---

## 📊 Manutenção

**Semanal (Friday 17h):**
- Process `_inbox/`
- Update projetos ativos
- Update STATUS_VAULT.md

**Protocol:** `00_SISTEMA/PROTOCOLO_REVISAO_SEMANAL.md`

**Ao criar conteúdo:**
1. Ler padrões
2. Atualizar MOCs
3. Seguir nomenclatura
4. Usar localização correta

---

## 🔗 Arquivos Críticos

**Must Read:**
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` (CRÍTICO)
- `00_SISTEMA/PADROES/NOMENCLATURA.md` (CRÍTICO)
- `STATUS_VAULT.md` - Estado atual
- MOC categoria relevante (conforme necessário)

**Para usuário:**
- `README.md` - Visão geral
- `00_SISTEMA/MOCs/MOC_SEGUNDO_CEREBRO_MASTER.md` - MOC master

---

## ✅ Compromisso Claude Code

**Comprometo-me a:**
1. Ler PROTOCOLO_CRIACAO_ARQUIVOS.md antes de criar arquivos
2. Consultar NOMENCLATURA.md para naming
3. Validar estrutura vs padrões
4. Atualizar MOCs
5. Informar localizações claramente
6. Admitir e corrigir erros prontamente

**ZERO EXCEÇÕES.**

---

## 🆘 Ajuda Rápida

**Confuso sobre onde criar?**
```bash
/validate "want to create [description]"
```

**Padrões não claros?**
```bash
Ler: 00_SISTEMA/PADROES/NOMENCLATURA.md
Ler: 00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md
```

**Cometeu erro?**
1. Admitir ao usuário
2. Explicar o que aconteceu
3. Corrigir (mover/renomear)
4. Documentar em STATUS_VAULT.md

---

**Version:** 3.1.0 (Auditoria Comandos)
**Updated:** 25/Jan/2026
**Status:** ✅ ACTIVE - Sistema Governança Implementado
**Tokens:** ~5k

**THIS FILE IS LAW IN THE VAULT.**
