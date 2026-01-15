# Gemini Handoff Skill

Intelligent delegation skill for offloading high-token and massive tasks from Claude Code to Gemini/Antigravity.

## Quick Start

**When to use:** Tasks requiring >50k tokens or >10 files.

**Core workflow:**
1. Claude estimates tokens and plans task
2. Claude generates structured handoff instructions
3. User passes instructions to Gemini
4. Gemini executes at scale
5. Claude audits output and validates quality

## Structure

```
gemini-handoff/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── scripts/
│   ├── token_estimator.py      # Estimate token cost
│   ├── handoff_generator.py    # Generate delegation instructions
│   └── audit_validator.py      # Validate Gemini's output
├── references/
│   ├── delegation_patterns.md  # When to delegate each task type
│   ├── validation_checklist.md # Pre/post delegation checks
│   └── gemini_strengths.md     # Gemini vs Claude comparison
└── assets/
    └── templates/
        ├── HANDOFF_TEMPLATE.md        # Handoff instructions template
        ├── AUDIT_REPORT_TEMPLATE.md   # Audit report template
        └── SESSION_UPDATE_TEMPLATE.md # SESSION_LOG.md update template
```

## Scripts Usage

### Token Estimator
```bash
python scripts/token_estimator.py file1.md file2.md file3.md
```

### Handoff Generator
```bash
python scripts/handoff_generator.py \
  --task-type "processing" \
  --objectives "Objective 1; Objective 2" \
  --files "file1.md,file2.md" \
  --references "SOURCE.md"
```

### Audit Validator
```bash
python scripts/audit_validator.py \
  --files "doc1.md,doc2.md,doc3.md" \
  --source-of-truth "SOURCE_OF_TRUTH.md"
```

## Key Workflows

1. **Planned Delegation:** Estimate → Plan → Generate instructions → Delegate → Audit
2. **Post-Facto Audit:** Gemini completed work → Audit → Report → Fix issues
3. **Quick Handoff:** Fast delegation with minimal validation

## Success Metrics

Based on KabaK benchmark:
- **Quality:** 95% approval (2/47 files with minor issues)
- **Token savings:** ~80k tokens
- **Time savings:** ~90 minutes
- **Iterations:** 1 (audit + quick fixes)

## Integration

Works seamlessly with other skills:
- KabaK skill (example: delegate meeting processing)
- Any project-specific skill (copy skill, continue work)
- Generic tasks (vault cleanup, batch updates)

## Version

v1.0 - 2026-01-15

Created by Claude Code (Sonnet 4.5) using skill-creator framework.
Based on successful KabaK delegation (95% quality, 80k tokens saved).
