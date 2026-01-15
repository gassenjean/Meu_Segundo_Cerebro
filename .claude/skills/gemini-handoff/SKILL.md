---
name: gemini-handoff
description: This skill should be used when delegating high-token or massive tasks from Claude to Gemini/Antigravity. It provides workflows for intelligent delegation, token estimation, instruction generation, and output validation to maximize efficiency and quality.
---

# Gemini Handoff - Intelligent Delegation Skill

Skill for intelligent task delegation from Claude Code to Gemini/Antigravity, focusing on token economy and massive execution.

## When to Use This Skill

Use this skill when:

1. **Token consumption is high** (>50k tokens estimated)
2. **Task involves massive processing** (>10 files to read/modify)
3. **Repetitive generation** is needed (>5 similar documents)
4. **Batch refactoring** is required (>20 files to update)
5. **Complete audits** are necessary (>30 files to check)
6. **User explicitly requests** Gemini delegation

**DO NOT use** for strategic decisions, architecture design, or critical validations (<10 files).

## Core Workflows

### Workflow 1: Planned Delegation (Recommended)

Use when task is known upfront and quality is critical.

**Steps:**

1. **Estimate tokens:**
   - Run `scripts/token_estimator.py` with list of files to process
   - If >50k tokens, proceed with delegation
   - If <50k tokens, consider if Claude can handle it

2. **Consult delegation patterns:**
   - Read `references/delegation_patterns.md`
   - Identify task type (Processing/Search/Generation/Refactoring/Audit)
   - Verify Gemini is appropriate for this task type

3. **Check prerequisites:**
   - Read `references/validation_checklist.md` (BEFORE section)
   - Ensure Gemini has file access
   - Verify "source of truth" is defined (e.g., VALORES_OFICIAIS.md)
   - Confirm templates/standards are clear

4. **Generate handoff instructions:**
   - Run `scripts/handoff_generator.py` with task details
   - Or manually use `assets/templates/HANDOFF_TEMPLATE.md`
   - Format: Hybrid (clear objectives + validation checklist + references)

5. **User approval:**
   - Present handoff instructions to user
   - Estimate: files, tokens, time
   - Wait for approval before proceeding

6. **Execute delegation:**
   - Update `SESSION_LOG.md` using `assets/templates/SESSION_UPDATE_TEMPLATE.md`
   - Add delegation entry with timestamp and task description
   - Include handoff instructions in SESSION_LOG
   - Inform user to pass instructions to Gemini/Antigravity

7. **Post-execution audit:**
   - When Gemini reports completion, read `SESSION_LOG.md`
   - Identify modified files (use `git status`)
   - Run `scripts/audit_validator.py` on output
   - Generate audit report using `assets/templates/AUDIT_REPORT_TEMPLATE.md`

8. **Corrections if needed:**
   - If audit shows >90% correct: Approve with minor fixes
   - If audit shows <90% correct: Identify issues and correct
   - Update `SESSION_LOG.md` with audit results

---

### Workflow 2: Gemini Work Audit (Post-Facto)

Use when Gemini has already completed work and audit is needed.

**Steps:**

1. **User triggers audit:**
   - User: "Gemini fez X, audite o trabalho"
   - User: "Recupere tudo que foi feito e veja se está correto"

2. **Load context:**
   - Read `SESSION_LOG.md` completely
   - Read `PC_SYNC_LOG.md` if multi-PC scenario
   - Run `git status` to see modified/new files

3. **Identify scope:**
   - From SESSION_LOG, extract what Gemini was supposed to do
   - List all files Gemini created/modified
   - Identify the project (e.g., KabaK, other)

4. **Check standards:**
   - If project has "source of truth" file (e.g., VALORES_OFICIAIS.md), read it
   - Check `00_SISTEMA/PADROES/NOMENCLATURA.md` for naming standards
   - Load project templates if available

5. **Run validation:**
   - Execute `scripts/audit_validator.py` with file list
   - Check: nomenclature, frontmatter, consistency, critical values
   - Cross-reference values across documents

6. **Generate report:**
   - Use `assets/templates/AUDIT_REPORT_TEMPLATE.md`
   - Include: approval %, files checked, divergences found, what's correct
   - Categorize divergences by severity (CRITICAL/MEDIUM/LOW)

7. **Present findings:**
   - Show audit report to user
   - If divergences found: List them clearly with file:line references
   - Offer to correct minor issues immediately

8. **Apply corrections:**
   - If user approves, fix divergences found
   - Update timestamps in frontmatter
   - Re-validate after corrections

---

### Workflow 3: Quick Handoff (Fast, Less Validation)

Use when speed matters more than perfection, or task is simple.

**Steps:**

1. **User requests delegation:**
   - User: "Delega isso pro Gemini"
   - User: "Passe isso para o Antigravity"

2. **Generate basic instructions:**
   - Use `assets/templates/HANDOFF_TEMPLATE.md` (simplified)
   - Clear objectives only, minimal validation
   - Essential references only

3. **Immediate delegation:**
   - Update `SESSION_LOG.md` briefly
   - Pass instructions to user for Gemini
   - No token estimation, no extensive validation

4. **Light audit afterwards:**
   - Quick check of key files only
   - Focus on critical issues only
   - Report major problems only

---

## Delegation Format (Hybrid Approach)

Based on KabaK success (95% quality), use **HYBRID FORMAT:**

```markdown
# DELEGATION TO GEMINI/ANTIGRAVITY

## Objectives (Clear WHAT)
- [Objective 1]
- [Objective 2]

## Delivery Checklist (HOW to ensure quality)
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

## References (WHERE to find standards)
- Source of truth: [file]
- Standards: [links]
- Templates: [links]

## Expected Validation (WHAT to check)
- [ ] [Validation item 1]
- [ ] [Validation item 2]

## Estimation
- Files to process: [N]
- Estimated tokens: [N]
- Estimated time: [N minutes]
```

**Example (KabaK):**

```markdown
# For Gemini: Continue KabaK Project

## Objectives
- Process Sansom meeting transcription
- Generate 5 official documents
- Update STATUS_ATUAL.md

## Delivery Checklist
- [ ] RESUMO_EXECUTIVO_REUNIAO_SANSOM.md created
- [ ] RESUMO_FINANCEIRO_SANSOM.md created
- [ ] PROXIMOS_PASSOS_SOCIEDADE_SANSOM.md created
- [ ] PROJETO_OUTLET_RODOVIA.md created (if outlet mentioned)
- [ ] STATUS_ATUAL.md updated with latest decisions

## References
- Source of truth: `VALORES_OFICIAIS.md`
- Skill: `.gemini/skills/kabak/SKILL.md`
- Standards: `00_SISTEMA/PADROES/NOMENCLATURA.md`
- Templates: `.gemini/skills/kabak/assets/templates/`

## Expected Validation
- [ ] Follow VALORES_OFICIAIS.md for all financial values
- [ ] Nomenclature: RESUMO_, PROJETO_, etc.
- [ ] Complete frontmatter in all docs
- [ ] Update SESSION_LOG.md with work summary

## Estimation
- Files to process: 1 (transcription) + 5 (output) = 6
- Estimated tokens: ~80k (transcription heavy)
- Estimated time: 20-30 minutes
```

---

## Scripts Usage

### token_estimator.py

Estimate token cost before delegating.

```bash
python scripts/token_estimator.py file1.md file2.md file3.md
```

**Output:**
```
Estimated tokens: 72,450
Recommendation: DELEGATE to Gemini (>50k)
```

### handoff_generator.py

Generate structured instructions for Gemini.

```bash
python scripts/handoff_generator.py \
  --task-type "processing" \
  --objectives "Process meeting, generate 5 docs" \
  --files "meeting.md" \
  --references "VALORES_OFICIAIS.md, SKILL.md"
```

**Output:** Complete HANDOFF.md file ready to pass to user.

### audit_validator.py

Validate Gemini's output automatically.

```bash
python scripts/audit_validator.py \
  --files "doc1.md,doc2.md,doc3.md" \
  --source-of-truth "VALORES_OFICIAIS.md" \
  --standards "NOMENCLATURA.md"
```

**Output:** Audit report with approval % and divergences list.

---

## References Documentation

### delegation_patterns.md

Detailed guide on when to delegate each task type:
- Document processing (>10 files)
- Search and consolidation (>50 files)
- Massive generation (>5 documents)
- Batch refactoring (>20 files)
- Complete audits (>30 files)

**Load when:** Deciding if task should be delegated.

### validation_checklist.md

Complete checklist for BEFORE and AFTER delegation:
- Pre-delegation checks (token estimate, file access, standards)
- Post-delegation validation (consistency, nomenclature, values)

**Load when:** Planning delegation or auditing results.

### gemini_strengths.md

Comparison matrix: Gemini vs Claude strengths and use cases.
- When Gemini excels (massive processing, long context)
- When Claude excels (strategic decisions, complex code)

**Load when:** Uncertain if delegation is appropriate.

---

## Assets and Templates

### HANDOFF_TEMPLATE.md

Template for generating delegation instructions. Contains all sections needed for a complete handoff with placeholders for customization.

**Use:** Copy and fill placeholders, or pass to `handoff_generator.py`.

### AUDIT_REPORT_TEMPLATE.md

Template for audit reports after Gemini completes work. Includes metrics, divergences, and recommendations.

**Use:** Generate report after validation, present to user.

### SESSION_UPDATE_TEMPLATE.md

Template for updating SESSION_LOG.md with delegation entries. Maintains consistent format for bi-AI communication.

**Use:** Update SESSION_LOG.md before and after delegation.

---

## Best Practices

### Before Delegating

1. **Always estimate tokens first** - Avoid delegating small tasks
2. **Define source of truth** - Ensure Gemini has clear reference
3. **Provide complete context** - Don't assume Gemini knows implicit info
4. **Use templates** - They worked 95% for KabaK
5. **Update SESSION_LOG.md** - Critical for bi-AI coordination

### During Delegation

1. **Be specific in objectives** - "Generate 5 docs" not "help with project"
2. **List expected deliverables** - Checklist format works best
3. **Reference skill if exists** - E.g., point to `.gemini/skills/kabak/`
4. **Include examples** - When pattern isn't obvious
5. **Estimate honestly** - Help user plan time

### After Delegation

1. **Always audit** - Even if Gemini reports success
2. **Check critical values first** - Financial data, dates, IDs
3. **Validate nomenclature** - Easiest divergence to spot
4. **Cross-reference documents** - Consistency across files
5. **Document results** - Update SESSION_LOG.md with audit

---

## Integration with Existing Skills

### KabaK Skill Integration

When delegating KabaK work:

1. **Reference KabaK skill:**
   - Point Gemini to `.gemini/skills/kabak/SKILL.md`
   - Ensure VALORES_OFICIAIS.md is referenced
   - Use KabaK templates from `assets/templates/`

2. **Use KabaK workflows:**
   - Meeting Processor
   - Briefing Generator
   - Financial Planner
   - Document Updater

3. **Validate against KabaK standards:**
   - Check stakeholders consistency
   - Verify financial values match VALORES_OFICIAIS.md
   - Ensure societal structure is correct (Jean+Gassen+Kris)

### Generic Skill Copying

When user asks Gemini to "copy skill X and continue":

1. **Prepare the skill:**
   - Ensure skill is in `.gemini/skills/` (Gemini's location)
   - Verify skill has complete SKILL.md
   - Check references are accessible

2. **Generate handoff:**
   - Objective: "Use skill X for task Y"
   - Reference: Full path to skill
   - Checklist: Key deliverables from skill context

3. **Audit afterwards:**
   - Compare output against skill's templates
   - Verify skill workflows were followed
   - Check skill-specific validation items

---

## Common Patterns (Real Examples)

### Pattern 1: Meeting Processing (KabaK Success)

**Trigger:** Large transcription needs structuring.

**Claude's Role:**
1. Estimate tokens (~80k for 50-page transcription)
2. Generate handoff with Meeting Processor workflow
3. Reference VALORES_OFICIAIS.md as source of truth
4. List 5 expected documents

**Gemini's Role:**
1. Process transcription
2. Generate 5 structured documents
3. Update STATUS_ATUAL.md
4. Update SESSION_LOG.md

**Claude's Audit:**
1. Check all 5 docs created
2. Validate financial values against VALORES_OFICIAIS.md
3. Verify nomenclature (RESUMO_, PROJETO_)
4. Check frontmatter completeness
5. Report 95% success (2 minor issues found and fixed)

### Pattern 2: Vault Cleanup

**Trigger:** User: "Limpar duplicatas da raiz do vault"

**Claude's Role:**
1. Estimate tokens (low, but task is tedious)
2. Generate handoff with file list to move
3. Reference NOMENCLATURA.md for proper locations
4. Checklist: files moved, no duplicates left

**Gemini's Role:**
1. Move files to correct folders
2. Update MOCs if needed
3. Delete empty folders
4. Document moves in SESSION_LOG.md

**Claude's Audit:**
1. Quick check: root is clean
2. Verify moved files are in correct locations
3. Check no broken links
4. Approve if all clean

### Pattern 3: Batch Documentation Update

**Trigger:** New standard requires updating 30+ files.

**Claude's Role:**
1. Estimate tokens (high - many file reads)
2. Define exact change pattern
3. Provide before/after examples
4. List all 30+ files to update

**Gemini's Role:**
1. Apply pattern to all files
2. Update timestamps
3. Verify no regressions
4. Report completion

**Claude's Audit:**
1. Sample check 10 files (33%)
2. Verify pattern applied correctly
3. Check no unintended changes
4. Spot-check edge cases
5. Approve if sample is 100%

---

## Troubleshooting

### Issue: Gemini misunderstood instructions

**Solution:**
- Review handoff format - was it clear?
- Add more examples in references
- Use HYBRID format (objectives + checklist + references)
- Be more explicit about "source of truth"

### Issue: Audit found many divergences (>20%)

**Solution:**
- Check if source of truth was referenced
- Verify Gemini had access to templates
- Review if standards were clear in handoff
- Consider if task was too complex for delegation

### Issue: Tokens still consumed heavily

**Solution:**
- Delegate earlier (before reading many files)
- Use token_estimator.py upfront
- Consider if task can be split into subtasks
- Check if Gemini is actually doing massive work

### Issue: User unsure when to delegate

**Solution:**
- Show delegation_patterns.md
- Use 50k tokens as rule of thumb
- If task feels repetitive, delegate
- If >10 files involved, consider delegation

---

## Success Metrics

Track these to measure delegation effectiveness:

1. **Token Savings:** Tokens saved vs. if Claude did it
2. **Quality:** Audit approval % (target: >90%)
3. **Time:** Wall-clock time saved
4. **Iteration:** How many correction rounds needed (target: <2)

**KabaK Benchmark:**
- Tokens saved: ~80k (estimated)
- Quality: 95% (2/47 files had minor issues)
- Time: ~30 minutes (vs. ~2 hours if Claude did it)
- Iterations: 1 (Claude corrected 2 issues)

**Target for new delegations:**
- Quality: >90% (less than KabaK acceptable initially)
- Iterations: <3 (may need more refinement than KabaK)
- Token savings: >50k (delegation threshold)

---

## Version History

- **v1.0** (2026-01-15): Initial skill creation based on KabaK success
  - 3 workflows (Planned, Audit, Quick)
  - 3 scripts (estimator, generator, validator)
  - 3 references (patterns, checklist, strengths)
  - 3 templates (handoff, audit, session update)

---

**Created:** 2026-01-15
**Author:** Claude Code (Sonnet 4.5) + skill-creator
**Based on:** KabaK delegation success (95% quality)
