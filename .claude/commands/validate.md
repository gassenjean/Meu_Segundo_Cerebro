# Validate - File Creation & Organization

You are helping validate file creation plans AND audit vault organization.

## TWO MODES

### MODE 1: Validate File Creation (User provides description)
### MODE 2: Audit Organization (User says "audit" or "check organization")

---

## MODE 1: VALIDATE FILE CREATION

When user provides description of what they want to create.

### Process

1. **Read the standards:**
   - Read `00_SISTEMA/PADROES/NOMENCLATURA.md`
   - Identify the correct prefix and naming pattern

2. **Determine location:**
   - Based on file type, identify exact folder
   - Use this guide:
     - Templates → `04_RECURSOS/TEMPLATES/`
     - Checklists → `04_RECURSOS/CHECKLISTS/`
     - Prompts → `04_RECURSOS/PROMPTS/`
     - MOCs (category) → In category folder with `_MOC_` prefix
     - MOCs (system) → `00_SISTEMA/MOCs/` with `MOC_` prefix
     - Protocols → `00_SISTEMA/`
     - Plans → `00_SISTEMA/planejamento/`
     - Course notes → `03_APRENDIZADO/[course]/notas/`
     - Course resources → `03_APRENDIZADO/[course]/recursos/`

3. **Identify MOC to update:**
   - Which MOC needs to be updated after creation?

4. **Check for structural needs:**
   - Does a folder structure need to be created first?

### Output Format

```
✅ VALIDATION RESULT

📁 File Type: [type]
📂 Location: [exact path]
📝 Naming: [exact filename with prefix]
🔗 Update MOC: [which MOC file]
📋 Structure: [any folders to create first]

✅ Ready to proceed
OR
⚠️ Considerations: [list any warnings/questions]
```

### Example

User: "want to create methodology IA templates"

```
✅ VALIDATION RESULT

📁 File Type: Templates
📂 Location: 04_RECURSOS/TEMPLATES/
📝 Naming: TEMPLATE_[specific_name].md
   - TEMPLATE_Briefing_Projeto.md
   - TEMPLATE_PRD_Tecnico.md
   - TEMPLATE_Checklist_Revisao.md
🔗 Update MOC: 04_RECURSOS/_MOC_Recursos.md
📋 Structure: Folder exists ✅

✅ Ready to proceed

⚠️ Consideration: Multiple templates - consider subfolder 04_RECURSOS/TEMPLATES/Metodologia_IA/
```

---

## MODE 2: AUDIT ORGANIZATION

When user asks to audit/check/validate vault organization.

### Context

**Vault**: Meu_Segundo_Cerebro
**Standards**:
- Nomenclatura: `00_SISTEMA/PADROES/NOMENCLATURA.md`
- Estrutura: `00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md`

### Files ALLOWED in Root

✅ **Only these:**
- `CLAUDE.md` - Claude Code guidance
- `README.md` - Vault overview
- `STATUS_VAULT.md` - Main dashboard

### Files NOT ALLOWED in Root

❌ **Must move to correct folders:**
- `MOC_*.md` → `00_SISTEMA/MOCs/`
- `PLANO_*.md` → `00_SISTEMA/planejamento/` or specific project
- `CHECKPOINT_*.md` → `00_SISTEMA/CHECKPOINTS/` or project
- `TEMPLATE_*.md` → `04_RECURSOS/TEMPLATES/`
- `Prompt_*.md` → `04_RECURSOS/PROMPTS/`
- Any other `.md` → Categorize in 01-05

### Correct Structure

```
Meu_Segundo_Cerebro/
├── CLAUDE.md              ✅ Root OK
├── README.md              ✅ Root OK
├── STATUS_VAULT.md        ✅ Root OK
├── _inbox/                ✅ Quick capture
├── .claude/commands/      ✅ Commands
├── .gemini/               ✅ Gemini config
├── 00_SISTEMA/
│   ├── MOCs/              ← MOCs go here
│   ├── PADROES/           ← Standards docs
│   ├── planejamento/      ← Planning docs
│   └── CHECKPOINTS/       ← System checkpoints
├── 01_CONHECIMENTO/       ← Knowledge
├── 02_PROJETOS/           ← Projects
├── 03_APRENDIZADO/        ← Courses
├── 04_RECURSOS/           ← Templates, prompts
│   ├── TEMPLATES/
│   ├── PROMPTS/
│   └── CHECKLISTS/
└── 05_PESSOAL/            ← Personal
```

### Validation Process

1. **Check Root**
   - List all .md files in root
   - Must have ONLY: CLAUDE.md, README.md, STATUS_VAULT.md
   - Any others → MOVE

2. **Check Naming**
   - Correct prefixes (MOC_, PLANO_, TEMPLATE_, etc)
   - CamelCase for hierarchy
   - Dates in DDMMMYYYY
   - No spaces (use underscores)

3. **Check Project Structure**
   Each project in `02_PROJETOS/` must have:
   - README.md
   - STATUS_ATUAL.md
   - Standard subfolders

4. **Check MOCs**
   - Category MOCs start with `_MOC_`
   - Reflect actual folder content
   - Working links

### Audit Report Format

```markdown
# Validation Report - [Date]

## Files Out of Place
- [file] → Should be in [location]

## Incorrect Naming
- [file] → Should be [correct name]

## Incomplete Structure
- [project] missing [folder/file]

## Actions Taken
- [x] Moved [file] to [destination]
- [x] Renamed [from] to [to]

## Status
✅ Vault compliant / ⚠️ Issues found
```

### Protocol

✅ **ALWAYS**:
- Verify before creating new file
- Ask if unsure about location
- Move immediately if created in wrong place
- Update links after moving files

❌ **NEVER**:
- Create important files in root
- Ignore naming standards
- Leave files out of compliance

---

## DETERMINE MODE

When user invokes `/validate`:

**IF** user provides description of what to create:
→ Use MODE 1 (Validate File Creation)

**IF** user says "audit", "check", "validate organization":
→ Use MODE 2 (Audit Organization)

**IF** unclear:
→ Ask: "Would you like to (1) validate a file creation plan, or (2) audit vault organization?"

---

## References

**Must Read:**
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - CRITICAL
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - CRITICAL
- `STATUS_VAULT.md` - Current state
