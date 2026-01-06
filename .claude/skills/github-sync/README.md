# GitHub Sync Skill

Skill para gerenciamento unificado do repositório GitHub do vault **Meu_Segundo_Cerebro**.

## Overview

Esta skill fornece workflows padronizados para sincronização entre:

- **Vault local** (OneDrive)
- **Repositório GitHub** (https://github.com/gassenjean/Meu_Segundo_Cerebro)
- **Claude Code** (agente estratégico)
- **Antigravity/Gemini** (agente de execução)
- **Multi-PC** (Alienware 💻 + Desktop Casa 🖥️)

## Installation

A skill está localizada em:

```
.claude/skills/github-sync/
```

Para usar, simplesmente invoque workflows descritos em `SKILL.md`.

## Quick Start

### Check Status

```bash
bash .claude/skills/github-sync/scripts/sync_check.sh
```

### Quick Backup

```bash
bash .claude/skills/github-sync/scripts/quick_backup.sh "my backup message"
```

### Clean Old Files

```bash
# Dry run first
bash .claude/skills/github-sync/scripts/cleanup_old.sh --dry-run

# Then execute
bash .claude/skills/github-sync/scripts/cleanup_old.sh
```

## Files

### SKILL.md

Main skill documentation with:

- Core workflows (pull, push, commit)
- Integration protocols (Claude + Antigravity)
- Multi-PC sync procedures
- Troubleshooting guide

### References

- `GIT_COMMANDS.md` - Complete git commands reference
- `COMMIT_CONVENTIONS.md` - Commit message standards

### Scripts

- `sync_check.sh` - Status verification
- `quick_backup.sh` - Emergency backup
- `cleanup_old.sh` - Clean deleted files

## Usage Examples

### Daily Workflow

**Morning (Start Session)**:

```bash
# 1. Check sync status
bash .claude/skills/github-sync/scripts/sync_check.sh

# 2. Pull latest
git pull --rebase origin master

# 3. Check logs
# - Read SESSION_LOG.md
# - Read PC_SYNC_LOG.md
```

**Evening (End Session)**:

```bash
# 1. Stage and commit
git add .
git commit -m "chore: daily sync $(date +%d%b%Y)"

# 2. Push
git push origin master

# 3. Update logs
# - Update SESSION_LOG.md
# - Update PC_SYNC_LOG.md
```

### Emergency Backup

```bash
bash .claude/skills/github-sync/scripts/quick_backup.sh "before refactoring"
```

### Weekly Maintenance

```bash
# 1. Check status
bash .claude/skills/github-sync/scripts/sync_check.sh

# 2. Clean old files
bash .claude/skills/github-sync/scripts/cleanup_old.sh

# 3. Create checkpoint
git tag -a "checkpoint-$(date +%Y%m%d)" -m "Weekly checkpoint"
git push --tags
```

## Integration

### With Claude Code

Invoke via skill patterns documented in SKILL.md

### With Antigravity

Same workflows, different agent signature in commits

### With SESSION_LOG.md

Always update when switching between agents

### With PC_SYNC_LOG.md

Always update when switching between computers

## Troubleshooting

See `SKILL.md` for comprehensive troubleshooting guide.

Common issues:

- Push rejected → Pull first
- Merge conflicts → Manual resolution
- Detached HEAD → Checkout master

## Best Practices

1. **Pull First** - Always before starting work
2. **Commit Often** - Small, atomic commits
3. **Push Daily** - At least once per day
4. **Sign Commits** - Include AI agent signature
5. **Update Logs** - Keep SESSION_LOG.md current
6. **Clear Messages** - Descriptive commit messages
7. **Check Status** - Regular sync_check.sh runs
8. **Backup Important** - Tag checkpoints

## Repository Info

- **URL**: https://github.com/gassenjean/Meu_Segundo_Cerebro.git
- **Branch**: master
- **Owner**: gassenjean
- **Path**: C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro

## Support

For issues or questions:

1. Check `SKILL.md` troubleshooting section
2. Review `GIT_COMMANDS.md` reference
3. Consult `COMMIT_CONVENTIONS.md` standards

## Version

- **Created**: 31/12/2025
- **Version**: 1.0
- **Status**: ✅ Active

---

**This skill ensures Claude Code, Antigravity, and multi-PC work in perfect sync! 🚀**
