# GitHub Sync - Gestão Unificada GitHub

Ativa skill **github-sync** para gerenciar repositório GitHub do vault.

---

## 🎯 QUANDO USAR

Use `/github-sync` quando precisar:

- ✅ Sincronizar vault com GitHub (push/pull)
- ✅ Fazer commits organizados
- ✅ Verificar status do repositório
- ✅ Coordenar entre Claude Code e Antigravity
- ✅ Resolver conflitos de sincronização
- ✅ Preparar backups/checkpoints

---

## 📚 CONTEXTO CARREGADO

**Material base:**

- Skill completa: `.claude/skills/github-sync/SKILL.md`
- Referências: Git commands + Commit conventions
- Scripts: sync_check, quick_backup, cleanup_old

**Repository:**

- URL: https://github.com/gassenjean/Meu_Segundo_Cerebro.git
- Branch: master
- Owner: gassenjean

---

## 🚀 WORKFLOWS PRINCIPAIS

### Status Check

```bash
bash .claude/skills/github-sync/scripts/sync_check.sh
```

### Full Sync

```bash
# Pull → Commit → Push
git pull --rebase origin master
git add .
git commit -m "type: message"
git push origin master
```

### Quick Backup

```bash
bash .claude/skills/github-sync/scripts/quick_backup.sh "mensagem"
```

### Clean Old Files

```bash
bash .claude/skills/github-sync/scripts/cleanup_old.sh
```

---

## 📋 COMMIT TYPES

| Type         | Use                 |
| ------------ | ------------------- |
| `feat`       | Nova funcionalidade |
| `fix`        | Correção de bug     |
| `docs`       | Documentação        |
| `refactor`   | Refatoração         |
| `chore`      | Manutenção          |
| `sync`       | Sincronização       |
| `checkpoint` | Snapshot/Backup     |
| `backup`     | Emergency backup    |

**Template**:

```
type: description

[optional body]

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

---

## 🔄 INTEGRATION BI-AI

### Claude Code

- Pull antes de começar
- Commit + push ao terminar
- Atualizar SESSION_LOG.md
- Assinatura: "🤖 Generated with Claude Code"

### Antigravity

- Pull antes de começar
- Commit + push ao terminar
- Atualizar SESSION_LOG.md
- Assinatura: "🚀 Generated with Antigravity"

---

## 💻🖥️ MULTI-PC SYNC

**Alienware 💻 ↔️ Desktop Casa 🖥️**

1. **Sempre pull** antes de começar
2. **Sempre push** ao terminar
3. **Identificar PC** no commit
4. **Atualizar** PC_SYNC_LOG.md
5. **Aguardar** sync OneDrive

---

## ⚠️ SAFETY CHECKLIST

Antes de push:

- [ ] `git status` executado
- [ ] Nenhum arquivo sensível
- [ ] Commit message claro
- [ ] Assinatura incluída
- [ ] SESSION_LOG.md atualizado
- [ ] PC_SYNC_LOG.md atualizado (se multi-PC)

---

## 🛠️ TROUBLESHOOTING

### Push Rejected

```bash
git pull --rebase origin master
git push origin master
```

### Merge Conflicts

```bash
# 1. Resolver manualmente
# 2. git add [arquivos]
# 3. git rebase --continue
```

### Detached HEAD

```bash
git checkout master
git pull --rebase origin master
```

---

## 📊 DAILY ROUTINE

**Morning**:

```bash
# 1. Check sync
bash .claude/skills/github-sync/scripts/sync_check.sh

# 2. Pull latest
git pull --rebase origin master

# 3. Read logs
# - SESSION_LOG.md
# - PC_SYNC_LOG.md
```

**Evening**:

```bash
# 1. Commit changes
git add .
git commit -m "chore: daily sync $(date +%d%b%Y)"

# 2. Push
git push origin master

# 3. Update logs
# - SESSION_LOG.md
# - PC_SYNC_LOG.md
```

---

## 💡 EXAMPLES

### Daily Sync

```bash
git add .
git commit -m "chore: daily vault sync - 31DEC2025

Updated files from today's session.

🤖 Generated with Claude Code"
git push origin master
```

### Feature Work

```bash
git add .
git commit -m "feat: add DeFi tracking module

Created new investment tracking:
- Portfolio dashboard
- Transaction history
- Performance metrics

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push origin master
```

### Emergency Backup

```bash
bash .claude/skills/github-sync/scripts/quick_backup.sh "before refactoring"
```

### Weekly Checkpoint

```bash
git add .
git commit -m "checkpoint: weekly backup 31DEC2025"
git tag -a "checkpoint-$(date +%Y%m%d)" -m "Weekly checkpoint"
git push --tags
```

---

## 🔗 INTEGRATION

**Com outras skills:**

- `/nevoa` - Orquestração
- `/claude-architect` - Padrões
- `/sync` - SESSION_LOG.md
- `/atualizar-status` - STATUS_VAULT.md

**Com arquivos de sync:**

- `SESSION_LOG.md` - Claude ↔️ Antigravity
- `PC_SYNC_LOG.md` - Alienware ↔️ Desktop
- `.gitignore` - Arquivos ignorados

---

## 📈 BEST PRACTICES

1. **Pull First** - Sempre antes de trabalhar
2. **Commit Often** - Pequenos e frequentes
3. **Push Daily** - Pelo menos 1x por dia
4. **Clear Messages** - Descritivos e úteis
5. **Sign Commits** - Sempre incluir assinatura
6. **Update Logs** - Manter logs atualizados
7. **Check Status** - Regularmente
8. **Avoid Conflicts** - Comunicar mudanças grandes
9. **Backup Important** - Tag checkpoints
10. **Clean Regularly** - Remover obsoletos

---

**Criado:** 31/12/2025
**Versão:** 1.0
**Status:** ✅ Ativo
**Repository:** https://github.com/gassenjean/Meu_Segundo_Cerebro.git

**SKILL GITHUB-SYNC ATIVADA. REPOSITÓRIO SINCRONIZADO! 🚀**
