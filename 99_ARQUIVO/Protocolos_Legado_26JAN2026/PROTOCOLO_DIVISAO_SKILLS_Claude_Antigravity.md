---
created: 2026-01-19T10:35
updated: 2026-01-26T11:16
---
# PROTOCOLO: Divisão de Responsabilidades - Skills Claude vs Antigravity

**Divisão Clara: Quem Cria Qual Skill**

**Criado:** 18/JAN/2026
**Versão:** 1.0
**Status:** ✅ ATIVO E OBRIGATÓRIO
**Propósito:** Definir claramente qual IA cria qual tipo de skill

---

## 🎯 PRINCÍPIO FUNDAMENTAL

> **"Claude Code cria skills Claude Code.**
> **Gemini/Antigravity cria skills Antigravity."**

**Motivo:** Cada IA conhece profundamente a arquitetura da sua própria plataforma.

---

## 📐 MATRIZ DE DECISÃO

### Claude Code Cria Skills Claude Code Quando:

| Critério | Explicação | Exemplo |
|----------|------------|---------|
| **Conhecimento Procedural** | Instruções de workflow, guidelines, best practices | Skill de code review, skill de planejamento |
| **Integração Vault** | Skills que precisam conhecer estrutura do vault | Marie Kondo, validate, atualizar-status |
| **Raciocínio Complexo** | Skills que exigem decisões estratégicas | Névoa (orquestração), Claude Architect |
| **Contexto Vault** | Skills que referenciam CLAUDE.md, MOCs, protocolos | Qualquer skill específica deste vault |
| **References Pesadas** | Skills com muita documentação em references/ | Skills com >10k palavras em references |

### Gemini/Antigravity Cria Skills Antigravity Quando:

| Critério | Explicação | Exemplo |
|----------|------------|---------|
| **Scripts Executáveis** | Skills com código Python/Bash embutido | Reddit scraper, PDF processor |
| **Automação Repetitiva** | Tasks 100% automatizáveis sem decisão humana | Formatação automática, limpeza de arquivos |
| **Processamento Massa** | Operar em múltiplos arquivos/dados | Bulk summarization, batch translation |
| **Execução Direta** | Quando o código já está pronto e só precisa executar | Status updater script, file organizer |
| **IDE-Specific** | Skills que aproveitam features do Antigravity IDE | Task Inbox skills, Browser sub-agent skills |

---

## 🗂️ LOCALIZAÇÃO DAS SKILLS

### Claude Code Skills

**Localização:** `.claude/skills/`

**Estrutura:**
```
.claude/skills/
├── skill-creator/           ← Meta-skill
├── brand-guidelines/
├── code-review/
├── marie-kondo/
├── nevoa/
├── elena/
├── pedro/
├── alan/
├── lucas/
├── dr-green/
└── validate/
```

**Criação:**
- **Quem cria:** Claude Code (você)
- **Quando:** Durante sessão Claude Code
- **Como:** Usando `scripts/init_skill.py` ou manualmente
- **Validação:** Usando `scripts/package_skill.py`

### Antigravity Skills

**Localização:** `.gemini/skills/` (NOVO!)

**Estrutura:**
```
.gemini/skills/
├── gemini-skill-creator/    ← Meta-skill (Gemini cria)
├── brand-automation/        ← Automação (Gemini cria)
├── reddit-scraper/          ← Script executável (Gemini cria)
├── bulk-processor/          ← Processamento massa (Gemini cria)
├── file-organizer/          ← Automação (Gemini cria)
└── status-updater/          ← Script automático (Gemini cria)
```

**Criação:**
- **Quem cria:** Gemini/Antigravity
- **Quando:** Via interface Antigravity ou comando Gemini CLI
- **Como:** Usando Gemini Skill Creator (meta-skill)
- **Validação:** Teste em nova conversa Antigravity (zero contexto)

---

## 🔀 WORKFLOW DE CRIAÇÃO

### Criar Skill Claude Code (Claude Creates)

```
1. Usuário solicita skill conhecimento/procedural
   ↓
2. Claude identifica: "É skill Claude Code"
   ↓
3. Claude usa skill-creator ou cria manualmente
   ↓
4. Claude popula SKILL.md + scripts/ + references/ + assets/
   ↓
5. Claude testa skill
   ↓
6. Claude empacota com scripts/package_skill.py
   ↓
7. Claude atualiza MOC_Skills_BiIA.md
   ↓
8. Skill disponível em .claude/skills/
```

### Criar Skill Antigravity (Gemini Creates)

```
1. Usuário solicita skill automação/executável
   ↓
2. Claude identifica: "É skill Antigravity"
   ↓
3. Claude delega para Gemini via /gemini ou SESSION_LOG.md
   ↓
4. Gemini cria skill usando Gemini Skill Creator
   ↓
5. Gemini testa em nova conversa (zero contexto)
   ↓
6. Gemini exporta skill (se possível)
   ↓
7. Gemini atualiza SESSION_LOG.md com status
   ↓
8. Claude valida e atualiza MOC_Skills_BiIA.md
   ↓
9. Skill disponível em .gemini/skills/
```

---

## 📊 SKILLS EXISTENTES - ANÁLISE DE COMPATIBILIDADE

### Skills Claude Code (19 atuais)

| Skill | Tipo | Pode virar Antigravity? | Prioridade Conversão |
|-------|------|------------------------|---------------------|
| `/skill-creator` | Meta-skill | ⚠️ Parcial (adaptar) | ALTA |
| `/nevoa` | Orquestração | ❌ (específico Claude) | N/A |
| `/claude-architect` | Guidelines | ❌ (específico Claude) | N/A |
| `/marie-kondo` | Organização | ✅ SIM (automação) | ⭐⭐⭐⭐⭐ ALTA |
| `/elena` | Conhecimento TDAH | ⚠️ Parcial (referencias) | MÉDIA |
| `/pedro` | Conhecimento Marketing | ⚠️ Parcial (referencias) | MÉDIA |
| `/alan` | Conhecimento IA | ⚠️ Parcial (referencias) | MÉDIA |
| `/lucas` | Conhecimento DeFi | ⚠️ Parcial (referencias) | MÉDIA |
| `/dr-green` | Conhecimento Cultivo | ⚠️ Parcial (referencias) | MÉDIA |
| `/validate` | Validação | ✅ SIM (script) | ⭐⭐⭐⭐ ALTA |
| `/gemini` | Delegação | ✅ SIM (orquestração) | ⭐⭐⭐ MÉDIA |
| `/ultra-think` | Raciocínio | ❌ (específico Claude) | N/A |
| `/sync` | Sincronização | ✅ SIM (automação) | ⭐⭐⭐⭐⭐ ALTA |
| `/mapa` | Carrega índice | ✅ SIM (script) | ⭐⭐⭐⭐ ALTA |
| `/learn` | Contexto | ⚠️ Parcial (referências) | BAIXA |
| `/work` | Contexto | ⚠️ Parcial (referências) | BAIXA |
| `/atualizar-status` | Automação | ✅ SIM (script) | ⭐⭐⭐⭐⭐ ALTA |
| `/limpeza-raiz-vault` | Automação | ✅ SIM (script) | ⭐⭐⭐⭐⭐ ALTA |
| `/devocionais-rpsp` | Conteúdo | ⚠️ Parcial (templates) | MÉDIA |
| `/kabak` | Projeto específico | ⚠️ Parcial (templates) | MÉDIA |
| `/kabak-agent` | Projeto específico | ⚠️ Parcial (templates) | MÉDIA |
| `/github-sync` | Automação | ✅ SIM (script) | ⭐⭐⭐⭐ ALTA |

**Legenda:**
- ✅ SIM = Deve criar versão Antigravity (automação)
- ⚠️ Parcial = Pode adaptar referências, mas core é conhecimento
- ❌ = Específico de plataforma (manter só Claude)

### Top 7 Skills para Conversão (Prioridade)

**Criar no Antigravity (Gemini cria):**

1. **`marie-kondo`** → Antigravity Vault Organizer
   - Script automático de organização
   - Movimentação de arquivos
   - Limpeza de duplicatas

2. **`atualizar-status`** → Antigravity Status Updater
   - Script que atualiza STATUS_VAULT.md automaticamente
   - Coleta métricas do vault
   - Gera relatórios

3. **`sync`** → Antigravity Session Logger
   - Automação de SESSION_LOG.md
   - Template de comunicação bi-IA
   - Timestamps automáticos

4. **`validate`** → Antigravity File Validator
   - Script de validação de nomenclatura
   - Checagem de estrutura
   - Relatório de conformidade

5. **`limpeza-raiz-vault`** → Antigravity Root Cleaner
   - Limpeza automática de raiz
   - Identificação de duplicatas
   - Movimentação para pastas corretas

6. **`github-sync`** → Antigravity GitHub Manager
   - Automação de commits
   - Push/pull automático
   - Resolução de conflitos simples

7. **`mapa`** → Antigravity Vault Indexer
   - Geração automática de índice
   - Atualização de MOCs
   - Grafo de dependências

---

## 🎯 REGRAS DE DECISÃO RÁPIDA

### Pergunte-se:

**1. A skill precisa RACIOCINAR ou EXECUTAR?**
- Raciocinar → Claude Code
- Executar → Antigravity

**2. A skill tem CÓDIGO PRONTO ou INSTRUÇÕES?**
- Código pronto → Antigravity
- Instruções procedurais → Claude Code

**3. A skill é ESPECÍFICA DO VAULT ou GENÉRICA?**
- Específica vault (conhece CLAUDE.md) → Claude Code
- Genérica (funciona em qualquer projeto) → Pode ser Antigravity

**4. A skill processa UM ARQUIVO ou MÚLTIPLOS?**
- Um arquivo (decisões) → Claude Code
- Múltiplos (batch) → Antigravity

**5. Usuário quer CONSISTÊNCIA ou ADAPTABILIDADE?**
- Consistência repetível → Antigravity
- Adaptabilidade contextual → Claude Code

---

## 🔄 SKILLS SINCRONIZADAS (Ambas Plataformas)

Algumas skills podem existir em AMBAS plataformas com propósitos complementares:

### Exemplo: Brand Guidelines

**Claude Code Skill: `brand-guidelines`**
- **Propósito:** Instruções de COMO aplicar marca
- **Conteúdo:** Guidelines, voice & tone, quando usar cada elemento
- **Uso:** Claude lê e aplica com julgamento contextual

**Antigravity Skill: `brand-automation`**
- **Propósito:** EXECUTAR aplicação automática de marca
- **Conteúdo:** Scripts que aplicam cores, fontes, templates
- **Uso:** Gemini executa script → resultado consistente

### Exemplo: Code Review

**Claude Code Skill: `code-review`**
- **Propósito:** COMO revisar código (metodologia)
- **Conteúdo:** Checklist, best practices, o que procurar
- **Uso:** Claude analisa e sugere melhorias

**Antigravity Skill: `code-formatter`**
- **Propósito:** FORMATAR código automaticamente
- **Conteúdo:** Script de formatação (prettier, black, etc)
- **Uso:** Gemini executa → código formatado

---

## 📋 CHECKLIST DE CRIAÇÃO

### Antes de Criar Skill (Decisão)

- [ ] Identificar tipo: Conhecimento vs Automação
- [ ] Escolher plataforma: Claude Code vs Antigravity
- [ ] Verificar se skill similar já existe
- [ ] Confirmar com usuário se necessário

### Durante Criação (Claude Code)

- [ ] Usar `scripts/init_skill.py` se aplicável
- [ ] Preencher SKILL.md (YAML frontmatter + instruções)
- [ ] Adicionar scripts/ se necessário
- [ ] Adicionar references/ se necessário
- [ ] Adicionar assets/ se necessário
- [ ] Testar skill em nova conversa
- [ ] Empacotar com `scripts/package_skill.py`
- [ ] Atualizar MOC_Skills_BiIA.md

### Durante Criação (Antigravity - Gemini faz)

- [ ] Delegar para Gemini via /gemini ou SESSION_LOG
- [ ] Gemini usa Gemini Skill Creator
- [ ] Gemini popula skill.md + scripts/
- [ ] Gemini testa em nova conversa (zero contexto)
- [ ] Gemini exporta skill
- [ ] Gemini atualiza SESSION_LOG.md
- [ ] Claude valida e atualiza MOC_Skills_BiIA.md

---

## 🚨 ANTI-PATTERNS

### ❌ NUNCA FAZER

1. **Claude tentando criar Antigravity Skill**
   - Claude não conhece arquitetura interna do Antigravity
   - Resultado: Skill incompatível ou subótima
   - Solução: Delegar para Gemini

2. **Gemini tentando criar Claude Code Skill**
   - Gemini não tem contexto profundo do vault
   - Gemini não conhece CLAUDE.md e protocolos
   - Solução: Deixar Claude criar

3. **Duplicar skills em ambas plataformas sem motivo**
   - Causa: Manutenção duplicada
   - Solução: Uma skill por plataforma, OU skills complementares

4. **Criar skill sem testar**
   - Causa: Skill quebrada vai para produção
   - Solução: Sempre testar em conversa nova (zero contexto)

5. **Não atualizar MOC após criar skill**
   - Causa: Skill "perdida", ninguém sabe que existe
   - Solução: SEMPRE atualizar MOC_Skills_BiIA.md

---

## ✅ BEST PRACTICES

### Progressive Complexity

**Começar simples:**
1. Criar skill básica (mínimo viável)
2. Testar em casos reais
3. Iterar baseado em feedback
4. Adicionar complexidade gradualmente

### Documentation First

**Antes de escrever código:**
1. Definir claramente: O que a skill faz?
2. Quando deve ser usada?
3. Exemplos concretos de uso
4. Depois escrever implementação

### Test in Isolation

**Validar sem contexto:**
- Criar nova conversa/sessão
- Testar skill sem contexto anterior
- Verificar se ativa corretamente
- Confirmar output esperado

### Version Control

**Sempre versionar:**
- Skills Claude Code → Git (`.claude/skills/`)
- Skills Antigravity → Exportar e versionar (`.gemini/skills/`)
- Changelog em cada skill
- Tag de versão no frontmatter

---

## 📖 EXEMPLOS PRÁTICOS

### Exemplo 1: Usuário pede "Skill de organização automática"

**Análise:**
- Tipo: Automação (movimentação de arquivos)
- Plataforma: Antigravity (script executável)

**Ação:**
```
Claude: "Esta é uma skill Antigravity. Vou delegar para Gemini."
→ Atualiza SESSION_LOG.md
→ Gemini cria `vault-organizer` skill
→ Gemini testa
→ Claude valida e atualiza MOC
```

### Exemplo 2: Usuário pede "Skill de code review guidelines"

**Análise:**
- Tipo: Conhecimento procedural (como revisar)
- Plataforma: Claude Code (instruções)

**Ação:**
```
Claude: "Esta é uma skill Claude Code. Vou criar agora."
→ Claude usa skill-creator
→ Claude popula SKILL.md com guidelines
→ Claude adiciona references/ com best practices
→ Claude testa
→ Claude empacota e atualiza MOC
```

### Exemplo 3: Usuário pede "Skill de brand guidelines"

**Análise:**
- Tipo: Híbrido (conhecimento + automação)
- Plataforma: AMBAS (complementares)

**Ação:**
```
Claude: "Vou criar duas skills complementares:"

1. Claude Code: brand-guidelines
   - Instruções de COMO aplicar marca
   - Voice & tone
   - Quando usar cada elemento

2. Antigravity: brand-automation (delegar Gemini)
   - Script que APLICA cores, fontes
   - Templates automatizados
   - Geração de assets

→ Claude cria brand-guidelines
→ Claude delega brand-automation para Gemini
→ Ambas skills registradas em MOC
```

---

## 🗺️ ROADMAP DE IMPLEMENTAÇÃO

### Fase 1: Fundação (Esta Semana)

- [x] Criar PROTOCOLO_DIVISAO_SKILLS_Claude_Antigravity.md (este arquivo)
- [ ] Criar pasta `.gemini/skills/` no vault
- [ ] Delegar criação de `gemini-skill-creator` para Gemini
- [ ] Criar MOC_Skills_BiIA.md (índice master)
- [ ] Testar primeira skill Antigravity

### Fase 2: Conversão Top 5 (Próximas 2 Semanas)

- [ ] marie-kondo → vault-organizer (Gemini cria)
- [ ] atualizar-status → status-updater (Gemini cria)
- [ ] sync → session-logger (Gemini cria)
- [ ] validate → file-validator (Gemini cria)
- [ ] limpeza-raiz-vault → root-cleaner (Gemini cria)

### Fase 3: Sincronização (Semana 3-4)

- [ ] Criar PROTOCOLO_SINCRONIZACAO_SKILLS.md
- [ ] Documentar workflow de handoff
- [ ] Templates de comunicação bi-IA
- [ ] Automação de updates em MOC

### Fase 4: Escala (Mês 2)

- [ ] Converter skills restantes (se aplicável)
- [ ] Criar biblioteca compartilhável
- [ ] Sistema de monitoramento de updates
- [ ] Métricas de uso e eficiência

---

## 📚 REFERÊNCIAS

### Documentação Sistema

- [[00_SISTEMA/ANALISES/ANALISE_Antigravity_Skills_Integracao_Sistema_BiIA.md]] - Análise completa
- [[.claude/skills/skill-creator/SKILL.md]] - Skill Creator (Claude)
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]] - Handoff bi-IA
- [[SESSION_LOG.md]] - Comunicação Claude ↔ Gemini
- [[CLAUDE.md]] - Sistema bi-IA

### Fontes Externas

- Vídeo: "Antigravity Skills are a Cheat Code" - Jack Roberts
- Transcrição: `Antigravity_Skills_are_a_Cheat_Code__NEW_System_.pdf`
- Claude Code Skills Docs (oficial Anthropic)
- Antigravity Skills Docs (pesquisa Gemini em andamento)

---

## 🆘 TROUBLESHOOTING

### "Não sei se skill deve ser Claude ou Antigravity"

**Solução:**
1. Ler seção "Matriz de Decisão" acima
2. Perguntar-se as "5 Perguntas Rápidas"
3. Se ainda não souber → Começar com Claude Code (sempre funciona)

### "Skill Antigravity não está ativando"

**Possíveis causas:**
- Descrição no skill.md não está clara
- Linguagem natural do prompt não combina
- Skill não foi testada em nova conversa
- Gemini não reconhece o padrão

**Solução:**
- Melhorar descrição (mais específica)
- Testar com prompt explícito: "use skill X"
- Verificar se skill está na pasta correta

### "Skill Claude Code muito grande (>10k palavras)"

**Solução:**
- Mover conteúdo para references/
- Criar sub-skills (hierarquia)
- Considerar criar versão Antigravity (se aplicável)

---

## ✅ CONCLUSÃO

**Regra de Ouro:**

> **Claude Code cria Claude Code Skills (conhecimento).**
> **Gemini cria Antigravity Skills (automação).**

**Quando em dúvida:**
1. Perguntar ao usuário
2. Começar com Claude Code (sempre seguro)
3. Migrar para Antigravity depois se fizer sentido

**Objetivo:**
- Máxima eficiência
- Zero duplicação desnecessária
- Cada IA no seu sweet spot

---

**Versão:** 1.0
**Criado:** 18/JAN/2026
**Status:** ✅ ATIVO E OBRIGATÓRIO
**Próxima Revisão:** Após criar primeiras 5 skills Antigravity

**CLAREZA NA DIVISÃO = EFICIÊNCIA MÁXIMA** 🎯✅
