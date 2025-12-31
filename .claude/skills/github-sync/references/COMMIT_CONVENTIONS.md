# Commit Message Conventions

Convenções de mensagens de commit para o repositório Meu_Segundo_Cerebro.

## Format

```
<type>: <subject>

[optional body]

[optional footer]
```

## Types

### Primary Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | Nova funcionalidade | `feat: add new learning module` |
| `fix` | Correção de bug | `fix: resolve link errors in MOC` |
| `docs` | Documentação | `docs: update README with new structure` |
| `refactor` | Refatoração de código | `refactor: reorganize knowledge base` |
| `chore` | Manutenção/Tarefas | `chore: clean up old files` |
| `style` | Formatação | `style: fix markdown formatting` |
| `test` | Testes | `test: add validation tests` |

### Secondary Types

| Type | Description | Example |
|------|-------------|---------|
| `perf` | Performance | `perf: optimize file loading` |
| `build` | Build system | `build: update dependencies` |
| `ci` | CI/CD | `ci: add GitHub Actions` |
| `revert` | Reverter commit | `revert: undo last migration` |
| `wip` | Work in progress | `wip: partial implementation` |
| `checkpoint` | Snapshot/Backup | `checkpoint: weekly backup` |
| `backup` | Emergency backup | `backup: quick save` |
| `sync` | Sincronização | `sync: vault updates` |

## Subject Line

**Rules**:
- Max 60 characters
- Lowercase (exceto nomes próprios)
- No período final
- Imperativo ("add" not "added")
- Português ou Inglês (consistente)

**Good Examples**:
```
feat: add DeFi knowledge base
fix: correct MOC links
docs: update learning structure
chore: clean old reference files
```

**Bad Examples**:
```
Added new files. (não imperativo, período final)
FEAT: NEW FEATURE (caps lock)
fix stuff (vago demais)
This is a very long commit message that exceeds sixty characters (muito longo)
```

## Body

**When to use**:
- Explicar "why" (não "what")
- Fornecer contexto
- Listar mudanças importantes
- Mencionar breaking changes

**Format**:
- Linha em branco após subject
- Wrap em 72 caracteres
- Bullet points com `-` ou `*`
- Múltiplos parágrafos OK

**Example**:
```
refactor: reorganize knowledge categories

Restructured vault to follow new PKM methodology:
- Moved learning materials to 03_APRENDIZADO
- Created new MOCs for better navigation
- Consolidated duplicate references

This improves discoverability and reduces redundancy.
```

## Footer

**Common footers**:

### AI Agent Signatures

**Claude Code**:
```
🤖 Generated with Claude Code

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Antigravity/Gemini**:
```
🚀 Generated with Antigravity

Co-Authored-By: Gemini 3 Pro <noreply@google.com>
```

### References

```
Refs: #123
Closes: #456
See: SESSION_LOG.md
Related: PC_SYNC_LOG.md
```

### Breaking Changes

```
BREAKING CHANGE: Removed old MOC structure.
Migration guide in docs/MIGRATION.md
```

## Examples by Scenario

### Daily Sync

```
chore: daily vault sync - 31DEC2025

Updated files from today's session.

🤖 Generated with Claude Code
```

### New Feature

```
feat: add DeFi investment tracking

Created new module for tracking DeFi investments:
- Portfolio overview dashboard
- Transaction history
- Performance metrics

Integrated with Lucas Amoedo agent context.

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Bug Fix

```
fix: resolve broken wikilinks in MOC_Projetos

Fixed 15 broken wikilinks pointing to old file locations.
Updated references to use new structure.

Closes: #42

🤖 Generated with Claude Code
```

### Refactoring

```
refactor: migrate learning materials structure

Reorganized 03_APRENDIZADO following new standards:
- Separated courses from notes
- Created unified README structure
- Updated MOC references

This aligns with PROTOCOLO_CRIACAO_ARQUIVOS.md

See: 00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md

🤖 Generated with Claude Code
```

### Documentation

```
docs: add GitHub sync skill documentation

Created comprehensive skill for GitHub management:
- Workflows for Claude and Antigravity
- Multi-PC sync protocols
- Troubleshooting guide

Location: .claude/skills/github-sync/

🤖 Generated with Claude Code
```

### Cleanup

```
chore: remove deprecated reference files

Deleted 300+ old files from Alan_Referencia_Vault:
- Duplicate content already migrated
- Obsolete templates
- Old MOC structure

Keeps only essential reference material.

🤖 Generated with Claude Code
```

### Weekly Checkpoint

```
checkpoint: weekly backup 31DEC2025

Weekly vault snapshot:
- All projects updated
- Learning progress tracked
- System maintained

Status: ✅ Vault healthy

🤖 Generated with Claude Code
```

### Emergency Backup

```
backup: emergency snapshot 2359

Quick backup before major refactoring.

🤖 Generated with Claude Code
```

### Multi-Agent Work

```
feat: integrate Dr. Green cultivo context

Added cultivation knowledge management:
- New agent: Dr. Green
- Skill: /dr-green
- Knowledge base structure

Work done on: Desktop Casa 🖥️
Coordinated with: Antigravity

See: SESSION_LOG.md for handoff details

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Sync Between PCs

```
sync: Alienware → Desktop sync 31DEC2025

Changes from Alienware notebook:
- Updated DeFi research notes
- Added new learning materials
- Fixed MOC links

Next PC: Review and continue at Desktop

See: PC_SYNC_LOG.md

🤖 Generated with Claude Code
```

## Anti-Patterns

### ❌ Avoid These

**Too vague**:
```
update files
fix stuff
changes
misc
```

**Too detailed in subject**:
```
fix: correct the broken wikilinks in MOC_Projetos.md file located in 00_SISTEMA/MOCs directory
```

**Missing type**:
```
updated readme
fixed bug
```

**Wrong tense**:
```
feat: added new feature
fix: fixing the bug
```

**All caps**:
```
FEAT: NEW FEATURE
FIX: BUG FIX
```

## Best Practices

1. **Atomic Commits**: One logical change per commit
2. **Frequent Commits**: Commit often, push daily
3. **Clear Subject**: What changed, not how
4. **Detailed Body**: Why it changed (when relevant)
5. **Sign Commits**: Always include AI agent signature
6. **Reference Issues**: Link to relevant issues/docs
7. **Consistent Style**: Follow conventions strictly
8. **Review Before Push**: Check message makes sense
9. **Meaningful Types**: Use correct type for change
10. **Context for Future**: Write for yourself in 6 months

## Validation Checklist

Before committing, verify:

- [ ] Type is correct
- [ ] Subject < 60 characters
- [ ] Subject is imperative mood
- [ ] Subject is lowercase
- [ ] No period at end of subject
- [ ] Body wraps at 72 characters (if present)
- [ ] AI agent signature included
- [ ] References added (if applicable)
- [ ] Message is clear and meaningful

## Tools

### Pre-commit Hook

Create `.git/hooks/commit-msg`:

```bash
#!/bin/bash

commit_msg_file=$1
commit_msg=$(cat "$commit_msg_file")

# Check if message has type prefix
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|refactor|chore|style|test|perf|build|ci|revert|wip|checkpoint|backup|sync):"; then
    echo "ERROR: Commit message must start with type: feat, fix, docs, etc."
    exit 1
fi

# Check subject length
subject=$(echo "$commit_msg" | head -n1)
if [ ${#subject} -gt 60 ]; then
    echo "ERROR: Subject line must be <= 60 characters (currently ${#subject})"
    exit 1
fi

exit 0
```

Make executable:
```bash
chmod +x .git/hooks/commit-msg
```

### Commit Template

Create `~/.gitmessage`:

```
<type>: <subject max 60 chars>

[Why is this change needed? What problem does it solve?]

[List specific changes if helpful]

[Add references, breaking changes, etc]

🤖 Generated with Claude Code

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

Configure git to use template:
```bash
git config --global commit.template ~/.gitmessage
```

---

**Updated**: 31/12/2025
**Version**: 1.0
**Status**: ✅ Active Standard
