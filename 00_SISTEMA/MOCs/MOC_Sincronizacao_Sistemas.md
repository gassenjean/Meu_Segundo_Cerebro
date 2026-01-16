# MOC: Sincronização de Sistemas

**Decision Tree - Qual Protocolo de Sincronização Usar?**

**Criado:** 16/Jan/2026
**Versão:** 1.0
**Propósito:** Eliminar confusão entre 4 protocolos de sincronização diferentes

---

## 🎯 DECISÃO RÁPIDA (30 SEGUNDOS)

### Pergunta: O que você está fazendo?

```
┌─────────────────────────────────────────────────────────────┐
│ Estou TROCANDO DE COMPUTADOR                               │
│ (Alienware → Desktop Casa ou vice-versa)                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
           📋 PROTOCOLO_MULTI_PC.md + PC_SYNC_LOG.md


┌─────────────────────────────────────────────────────────────┐
│ Estou fazendo HANDOFF ENTRE IAs                            │
│ (Claude → Gemini ou Gemini → Claude)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
   🤖 PROTOCOLO_SINCRONIZACAO_AGENTES.md + SESSION_LOG.md


┌─────────────────────────────────────────────────────────────┐
│ Preciso RESOLVER BRANCHES do Claude Code no GitHub        │
│ (claude/*, branches do iPhone)                             │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
           🔀 PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md


┌─────────────────────────────────────────────────────────────┐
│ Quero usar GITHUB API via Gemini/Antigravity              │
│ (criar issues, PRs, relatórios sem git CLI)               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
              🚀 PROTOCOLO_ANTIGRAVITY_GITHUB.md
```

---

## 📊 TABELA COMPARATIVA

| Aspecto | Multi-PC | Sincronização Agentes | GitHub Multi-Dispositivo | Antigravity GitHub |
|---------|----------|----------------------|--------------------------|-------------------|
| **Arquivo** | PROTOCOLO_MULTI_PC.md | PROTOCOLO_SINCRONIZACAO_AGENTES.md | PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md | PROTOCOLO_ANTIGRAVITY_GITHUB.md |
| **Log usado** | PC_SYNC_LOG.md | SESSION_LOG.md | Git (branches) | SESSION_LOG.md |
| **Sincroniza** | Alienware ↔ Desktop | Claude ↔ Gemini | iPhone ↔ Desktop ↔ Alienware | Antigravity ↔ GitHub |
| **Frequência** | Ao trocar PC | Ao fazer handoff IA | Ao abrir iPhone/resolver branches | Sob demanda |
| **Método** | OneDrive + log manual | Log manual | Git CLI (merge/push) | GitHub API (gh CLI) |
| **Complexidade** | Baixa | Baixa | Média | Média |
| **Automático?** | Não (manual) | Não (manual) | Parcial (OneDrive sync, merge manual) | Não (comandos API) |

---

## 📖 PROTOCOLO 1: MULTI-PC

**Arquivo:** [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md]]
**Log:** [[PC_SYNC_LOG.md]] (raiz)

### Quando Usar

- Abrir vault no Alienware (depois de trabalhar no Desktop)
- Abrir vault no Desktop (depois de trabalhar no Alienware)
- Finalizar trabalho em qualquer PC

### Como Funciona

1. **OneDrive sincroniza arquivos** automaticamente
2. **PC_SYNC_LOG.md comunica mudanças** (manual)
3. **Agente lê log** ao iniciar sessão
4. **Agente atualiza log** ao finalizar

### Workflow

```
DESKTOP CASA:
1. Trabalhou no vault
2. Atualiza PC_SYNC_LOG.md (seção "Desktop → Alienware")
3. Aguarda OneDrive sync
4. Fecha vault

ALIENWARE (depois):
1. Abre vault
2. LÊ PC_SYNC_LOG.md PRIMEIRO
3. Vê o que Desktop fez
4. Continua trabalho
5. Atualiza PC_SYNC_LOG.md (seção "Alienware → Desktop")
```

### Exemplo Real

```markdown
### 🖥️ Desktop Casa - 16/01/2026 (15:30)

**Ações realizadas:**
- Criado MOC_Padroes_Protocolos_Guidelines.md
- Criado GUIA_Leitura_Claude.md

**Mensagem para Alienware:**
> Consolidação de padrões completa.
> 7 novos arquivos em 00_SISTEMA/.
> Economia estimada -40% tokens!
```

---

## 🤖 PROTOCOLO 2: SINCRONIZAÇÃO AGENTES

**Arquivo:** [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]]
**Log:** [[SESSION_LOG.md]] (raiz)

### Quando Usar

- Claude Code terminou tarefa, Gemini vai continuar
- Gemini terminou processamento, Claude vai revisar
- Handoff de contexto entre IAs

### Como Funciona

1. **IA finalizando atualiza SESSION_LOG.md**
2. **IA recebendo lê SESSION_LOG.md ao iniciar**
3. **Comunicação bidirecional** (seções separadas)
4. **Mensagens diretas** entre agentes

### Workflow

```
CLAUDE CODE:
1. Fez planejamento estratégico
2. Atualiza SESSION_LOG.md
3. Deixa mensagem para Gemini:
   "Gemini: Execute as 10 tarefas do plano.
    Retorne quando finalizar."

GEMINI (depois):
1. Lê SESSION_LOG.md
2. Vê mensagem de Claude
3. Executa as 10 tarefas
4. Atualiza SESSION_LOG.md
5. Mensagem: "Claude: 10 tarefas concluídas.
    Revisar arquivo X."
```

### Exemplo Real

```markdown
## 🔵 Claude Code - 16/01/2026 (10:00)

**Trabalho Realizado:**
- Plano de consolidação criado (7 fases)

**Mensagem para Gemini:**
> Plano pronto. Se houver tarefas de processamento
> massivo (>100k tokens), você executa. Eu reviso.

---

## 🟣 Antigravity/Gemini - 16/01/2026 (14:00)

**Trabalho Realizado:**
- Processou 10 lives do Alan Nicolas
- Total: 50k linhas de notas

**Mensagem para Claude:**
> Processamento completo. Revisar nomenclatura
> dos arquivos criados (alguns >60 chars).
```

---

## 🔀 PROTOCOLO 3: GITHUB MULTI-DISPOSITIVO

**Arquivo:** [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]]
**Método:** Git CLI

### Quando Usar

- Branches automáticas do Claude no iPhone (`claude/*`)
- Resolver conflitos entre commits de diferentes dispositivos
- Sincronizar repositório GitHub com local

### Como Funciona

1. **Claude Code no iPhone cria branches** automáticas
2. **Desktop/Alienware faz merge** dessas branches
3. **Git push sincroniza** para origin/master
4. **Long paths habilitados** (Windows)

### Workflow

```bash
# 1. Verificar branches remotas
git fetch origin

# 2. Ver branches do iPhone
git branch -r | grep claude/

# 3. Merge branch específica
git checkout master
git merge origin/claude/nome-da-branch

# 4. Resolver conflitos (se houver)
git status
# Editar arquivos conflitantes
git add .
git commit -m "Merge branch do iPhone"

# 5. Push para origin
git push origin master

# 6. Deletar branch remota (opcional)
git push origin --delete claude/nome-da-branch
```

### Configuração Necessária

```bash
# Habilitar long paths (Windows)
git config core.longpaths true

# Verificar
git config --get core.longpaths  # deve retornar "true"
```

### Exemplo Real

```bash
# Situação: 3 branches do iPhone não mescladas
$ git branch -r
  origin/master
  origin/claude/document-legal-meeting
  origin/claude/find-moc-sharing-studies
  origin/claude/review-vault-contents

# Merge das 3
git merge origin/claude/document-legal-meeting
git merge origin/claude/find-moc-sharing-studies
git merge origin/claude/review-vault-contents

# Push
git push origin master

# Limpar branches antigas
git push origin --delete claude/document-legal-meeting
git push origin --delete claude/find-moc-sharing-studies
git push origin --delete claude/review-vault-contents
```

---

## 🚀 PROTOCOLO 4: ANTIGRAVITY GITHUB

**Arquivo:** [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_ANTIGRAVITY_GITHUB.md]]
**Método:** GitHub API (gh CLI)

### Quando Usar

- Criar issues no GitHub via Gemini
- Gerar relatórios de atividade do repositório
- Criar PRs sem usar git CLI
- Automatizar workflows GitHub

### Como Funciona

1. **gh CLI autenticado** no Antigravity
2. **Gemini executa comandos** via API
3. **Sem necessidade de git local**
4. **Comandos prontos** no quick start

### Workflow

```bash
# 1. Criar issue
gh issue create --title "Título" --body "Descrição"

# 2. Listar issues
gh issue list

# 3. Fechar issue
gh issue close 123

# 4. Ver commits recentes
gh api repos/{owner}/{repo}/commits

# 5. Criar PR
gh pr create --title "Título" --body "Descrição"

# 6. Relatório semanal
# (script customizado, ver PROTOCOLO_ANTIGRAVITY_GITHUB.md)
```

### Quick Start

**Ver comandos prontos:**
[[00_SISTEMA/QUICK_START_ANTIGRAVITY_GITHUB.md]]

### Exemplo Real

```bash
# Gemini criando issue de teste
$ gh issue create \
  --title "[TEST] Antigravity Integration" \
  --body "Teste de integração GitHub API via Antigravity"

Creating issue in {owner}/{repo}
✓ Created issue #8

# Verificar
$ gh issue list
#8  [TEST] Antigravity Integration  (Open)
```

---

## 🔄 FLUXOS COMBINADOS

### Cenário 1: Trabalho Completo (Multi-PC + Multi-IA)

```
DESKTOP CASA (Claude):
1. Planeja consolidação de padrões
2. Atualiza SESSION_LOG.md → Mensagem para Gemini
3. Atualiza PC_SYNC_LOG.md → Mensagem para Alienware
4. Commit + push GitHub

ALIENWARE (Gemini, depois):
1. Lê PC_SYNC_LOG.md → Vê trabalho do Desktop
2. Lê SESSION_LOG.md → Vê mensagem de Claude
3. Executa 10 tarefas delegadas
4. Atualiza SESSION_LOG.md → Mensagem para Claude
5. Atualiza PC_SYNC_LOG.md → Mensagem para Desktop
6. Commit + push GitHub
```

### Cenário 2: iPhone → Desktop → GitHub

```
IPHONE (Claude Code):
1. Cria nota de devocional
2. Branch automática: claude/add-devotional-xyz
3. Commit + push para branch

DESKTOP (Claude Code, depois):
1. Lê PROTOCOLO_GITHUB_MULTI_DISPOSITIVO
2. Fetch origin
3. Merge claude/add-devotional-xyz
4. Push origin master
5. Delete branch remota
```

### Cenário 3: Gemini + GitHub API

```
DESKTOP (Gemini):
1. Usuário: "Cria issue para documentar X"
2. Gemini lê PROTOCOLO_ANTIGRAVITY_GITHUB
3. Gemini executa: gh issue create --title "Documentar X"
4. Issue criada, atualiza SESSION_LOG.md
```

---

## 🚨 TROUBLESHOOTING

### Problema 1: Não sei qual protocolo usar

**Solução:** Use decision tree no topo deste arquivo (30 segundos)

### Problema 2: Esqueci de atualizar log

**Multi-PC:**
```
1. Abra PC_SYNC_LOG.md
2. Adicione seção com trabalho realizado
3. Use template fornecido no protocolo
```

**Multi-IA:**
```
1. Abra SESSION_LOG.md
2. Adicione seção no topo (mais recente)
3. Use template fornecido no protocolo
```

### Problema 3: Branches do iPhone acumuladas

**Solução:**
```bash
# Ver todas branches remotas
git branch -r | grep claude/

# Merge todas de uma vez (se não houver conflitos)
for branch in $(git branch -r | grep claude/ | sed 's/origin\///'); do
  git merge origin/$branch
done

# Push
git push origin master

# Deletar todas branches claude/* remotas
for branch in $(git branch -r | grep claude/ | sed 's/origin\///'); do
  git push origin --delete $branch
done
```

### Problema 4: GitHub API não autenticado

**Solução:**
```bash
# Verificar autenticação
gh auth status

# Se não autenticado
gh auth login
# Seguir instruções (navegador)

# Testar
gh issue list
```

---

## 📊 COMPARAÇÃO DE USO

| Situação | Protocolo Correto | Log Usado | Frequência |
|----------|-------------------|-----------|------------|
| Trabalhou no Desktop, agora Alienware | Multi-PC | PC_SYNC_LOG.md | Sempre que troca PC |
| Claude planejou, Gemini executa | Sincronização Agentes | SESSION_LOG.md | Handoff IA |
| iPhone criou branch, Desktop precisa merge | GitHub Multi-Dispositivo | Git (branches) | Semanal |
| Gemini precisa criar issue | Antigravity GitHub | N/A (API) | Sob demanda |
| Alienware commitou, Desktop puxa | Git normal | N/A (git pull) | Sempre ao iniciar |

---

## ✅ CHECKLIST DE DECISÃO

**Antes de escolher protocolo, pergunte:**

- [ ] Estou trocando de PC físico? → Multi-PC
- [ ] Estou passando tarefa de IA para outra? → Sincronização Agentes
- [ ] Preciso resolver branches do iPhone? → GitHub Multi-Dispositivo
- [ ] Quero usar GitHub sem git CLI? → Antigravity GitHub

**Se ainda incerto:**
→ Leia decision tree no topo deste arquivo

---

## 📖 REFERÊNCIAS

**Protocolos completos:**
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md]]
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]]
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]]
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_ANTIGRAVITY_GITHUB.md]]

**Logs:**
- [[PC_SYNC_LOG.md]] (raiz) - Multi-PC
- [[SESSION_LOG.md]] (raiz) - Multi-IA

**Quick starts:**
- [[00_SISTEMA/QUICK_START_ANTIGRAVITY_GITHUB.md]]

**MOC Master:**
- [[00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md]]

---

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Última atualização:** 16/Jan/2026

**DECISÃO CLARA = ZERO CONFUSÃO = MÁXIMA EFICIÊNCIA** 🗺️✅
