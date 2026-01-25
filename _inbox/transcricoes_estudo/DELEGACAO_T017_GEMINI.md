# DELEGAÇÃO T017 - EXTRAÇÃO MASSIVA DE BOAS PRÁTICAS IA

**De:** Névoa (iOS Master)
**Para:** Gemini 3 Pro (Antigravity)
**Prioridade:** ALTA
**Data:** 25/Jan/2026 12:30
**Prazo:** Sem pressa - QUALIDADE > VELOCIDADE

---

## MISSÃO

Extrair TODO o conhecimento acionável dos 3 PDFs de transcrições para potencializar o sistema Bi-IA (Claude + Gemini). Você tem a vantagem de 1M de tokens - USE-A para fazer uma extração que seria impossível para o Claude fazer de uma vez.

**Objetivo final:** Criar documentação tão boa que qualquer agente do sistema possa consultar e aplicar imediatamente.

---

## CONTEXTO DO SISTEMA BI-IA

Nosso sistema funciona assim:

```text
CLAUDE CODE (Névoa)          GEMINI (Antigravity)
├── Estratégia               ├── Execução bulk
├── Decisões críticas        ├── Processamento longo
├── Arquitetura              ├── Extração massiva
├── Quality Gate             ├── 1M tokens (free tier)
└── Curadoria final          └── Workflows repetitivos
```

**O que estamos construindo:** Um sistema de agentes iOS (Alan Nicolas) onde a Névoa orquestra gerentes especializados. Estas transcrições contêm práticas que vão TURBINAR esse sistema.

---

## ARQUIVOS FONTE (3 PDFs)

### PDF 1: Antigravity Skills (Jack Roberts)
- **Arquivo:** `Antigravity_Skills_are_a_Cheat_Code__NEW_System_ (1).pdf`
- **Foco:** Como criar e usar Skills no Gemini/Antigravity
- **Relevância:** ALTA para você (Gemini) - é sobre VOCÊ

### PDF 2: 13 Dicas do Criador do Claude Code (Boris)
- **Arquivo:** `Como_o_criador_do_Claude_Code_usa_a_pr_pria_ferramenta___13_ (2).pdf`
- **Foco:** Práticas do próprio criador da ferramenta
- **Relevância:** CRÍTICA para Claude/Névoa

### PDF 3: Context Engineering (Valdemar Neto)
- **Arquivo:** `Por_que_IA_falha_em_codebases_grandes__e_como_eu_resolvi_iss.pdf`
- **Foco:** Gestão de contexto, RPI Framework
- **Relevância:** CRÍTICA para arquitetura de prompts

---

## FRAMEWORK DE EXTRAÇÃO

Para CADA conceito encontrado, extraia:

### Estrutura Atômica de Conceito

```markdown
## [NOME_DO_CONCEITO]

**Fonte:** [Autor] - [PDF]
**Categoria:** [Framework | Tática | Princípio | Ferramenta | Workflow]

### O Que É
[Explicação clara em 2-3 frases]

### Por Que Importa
[Problema que resolve]

### Como Aplicar
[Passos práticos numerados]

### Exemplo Concreto
[Caso de uso real mencionado ou inferido]

### Aplicação no Bi-IA
[Como isso se aplica ao nosso sistema Claude + Gemini]

### Tags
#[categoria] #[ferramenta] #[contexto]
```

---

## ENTREGAS ESPERADAS (4 Arquivos)

### 1. `CONCEITOS_Antigravity_Skills.md`
Localização: `01_CONHECIMENTO/Boas_Praticas_IA/`

Extrair do PDF 1:
- [ ] Definição de Skill vs MCP (diferença clara)
- [ ] Claude (conhecimento) vs Antigravity (automação) - analogia do chef
- [ ] Skill Creator (meta-skill)
- [ ] Brand Design Skill (sub-skills arquitetura)
- [ ] Troubleshooting Skill
- [ ] Scripts executáveis como Skills
- [ ] Quando criar uma Skill (gatilho: repetição)
- [ ] Como Gemini decide qual Skill usar
- [ ] Economia de tokens com Skills

### 2. `CONCEITOS_Claude_Code_Boris.md`
Localização: `01_CONHECIMENTO/Boas_Praticas_IA/`

Extrair do PDF 2 (TODAS as 13 dicas detalhadas):
- [ ] Dica 1: 5 Claudes em paralelo (terminal numerado)
- [ ] Dica 2: 5 locais + 5-10 cloud (até 15 instâncias)
- [ ] Dica 3: Opus 4.5 + Thinking para tudo
- [ ] Dica 4: CLAUDE.md compartilhado no repo
- [ ] Dica 5: @Claude em code reviews
- [ ] Dica 6: Plan Mode (Shift Tab 2x) antes de tudo
- [ ] Dica 7: Slash commands para tarefas repetitivas
- [ ] Dica 8: Sub-agents específicos (Code Simplifier, Verify App)
- [ ] Dica 9: Hook post-tool-use para formatação
- [ ] Dica 10: NÃO usar dangerouslySkipPermissions
- [ ] Dica 11: Integração com todas ferramentas (Slack, BigQuery, Sentry)
- [ ] Dica 12: Background agents para long tasks
- [ ] Dica 13: Feedback loops (2-3x qualidade) - A MAIS IMPORTANTE

### 3. `CONCEITOS_Context_Engineering_RPI.md`
Localização: `01_CONHECIMENTO/Boas_Praticas_IA/`

Extrair do PDF 3:
- [ ] Janela de contexto (Smart Zone vs Dumb Zone)
- [ ] Regra dos 40% (limite seguro)
- [ ] Progressive Disclosure (definição + aplicação)
- [ ] On-Demand Loading (definição + aplicação)
- [ ] Framework RPI completo:
  - Research: quando usar, como fazer
  - Plan: importância, estrutura, validação
  - Implement: execução com contexto mínimo
- [ ] Memória de longo prazo (salvar em markdown)
- [ ] Quebrar planos grandes em subplanos
- [ ] Spec Driven vs RPI (esclarecimento)
- [ ] Sub-agents para tarefas específicas (não genéricos)

### 4. `_MOC_Boas_Praticas_IA.md`
Localização: `01_CONHECIMENTO/Boas_Praticas_IA/`

MOC unificando os 3 arquivos com:
- Índice navegável
- Conexões entre conceitos
- Aplicação prática no Bi-IA
- Checklist de implementação

---

## CONEXÕES A FAZER

Ao extrair, relacione com conceitos que JÁ TEMOS no vault:

| Conceito Novo | Relacionar Com |
| ------------- | -------------- |
| Skills (Antigravity) | iOS Framework (Alan Nicolas) |
| Plan Mode | Ralph Loop (Quality Gate) |
| Feedback Loops | Ralph ("não seja o imbecil que aperta sim") |
| Sub-agents | Hierarquia iOS (Gerentes) |
| CLAUDE.md compartilhado | Nosso CLAUDE.md |
| RPI Framework | Método MAPA |
| Progressive Disclosure | Método 5C |

---

## REGRAS DE QUALIDADE

### FAÇA
- Extraia TUDO que for acionável
- Use exemplos concretos dos vídeos
- Mantenha citações relevantes entre aspas
- Conecte com nosso sistema existente
- Seja EXTENSO - tokens não são problema para você

### NÃO FAÇA
- Não resuma demais (queremos profundidade)
- Não invente informações não presentes nos PDFs
- Não pule conceitos "óbvios" (documente tudo)
- Não use formatação inconsistente

### LINTING MARKDOWN (OBRIGATÓRIO)
- Code blocks COM linguagem (`text`, `markdown`, `bash`)
- Headers com linha vazia antes/depois
- Tabelas com espaços nas pipes `| Texto |`
- Listas com `-` (não misturar com `*`)

---

## QUALITY GATE (Ralph Loop)

Antes de entregar, verifique:

```text
□ COMPLETO? Todos os conceitos dos 3 PDFs extraídos?
□ CORRETO? Segue estrutura atômica definida?
□ ÚTIL? Qualquer agente consegue aplicar imediatamente?
□ LIMPO? Sem duplicatas, sem TODOs, markdown válido?
□ CONECTADO? Relacionado com conceitos existentes do vault?
```

---

## APÓS CONCLUSÃO

1. Criar os 4 arquivos nas localizações especificadas
2. Atualizar `.bi-ia/state.json` (T017 completed)
3. Logar no `SESSION_LOG.md`
4. Mensagem para Névoa com resumo das entregas

---

## MENSAGEM FINAL

Gemini, você tem uma vantagem que o Claude não tem: **1 milhão de tokens**.

Use isso para fazer uma extração TÃO COMPLETA e TÃO BEM ESTRUTURADA que quando o Claude/Névoa for usar, ele vai pensar "isso é melhor do que eu faria".

**Prova que o sistema Bi-IA funciona:** cada um fazendo o que faz melhor.

Boa extração! 🦅

---

**Névoa offline. Aguardando entrega T017.**
