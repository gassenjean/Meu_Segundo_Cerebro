---
name: kabak
description: This skill should be used when working on KabaK project tasks - processing meetings, creating briefings, managing status updates, generating financial reports, or any KabaK-related documentation and project management.
---

# KabaK Project Management Skill

Specialized skill for managing the KabaK e-commerce project - a R$ 2.6M partnership to launch a women's fitness apparel brand.

## When to Use This Skill

Activate this skill when the user needs to:
- Process meeting transcriptions and generate structured summaries
- Create detailed briefings for stakeholders (lawyers, investors, partners)
- Update project status, tasks, or metrics dashboards
- Generate or update financial projections and reports
- Manage documentation for the KabaK project
- Any task mentioning "KabaK", "Sansom", "sociedade", or related to the fitness e-commerce project

## Project Overview

**KabaK** is an e-commerce venture for women's fitness apparel with:
- **Partnership:** 51% Sansom (decision power) / 49% Jean family (operations)
- **Profit split:** 50% Sansom / 50% Jean family (Jean + Gassen + Kris)
- **Product:** Fitness kits (3 pieces: leggings + top + shorts) at R$ 129
- **Investment:** R$ 2.6M over 6 months
- **Goal:** R$ 10M/month revenue (replicate Atara's success)
- **Launch:** May 2026

**Key Stakeholders:**
- **Sansom:** Chinese entrepreneur, manages China imports and finances (wife is Chinese)
- **Jean:** Factory owner, CEO, General Manager (production, strategy)
- **Gassen:** E-commerce, marketing, project management, brand management
- **Kris (Kristyellen):** Stylist, Product Manager, Product Development, Production (co-creator)
- **Titanium:** Marketing agency ✅ APPROVED (R$ 50k setup + R$ 45-60k/month escalating)
- **Dr. Alexandre:** Corporate lawyer for legal structuring

## Core Workflows

### 1. Meeting Processor

**Trigger:** User mentions processing a meeting, has a transcription, or needs meeting summaries.

**Steps:**
1. Ask if user has transcription or will narrate key points
2. Consult `references/stakeholders.md` for participant context
3. Extract key decisions, action items, and next steps
4. Use templates from `assets/templates/` to generate:
   - `Reuniao_[TOPIC]_[DATE].md` - Complete meeting summary (in `docs/reunioes/`)
   - `Resumo_Financeiro_[STAKEHOLDER].md` - Financial summary if relevant
   - `PLANO_[TOPIC].md` - Detailed action plan with deadlines (in `planejamento/`)
5. Update `TODO_Sprint_Atual.md` with new action items
6. Update `DASHBOARD.md` with new metrics if mentioned
7. Create entries in `CONCLUIDAS.md` for completed tasks mentioned

**When to consult references:**
- `references/estrutura_societaria.md` - For ownership/profit discussions
- `references/stakeholders.md` - For participant roles/responsibilities
- `references/metricas_kpis.md` - For metrics mentioned

### 2. Briefing Generator

**Trigger:** User needs to create a briefing for a stakeholder (lawyer, investor, partner, supplier).

**Steps:**
1. Ask: Who is the briefing for? What's the purpose?
2. Consult all references to load complete context:
   - `references/estrutura_societaria.md` - Ownership structure
   - `references/produto_tecnico.md` - Product specs, costs, margins
   - `references/metricas_kpis.md` - Financial projections, KPIs
   - `references/stakeholders.md` - Stakeholder details
3. Use `assets/templates/TEMPLATE_BRIEFING.md` as base structure
4. Customize sections based on audience:
   - **Lawyer:** Focus on legal structure, contracts, governance
   - **Investor:** Focus on financials, ROI, risk mitigation
   - **Supplier:** Focus on product specs, volumes, timelines
   - **Partner:** Focus on collaboration model, responsibilities
5. Include specific questions for the stakeholder
6. Generate comprehensive document (500-1000+ lines typical)
7. Save as `BRIEFING_[STAKEHOLDER]_[PURPOSE]_[DATE].md`

### 3. Project Manager

**Trigger:** User needs to update project status, manage tasks, or review progress.

**Steps:**
1. Read current state:
   - `STATUS_ATUAL.md` - Overall project status
   - `TODO_Sprint_Atual.md` - Current sprint tasks
   - `DASHBOARD.md` - Metrics and KPIs
2. Ask: What changed? What needs updating?
3. Update all relevant files:
   - Move completed tasks from TODO to `CONCLUIDAS.md`
   - Update progress percentages in STATUS_ATUAL
   - Update metrics in DASHBOARD
   - Add new blockers/risks if mentioned
4. Use `references/metricas_kpis.md` to validate metric updates
5. Generate mini progress report highlighting:
   - What was completed
   - What's blocked
   - What's next
   - Key metrics changes

**Update patterns:**
- Weekly: Update all 3 files (STATUS, TODO, DASHBOARD)
- Post-meeting: Update based on decisions/action items
- Ad-hoc: User-requested specific updates

### 4. Financial Planner

**Trigger:** User needs financial projections, ROI calculations, or cost analysis.

**Steps:**
1. Determine scope:
   - New projection? (6-month, 12-month, 24-month)
   - Update existing? (validate numbers, adjust assumptions)
   - Scenario analysis? (conservative, realistic, optimistic)
2. Consult `references/produto_tecnico.md` for:
   - Product costs (fabric R$ 15/kit, production R$ 30/kit, packaging R$ 3/kit = total R$ 48/kit)
   - Pricing (R$ 129/kit)
   - Fixed costs (Titanium R$ 45-60k escalating, traffic R$ 40-100k)
3. Use `assets/templates/TEMPLATE_PLANILHA_FINANCEIRA.md` as base
4. Calculate:
   - Monthly revenue (units × price)
   - Variable costs (units × cost per unit)
   - Fixed costs (marketing, operations, admin)
   - Gross profit, net profit, cash flow
   - Break-even point, ROI, payback period
5. Generate scenarios if requested
6. Format in clear tables with visual indicators
7. Include key insights and recommendations

**When to use scripts:**
- `scripts/excel_calculator.py` - Complex financial calculations
- Ensures consistency across projections
- Faster than recalculating manually

### 5. Document Updater

**Trigger:** User needs to update existing KabaK documents with new information.

**Steps:**
1. Identify which document needs updating:
   - README.md (project overview)
   - STATUS_ATUAL.md (current status)
   - DASHBOARD.md (metrics)
   - Planning docs in `planejamento/`
   - Documentation in `docs/`
2. Read current content
3. Ask: What needs to change?
4. Make targeted updates preserving:
   - Frontmatter (update `atualizado` timestamp)
   - Existing structure and formatting
   - Emoji indicators (🔴, 🟡, 🟢)
   - Checklists and progress bars
5. Validate updates against `references/` for accuracy
6. Update related docs if changes cascade:
   - STATUS change → Update DASHBOARD
   - TODO completion → Move to CONCLUIDAS
   - New decision → Update PROXIMOS_PASSOS

## Templates Available

All templates are in `assets/templates/` and follow KabaK documentation standards:

1. **TEMPLATE_Reuniao.md** - Meeting summary
   - Structured sections with emojis
   - Participants, decisions, action items
   - Next steps with deadlines and owners

2. **TEMPLATE_RESUMO_FINANCEIRO.md** - Financial summary for stakeholders
   - Investment breakdown
   - ROI projections
   - Cash flow timeline
   - Risk mitigation

3. **TEMPLATE_Plano_Acao.md** - Detailed action plan (PLANO_)
   - Organized by priority (🔴 Critical, 🟡 Urgent, 🟢 Nice-to-have)
   - Responsible parties and deadlines
   - Dependencies and blockers
   - Weekly/sprint structure

4. **TEMPLATE_BRIEFING.md** - Comprehensive stakeholder briefing
   - Executive summary
   - Business context
   - Stakeholder profiles
   - Detailed requirements
   - Questions for stakeholder
   - Next steps

5. **TEMPLATE_STATUS_PROJETO.md** - Project status document
   - Current phase and progress
   - Recent decisions
   - Next actions
   - Blockers and risks
   - Stakeholder responsibilities

6. **TEMPLATE_DASHBOARD.md** - KPI dashboard
   - Main metrics table
   - Financial projections
   - Phase progress bars
   - Alerts and actions

7. **TEMPLATE_TODO_SPRINT.md** - Sprint task management
   - Organized by priority
   - Responsible parties
   - Completed items tracking

## References (Load as Needed)

References contain detailed context loaded only when relevant:

- **estrutura_societaria.md** - Complete ownership structure, profit split, decision-making model
- **produto_tecnico.md** - Product specifications, costs, suppliers, production capacity
- **metricas_kpis.md** - All financial projections, KPIs, benchmarks, success metrics
- **stakeholders.md** - Detailed profiles of all stakeholders with roles and responsibilities
- **templates_guide.md** - Comprehensive guide to using all templates

**When to consult:**
- estrutura_societaria.md: Any ownership, profit, or governance questions
- produto_tecnico.md: Product specs, costs, pricing, production questions
- metricas_kpis.md: Financial projections, ROI, break-even, metrics
- stakeholders.md: Any mention of Sansom, Jean, Gassen, Kris, partners
- templates_guide.md: When unsure which template to use

## Scripts (Automation)

Scripts in `scripts/` automate repetitive calculations and updates:

- **meeting_extractor.py** - Extract action items from meeting text
- **dashboard_updater.py** - Update dashboard metrics programmatically
- **excel_calculator.py** - Financial calculations and projections
- **validate_structure.py** - Validate KabaK document naming and structure

**Usage pattern:**
1. Check if task is repetitive or calculation-heavy
2. If yes, use appropriate script
3. If no script exists, perform task manually
4. Consider creating script if task repeats 3+ times

## Documentation Standards

**⚠️ IMPORTANTE:** Sempre consultar `00_SISTEMA/PADROES/NOMENCLATURA.md` antes de criar arquivos.
Prefixos válidos: `MOC_`, `PLANO_`, `CHECKPOINT_`, `TEMPLATE_`, `STATUS_`, `ROADMAP_`, `GUIA_`, `README`

All KabaK documents follow these standards:

**Frontmatter:**
```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: [resumo_executivo|briefing|status|plano_acao|dashboard]
prioridade: [critica|alta|media|baixa]
status: [ativo|concluido|pausado]
---
```

**Naming (seguir NOMENCLATURA.md do vault):**
- `Reuniao_[TOPIC]_[DATE].md` - Meeting summaries (in `docs/reunioes/`)
- `Resumo_Financeiro_[STAKEHOLDER].md` - Financial summaries
- `PLANO_[TOPIC].md` - Action plans (in `planejamento/`)
- `BRIEFING_[STAKEHOLDER]_[DATE].md` - Stakeholder briefings (in `docs/`)
- `STATUS_ATUAL.md` - Single source of truth (project root)
- `DASHBOARD.md` - Single metrics view (in `metricas/`)

**Formatting:**
- Use emojis for sections (🎯, 🔴, 🟡, 🟢, ✅, 📊, 💰)
- Tables for structured data
- Checklists with [ ] for tasks
- Progress bars with █ and ░
- Clear hierarchies with ##, ###
- Bold for emphasis (**CRÍTICO**)

**Language:**
- Brazilian Portuguese for all content
- Executive and actionable tone
- Clear ownership (Responsável: Name)
- Specific deadlines (até DD/MMM/YYYY)
- Quantifiable metrics where possible

## Key Principles

1. **Always use templates** - Don't recreate structure, use `assets/templates/`
2. **Consult references** - Load context from `references/` when needed
3. **Update related docs** - Changes cascade (STATUS → DASHBOARD → TODO)
4. **Preserve formatting** - Maintain emoji indicators, frontmatter, structure
5. **Be action-oriented** - Every doc should have clear next steps with owners
6. **Think stakeholder** - Tailor content to audience (lawyer vs investor vs partner)
7. **Validate numbers** - Cross-reference with `references/` for accuracy
8. **Track everything** - Tasks, decisions, metrics - all documented

## Workflow Selection Guide

Ask yourself:
- **Meeting just happened?** → Use Meeting Processor
- **Need stakeholder document?** → Use Briefing Generator
- **Weekly update needed?** → Use Project Manager
- **Need numbers/projections?** → Use Financial Planner
- **Update existing doc?** → Use Document Updater

When in doubt, ask user which workflow they prefer or suggest the most relevant one based on context.

---

**Version:** 1.1
**Created:** 2026-01-14
**Updated:** 2026-01-21 (Correção nomenclatura + custos atualizados)
**For:** KabaK E-commerce Project (Sociedade Sansom/Jean)
