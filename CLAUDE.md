---
criado: 2025-11-24T21:45:11-03:00
atualizado: 2025-11-28T12:10:52-03:00
---
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

---

## ⚠️ PROTOCOLO OBRIGATÓRIO - LER PRIMEIRO

**ANTES DE CRIAR QUALQUER ARQUIVO, VOCÊ DEVE:**

1. **LER:** `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` (OBRIGATÓRIO)
2. **LER:** `00_SISTEMA/PADROES/NOMENCLATURA.md` (OBRIGATÓRIO)
3. **CONSULTAR:** MOC relevante da categoria
4. **VALIDAR:** Localização e nomenclatura corretas
5. **SÓ ENTÃO:** Criar arquivo(s)

**ZERO EXCEÇÕES. Este é um sistema PKM (Personal Knowledge Management) com padrões rigorosos.**

---

## Repository Overview

**Meu_Segundo_Cerebro** - Sistema de Gestão de Conhecimento Pessoal (PKM)

**Owner:** Gassen Jean Bou Karim
**System:** Híbrido Alan Nicolas + Névoa 3.0
**Status:** ✅ Estrutura Base Completa (Fase 4/5)
**Version:** 2.0
**Agentes:** 9 especializados (Plataforma + Domínio)

### O Que É Este Vault

Um segundo cérebro digital organizado com:
- 6 categorias principais (00-05)
- MOCs (Maps of Content) como camada organizacional
- Padrões rigorosos de nomenclatura
- Sistema bi-IA (Claude Code + Gemini CLI)
- **9 Agentes especializados** (Névoa, Elena, Pedro, Alan, Lucas, Dr. Green, Marie Kondo, Gemini Guardian, Claude Architect)
- Slash commands para economia de tokens

### Sistema de Agentes

**Agentes de Plataforma:**
- `Claude Architect` - Guardião de padrões quando usando Claude Code
- `Gemini Guardian` - Otimizador quando usando Gemini

**Agentes de Domínio:**
- `Névoa` - Orquestração e continuidade
- `Elena Vasquez` - Produtividade & TDAH
- `Pedro Sobral` - Tráfego & Marketing
- `Alan Nicolas` - IA & Automação
- `Lucas Amoedo` - DeFi & Cripto
- `Dr. Green` - Cultivo Medicinal
- `Marie Kondo` - Organização de Vaults

**Workflows Disponíveis:**
- `/nevoa` - Ativar Névoa
- `/claude-architect` - Ativar Claude Architect
- `/marie-kondo` - Ativar Marie Kondo
- `/atualizar-status` - Atualizar STATUS_VAULT.md
- `/limpeza-raiz-vault` - Limpar duplicatas da raiz

---

## 📂 Structure

```
Meu_Segundo_Cerebro/
│
├── .claude/                    # Claude Code configuration
│   └── commands/              # Slash commands (/learn, /work, etc)
│
├── .gemini/                    # Gemini CLI configuration
│   └── GEMINI.md              # Custom instructions
│
├── 00_SISTEMA/                 # Meta organization
│   ├── MOCs/                  # System-level Maps of Content
│   ├── PADROES/               # Standards documentation
│   │   ├── NOMENCLATURA.md    # Naming standards (READ THIS!)
│   │   └── ESTRUTURA_PROJETOS.md  # Project structure standards
│   ├── PROTOCOLOS/            # System protocols
│   │   └── PROTOCOLO_CRIACAO_ARQUIVOS.md  # File creation protocol (MANDATORY!)
│   └── planejamento/          # System planning docs
│
├── 01_CONHECIMENTO/            # Knowledge base
├── 02_PROJETOS/                # Active projects
├── 03_APRENDIZADO/             # Courses and learning
├── 04_RECURSOS/                # Templates, prompts, checklists
│   ├── TEMPLATES/
│   ├── PROMPTS/
│   └── CHECKLISTS/
├── 05_PESSOAL/                 # Personal notes
│
├── _inbox/                     # Quick capture
├── CLAUDE.md                   # This file
├── README.md                   # Vault overview
└── STATUS_VAULT.md             # Current vault status
```

---

## 🎯 Core Principles

### 1. Standards Are Law

**Everything** follows standards documented in:
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Naming conventions
- `00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md` - Project structure
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - File creation protocol

**NO EXCEPTIONS.**

### 2. MOCs Are Organizational Layer

MOCs (Maps of Content) = Index files that organize other files.

**3 Levels:**
1. **MOC Master** → `00_SISTEMA/MOCs/MOC_SEGUNDO_CEREBRO_MASTER.md`
2. **Category MOCs** → `_MOC_Conhecimento.md`, `_MOC_Projetos.md`, etc
3. **Specific MOCs** → Per project/topic

**Always update MOCs when creating/moving files.**

### 3. Naming Conventions

```
MOC_Name.md           → Map of Content (system)
_MOC_Name.md          → Map of Content (category - with underscore!)
TEMPLATE_Type.md      → Reusable template
PLANO_Name.md         → Planning document
PROTOCOLO_Name.md     → Protocol/procedure
STATUS_Name.md        → Status document
CHECKPOINT_17JAN2025.md → Snapshot with date
Category_Sub_Topic.md → Regular content (hierarchical)
```

**Rules:**
- UPPERCASE for special prefixes
- CamelCase for hierarchy
- Dates: DDMMMYYYY (17JAN2025)
- Underscores, NEVER spaces
- < 60 characters

### 4. Course/Project Structure

**Course (03_APRENDIZADO/):**
```
Nome_Curso/
├── README.md
├── notas/           # Notes only!
└── recursos/        # Supporting materials
```

**Project (02_PROJETOS/):**
```
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
├── checkpoints/
├── docs/
├── recursos/
├── tarefas/
└── metricas/
```

---

## 🚀 Available Commands

Slash commands are defined in `.claude/commands/`:

| Command | Purpose |
|---------|---------|
| `/learn` | Activate learning context |
| `/work` | Activate project context |
| `/knowledge` | Query knowledge base |
| `/system` | Vault management |
| `/gemini` | Delegate to Gemini Agent / Antigravity |
| `/validate` | Validate file creation (use before creating!) |

---

## 📋 Workflow: Creating Files

**MANDATORY WORKFLOW:**

```
1. User requests file creation
   ↓
2. PAUSE - Read 00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md
   ↓
3. Read NOMENCLATURA.md - Identify prefix/pattern
   ↓
4. Identify category - Read relevant MOC
   ↓
5. Determine exact location
   ↓
6. Validate with user IF new structure
   ↓
7. Create file(s)
   ↓
8. Update MOC
   ↓
9. Update STATUS_VAULT.md (if structural)
   ↓
10. Inform user of final location
```

**Use `/validate` command to check before creating!**

---

## 📍 File Location Guide

| File Type | Location | Prefix |
|-----------|----------|--------|
| Templates | 04_RECURSOS/TEMPLATES/ | TEMPLATE_ |
| Prompts | 04_RECURSOS/PROMPTS/ | (varies) |
| Checklists | 04_RECURSOS/CHECKLISTS/ | CHECKLIST_ |
| Category MOC | In category folder | _MOC_ |
| System MOC | 00_SISTEMA/MOCs/ | MOC_ |
| Protocols | 00_SISTEMA/ | PROTOCOLO_ |
| Plans | 00_SISTEMA/planejamento/ | PLANO_ |
| Course notes | curso/notas/ | Category_Sub |
| Course resources | curso/recursos/ | (varies) |

---

## ⚠️ Common Mistakes to Avoid

### ❌ NEVER DO THIS:

1. **Create without reading standards**
   ```
   ❌ Create INDEX_Something.md
   ✅ Read NOMENCLATURA.md → Use MOC_Something.md
   ```

2. **Templates in wrong place**
   ```
   ❌ curso/notas/TEMPLATE_X.md
   ✅ 04_RECURSOS/TEMPLATES/TEMPLATE_X.md
   ```

3. **Spaces in names**
   ```
   ❌ My File.md
   ✅ My_File.md
   ```

4. **Forget to update MOCs**
   ```
   ❌ Create file, forget to link in MOC
   ✅ Create file AND update relevant MOC
   ```

5. **Wrong prefix**
   ```
   ❌ INDEX_Methodology.md
   ✅ MOC_Methodology.md
   ```

---

## 🎓 Learning Context (Alan Nicolas)

Current learning source:
- **03_APRENDIZADO/Alan_Nicolas_Academia_Lendaria/**
- Lives processed, episodes, second brain content
- Follow course structure: README → notas/ → recursos/

---

## 🤖 Bi-AI System

**Claude Code (Strategic Agent):**
- Strategic planning
- Complex code & Architecture
- Critical decisions
- Vault Management

**Antigravity (Gemini 3 Pro - Execution Agent):**
- **IDE & Execution Environment**
- Long-context processing (1M tokens)
- Bulk file operations & Refactoring
- Content processing (Summarization, Translation)
- Cost efficiency (Free tier)

Configuration in `.gemini/GEMINI.md`

---

## 📊 Maintenance

### Weekly Checkpoint (Friday 17h)

Protocol: `00_SISTEMA/PROTOCOLO_REVISAO_SEMANAL.md`

Checklist:
- [ ] Process `_inbox/` (should be empty)
- [ ] Update active projects
- [ ] Update learning progress
- [ ] Update STATUS_VAULT.md
- [ ] Create weekly checkpoint

### When Creating New Content

1. **Always** read relevant standards first
2. **Always** update MOCs
3. **Always** follow naming conventions
4. **Always** use correct location

---

## 🔗 Important Files

**Must Read (for Claude):**
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - CRITICAL
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - CRITICAL
- `00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md` - CRITICAL
- `STATUS_VAULT.md` - Current state
- Relevant category MOC - As needed

**For User:**
- `README.md` - Vault overview
- `00_SISTEMA/MOCs/MOC_SEGUNDO_CEREBRO_MASTER.md` - Master MOC

---

## ✅ Claude Code Commitment

**I, Claude Code, commit to:**

1. ✅ Read 00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md before creating ANY file
2. ✅ Consult NOMENCLATURA.md for naming
3. ✅ Check relevant MOC for location
4. ✅ Validate structure matches standards
5. ✅ Update MOCs after creating files
6. ✅ Inform user clearly of final locations
7. ✅ Admit mistakes immediately if standards violated
8. ✅ Correct errors promptly

**ZERO EXCEPTIONS.**

---

## 📖 Glossary

- **MOC** - Map of Content (index file)
- **PKM** - Personal Knowledge Management
- **Slash Command** - Claude Code command (e.g., /learn)
- **Token Economy** - Strategy to save tokens
- **Wikilink** - Obsidian link: `[[File]]`
- **Checkpoint** - Progress snapshot

---

## 🆘 Help

**If confused about where to create file:**
```bash
/validate "want to create [description]"
```

**If standards unclear:**
```bash
Read: 00_SISTEMA/PADROES/NOMENCLATURA.md
Read: 00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md
```

**If made mistake:**
1. Admit to user
2. Explain what happened
3. Correct (move/rename)
4. Document in STATUS_VAULT.md

---

**Version:** 2.0
**Updated:** 24/Nov/2025
**Status:** ✅ ACTIVE AND MANDATORY

**THIS FILE IS LAW IN THE VAULT.**
