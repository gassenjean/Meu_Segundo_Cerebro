# PROTOCOLO: Antigravity + GitHub Plugins

**Status**: ✅ Active
**Criado**: 14/Jan/2026
**Versão**: 1.0

---

## 🚀 O Que É Antigravity com GitHub Plugins?

**Antigravity** = Terminal do Gemini 3 Pro com acesso a plugins/MCPs

**Plugins GitHub** = Conexão direta com GitHub API, permitindo:
- ✅ Criar/gerenciar **Pull Requests**
- ✅ Criar/gerenciar **Issues**
- ✅ Revisar código automaticamente
- ✅ Gerenciar **Releases**
- ✅ Configurar **GitHub Actions**
- ✅ Ver estatísticas e insights do repositório
- ✅ Gerenciar webhooks e integrações
- ✅ Criar/editar **Gists**

**Por que isso é poderoso?**
Git CLI (terminal normal) só faz commits/push/pull.
Antigravity com plugins faz **tudo que você faria na interface web do GitHub!**

---

## 🎯 Divisão de Responsabilidades

### Claude Code (Desktop/iPhone)
**Especialidade**: Trabalho técnico direto no código

- ✅ Editar arquivos
- ✅ Escrever código
- ✅ Commits locais
- ✅ Merge de branches
- ✅ Resolver conflitos
- ✅ Pull/Push básico

### Antigravity/Gemini (Terminal com Plugins)
**Especialidade**: Gerenciamento GitHub via API

- ✅ Criar Pull Requests
- ✅ Revisar código automaticamente
- ✅ Criar Issues e gerenciar projeto
- ✅ Automatizar workflows
- ✅ Gerar releases
- ✅ Análise de repositório
- ✅ Estatísticas e insights

---

## 📋 Workflows Recomendados

### Workflow 1: Feature Branch com PR Automático

**Cenário**: Você quer desenvolver uma feature em uma branch e criar PR

**No Claude Code (Desktop):**
```bash
# 1. Criar branch
git checkout -b feature/nova-funcionalidade

# 2. Fazer mudanças
# ... editar arquivos ...

# 3. Commit
git add .
git commit -m "feat: nova funcionalidade X"

# 4. Push da branch
git push -u origin feature/nova-funcionalidade
```

**No Antigravity (Gemini):**
```
Agora use os plugins GitHub para:

1. "Crie um Pull Request da branch feature/nova-funcionalidade para master"

   Title: "feat: Nova Funcionalidade X"
   Description:
   - O que foi feito
   - Por que foi feito
   - Como testar

2. "Adicione labels ao PR: enhancement, priority-high"

3. "Atribua o PR para revisão"

4. "Configure auto-merge quando aprovado"
```

---

### Workflow 2: Issue Tracking com Gemini

**Cenário**: Você encontrou bugs ou tem ideias de features

**No Antigravity (Gemini):**
```
"Crie uma Issue no repositório Meu_Segundo_Cerebro:

Title: [BUG] Problema com sincronização multi-dispositivo
Labels: bug, priority-high
Assignee: gassenjean

Description:
## Descrição
Quando trabalho no iPhone e depois no Desktop, ocorre conflito em...

## Passos para Reproduzir
1. Abrir iPhone
2. Fazer mudanças
3. Abrir Desktop sem pull
4. Conflito

## Comportamento Esperado
Sistema deveria avisar ou auto-pull

## Ambiente
- Desktop: Windows 11
- iPhone: iOS 17
- Claude Code versão X"
```

**Vantagens:**
- Gemini pode criar múltiplas issues de uma vez
- Pode extrair issues de conversas antigas
- Pode priorizar e organizar automaticamente
- Pode vincular issues a PRs

---

### Workflow 3: Code Review Automático

**Cenário**: Você fez um PR e quer review automático

**No Antigravity (Gemini):**
```
"Revise o Pull Request #7 do repositório:

Analise:
1. Qualidade do código
2. Padrões de nomenclatura (NOMENCLATURA.md)
3. Estrutura de arquivos (ESTRUTURA_PROJETOS.md)
4. Comentários necessários
5. Possíveis bugs
6. Performance

Deixe comentários inline no código se necessário."
```

**Gemini pode:**
- Ler o código do PR
- Comparar com padrões do vault
- Identificar problemas
- Sugerir melhorias
- Aprovar ou solicitar mudanças

---

### Workflow 4: Release Management

**Cenário**: Você quer criar uma release do vault

**No Claude Code:**
```bash
# 1. Tag de versão
git tag -a v2.0.77 -m "Release 2.0.77 - Multi-device sync"
git push origin v2.0.77
```

**No Antigravity (Gemini):**
```
"Crie uma Release no GitHub:

Tag: v2.0.77
Title: Meu_Segundo_Cerebro v2.0.77 - Multi-Device Sync

Release Notes:
## ✨ Novidades
- Protocolo multi-dispositivo implementado
- Sincronização iPhone + Desktop + Alienware
- Guia de boas práticas GitHub

## 🐛 Correções
- Conflitos de merge resolvidos
- Long paths habilitados

## 📚 Documentação
- PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md
- Workflows atualizados

## 📊 Estatísticas
- 1.978 arquivos sincronizados
- 17 commits do remoto mesclados
- 4 branches limpas

Arquivos: Anexar CHANGELOG.md se houver"
```

---

### Workflow 5: Análise de Repositório

**No Antigravity (Gemini):**
```
"Analise o repositório Meu_Segundo_Cerebro e me dê:

1. Estatísticas de commits (últimos 30 dias)
2. Principais contribuidores
3. Arquivos mais modificados
4. Branches ativas
5. Issues abertas vs fechadas
6. PRs abertos vs mesclados
7. Linguagens usadas
8. Tamanho do repositório
9. Atividade por dispositivo (se possível identificar)
10. Recomendações de melhoria"
```

**Gemini pode gerar relatórios completos** que você não conseguiria facilmente com git CLI.

---

### Workflow 6: Automação de Backups

**Cenário**: Você quer criar backups automáticos semanais

**No Antigravity (Gemini):**
```
"Configure um GitHub Action para:

1. Rodar toda sexta às 17h
2. Criar uma tag backup-DDMMMYYYY
3. Gerar um relatório de mudanças da semana
4. Criar uma Issue resumindo o progresso
5. Notificar no canal de comunicação

Arquivo: .github/workflows/weekly-backup.yml"
```

---

### Workflow 7: Integração com Projects

**No Antigravity (Gemini):**
```
"Configure um GitHub Project para o repositório:

Colunas:
- 📥 Backlog
- 🎯 Todo
- 🔄 In Progress
- 👀 Review
- ✅ Done

Automatizações:
- Issue criada → Backlog
- PR aberto → In Progress
- PR aprovado → Review
- PR merged → Done

Adicione todas as Issues e PRs existentes ao board."
```

---

### Workflow 8: Gists para Snippets

**No Antigravity (Gemini):**
```
"Crie um Gist público com o conteúdo:

Título: Workflow Git Multi-Dispositivo
Descrição: Comandos essenciais para trabalhar em múltiplos dispositivos

Arquivo: git-multi-device.md
[Conteúdo do checklist do PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]

Adicione ao README do repositório."
```

---

## 🔧 Comandos Específicos Antigravity

### Criar Pull Request
```
"Crie um Pull Request:
- Base: master
- Head: feature/nome
- Title: feat: descrição
- Description: [descrição detalhada]
- Reviewers: [lista]
- Labels: enhancement, documentation"
```

### Gerenciar Issues
```
"Liste todas as Issues abertas com label 'bug'"
"Crie Issue: [título] com labels [x,y,z]"
"Feche Issue #X com comentário 'Resolvido em commit ABC'"
"Mova Issue #X para milestone 'Q1 2026'"
```

### Code Review
```
"Revise PR #X focando em:
- Performance
- Segurança
- Boas práticas
Deixe comentários específicos no código."
```

### Releases
```
"Crie Release v2.0.77 com notas baseadas nos últimos commits"
"Liste todas as releases e suas datas"
"Baixe assets da release v2.0.76"
```

### Estatísticas
```
"Mostre estatísticas do repositório dos últimos 30 dias"
"Quais arquivos foram mais modificados em 2026?"
"Gere um relatório de atividade para compartilhar"
```

### GitHub Actions
```
"Liste todos os workflows ativos"
"Mostre logs do último run do workflow 'backup'"
"Desabilite workflow 'test' temporariamente"
"Crie workflow para [tarefa específica]"
```

---

## 🎨 Templates Recomendados

### Template: Pull Request
```markdown
## 📝 Descrição
[Descrição clara do que foi feito]

## 🎯 Motivação
[Por que essa mudança foi necessária]

## 🧪 Como Testar
1. [Passo 1]
2. [Passo 2]

## 📸 Screenshots (se aplicável)
[Imagens]

## ✅ Checklist
- [ ] Código segue padrões (NOMENCLATURA.md)
- [ ] Arquivos na estrutura correta
- [ ] Testado localmente
- [ ] Documentação atualizada
- [ ] Sem conflitos com master

## 🔗 Issues Relacionadas
Closes #X
```

### Template: Issue (Bug)
```markdown
## 🐛 Descrição do Bug
[Descrição clara e concisa]

## 📝 Passos para Reproduzir
1. [Passo 1]
2. [Passo 2]
3. [Erro acontece]

## ✅ Comportamento Esperado
[O que deveria acontecer]

## ❌ Comportamento Atual
[O que está acontecendo]

## 🖥️ Ambiente
- Dispositivo: [Desktop/iPhone/Alienware]
- OS: [Windows 11/iOS 17]
- Claude Code versão: [X]

## 📸 Screenshots
[Se aplicável]

## 💡 Possível Solução
[Se você tiver ideia de como resolver]
```

### Template: Issue (Feature)
```markdown
## ✨ Feature Request

### 📝 Problema Atual
[Qual problema isso resolve?]

### 💡 Solução Proposta
[Como você imagina a feature?]

### 🎯 Casos de Uso
1. [Uso 1]
2. [Uso 2]

### 🔄 Alternativas Consideradas
[Outras formas de resolver isso]

### 📚 Recursos Adicionais
[Links, referências, exemplos]

### 🎨 UI/UX (se aplicável)
[Mockups, wireframes]
```

---

## 🚀 Workflows Avançados

### Workflow: Feature Branch com CI/CD

**1. No Claude Code (criar branch):**
```bash
git checkout -b feature/automation
# ... fazer mudanças ...
git add .
git commit -m "feat: adicionar automação X"
git push -u origin feature/automation
```

**2. No Antigravity (criar PR com CI):**
```
"Crie PR da branch feature/automation:
- Title: feat: Adicionar Automação X
- Description: [usar template]
- Labels: enhancement, automation
- Reviewers: auto
- Configure checks obrigatórios:
  * Lint código
  * Validar nomenclatura
  * Verificar estrutura de pastas"
```

**3. Antigravity monitora:**
```
"Monitore PR #X e me notifique quando:
- Checks passarem
- Houver conflitos
- Receber comentários
- Estar pronto para merge"
```

**4. Auto-merge quando aprovado:**
```
"Configure auto-merge no PR #X:
- Merge strategy: squash
- Delete branch após merge
- Atualizar Issues relacionadas"
```

---

### Workflow: Análise Semanal Automática

**Todo domingo 20h, Antigravity executa:**

1. **Coleta dados:**
```
- Commits da semana
- PRs abertos/fechados
- Issues criadas/resolvidas
- Arquivos mais modificados
- Contribuições por dispositivo
```

2. **Gera relatório:**
```markdown
# 📊 Relatório Semanal - DD/MM/YYYY

## 🎯 Produtividade
- ✅ X commits realizados
- 📝 Y arquivos modificados
- 🔀 Z PRs mesclados
- 🐛 W bugs corrigidos

## 📱 Por Dispositivo
- Desktop: X commits
- iPhone: Y commits
- Alienware: Z commits

## 🏆 Conquistas
- [Maior milestone atingido]
- [Feature importante]

## ⚠️ Alertas
- [Branches antigas não mescladas]
- [Issues abertas há >7 dias]

## 🎯 Próxima Semana
- [Prioridades]
```

3. **Cria Issue com relatório:**
```
"Crie Issue:
Title: 📊 Relatório Semanal - DD/MM/YYYY
Label: report, weekly
Assignee: gassenjean
[Conteúdo do relatório]"
```

---

### Workflow: Sincronização Inteligente

**Antigravity pode monitorar e alertar:**

```
"Configure monitoramento:

1. Se branch 'claude/*' for criada:
   → Notificar: 'Nova branch do iPhone detectada'
   → Sugerir merge no próximo acesso do Desktop

2. Se houver commits no master sem pull local:
   → Notificar: 'Master está X commits à frente'
   → Lembrar de fazer pull

3. Se houver conflitos em PR:
   → Notificar imediatamente
   → Sugerir estratégia de resolução

4. Se branch estiver >7 dias sem atividade:
   → Notificar: 'Branch feature/X está inativa'
   → Sugerir merge ou delete"
```

---

## 🎓 Casos de Uso Práticos

### Caso 1: Organizar Backlog de Ideias

**Você tem 20 ideias espalhadas em notas. Antigravity organiza:**

```
"Leia o arquivo 00_SISTEMA/planejamento/IDEIAS_FUTURAS.md

Para cada ideia:
1. Crie uma Issue no GitHub
2. Classifique por:
   - Categoria (feature/enhancement/research)
   - Prioridade (low/medium/high)
   - Complexidade (simple/medium/complex)
3. Adicione ao Project Board na coluna Backlog
4. Vincule Issues relacionadas

Gere um resumo quando terminar."
```

---

### Caso 2: Code Review por Padrões

**Antigravity revisa PR seguindo padrões do vault:**

```
"Revise PR #X seguindo:

1. NOMENCLATURA.md
   - Todos os arquivos seguem CamelCase?
   - Prefixos corretos (MOC_, TEMPLATE_, etc)?
   - Nomes < 60 caracteres?

2. ESTRUTURA_PROJETOS.md
   - Arquivos nas pastas corretas?
   - README.md presente?
   - STATUS_ATUAL.md atualizado?

3. PROTOCOLO_CRIACAO_ARQUIVOS.md
   - MOCs atualizados?
   - Padrões respeitados?

Deixe comentários específicos no código."
```

---

### Caso 3: Release Notes Automáticas

**Antigravity gera release notes baseado em commits:**

```
"Gere Release Notes para v2.0.77:

Analise commits desde v2.0.76:
- Agrupe por tipo (feat/fix/docs/chore)
- Liste mudanças importantes
- Mencione breaking changes
- Inclua estatísticas (arquivos, linhas)
- Liste contribuidores
- Adicione links para Issues/PRs

Formato markdown para copiar no GitHub Release."
```

---

### Caso 4: Detectar Duplicação de Código

**Antigravity analisa repositório:**

```
"Analise o repositório buscando:

1. Arquivos duplicados ou muito similares
2. Código copiado/colado
3. Funções que poderiam ser utilitários
4. Documentação duplicada

Para cada duplicação encontrada:
- Mostre onde está
- Sugira como consolidar
- Crie Issue se necessário"
```

---

## 📊 Métricas e Dashboards

### Dashboard Pessoal (Gemini cria)

```
"Crie um dashboard markdown em 00_SISTEMA/DASHBOARD_GITHUB.md:

## 📊 Dashboard GitHub - Atualizado DD/MM/YYYY

### 🎯 Overview
- Total commits: X
- Total Issues: Y (Z abertas)
- Total PRs: W (Q abertos)
- Contribuidores: N

### 📈 Últimos 30 Dias
- Commits: X (+Y% vs mês anterior)
- Issues resolvidas: Z
- PRs merged: W
- Arquivos modificados: Q

### 🏆 Top 10 Arquivos Mais Modificados
1. [arquivo] - X modificações
2. [arquivo] - Y modificações
...

### 🚀 Produtividade por Dispositivo
- 🖥️ Desktop: X commits (Y%)
- 📱 iPhone: Z commits (W%)
- 💻 Alienware: Q commits (R%)

### ⚠️ Alertas
- [ ] Branches antigas: [lista]
- [ ] Issues >30 dias: [lista]
- [ ] PRs pendentes: [lista]

### 🎯 Metas Q1 2026
- [ ] Meta 1 (X% completo)
- [ ] Meta 2 (Y% completo)

---
*Atualizado automaticamente via Antigravity*"
```

---

## 🔐 Segurança e Boas Práticas

### Configurações Recomendadas

**No GitHub (via Antigravity):**

```
"Configure as seguintes proteções no repositório:

1. Branch Protection (master):
   - Require pull request reviews: 0 (solo dev)
   - Require status checks to pass: true
   - Require branches to be up to date: true
   - Include administrators: false

2. Settings:
   - Automatically delete head branches: true
   - Allow squash merging: true
   - Allow merge commits: false (manter histórico limpo)

3. Notifications:
   - Watch: All Activity
   - Email: On
   - Push notifications (mobile): On"
```

### Secrets e Tokens

**NUNCA commite:**
- API tokens
- Senhas
- Chaves SSH
- Credentials

**Use GitHub Secrets (via Antigravity):**
```
"Configure secrets no repositório:
- ANTHROPIC_API_KEY
- GEMINI_API_KEY
- DEPLOY_TOKEN

Adicione ao .gitignore:
- .env
- credentials.json
- *.key
- secrets/
```

---

## 🎯 Resumo Executivo

### Claude Code → Código
- Editar arquivos
- Commits locais
- Merge branches
- Pull/Push básico

### Antigravity → GitHub API
- Criar PRs
- Gerenciar Issues
- Code Review
- Releases
- Automações
- Analytics
- Project Management

### Workflow Ideal

1. **Trabalho técnico** → Claude Code
2. **Gerenciamento GitHub** → Antigravity
3. **Sincronização** → Protocolo multi-dispositivo
4. **Automações** → GitHub Actions + Antigravity monitoring

---

## 📚 Próximos Passos

1. **Teste workflows básicos** (criar PR, Issue)
2. **Configure automações** (backup semanal)
3. **Crie dashboard** de métricas
4. **Implemente CI/CD** simples
5. **Automatize code review**

---

## 🔗 Referências

- `PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md` - Workflow git multi-device
- `PROTOCOLO_SINCRONIZACAO_AGENTES.md` - Sync Claude/Gemini
- `.gemini/GEMINI.md` - Configuração Antigravity
- `SESSION_LOG.md` - Log de sincronização

---

**🤖 Generated with Claude Code**
**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
