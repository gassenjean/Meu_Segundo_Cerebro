# Git Commands Reference

Referência completa de comandos git para gerenciamento do vault.

## Basic Commands

### Status & Information

```bash
# Ver status atual
git status

# Ver status resumido
git status --short

# Ver histórico
git log

# Ver histórico resumido
git log --oneline

# Ver últimos N commits
git log -n 5 --oneline

# Ver mudanças não commitadas
git diff

# Ver mudanças staged
git diff --staged

# Ver branches
git branch

# Ver remotes
git remote -v
```

### Staging

```bash
# Stage arquivo específico
git add [arquivo]

# Stage todos os arquivos
git add .

# Stage apenas updates (sem new files)
git add -u

# Stage interativo
git add -p

# Unstage arquivo
git reset HEAD [arquivo]

# Unstage tudo
git reset HEAD
```

### Committing

```bash
# Commit simples
git commit -m "mensagem"

# Commit com editor
git commit

# Commit e stage tudo
git commit -am "mensagem"

# Amend último commit
git commit --amend

# Amend sem mudar mensagem
git commit --amend --no-edit
```

### Branching

```bash
# Criar branch
git branch [nome]

# Criar e mudar para branch
git checkout -b [nome]

# Mudar de branch
git checkout [nome]

# Deletar branch
git branch -d [nome]

# Deletar branch forçado
git branch -D [nome]

# Listar branches
git branch -a

# Renomear branch
git branch -m [novo-nome]
```

## Synchronization

### Pull

```bash
# Pull com merge
git pull origin master

# Pull com rebase
git pull --rebase origin master

# Fetch sem merge
git fetch origin

# Fetch específico
git fetch origin master
```

### Push

```bash
# Push para master
git push origin master

# Push com upstream
git push -u origin master

# Push todas branches
git push --all

# Push tags
git push --tags

# Force push (cuidado!)
git push --force origin master

# Force push seguro
git push --force-with-lease origin master
```

## Undoing Changes

### Local Changes

```bash
# Descartar mudanças em arquivo
git checkout -- [arquivo]

# Descartar todas mudanças
git checkout -- .

# Limpar arquivos untracked
git clean -f

# Limpar arquivos e diretórios
git clean -fd

# Preview de clean
git clean -n
```

### Commits

```bash
# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1

# Desfazer último commit (mantém working directory)
git reset --mixed HEAD~1

# Desfazer último commit (descarta tudo)
git reset --hard HEAD~1

# Desfazer N commits
git reset --soft HEAD~N

# Reverter commit (cria novo commit)
git revert [commit-hash]

# Reverter merge
git revert -m 1 [merge-commit-hash]
```

### Remote

```bash
# Sincronizar com remote
git fetch --prune

# Reset para remote
git reset --hard origin/master

# Limpar refs antigas
git remote prune origin
```

## Advanced Operations

### Stashing

```bash
# Salvar mudanças temporariamente
git stash

# Salvar com mensagem
git stash save "mensagem"

# Listar stashes
git stash list

# Aplicar último stash
git stash apply

# Aplicar e remover stash
git stash pop

# Aplicar stash específico
git stash apply stash@{0}

# Deletar stash
git stash drop stash@{0}

# Limpar todos stashes
git stash clear
```

### Tagging

```bash
# Criar tag leve
git tag [nome]

# Criar tag anotada
git tag -a [nome] -m "mensagem"

# Tag em commit específico
git tag -a [nome] [commit-hash] -m "mensagem"

# Listar tags
git tag

# Ver tag específica
git show [tag-name]

# Push tag
git push origin [tag-name]

# Push todas tags
git push --tags

# Deletar tag local
git tag -d [nome]

# Deletar tag remota
git push origin :refs/tags/[nome]
```

### Cherry-Pick

```bash
# Aplicar commit específico
git cherry-pick [commit-hash]

# Cherry-pick sem commit
git cherry-pick -n [commit-hash]

# Cherry-pick range
git cherry-pick [commit1]..[commit2]

# Abortar cherry-pick
git cherry-pick --abort

# Continuar cherry-pick
git cherry-pick --continue
```

### Rebase

```bash
# Rebase em master
git rebase master

# Rebase interativo
git rebase -i HEAD~N

# Continuar rebase
git rebase --continue

# Pular commit
git rebase --skip

# Abortar rebase
git rebase --abort
```

## Configuration

### User Settings

```bash
# Set user name
git config --global user.name "Nome"

# Set user email
git config --global user.email "email@example.com"

# Ver config
git config --list

# Ver config específica
git config user.name
```

### Repository Settings

```bash
# Set remote URL
git remote set-url origin [url]

# Add remote
git remote add [name] [url]

# Remove remote
git remote remove [name]

# Rename remote
git remote rename [old] [new]
```

### Aliases

```bash
# Criar alias
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
```

## Inspection

### Logs

```bash
# Log básico
git log

# Log oneline
git log --oneline

# Log com graph
git log --graph --oneline --all

# Log com diff
git log -p

# Log de arquivo
git log -- [arquivo]

# Log com grep
git log --grep="pattern"

# Log de autor
git log --author="nome"

# Log por data
git log --since="2 weeks ago"
git log --after="2023-01-01"
git log --before="2023-12-31"
```

### Diff

```bash
# Diff working vs staging
git diff

# Diff staging vs last commit
git diff --staged

# Diff entre commits
git diff [commit1] [commit2]

# Diff arquivo específico
git diff [arquivo]

# Diff stat
git diff --stat

# Diff de branch
git diff master..feature
```

### Blame

```bash
# Ver quem mudou cada linha
git blame [arquivo]

# Blame com range
git blame -L 10,20 [arquivo]

# Blame ignorando whitespace
git blame -w [arquivo]
```

## Maintenance

### Cleanup

```bash
# Garbage collection
git gc

# Agressivo cleanup
git gc --aggressive --prune=now

# Verificar integridade
git fsck

# Otimizar repositório
git repack -a -d --depth=250 --window=250
```

### Info

```bash
# Tamanho do repositório
git count-objects -vH

# Ver objetos grandes
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sed -n 's/^blob //p' | sort --numeric-sort --key=2 | tail -10
```

## Emergency Commands

### Recover Lost Commits

```bash
# Ver reflog
git reflog

# Recover commit
git checkout [commit-hash]
git checkout -b recovery-branch

# Merge recovery
git merge recovery-branch
```

### Fix Detached HEAD

```bash
# Criar branch do HEAD atual
git checkout -b temp-branch

# OU voltar para master
git checkout master
```

### Reset to Remote

```bash
# Backup local
git branch backup-branch

# Reset para remote
git fetch origin
git reset --hard origin/master
```

---

**Nota**: Comandos com `--force` ou `--hard` são destrutivos. Use com cuidado!
