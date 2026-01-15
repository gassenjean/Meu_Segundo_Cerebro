# Delegation Patterns - When to Delegate to Gemini

This reference explains when each type of task should be delegated from Claude to Gemini/Antigravity.

---

## General Rule: 50k Token Threshold

**Primary trigger:** If task requires >50k tokens, consider delegation.

**Secondary triggers:**
- Task is highly repetitive
- >10 files need processing
- User explicitly requests Gemini
- Task is tedious but straightforward

**Never delegate:**
- Strategic decisions
- Architecture design
- Complex code writing
- Critical validation (<10 files)

---

## Task Type 1: Document Processing

**Definition:** Processing large documents (transcriptions, reports) into structured outputs.

### When to Delegate

- **Transcription >10 pages:** Always delegate
- **Meeting notes >5k words:** Delegate
- **Multiple documents → consolidated output:** Delegate if >5 docs
- **Structuring unstructured content:** Delegate if >20k words

### Example Triggers

- "Process essa transcrição de 50 páginas"
- "Gera resumo executivo dessa reunião de 2h30"
- "Extrai decisões e ações desse documento"

### What Gemini Does Well

- Extract decisions from long text
- Generate structured summaries
- Create multiple documents from single source
- Apply templates to unstructured content

### What to Watch

- Ensure "source of truth" is clear (e.g., VALORES_OFICIAIS.md)
- Provide template/structure examples
- List all expected deliverables explicitly

### Success Pattern (KabaK)

- **Task:** Process 50-page meeting transcription
- **Deliverables:** 5 structured documents
- **Result:** 95% quality, 2 minor corrections
- **Tokens saved:** ~80k

---

## Task Type 2: Search and Consolidation

**Definition:** Searching across many files and consolidating findings.

### When to Delegate

- **>50 files to search:** Always delegate
- **Vault-wide grep:** Delegate
- **Cross-referencing many docs:** Delegate if >20 files
- **Audit all files in project:** Delegate if >30 files

### Example Triggers

- "Busca todas referências a 'investimento' no vault"
- "Consolida todos valores financeiros em único doc"
- "Faz auditoria completa dos 47 arquivos KabaK"

### What Gemini Does Well

- Search large file sets (100+ files)
- Grep patterns across vault
- Consolidate scattered information
- Generate comprehensive reports

### What to Watch

- Define search patterns clearly
- Specify output format
- Expect long processing time (>30 min for vault-wide)

---

## Task Type 3: Massive Generation

**Definition:** Creating many similar documents using templates.

### When to Delegate

- **>5 similar documents:** Consider delegation
- **>10 similar documents:** Always delegate
- **Repetitive template application:** Delegate
- **Bulk document creation:** Delegate if >3 docs

### Example Triggers

- "Gera 10 briefings usando esse template"
- "Cria documentação completa de 50 endpoints"
- "Gera relatório financeiro para cada mês (12 docs)"

### What Gemini Does Well

- Apply templates consistently
- Generate many documents quickly
- Maintain consistency across outputs
- Handle repetitive content creation

### What to Watch

- Provide clear template
- Define all variables/placeholders
- Specify naming convention
- Check first output before bulk generation

---

## Task Type 4: Batch Refactoring

**Definition:** Applying same change pattern across many files.

### When to Delegate

- **>20 files to update:** Always delegate
- **>10 files to update:** Consider delegation
- **Pattern-based changes:** Delegate if pattern is clear
- **Renaming/restructuring:** Delegate if >15 files

### Example Triggers

- "Atualiza nomenclatura em todos os 30 arquivos"
- "Aplica novo padrão de frontmatter em projeto"
- "Move todos arquivos para nova estrutura"

### What Gemini Does Well

- Apply patterns consistently
- Batch file operations
- Systematic refactoring
- Update timestamps/metadata

### What to Watch

- Define pattern with before/after examples
- Test on 2-3 files first
- Specify what NOT to change
- Check edge cases

---

## Task Type 5: Complete Audit

**Definition:** Comprehensive validation of many files.

### When to Delegate

- **>30 files to audit:** Always delegate
- **>20 files to audit:** Consider delegation
- **Cross-file consistency check:** Delegate if >15 files
- **Value validation across docs:** Delegate if >10 docs

### Example Triggers

- "Audita tudo que Gemini fez"
- "Valida consistência em todos docs KabaK"
- "Verifica se todos valores batem com VALORES_OFICIAIS.md"

### What Gemini Does Well

- Systematic file checking
- Cross-reference validation
- Pattern matching at scale
- Generate comprehensive reports

### What to Watch

- Define validation checklist clearly
- Specify "source of truth" document
- List all patterns to check
- Expect detailed report output

---

## Decision Matrix

| Task Characteristic | Claude | Gemini | Notes |
|:-------------------|:------:|:------:|:------|
| **Files involved** | <10 | >10 | Primary factor |
| **Tokens estimated** | <50k | >50k | Use token_estimator.py |
| **Repetitive?** | No | Yes | Gemini excels at repetition |
| **Strategic?** | YES | No | Never delegate strategy |
| **Critical values?** | YES | No | Claude validates, Gemini executes |
| **Complex code?** | YES | No | Architecture stays with Claude |
| **Tedious work?** | No | YES | Delegate tedium |
| **Time-sensitive?** | Either | Prefer | Gemini usually faster |
| **User preference?** | Respect | Respect | User knows best |

---

## Real-World Examples

### Example 1: KabaK Meeting Processing ✅ DELEGATED

- **Files:** 1 transcription → 5 outputs = 6 total
- **Tokens:** ~80k estimated
- **Decision:** DELEGATE (>50k tokens)
- **Result:** 95% quality, 2 minor fixes
- **Verdict:** Correct delegation

### Example 2: Single Briefing Update ❌ NOT DELEGATED

- **Files:** 1
- **Tokens:** ~5k estimated
- **Decision:** Claude handles (< 50k tokens)
- **Result:** Done in 2 minutes
- **Verdict:** Correct decision not to delegate

### Example 3: Vault-Wide Search ✅ DELEGATED

- **Files:** 2000+ in vault
- **Tokens:** >200k estimated
- **Decision:** DELEGATE (massive scale)
- **Result:** Complete in 20 minutes
- **Verdict:** Correct delegation

### Example 4: Architecture Decision ❌ NOT DELEGATED

- **Files:** 5-10 to review
- **Tokens:** ~30k estimated
- **Decision:** Claude handles (strategic decision)
- **Result:** Thoughtful architecture design
- **Verdict:** Correct - never delegate strategy

---

## Common Anti-Patterns (Mistakes)

### Anti-Pattern 1: Delegating Too Early

**Mistake:** Delegate before reading any files.

**Problem:** Don't know if task is truly massive yet.

**Solution:** Read 1-2 key files first, THEN estimate tokens.

### Anti-Pattern 2: Delegating Strategy

**Mistake:** "Gemini, decide if we should use X or Y approach"

**Problem:** Gemini shouldn't make strategic calls.

**Solution:** Claude decides strategy, Gemini executes.

### Anti-Pattern 3: Under-Specifying

**Mistake:** "Gemini, help with the project"

**Problem:** Too vague, unclear deliverables.

**Solution:** Use handoff_generator.py for structured instructions.

### Anti-Pattern 4: No Source of Truth

**Mistake:** Delegate without defining authoritative reference.

**Problem:** Gemini invents or guesses values.

**Solution:** Always specify "source of truth" document.

### Anti-Pattern 5: Skipping Audit

**Mistake:** Trust Gemini's output without validation.

**Problem:** Small errors compound, divergences unnoticed.

**Solution:** Always run audit_validator.py or manual check.

---

## Workflow Integration

### When User Says "Isso é pra Gemini?"

1. Estimate tokens (`token_estimator.py`)
2. Check this reference for task type
3. Consult decision matrix above
4. Recommend: DELEGATE or CLAUDE HANDLES
5. If uncertain, ask user preference

### When in Doubt

**Default heuristic:**
- **>50k tokens:** Lean towards delegation
- **<50k tokens:** Lean towards Claude
- **Strategic/critical:** Always Claude
- **Repetitive/tedious:** Always Gemini

---

**Last Updated:** 2026-01-15
**Based on:** KabaK success case (95% quality)
