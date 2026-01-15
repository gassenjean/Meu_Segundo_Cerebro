---
name: github-sync
description: Manage GitHub repository synchronization for Meu_Segundo_Cerebro vault. Handles commits, pushes, pulls, and ensures Claude Code and Antigravity work in sync with standardized workflows. Use this skill when syncing the vault with GitHub, managing git operations, or coordinating between AI agents.
---

# GitHub Sync - Gestão Unificada do Repositório

Skill para gerenciar sincronização do vault **Meu_Segundo_Cerebro** com GitHub, garantindo que **Claude Code** e **Antigravity** trabalhem de forma coordenada.

## Purpose

Esta skill fornece workflows padronizados para:

- Sincronizar vault local com repositório GitHub
- Coordenar trabalho entre Claude Code e Antigravity
- Garantir commits consistentes e organizados
- Manter histórico limpo e rastreável
- Evitar conflitos entre agentes IA

## When to Use

Use esta skill quando precisar:

- ✅ Sincronizar vault com GitHub (push/pull)
- ✅ Fazer commit de mudanças
- ✅ Verificar status do repositório
- ✅ Coordenar trabalho entre Claude e Antigravity
- ✅ Resolver conflitos de sincronização
- ✅ Preparar releases/checkpoints

## Repository Information

**Repository**: https://github.com/gassenjean/Meu_Segundo_Cerebro.git
**Branch**: master
**Owner**: gassenjean
**Vault Path**: C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro

## Core Workflows

### 1. Status Check

Verificar estado atual do repositório antes de qualquer operação:

```bash
git status
git log -5 --oneline
git remote -v
```

**Output**: Lista de mudanças pendentes, últimos commits, configuração de remote.

### 2. Sync Down (Pull)

Sincronizar mudanças do GitHub para o vault local:

```bash
# Verificar mudanças remotas
git fetch origin master

# Pull com rebase para manter histórico limpo
git pull --rebase origin master
```

**Quando usar**:

- Ao iniciar sessão (verificar se há mudanças de outro PC ou Antigravity)
- Antes de começar trabalho novo
- Após mensagem em SESSION_LOG.md ou PC_SYNC_LOG.md

### 3. Commit Changes

Criar commit organizado seguindo padrões do vault:

```bash
# Stage mudanças relevantes
git add [arquivos específicos]

# OU stage tudo (com cuidado)
git add .

# Commit com mensagem descritiva
git commit -m "tipo: descrição concisa

Detalhes adicionais se necessário.

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Tipos de commit**:

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `refactor:` - Refatoração
- `chore:` - Manutenção
- `style:` - Formatação
- `test:` - Testes

**Regras**:

- Mensagens em português ou inglês (consistente)
- Primeira linha: max 60 caracteres
- Sempre incluir assinatura Claude Code/Antigravity
- Nunca commitar arquivos sensíveis (.env, credentials, etc)

### 4. Sync Up (Push)

Enviar mudanças locais para GitHub:

```bash
# Push para master
git push origin master

# OU push com upstream
git push -u origin master
```

**Quando usar**:

- Após commit de mudanças importantes
- Ao finalizar sessão de trabalho
- Para backup de progresso
- Para compartilhar entre PCs

### 5. Full Sync Workflow

Workflow completo de sincronização:

```bash
# 1. Status check
git status

# 2. Pull latest
git pull --rebase origin master

# 3. Stage changes
git add .

# 4. Commit
git commit -m "chore: sync vault updates

- Updated files from session
- Cleaned up old references

🤖 Generated with Claude Code"

# 5. Push
git push origin master
```

### 6. Conflict Resolution

Resolver conflitos de merge:

```bash
# 1. Verificar conflitos
git status

# 2. Resolver manualmente arquivos conflitantes
# Editar arquivos com conflitos (<<<<<<< HEAD, =======, >>>>>>>)

# 3. Stage resoluções
git add [arquivos resolvidos]

# 4. Continuar rebase
git rebase --continue

# OU abortar se necessário
git rebase --abort
```

## Integration with Bi-AI System

### Claude Code Workflows

**Ao iniciar sessão**:

1. Ler `SESSION_LOG.md` - verificar mensagens de Antigravity
2. Ler `PC_SYNC_LOG.md` - verificar mudanças de outro PC
3. Executar `git pull --rebase` - sincronizar
4. Começar trabalho

**Ao finalizar sessão**:

1. Executar `git add .` - stage mudanças
2. Criar commit descritivo
3. Executar `git push` - enviar para GitHub
4. Atualizar `SESSION_LOG.md` - deixar mensagem para Antigravity
5. Atualizar `PC_SYNC_LOG.md` - deixar mensagem para outro PC

### Antigravity Workflows

**Ao iniciar sessão**:

1. Ler `SESSION_LOG.md` - verificar mensagens de Claude
2. Executar `git pull --rebase` - sincronizar
3. Começar trabalho

**Ao finalizar sessão**:

1. Executar `git add .` - stage mudanças
2. Criar commit com assinatura Antigravity
3. Executar `git push` - enviar para GitHub
4. Atualizar `SESSION_LOG.md` - deixar mensagem para Claude

## Coordination Protocols

### Multi-PC Sync

Quando trabalhando em **2 PCs** (Alienware 💻 + Desktop 🖥️):

1. **Sempre** pull antes de começar
2. **Sempre** push ao terminar
3. **Identificar** qual PC no commit
4. **Aguardar** sync OneDrive antes de fechar vault
5. **Atualizar** `PC_SYNC_LOG.md`

### Multi-Agent Sync

Quando trabalhando com **2 agentes** (Claude + Antigravity):

1. **Sempre** ler `SESSION_LOG.md` antes de começar
2. **Sempre** atualizar `SESSION_LOG.md` ao terminar
3. **Incluir assinatura** no commit (Claude Code ou Antigravity)
4. **Evitar** trabalho simultâneo no mesmo arquivo
5. **Comunicar** mudanças estruturais importantes

## Safety Protocols

### Before Push

Verificar checklist antes de push:

- [ ] `git status` executado
- [ ] Nenhum arquivo sensível (.env, credentials)
- [ ] Commit message descritivo e claro
- [ ] Assinatura Claude/Antigravity incluída
- [ ] `SESSION_LOG.md` atualizado
- [ ] `PC_SYNC_LOG.md` atualizado (se multi-PC)

### Backup Strategy

Estratégia de backup automático:

1. **OneDrive** - Sync automático do vault local
2. **GitHub** - Versionamento e histórico
3. **Checkpoints** - Snapshots semanais em `00_SISTEMA/CHECKPOINTS/`

### Rollback

Reverter mudanças se necessário:

```bash
# Reverter último commit (mantém mudanças)
git reset --soft HEAD~1

# Reverter último commit (descarta mudanças)
git reset --hard HEAD~1

# Reverter arquivo específico
git checkout HEAD -- [arquivo]

# Reverter para commit específico
git reset --hard [commit-hash]
```

## Common Tasks

### Task: Sync Vault Daily

```bash
# Morning routine
git pull --rebase origin master

# Evening routine
git add .
git commit -m "chore: daily vault sync - $(date +%d%b%Y)"
git push origin master
```

### Task: Create Weekly Checkpoint

```bash
# Create checkpoint
git add .
git commit -m "checkpoint: weekly backup $(date +%d%b%Y)

Weekly vault snapshot.

🤖 Generated with Claude Code"
git tag -a "checkpoint-$(date +%Y%m%d)" -m "Weekly checkpoint"
git push origin master --tags
```

### Task: Clean Old Files

```bash
# Stage deletions
git add -u

# Commit
git commit -m "chore: clean old files

Removed deprecated references and duplicates.

🤖 Generated with Claude Code"

# Push
git push origin master
```

### Task: Emergency Backup

```bash
# Quick backup
git add .
git commit -m "backup: emergency snapshot $(date +%H%M)"
git push origin master
```

## Troubleshooting

### Issue: Push Rejected

**Sintoma**: `! [rejected] master -> master (fetch first)`

**Solução**:

```bash
git pull --rebase origin master
git push origin master
```

### Issue: Merge Conflicts

**Sintoma**: `CONFLICT (content): Merge conflict in [file]`

**Solução**:

1. Abrir arquivo conflitante
2. Resolver manualmente (escolher entre HEAD e incoming)
3. `git add [arquivo]`
4. `git rebase --continue`

### Issue: Detached HEAD

**Sintoma**: `HEAD detached at [commit]`

**Solução**:

```bash
git checkout master
git pull --rebase origin master
```

### Issue: Untracked Files

**Sintoma**: Arquivos não rastreados acumulando

**Solução**:

```bash
# Verificar gitignore
cat .gitignore

# Adicionar padrões se necessário
echo "*.tmp" >> .gitignore

# Limpar cache
git rm -r --cached .
git add .
```

## References

Para informações adicionais, consultar:

- `references/GIT_COMMANDS.md` - Lista completa de comandos git
- `references/COMMIT_CONVENTIONS.md` - Convenções de mensagens de commit
- `.gitignore` - Arquivos ignorados pelo git

## Scripts

Scripts auxiliares disponíveis em `scripts/`:

- `scripts/sync_check.sh` - Verificar estado de sincronização
- `scripts/quick_backup.sh` - Backup rápido com timestamp
- `scripts/cleanup_old.sh` - Limpar arquivos antigos marcados para deletion

## Integration with Other Skills

Esta skill integra com:

- `/nevoa` - Orquestração e continuidade
- `/claude-architect` - Padrões e qualidade
- `/sync` - Atualizar SESSION_LOG.md
- `/atualizar-status` - Atualizar STATUS_VAULT.md

## Best Practices

1. **Pull First** - Sempre pull antes de começar trabalho
2. **Commit Often** - Commits pequenos e frequentes
3. **Push Daily** - Pelo menos uma vez por dia
4. **Clear Messages** - Mensagens de commit descritivas
5. **Sign Commits** - Sempre incluir assinatura do agente
6. **Update Logs** - Manter SESSION_LOG.md e PC_SYNC_LOG.md atualizados
7. **Check Status** - Verificar `git status` regularmente
8. **Avoid Conflicts** - Comunicar mudanças grandes
9. **Backup Important** - Tag checkpoints importantes
10. **Clean Regularly** - Remover arquivos obsoletos

---

**Created**: 31/12/2025
**Version**: 1.0
**Status**: ✅ Active
**Repository**: https://github.com/gassenjean/Meu_Segundo_Cerebro.git
