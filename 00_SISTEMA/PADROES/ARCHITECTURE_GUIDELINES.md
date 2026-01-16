# 🏗️ ARCHITECTURE GUIDELINES

**Meu Segundo Cérebro - Architectural Design Document**

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Autor:** Claude Sonnet 4.5
**Status:** ✅ Ativo e Obrigatório
**Inspiração:** AI Large Codebase Management (300k+ lines) + Boris Engineering + Alan Nicolas PKM

---

## 🎯 ARCHITECTURAL VISION

> **"A Personal Knowledge Management system designed for AI-first interaction, with progressive context loading, modular organization, and zero exceptions to standards."**

### Core Philosophy

1. **AI-Native Architecture**: Designed for Claude Code + Gemini collaboration
2. **Context-Aware Loading**: Smart Zone (stay under 40% context window)
3. **Progressive Disclosure**: Load only what's needed, when needed
4. **Modular Organization**: Self-contained units with clear boundaries
5. **Standards Enforcement**: Zero tolerance for deviations

---

## 📊 SYSTEM OVERVIEW

### 1. Vault Structure (6-Category System)

```
Meu_Segundo_Cerebro/
│
├── 00_SISTEMA/          # Meta-organization (Core System)
│   ├── PADROES/         # Standards (Load Always)
│   ├── PROTOCOLOS/      # Protocols (Load Always)
│   ├── MOCs/            # Maps of Content (Load on-demand)
│   ├── AGENTES/         # Agent profiles (Load on-demand)
│   ├── CHECKPOINTS/     # System snapshots (Load on-demand)
│   └── REFERENCIAS/     # External docs (Load rarely)
│
├── 01_CONHECIMENTO/     # Knowledge Base (Load on-demand by topic)
│   └── [15+ categories organized by domain]
│
├── 02_PROJETOS/         # Active Projects (Load per-project)
│   └── [Project folders with standardized structure]
│
├── 03_APRENDIZADO/      # Courses & Learning (Load per-course)
│   └── [Course folders with notes/ and recursos/]
│
├── 04_RECURSOS/         # Templates, Prompts, Tools (Load on-demand)
│   ├── TEMPLATES/
│   ├── PROMPTS/
│   └── CHECKLISTS/
│
└── 05_PESSOAL/          # Personal Notes (Load rarely)
```

### 2. MOC Hierarchy (3-Level System)

```
Level 1: MOC_SEGUNDO_CEREBRO_MASTER.md
         └── Central index (26KB, load on-demand)

Level 2: Category MOCs (_MOC_*.md)
         ├── _MOC_Conhecimento.md
         ├── _MOC_Projetos.md
         ├── _MOC_Aprendizado.md
         ├── _MOC_Recursos.md
         └── _MOC_Pessoal.md

Level 3: Specific MOCs (Per project/topic)
         ├── MOC_DeFi_Crypto.md
         ├── MOC_IA_Ferramentas_Digitais.md
         └── [20+ domain-specific MOCs]
```

---

## 🧠 CONTEXT WINDOW MANAGEMENT

### The Smart Zone Principle (40% Rule)

**Inspiration:** AI codebase management (300k+ lines)

**Rule:** Keep context usage under 40% (80k/200k tokens for Claude)

**Implementation:**

```
┌─────────────────────────────────────────────────┐
│ CONTEXT WINDOW (200k tokens max)                │
│                                                  │
│ ████████████████ 40% = SMART ZONE (80k tokens)  │
│ ░░░░░░░░░░░░░░░░░░░░░░░░ 60% = Reserve          │
│                                                  │
│ WHY 40%?                                         │
│ - Leaves room for agent responses (30-40k)      │
│ - Buffer for tool use and iterations (20-30k)   │
│ - Prevents truncation and context loss          │
└─────────────────────────────────────────────────┘
```

### Context Zones

```
┌─────────────────────────────┬──────────┬──────────────┐
│ Zone                        │ Tokens   │ When to Load │
├─────────────────────────────┼──────────┼──────────────┤
│ Core (Always Load)          │ ~15k     │ Session Start│
│ - CLAUDE.md                 │          │              │
│ - SESSION_LOG.md            │          │              │
│ - PC_SYNC_LOG.md            │          │              │
│ - NOMENCLATURA.md           │          │              │
│ - PROTOCOLO_CRIACAO.md      │          │              │
├─────────────────────────────┼──────────┼──────────────┤
│ Context (Load on-demand)    │ ~30-50k  │ When Needed  │
│ - Category MOCs             │          │              │
│ - Project README/STATUS     │          │              │
│ - Course materials          │          │              │
├─────────────────────────────┼──────────┼──────────────┤
│ Deep (Load selectively)     │ ~20-30k  │ Specific Task│
│ - Full file contents        │          │              │
│ - Historical checkpoints    │          │              │
│ - References                │          │              │
└─────────────────────────────┴──────────┴──────────────┘
```

---

## 🔄 PROGRESSIVE DISCLOSURE STRATEGY

### Research → Plan → Implementation (RPI Framework)

**Stage 1: RESEARCH** (Context: 20-30k tokens)
```bash
# Load minimal context to understand the ask
1. Read: CLAUDE.md (know the rules)
2. Read: SESSION_LOG.md (know what Gemini did)
3. Read: Relevant Category MOC (know the structure)
4. Grep: Find relevant files (don't read yet)
```

**Stage 2: PLAN** (Context: 30-50k tokens)
```bash
# Load what you need to design the solution
1. Read: 3-5 critical files identified in Research
2. Read: Related templates/protocols
3. Design: Architecture/approach
4. Validate: Against standards
```

**Stage 3: IMPLEMENTATION** (Context: 40-70k tokens)
```bash
# Execute with full context of target area
1. Load: Files to be modified
2. Execute: Changes following plan
3. Update: MOCs and STATUS files
4. Document: In SESSION_LOG.md
```

### On-Demand Loading Pattern

**Bad (Context Explosion):**
```bash
❌ Read entire vault structure upfront (150k tokens)
❌ Load all MOCs simultaneously (80k tokens)
❌ Read files before knowing if needed (waste)
```

**Good (Progressive Loading):**
```bash
✅ Start with CLAUDE.md only (5k tokens)
✅ Use /mapa skill for index (2k tokens vs 50k)
✅ Load category MOC when category identified (5-10k)
✅ Read specific files only when ready to act (10-20k)
```

### Example: Creating a New Project

```
Step 1: RESEARCH (Total: 25k tokens)
├── Read: CLAUDE.md (5k)
├── Read: NOMENCLATURA.md (13k)
├── Read: ESTRUTURA_PROJETOS.md (7k)
└── DECISION: Need to create project structure

Step 2: PLAN (Additional: 20k tokens)
├── Read: TEMPLATE_Projeto_Padrao.md (8k)
├── Read: _MOC_Projetos.md (5k)
├── Read: Existing project as reference (7k)
└── DECISION: Create [Project] with 7 folders

Step 3: IMPLEMENT (Additional: 15k tokens)
├── Create: Project folder structure
├── Write: README.md, STATUS_ATUAL.md
├── Update: _MOC_Projetos.md (5k)
├── Update: SESSION_LOG.md (10k)
└── TOTAL SESSION: 60k tokens (30% of limit) ✅
```

---

## 🗂️ FILE ORGANIZATION PATTERNS

### Decision Matrix: Where Does This File Go?

```
┌─────────────────────┬────────────────────┬──────────────────┐
│ File Type           │ Location           │ Prefix           │
├─────────────────────┼────────────────────┼──────────────────┤
│ Template            │ 04_RECURSOS/       │ TEMPLATE_        │
│                     │ TEMPLATES/         │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Prompt              │ 04_RECURSOS/       │ Prompt_          │
│                     │ PROMPTS/[AI]/      │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Checklist           │ 04_RECURSOS/       │ CHECKLIST_       │
│                     │ CHECKLISTS/        │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Category MOC        │ [Category folder]  │ _MOC_            │
├─────────────────────┼────────────────────┼──────────────────┤
│ System MOC          │ 00_SISTEMA/MOCs/   │ MOC_             │
├─────────────────────┼────────────────────┼──────────────────┤
│ Protocol            │ 00_SISTEMA/        │ PROTOCOLO_       │
│                     │ PROTOCOLOS/        │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Standard            │ 00_SISTEMA/        │ (varies)         │
│                     │ PADROES/           │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Checkpoint          │ [Project]/         │ CHECKPOINT_      │
│                     │ checkpoints/       │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Plan                │ [Project]/         │ PLANO_           │
│                     │ planejamento/      │                  │
├─────────────────────┼────────────────────┼──────────────────┤
│ Course Notes        │ [Course]/notas/    │ Category_Sub_    │
├─────────────────────┼────────────────────┼──────────────────┤
│ Knowledge Content   │ 01_CONHECIMENTO/   │ Category_Sub_    │
│                     │ [Domain]/          │ Topic            │
└─────────────────────┴────────────────────┴──────────────────┘
```

### Naming Convention by Category

**Refer to:** `NOMENCLATURA.md` for full specification

**Key Rules:**
1. **UPPERCASE prefixes** for special files (MOC_, PLANO_, TEMPLATE_)
2. **CamelCase** for hierarchy (Marketing_Digital_Facebook_Ads)
3. **Underscores** instead of spaces (NEVER spaces)
4. **Dates:** DDMMMYYYY format (17JAN2026)
5. **Length:** <60 characters
6. **Forbidden chars:** / \ : * ? " < > |

### When to Create Sub-folders

```
Rule: Create sub-folder when:
├── 1. More than 5 files of same type
├── 2. Clear logical grouping exists
├── 3. Improves navigation and discoverability
└── 4. Follows established pattern

Example:
❌ Bad: 10 loose templates in 04_RECURSOS/
✅ Good: 04_RECURSOS/TEMPLATES/Metodologia_IA/ (organized)

❌ Bad: 50 knowledge files in 01_CONHECIMENTO/ root
✅ Good: 01_CONHECIMENTO/IA/, /Marketing/, /DeFi/ (categorized)
```

---

## 🤖 AI INTEGRATION GUIDELINES

### Bi-AI Architecture (Claude + Gemini)

```
┌────────────────────────────────────────────────────┐
│ ANTIGRAVITY (IDE Environment)                      │
│                                                     │
│  ┌─────────────────┐      ┌──────────────────┐    │
│  │ CLAUDE SONNET   │      │ GEMINI 3 PRO     │    │
│  │ 4.5             │      │                  │    │
│  │                 │      │                  │    │
│  │ 200k tokens     │◄────►│ 1M tokens        │    │
│  │ Strategic Brain │      │ Processing Power │    │
│  │                 │      │                  │    │
│  │ USE FOR:        │      │ USE FOR:         │    │
│  │ - Decisions     │      │ - Volume reading │    │
│  │ - Architecture  │      │ - Analysis       │    │
│  │ - Code review   │      │ - Reports        │    │
│  │ - Edits         │      │ - GitHub API     │    │
│  └─────────────────┘      └──────────────────┘    │
│           │                         │              │
│           └─────────┬───────────────┘              │
│                     ▼                              │
│            SESSION_LOG.md                          │
│         (Bi-directional comms)                     │
└────────────────────────────────────────────────────┘
```

**Communication Protocol:**
- **ALWAYS** read `SESSION_LOG.md` at session start
- **ALWAYS** update `SESSION_LOG.md` before session end
- **ALWAYS** check `PC_SYNC_LOG.md` for multi-device sync

### Skills vs Direct Commands

**Use Skills (/) when:**
```bash
✅ Activating specialized context (domain agents)
✅ Complex multi-step workflows
✅ Loading domain-specific knowledge
✅ Triggering pre-defined automations

Examples:
/nevoa     # Activate orchestration agent
/elena     # Load TDAH productivity context
/mapa      # Load full vault index (2k vs 50k tokens!)
/validate  # Validate file creation before doing
```

**Use Direct Tool Calls when:**
```bash
✅ One-off file operations
✅ Simple reads/writes
✅ Ad-hoc searches
✅ Exploratory analysis

Examples:
Read specific file
Grep for pattern
Create single document
```

### When to Use /mapa Skill

**The /mapa Advantage:**
```
WITHOUT /mapa:
├── Read: MOC_MASTER.md (26k tokens)
├── Read: 5x Category MOCs (30k tokens)
├── Read: 10x Specific MOCs (40k tokens)
└── TOTAL: ~96k tokens (48% of limit) ❌

WITH /mapa:
├── Load: Pre-computed index (2k tokens)
├── Query: "Find all DeFi files"
├── Result: Instant list, zero exploration
└── TOTAL: ~2k tokens (1% of limit) ✅

SAVINGS: 94k tokens = 47% of context window!
```

**Use /mapa when:**
- Session start (get orientation)
- Finding files across categories
- Need to see full vault structure
- Planning large-scale changes

---

## 🎯 DESIGN DECISIONS & TRADE-OFFS

### 1. Why 6 Categories (00-05)?

**Decision:** Fixed top-level structure with numeric prefixes

**Rationale:**
```
✅ Pros:
├── Forces consistent organization
├── Numeric prefix ensures order (OS-independent)
├── Predictable locations (cognitive load ↓)
├── Scales indefinitely within each category
└── Clear separation of concerns

❌ Cons:
├── Rigid structure (but that's the point!)
└── Requires discipline (enforced by protocols)

Trade-off: Rigidity for Predictability ✅
```

### 2. Why MOC System (vs Tags/Folders)?

**Decision:** 3-level MOC hierarchy as primary organization

**Rationale:**
```
MOCs vs Tags:
├── MOCs: Contextual connections (why files relate)
├── Tags: Flat categorization (no relationship info)
└── WINNER: MOCs (richer semantics)

MOCs vs Deep Folders:
├── MOCs: Flat files, rich linking
├── Folders: Deep nesting, hard to navigate
└── WINNER: MOCs (easier AI traversal)

Trade-off: Manual MOC Updates for Better Navigation ✅
```

### 3. Why Bi-AI System?

**Decision:** Claude (strategic) + Gemini (volume) instead of single AI

**Rationale:**
```
Claude Only:
├── Limited to 200k tokens
├── Expensive for high-volume tasks
└── PROBLEM: Cost and capacity constraints

Gemini Only:
├── 1M tokens (great!)
├── Less precise for architecture decisions
└── PROBLEM: Quality trade-off

Claude + Gemini:
├── Claude: Strategic decisions (high-value tokens)
├── Gemini: Volume processing (free tokens)
└── SOLUTION: Best of both worlds ✅

Trade-off: Coordination Overhead for 90% Token Savings ✅
```

### 4. Why Strict Naming Standards?

**Decision:** Zero exceptions to NOMENCLATURA.md

**Rationale:**
```
Flexible Naming:
├── Creative freedom
├── User preference respected
└── PROBLEM: Inconsistency, hard to find files

Strict Standards:
├── TEMPLATE_ = instantly recognizable
├── CamelCase = hierarchy visible in name
├── DDMMMYYYY = sortable dates
└── SOLUTION: Predictable, AI-friendly ✅

Trade-off: Creativity for Discoverability ✅
```

### 5. Why Modular Project Structure?

**Decision:** 7 mandatory folders in every project

**Rationale:**
```
Variable Structure:
├── Each project organized differently
└── PROBLEM: Cognitive load when switching projects

Standard Structure:
├── planejamento/ (always know where plans are)
├── checkpoints/ (always know where history is)
├── docs/ (always know where guides are)
└── SOLUTION: Zero cognitive load ✅

Trade-off: Flexibility for Consistency ✅
```

---

## 📐 ARCHITECTURAL PRINCIPLES

### Principle 1: Context is Precious

**Rule:** Treat context window like RAM in 1990s

**Implementation:**
```bash
# Bad (Context Bloat)
❌ Load everything upfront
❌ Keep unused files in context
❌ Duplicate information across docs

# Good (Context Economy)
✅ Load progressively (RPI framework)
✅ Use /mapa for index (2k vs 50k)
✅ Single source of truth (SSOT)
```

**Example:**
```
Project Status Info:

❌ WRONG: STATUS in README + STATUS_ATUAL + checkpoints
          (triple redundancy, 30k tokens)

✅ RIGHT: STATUS_ATUAL.md = SSOT, README links to it
          (single source, 10k tokens)
```

### Principle 2: Progressive Disclosure

**Rule:** Load context in stages, not all at once

**Implementation:**
```
Stage 1: Orientation (What am I working on?)
├── CLAUDE.md (5k tokens)
├── SESSION_LOG.md (15k tokens)
└── Category MOC (5k tokens)

Stage 2: Planning (How to approach this?)
├── Relevant protocols (10k tokens)
├── Templates/examples (10k tokens)
└── Related files (15k tokens)

Stage 3: Execution (Make it happen)
├── Files to modify (20k tokens)
├── Supporting context (10k tokens)
└── Documentation updates (10k tokens)
```

### Principle 3: Modular Organization

**Rule:** Self-contained units with clear boundaries

**Implementation:**
```
Project Module:
02_PROJETOS/Project_Name/
├── README.md              # Interface (what it is)
├── STATUS_ATUAL.md        # State (where we are)
├── planejamento/          # Plans (where we're going)
├── checkpoints/           # History (where we've been)
├── docs/                  # Knowledge (how it works)
├── recursos/              # Assets (what we use)
├── tarefas/               # Work (what to do)
└── metricas/              # Metrics (how we're doing)

Benefits:
✅ Load one project without bleeding into others
✅ Delete/archive entire project as unit
✅ AI can understand scope in single read
```

### Principle 4: Standards Enforcement

**Rule:** Zero exceptions, zero tolerance

**Implementation:**
```
Enforcement Layers:

Layer 1: Documentation (NOMENCLATURA.md, ESTRUTURA_PROJETOS.md)
├── Standards clearly written
└── Examples provided

Layer 2: Validation (/validate skill)
├── Check before creating
└── Prevent errors proactively

Layer 3: Protocols (PROTOCOLO_CRIACAO_ARQUIVOS.md)
├── Mandatory workflow
└── No shortcuts allowed

Layer 4: Auditing (SESSION_LOG.md)
├── Document deviations
└── Correct immediately
```

**Why Zero Exceptions?**
```
With Exceptions:
├── "Just this once" becomes pattern
├── Inconsistency spreads like virus
└── AI wastes tokens disambiguating

Without Exceptions:
├── Predictable structure always
├── AI finds files instantly
└── Standards actually mean something ✅
```

### Principle 5: AI-First Design

**Rule:** Optimize for AI interaction, not just human

**Implementation:**
```
Human-Optimized:
├── Nested folders (visual hierarchy)
├── Rich formatting (pretty docs)
└── Implicit context (humans infer)

AI-Optimized:
├── Flat structure + MOCs (explicit links)
├── Semantic prefixes (MOC_, PLANO_)
├── Explicit context (no inference needed)
└── Progressive loading (context economy)

RESULT: Design for AI = Better for humans too ✅
```

---

## 📊 METRICS & MONITORING

### Context Window Health

**Monitor these metrics:**

```
┌─────────────────────────┬────────┬──────────┐
│ Metric                  │ Target │ Alert At │
├─────────────────────────┼────────┼──────────┤
│ Session Start Context   │ <15k   │ >25k     │
│ Peak Context Usage      │ <80k   │ >120k    │
│ Average per Operation   │ <30k   │ >50k     │
│ MOC Load Frequency      │ 2-3x   │ >5x      │
│ File Re-reads           │ <2x    │ >3x      │
└─────────────────────────┴────────┴──────────┘
```

**If metrics red:**
```
1. Identify: What's loading too much?
2. Refactor: Break large files into modules
3. Delegate: Volume tasks to Gemini
4. Archive: Old/unused content
```

### Vault Health

**Monitor these structural metrics:**

```
┌─────────────────────────┬────────┬──────────┐
│ Metric                  │ Target │ Alert At │
├─────────────────────────┼────────┼──────────┤
│ Files in root (00-05)   │ 5-10   │ >15      │
│ MOC updates per week    │ 2-5    │ <1       │
│ Avg files per project   │ 15-30  │ >50      │
│ Orphaned files          │ 0      │ >5       │
│ Naming violations       │ 0      │ >0       │
└─────────────────────────┴────────┴──────────┘
```

**Audit checklist (monthly):**
```
[ ] All MOCs updated in last 30 days?
[ ] All projects have STATUS_ATUAL.md updated?
[ ] No files in wrong locations?
[ ] All new files follow NOMENCLATURA.md?
[ ] SESSION_LOG.md not bloated (archive if >3k lines)?
[ ] No duplicate/redundant files?
```

---

## 🏁 IMPLEMENTATION CHECKLIST

### For Claude Code (This Agent)

**When working in this vault, Claude MUST:**

```
[ ] Start every session reading CLAUDE.md
[ ] Check SESSION_LOG.md for Gemini updates
[ ] Check PC_SYNC_LOG.md for multi-device sync
[ ] Use progressive loading (RPI: Research → Plan → Implement)
[ ] Stay under 40% context window (80k/200k tokens)
[ ] Follow PROTOCOLO_CRIACAO_ARQUIVOS.md for file creation
[ ] Update MOCs after creating/moving files
[ ] Document work in SESSION_LOG.md before ending
[ ] Validate naming against NOMENCLATURA.md (zero exceptions)
[ ] Delegate volume tasks to Gemini (save tokens)
[ ] Use /mapa for orientation (not full vault load)
[ ] Maintain SSOT principle (no duplicate info)
```

### For Gemini (Partner Agent)

**When Gemini works in this vault, Gemini MUST:**

```
[ ] Read SESSION_LOG.md for Claude instructions
[ ] Read GEMINI.md for Gemini-specific guidance
[ ] Handle high-volume tasks (analysis, reports, cataloging)
[ ] Use 1M token capacity for deep processing
[ ] Document findings in SESSION_LOG.md for Claude
[ ] Follow same naming standards as Claude (NOMENCLATURA.md)
[ ] Use GitHub API for repository operations
[ ] Generate comprehensive reports (Claude reads summaries)
[ ] Archive old content when vault grows
[ ] Validate work against standards before committing
```

### For User (Gassen)

**To maintain vault health:**

```
[ ] Review SESSION_LOG.md weekly (know what AIs did)
[ ] Run /atualizar-status monthly (update STATUS_VAULT.md)
[ ] Sync across devices using PC_SYNC_LOG.md
[ ] Use /validate before asking AI to create files
[ ] Archive completed projects to 99_ARQUIVO/
[ ] Update CLAUDE.md when adding new protocols
[ ] Commit to GitHub weekly (backup)
[ ] Review and close old GitHub Issues/PRs
[ ] Audit vault health monthly (use checklist above)
```

---

## 📚 REFERENCE ARCHITECTURE DOCS

**Core Documents (Load Always):**
- `CLAUDE.md` - Instructions for Claude Code
- `NOMENCLATURA.md` - Naming standards
- `PROTOCOLO_CRIACAO_ARQUIVOS.md` - File creation protocol
- `ESTRUTURA_PROJETOS.md` - Project structure standard

**Context Documents (Load on-demand):**
- `SESSION_LOG.md` - Claude ↔ Gemini sync
- `PC_SYNC_LOG.md` - Multi-device sync
- `PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO.md` - Bi-AI workflows
- `STATUS_VAULT.md` - Current vault state

**MOC System (Load progressively):**
- `MOC_SEGUNDO_CEREBRO_MASTER.md` - Level 1 (master index)
- `_MOC_[Category].md` - Level 2 (category indices)
- `MOC_[Specific].md` - Level 3 (domain indices)

**Skills Documentation:**
- `00_SISTEMA/GUIA_COMANDOS_CLAUDE.md` - All available skills
- `.claude/commands/[skill].md` - Individual skill definitions

---

## 🎯 SUCCESS METRICS

**This architecture is successful when:**

```
✅ Context Usage: Sessions average <40% (80k/200k tokens)
✅ Token Economy: 90% savings via Gemini delegation
✅ Consistency: 100% compliance with NOMENCLATURA.md
✅ Findability: Any file located in <30 seconds
✅ Scalability: Vault grows to 10k+ files without slowdown
✅ Sync Quality: Zero conflicts between Claude/Gemini/PCs
✅ Maintenance: Monthly audit takes <30 minutes
✅ Onboarding: New AI agent productive in <1 session
```

---

## 📖 GLOSSARY

- **RPI Framework**: Research → Plan → Implementation (progressive context loading)
- **Smart Zone**: Keep context under 40% of limit (80k/200k tokens)
- **Progressive Disclosure**: Load context in stages as needed
- **SSOT**: Single Source of Truth (no duplicate information)
- **MOC**: Map of Content (index file linking related content)
- **Bi-AI**: Claude (strategic) + Gemini (volume) architecture
- **Context Window**: Token limit for AI conversation (200k for Claude, 1M for Gemini)
- **Handoff**: Passing work from Claude to Gemini or vice versa
- **On-Demand Loading**: Load files only when needed, not upfront

---

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO E OBRIGATÓRIO
**Próxima Revisão:** 16/Fev/2026

**ARCHITECTURE IS THE FOUNDATION OF SCALE! 🏗️✅**
