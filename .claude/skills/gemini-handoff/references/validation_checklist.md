# Validation Checklist - Before and After Delegation

Complete checklist for ensuring delegation quality.

---

## ✅ BEFORE DELEGATION

### 1. Token Estimation

- [ ] Run `token_estimator.py` with file list
- [ ] Confirm >50k tokens (or other clear trigger)
- [ ] Document estimated tokens in handoff

**Why:** Avoid delegating small tasks (overhead not worth it).

### 2. File Access Verification

- [ ] Confirm Gemini has access to all required files
- [ ] Check files are in OneDrive (if multi-PC scenario)
- [ ] Verify no file permission issues
- [ ] Test reading 1-2 files first

**Why:** Gemini can't process files it can't read.

### 3. Source of Truth Definition

- [ ] Identify authoritative reference document (e.g., VALORES_OFICIAIS.md)
- [ ] Ensure source of truth is complete and correct
- [ ] Reference it explicitly in handoff
- [ ] Verify Gemini can read source of truth

**Why:** Prevents Gemini from inventing or guessing values.

**Example:**
```markdown
## References
- Source of truth: `02_PROJETOS/KabaK/VALORES_OFICIAIS.md`
- ALL financial values MUST match this document
```

### 4. Standards Clarity

- [ ] Identify relevant standards (nomenclature, templates, etc.)
- [ ] Reference standards documents explicitly
- [ ] Provide examples if pattern isn't obvious
- [ ] Link to templates if available

**Why:** Gemini needs clear guidelines to follow.

**Example:**
```markdown
## References
- Nomenclature: `00_SISTEMA/PADROES/NOMENCLATURA.md`
- Use prefixes: RESUMO_, PROJETO_, BRIEFING_
- Templates: `.gemini/skills/kabak/assets/templates/`
```

### 5. Deliverables Checklist

- [ ] List ALL expected outputs explicitly
- [ ] Include filenames with exact nomenclature
- [ ] Specify which files to update (vs. create new)
- [ ] Define success criteria clearly

**Why:** Prevents incomplete work or missing deliverables.

**Example:**
```markdown
## Delivery Checklist
- [ ] RESUMO_EXECUTIVO_REUNIAO_SANSOM.md created
- [ ] RESUMO_FINANCEIRO_SANSOM.md created
- [ ] STATUS_ATUAL.md updated (sections X, Y, Z)
- [ ] SESSION_LOG.md updated with work summary
```

### 6. Validation Items

- [ ] Define what to check after completion
- [ ] List critical values to validate
- [ ] Specify cross-file consistency checks
- [ ] Document quality threshold (e.g., >90%)

**Why:** Sets clear expectations for audit phase.

---

## ✅ AFTER DELEGATION

### 7. Completeness Check

- [ ] All expected deliverables created/updated?
- [ ] Run `git status` to see all changes
- [ ] Check file count matches expectation
- [ ] Verify no missing files

**Why:** Catch incomplete work early.

**Command:**
```bash
git status --short
```

### 8. Nomenclature Validation

- [ ] All filenames follow standards?
- [ ] Prefixes correct (RESUMO_, PROJETO_, etc.)?
- [ ] No spaces in filenames?
- [ ] CamelCase used correctly?

**Why:** Easiest divergence to spot and fix.

**Tool:** Use `audit_validator.py --files "file1.md,file2.md"`

### 9. Frontmatter Validation

- [ ] All files have frontmatter?
- [ ] Required fields present (criado, atualizado)?
- [ ] Timestamps correct?
- [ ] Other metadata fields as needed?

**Why:** Ensures Obsidian compatibility and tracking.

**Tool:** `audit_validator.py` checks this automatically.

### 10. Critical Values Validation

- [ ] All financial values match source of truth?
- [ ] All dates consistent across files?
- [ ] All percentages/metrics aligned?
- [ ] No contradictory information?

**Why:** Financial and critical data must be 100% accurate.

**Method:**
1. Open source of truth (e.g., VALORES_OFICIAIS.md)
2. Grep for key values in output files
3. Compare systematically
4. Use `audit_validator.py` for automation

**Example checks:**
- Investment: R$ 2.106.300 (not R$ 2.6M)
- ROI: 155% (not 288%, 356%, or 5.940%)
- Break-even: Mês 4 (not Mês 3)
- Partners: Jean+Gassen+Kris (not just Gassen+Kris)

### 11. Cross-File Consistency

- [ ] Same facts stated consistently across all docs?
- [ ] No contradictions between files?
- [ ] References between files correct?
- [ ] Updated docs reflect changes in related docs?

**Why:** Inconsistencies confuse readers and reduce credibility.

**Method:**
1. Pick key fact (e.g., investment amount)
2. Grep for it in all files
3. Verify same value everywhere
4. Repeat for 5-10 key facts

### 12. Template/Pattern Adherence

- [ ] Documents follow expected templates?
- [ ] Structure consistent with examples?
- [ ] Sections in correct order?
- [ ] Formatting consistent (headers, lists, tables)?

**Why:** Templates exist for a reason - consistency matters.

### 13. SESSION_LOG.md Update

- [ ] Gemini updated SESSION_LOG.md?
- [ ] Entry has correct timestamp?
- [ ] Work summary is clear?
- [ ] Files modified are listed?

**Why:** Critical for bi-AI coordination and continuity.

### 14. Quality Threshold

- [ ] Run `audit_validator.py` for overall score
- [ ] Check approval percentage (target: >90%)
- [ ] Count total divergences found
- [ ] Assess severity of issues

**Why:** Quantifies quality objectively.

**Interpretation:**
- **>90%:** ✅ APPROVE (excellent, minor fixes only)
- **70-90%:** ⚠️ APPROVE WITH CORRECTIONS (acceptable, fix issues)
- **<70%:** ❌ NEEDS REWORK (significant problems)

### 15. User Notification

- [ ] Generate audit report
- [ ] Present findings clearly
- [ ] Offer to fix minor issues immediately
- [ ] Document corrections made

**Why:** User should know results without re-checking everything.

---

## 🎯 Quick Checklist (Summary)

### Before:
1. ✅ Tokens >50k?
2. ✅ Source of truth defined?
3. ✅ Deliverables listed?
4. ✅ Validation items specified?

### After:
1. ✅ All files created?
2. ✅ Nomenclature correct?
3. ✅ Critical values match source?
4. ✅ Quality >90%?

---

## 📊 Validation Priority Matrix

| Check | Priority | Why | Effort |
|:------|:--------:|:----|:------:|
| Critical values | 🔴 HIGH | Financial errors are serious | Medium |
| Completeness | 🔴 HIGH | Missing files = incomplete | Low |
| Nomenclature | 🟡 MEDIUM | Easy to fix, affects findability | Low |
| Frontmatter | 🟡 MEDIUM | Obsidian compatibility | Low |
| Consistency | 🟡 MEDIUM | Prevents confusion | Medium |
| Templates | 🟢 LOW | Nice-to-have, cosmetic | Low |

**Recommendation:** Always check HIGH priority items. Check MEDIUM if time permits. Check LOW if quality threshold not met.

---

## 🛠️ Tools Quick Reference

### token_estimator.py
```bash
python scripts/token_estimator.py file1.md file2.md file3.md
```

### audit_validator.py
```bash
python scripts/audit_validator.py \
  --files "doc1.md,doc2.md,doc3.md" \
  --source-of-truth "VALORES_OFICIAIS.md"
```

### Manual checks
```bash
# See what changed
git status --short

# Check for value across files
grep -r "R\$ 2.106.300" 02_PROJETOS/KabaK/

# Check nomenclature
ls 02_PROJETOS/KabaK/docs/ | grep -v "^[A-Z]"
```

---

## 🎓 Learning from KabaK

**What went well:**
- Source of truth (VALORES_OFICIAIS.md) was created BEFORE audit
- Templates provided in skill
- Clear deliverable list (5 documents)
- Frontmatter mostly correct

**What could improve:**
- Could have checked 2 minor issues during delegation (not after)
- Could have validated first doc before generating all 5

**Lessons:**
1. Source of truth is CRITICAL - create it first
2. Templates dramatically improve consistency
3. Audit is fast when standards are clear
4. 95% quality is excellent for first delegation

---

**Last Updated:** 2026-01-15
**Based on:** KabaK audit experience
