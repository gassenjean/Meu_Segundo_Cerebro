# PROTOCOLO: GitHub Multi-Dispositivo

**Status**: ✅ Active
**Criado**: 14/Jan/2026
**Atualizado**: 14/Jan/2026
**Versão**: 1.0

---

## 📱 Dispositivos do Sistema

- **🖥️ Desktop Casa** - Windows, Claude Code CLI
- **💻 Alienware** - Windows, Claude Code CLI (trabalho/externo)
- **📱 iPhone** - iOS, Claude Code Mobile App

---

## ⚠️ PROBLEMA IDENTIFICADO

Você estava criando **branches diferentes em cada dispositivo** sem sincronizar, causando:
- ❌ Conflitos de merge
- ❌ Trabalho duplicado
- ❌ Branches órfãs no GitHub
- ❌ Histórico confuso

**Exemplo do que acontecia:**
```
iPhone cria: claude/document-legal-meeting-QplYn
Desktop cria: mudanças locais não commitadas
Alienware cria: master-aliengass

Result: 🔥 CONFLITO!
```

---

## ✅ SOLUÇÃO: Workflow Correto

### 🔄 Regra de Ouro

> **SEMPRE pull ANTES de começar a trabalhar**
> **SEMPRE commit e push DEPOIS de terminar**

---

## 📋 Protocolo por Dispositivo

### 🖥️ Desktop Casa (Principal)

**AO INICIAR:**
```bash
# 1. Ver status
git status

# 2. Pull primeiro (SEMPRE!)
git pull origin master

# 3. Trabalhar normalmente
```

**AO FINALIZAR:**
```bash
# 1. Adicionar mudanças
git add -A

# 2. Commit descritivo
git commit -m "feat: descrição do que fiz

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 3. Push imediatamente
git push origin master

# 4. Atualizar SESSION_LOG.md e PC_SYNC_LOG.md
```

---

### 📱 iPhone (Claude Code Mobile)

**⚠️ IMPORTANTE: iPhone cria branches automaticamente!**

Claude Code no iPhone cria branches como:
- `claude/document-legal-meeting-QplYn`
- `claude/find-moc-sharing-studies-OZyae`
- `claude/review-vault-contents-018YVFAPmd4G86N94N1G7BG8`

**NUNCA delete essas branches manualmente!**

**O QUE FAZER:**

1. **Trabalhe normalmente no iPhone** - Claude Code cuida das branches
2. **Quando terminar, abra o Desktop** e faça:

```bash
# 1. Ver branches remotas
git fetch --all
git branch -r

# 2. Identificar nova branch do iPhone
# Exemplo: origin/claude/document-legal-meeting-QplYn

# 3. Ver o que tem nela
git log origin/claude/NOME-DA-BRANCH --oneline -10

# 4. Mesclar no master
git merge origin/claude/NOME-DA-BRANCH -m "feat: mesclar trabalho do iPhone

Descrição do que foi feito.

🤖 Generated with Claude Code"

# 5. Push
git push origin master

# 6. Deletar branch remota (DEPOIS do merge!)
git push origin --delete claude/NOME-DA-BRANCH
```

---

### 💻 Alienware (Trabalho/Externo)

**AO INICIAR:**
```bash
# 1. Ler PC_SYNC_LOG.md
cat PC_SYNC_LOG.md

# 2. Pull SEMPRE primeiro
git pull origin master

# 3. Trabalhar
```

**AO FINALIZAR:**
```bash
# 1. Commit com identificação
git add -A
git commit -m "feat: descrição [Alienware]

🤖 Generated with Claude Code"

# 2. Push
git push origin master

# 3. Atualizar PC_SYNC_LOG.md
```

---

## 🚫 O QUE NUNCA FAZER

### ❌ ERRO 1: Trabalhar sem Pull
```bash
# ERRADO:
git add .
git commit
git push  # 🔥 CONFLITO!

# CERTO:
git pull origin master  # PRIMEIRO!
git add .
git commit
git push
```

### ❌ ERRO 2: Deixar Mudanças Sem Commit
```bash
# ERRADO:
# Fazer mudanças no Desktop
# Fechar sem commitar
# Abrir no iPhone
# 🔥 CONFLITO quando voltar ao Desktop!

# CERTO:
# Sempre commit ANTES de trocar de dispositivo
```

### ❌ ERRO 3: Forçar Push
```bash
# NUNCA FAÇA:
git push --force origin master  # 🔥 PERDE TRABALHO DOS OUTROS DISPOSITIVOS!

# SE DER ERRO DE PUSH:
git pull --rebase origin master  # Tenta rebase
# OU
git pull origin master  # Merge normal
git push origin master
```

### ❌ ERRO 4: Ignorar Branches do iPhone
```bash
# ERRADO:
# Ver branch no GitHub
# Ignorar e continuar trabalhando no master
# 🔥 Trabalho do iPhone fica perdido!

# CERTO:
# Sempre mesclar branches do iPhone no master
```

---

## 🔄 Workflow Diário Ideal

### Manhã (Desktop Casa)

```bash
# 1. Abrir terminal no vault
cd C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro

# 2. Ver status geral
git status
git log -5 --oneline

# 3. Pull mudanças
git pull origin master

# 4. Verificar se há branches do iPhone
git fetch --all
git branch -r | grep "claude/"

# 5. Se houver, mesclar ANTES de trabalhar
git merge origin/claude/NOME -m "feat: merge iPhone work"
git push origin master

# 6. Agora pode trabalhar!
```

### Tarde (Alienware - Trabalho Externo)

```bash
# 1. Pull SEMPRE primeiro
git pull origin master

# 2. Trabalhar

# 3. Commit com tag [Alienware]
git add -A
git commit -m "feat: trabalho externo [Alienware]

🤖 Generated with Claude Code"

# 4. Push imediatamente
git push origin master

# 5. Atualizar PC_SYNC_LOG.md antes de fechar
```

### Noite (iPhone - Leitura/Revisão)

```bash
# Trabalhe normalmente
# Claude Code cuida de tudo
# Branches são criadas automaticamente
```

### Noite (Desktop Casa - Finalizar Dia)

```bash
# 1. Ver branches do iPhone
git fetch --all
git branch -r

# 2. Mesclar se houver
git merge origin/claude/NOME -m "feat: merge iPhone evening work"

# 3. Commit mudanças locais
git add -A
git commit -m "chore: daily sync

🤖 Generated with Claude Code"

# 4. Push final do dia
git push origin master

# 5. Limpar branches já mescladas
git push origin --delete claude/BRANCH-JA-MESCLADA
```

---

## 🧹 Limpeza de Branches

### Quando Limpar

Limpe branches **DEPOIS** de mesclar no master:

```bash
# 1. Verificar que branch foi mesclada
git log origin/claude/NOME --oneline -1

# 2. Verificar que está no master
git log master --oneline -5 | grep "merge"

# 3. Deletar branch remota
git push origin --delete claude/NOME

# 4. Limpar referências locais
git fetch --prune
```

### Checklist Semanal (Sexta 17h)

- [ ] Todas as branches do iPhone foram mescladas?
- [ ] Branches antigas foram deletadas?
- [ ] Master está sincronizado em todos os dispositivos?
- [ ] SESSION_LOG.md atualizado?
- [ ] PC_SYNC_LOG.md atualizado?
- [ ] Backup tag criada? (`git tag backup-DDMMMYYYY`)

---

## 🔧 Comandos Úteis

### Ver Branches Remotas
```bash
git branch -r
```

### Ver Diferenças Entre Branches
```bash
git diff master origin/claude/NOME --stat
```

### Ver Commits de Uma Branch
```bash
git log origin/claude/NOME --oneline -10
```

### Mesclar Branch Remota
```bash
git merge origin/claude/NOME -m "feat: merge iPhone work"
```

### Deletar Branch Remota
```bash
git push origin --delete claude/NOME
```

### Verificar Status de Sincronização
```bash
git fetch --all
git status
git log --oneline --graph --all -10
```

---

## 🆘 Resolver Conflitos

### Cenário 1: Conflito ao Pull

```bash
# Aconteceu:
git pull origin master
# Auto-merging file.md
# CONFLICT (content): Merge conflict in file.md

# SOLUÇÃO:
# 1. Abrir arquivo conflitante
# 2. Procurar por:
<<<<<<< HEAD
(sua versão local)
=======
(versão remota)
>>>>>>> origin/master

# 3. Escolher qual versão manter (ou mesclar manualmente)
# 4. Remover os marcadores de conflito
# 5. Adicionar arquivo resolvido
git add file.md

# 6. Finalizar merge
git commit -m "fix: resolve merge conflict

🤖 Generated with Claude Code"

# 7. Push
git push origin master
```

### Cenário 2: Push Rejeitado

```bash
# Aconteceu:
git push origin master
# ! [rejected] master -> master (fetch first)

# SOLUÇÃO:
# 1. Pull com rebase
git pull --rebase origin master

# 2. Se houver conflitos, resolver
git add .
git rebase --continue

# 3. Push
git push origin master
```

### Cenário 3: Branches Divergentes

```bash
# Aconteceu:
# Desktop e iPhone fizeram mudanças no mesmo arquivo

# SOLUÇÃO PREVENTIVA:
# Sempre pull ANTES de começar a trabalhar!

# SOLUÇÃO CORRETIVA:
git fetch --all
git merge origin/claude/BRANCH -m "fix: merge divergent branches"
# Resolver conflitos manualmente
git add .
git commit
git push origin master
```

---

## 📊 Diagrama de Workflow

```
Desktop Casa                 iPhone                   GitHub
     │                         │                         │
     │───── Pull ─────────────────────────────────────>│
     │                         │                         │
     │                         │◄──── Criar Branch ──────│
     │                         │   claude/work-X         │
     │                         │                         │
     │◄──── Fetch Branches ────────────────────────────>│
     │                         │                         │
     │───── Merge Branch ───────────────────────────────>│
     │        no Master        │                         │
     │                         │                         │
     │───── Push Master ───────────────────────────────>│
     │                         │                         │
     │───── Delete Branch ─────────────────────────────>│
     │   claude/work-X         │                         │
     │                         │                         │
     └─────────────────────────┴─────────────────────────┘
```

---

## 🎯 Resumo Executivo

### 3 Regras de Ouro

1. **PULL PRIMEIRO** - Sempre `git pull origin master` ao iniciar
2. **COMMIT SEMPRE** - Nunca deixe mudanças sem commit
3. **PUSH LOGO** - Sempre `git push origin master` ao terminar

### Fluxo Simplificado

```bash
# INICIAR TRABALHO
git pull origin master

# TRABALHAR
# ... fazer mudanças ...

# FINALIZAR TRABALHO
git add -A
git commit -m "feat: descrição"
git push origin master

# MESCLAR BRANCHES DO IPHONE (quando houver)
git fetch --all
git merge origin/claude/NOME -m "feat: merge iPhone"
git push origin master
git push origin --delete claude/NOME
```

---

## 📝 Checklist Rápido

**Antes de começar:**
- [ ] `git pull origin master`
- [ ] `git fetch --all`
- [ ] Ver se há branches do iPhone para mesclar

**Ao terminar:**
- [ ] `git add -A`
- [ ] `git commit -m "mensagem"`
- [ ] `git push origin master`
- [ ] Atualizar SESSION_LOG.md
- [ ] Atualizar PC_SYNC_LOG.md

**Semanalmente:**
- [ ] Limpar branches mescladas
- [ ] Criar backup tag
- [ ] Revisar histórico de commits

---

## 📚 Referências

- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md` - Protocolo multi-PC
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md` - Sync agentes IA
- `.claude/skills/github-sync/README.md` - Skill GitHub Sync
- `SESSION_LOG.md` - Log de sincronização Gemini/Claude
- `PC_SYNC_LOG.md` - Log de sincronização entre PCs

---

**🤖 Generated with Claude Code**
**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
