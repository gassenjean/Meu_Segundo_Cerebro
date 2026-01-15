---
criado: 2026-01-14T12:22:26-03:00
atualizado: 2026-01-14T17:02:53-03:00
---
# 🔍 PROMPT DE VERIFICAÇÃO - Colar no Gemini/Antigravity

**Data:** 31/DEZ/2025
**Versão:** 1.0
**Objetivo:** Verificar sincronização após criação da skill github-sync

---

## 📋 COLE ESTE PROMPT NO GEMINI:

```
Olá Gemini! 👋

Claude Code acabou de criar a skill **github-sync** e preciso verificar se está tudo sincronizado corretamente entre nós dois.

**TAREFA DE VERIFICAÇÃO:**

## 1. Verificar Configuração GitHub

Execute e me mostre o resultado:

```bash
cd /path/to/Meu_Segundo_Cerebro
git status
git remote -v
git log -5 --oneline
```

## 2. Verificar Skill GitHub-Sync

Confirme se esses arquivos existem:

```bash
ls -la .claude/skills/github-sync/
cat .claude/skills/github-sync/SKILL.md | head -50
```

## 3. Testar Script sync_check

Execute o script de verificação:

```bash
bash .claude/skills/github-sync/scripts/sync_check.sh
```

## 4. Verificar GEMINI.md Atualizado

Confirme que você recebeu as atualizações:

```bash
cat .gemini/GEMINI.md | grep -A 10 "SINCRONIZAÇÃO GITHUB"
cat .gemini/GEMINI.md | grep "Versão:"
```

## 5. Verificar Logs de Sync

Leia os logs atuais:

```bash
cat SESSION_LOG.md | tail -50
cat PC_SYNC_LOG.md | tail -30
```

## 6. Resumo Final

Me forneça um resumo estruturado:

### ✅ O Que Está Funcionando
- [ ] Repository conectado corretamente
- [ ] Skill github-sync instalada
- [ ] Scripts executáveis
- [ ] GEMINI.md atualizado (versão 2.1)
- [ ] SESSION_LOG.md legível
- [ ] PC_SYNC_LOG.md legível

### ⚠️ Problemas Encontrados
(Liste se houver)

### 📊 Status do Repositório
- Uncommitted changes: ?
- Commits ahead/behind: ?
- Último commit: ?

### 🚀 Próximos Passos Recomendados
(O que você sugere fazer agora?)

---

**IMPORTANTE:**
- Use sua capacidade de 1M tokens para processar TUDO
- Seja conciso mas completo
- Estruture a resposta em seções claras
- Indique problemas com ⚠️ e sucessos com ✅
```

---

## 📝 INFORMAÇÕES PARA REFERÊNCIA

### O Que Claude Code Criou:

**Skill github-sync:**
- Localização: `.claude/skills/github-sync/`
- SKILL.md (15KB) - Documentação completa
- Scripts: sync_check.sh, quick_backup.sh, cleanup_old.sh
- References: GIT_COMMANDS.md, COMMIT_CONVENTIONS.md
- Comando: `/github-sync`

**Atualizações:**
- `.gemini/GEMINI.md` → Versão 2.1
- Protocolo GitHub adicionado
- Integração bi-IA documentada

### Estado Atual do Repositório:

**Repository:** https://github.com/gassenjean/Meu_Segundo_Cerebro.git
**Branch:** master
**Status:** ~1908 uncommitted changes (pendentes de limpeza)

### Logs de Sincronização:

**SESSION_LOG.md:**
- Claude Code ↔️ Antigravity/Gemini
- Atualizar ao trocar de agente

**PC_SYNC_LOG.md:**
- Alienware 💻 ↔️ Desktop Casa 🖥️
- Atualizar ao trocar de PC

---

## 🎯 RESULTADO ESPERADO DO GEMINI:

O Gemini deve retornar:

1. ✅ **Confirmação** que todos arquivos da skill existem
2. ✅ **Output** do sync_check.sh mostrando status
3. ✅ **Validação** que GEMINI.md está atualizado (v2.1)
4. ✅ **Leitura** dos logs SESSION_LOG.md e PC_SYNC_LOG.md
5. 📊 **Resumo estruturado** do estado atual
6. 🚀 **Recomendações** do que fazer a seguir

---

## ⚠️ PROBLEMAS POTENCIAIS E SOLUÇÕES:

### Problema 1: "git command not found"
**Solução:** Gemini precisa estar rodando em ambiente com git instalado

### Problema 2: "Permission denied" nos scripts
**Solução:**
```bash
chmod +x .claude/skills/github-sync/scripts/*.sh
```

### Problema 3: GEMINI.md não atualizado
**Solução:** Claude Code já atualizou. Gemini precisa recarregar contexto.

### Problema 4: 1908 uncommitted changes
**Solução:** Normal. São arquivos antigos marcados para deletion. Usar:
```bash
bash .claude/skills/github-sync/scripts/cleanup_old.sh
```

---

## 📊 CHECKLIST DE VALIDAÇÃO:

Após receber resposta do Gemini, verificar:

- [ ] Gemini conseguiu ler SKILL.md
- [ ] Script sync_check.sh executou
- [ ] GEMINI.md versão 2.1 confirmada
- [ ] Repository info correto (URL, branch)
- [ ] SESSION_LOG.md acessível
- [ ] PC_SYNC_LOG.md acessível
- [ ] Status do git mostrado
- [ ] Recomendações claras fornecidas

---

## 🎉 SE TUDO OK:

**Próximos passos:**

1. **Limpar vault** (Gemini pode fazer):
   ```bash
   bash .claude/skills/github-sync/scripts/cleanup_old.sh
   ```

2. **Commit a skill** (Gemini pode fazer):
   ```bash
   git add .claude/skills/github-sync
   git add .claude/commands/github-sync.md
   git add .gemini/GEMINI.md
   git commit -m "feat: add GitHub sync skill

   Created comprehensive GitHub sync management:
   - Unified Claude Code + Antigravity workflows
   - Multi-PC sync protocols
   - Scripts: sync_check, quick_backup, cleanup_old
   - Updated GEMINI.md with GitHub protocols

   🚀 Generated with Antigravity
   Co-Authored-By: Gemini 3 Pro <noreply@google.com>"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin master
   ```

4. **Atualizar SESSION_LOG.md**:
   - Gemini documenta o que foi feito
   - Deixa mensagem para Claude Code

---

**Criado:** 31/12/2025
**Versão:** 1.0
**Status:** ✅ Pronto para colar no Gemini

**COLE O PROMPT E VEJA A MÁGICA ACONTECER! 🚀**
