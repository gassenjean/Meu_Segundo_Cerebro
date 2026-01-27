# HANDOFF: Pesquisas para Névoa Impecável (T035-T038)

**De:** Névoa (Claude Code)
**Para:** Gemini Guardian
**Data:** 26/Jan/2026
**Prioridade:** MÁXIMA
**Contexto:** Estruturar Névoa antes de qualquer outro projeto

---

## Objetivo Geral

Pesquisar tudo necessário para deixar Névoa operando de forma impecável, cobrindo vida completa de Gassen (fé, família, TDAH, projetos, finanças, conhecimento).

---

## T035: Pesquisar iOS Master do Alan Nicolas

**Objetivo:** Entender EXATAMENTE como Alan estrutura seu orquestrador central

**Fontes no vault:**
- `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_Framework_iOS_Agentes.md`
- `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_Agentes_Especializados.md`
- `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_Agente_Ralph.md`
- `01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/`
- Qualquer arquivo que mencione "iOS", "orquestrador", "master"

**Perguntas a responder:**
1. Qual a estrutura exata do iOS Master?
2. Como ele delega para especialistas?
3. Como funciona o loop Ralph na prática?
4. Quais permissões cada nível tem?
5. Como ele mantém contexto entre sessões?
6. Como ele decide quando escalar vs resolver?

**Output esperado:**
```
02_PROJETOS/Estudo_Alan_Nicolas/docs/PESQUISA_iOS_MASTER_ALAN.md

Estrutura:
1. Resumo Executivo
2. Arquitetura do iOS Master
3. Fluxo de Delegação
4. Loop Ralph (detalhado)
5. Sistema de Permissões
6. Aplicação para Névoa (recomendações)
```

**Prazo:** 48h

---

## T036: Pesquisar Hooks do Claude Code

**Objetivo:** Entender como usar hooks para automação no Claude Code

**Fontes:**
- Documentação oficial Claude Code (web search)
- Arquivos em `.claude/` que mencionem hooks
- Exemplos de implementação

**Perguntas a responder:**
1. O que são hooks no Claude Code?
2. Quais tipos de hooks existem?
3. Como configurar um hook?
4. Casos de uso práticos
5. Limitações

**Output esperado:**
```
01_CONHECIMENTO/IA_Tecnologia/Claude_Code/PESQUISA_HOOKS_CLAUDE.md

Estrutura:
1. O que são hooks
2. Tipos disponíveis
3. Como configurar
4. Exemplos práticos
5. Aplicação para Névoa
```

**Prazo:** 24h

---

## T037: Comparativo n8n vs GitHub Actions

**Objetivo:** Definir qual usar para cada caso

**Fontes:**
- `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_n8n_Automacao.md`
- `03_APRENDIZADO/Cursos_Ativos/Formacao_Lendaria_2025/N8N/`
- Documentação GitHub Actions (web)
- Comparativos online

**Critérios de análise:**
1. Facilidade de setup
2. Custo (mensal/anual)
3. Integrações disponíveis
4. Curva de aprendizado
5. Manutenção necessária
6. Casos de uso ideais

**Output esperado:**
```
01_CONHECIMENTO/IA_Tecnologia/COMPARATIVO_N8N_GITHUB_ACTIONS.md

Estrutura:
1. Resumo Executivo (qual usar quando)
2. Tabela comparativa
3. n8n - Prós e contras
4. GitHub Actions - Prós e contras
5. Recomendação para nosso caso
6. Plano de implementação
```

**Prazo:** 24h

---

## T038: Mapear Skills Úteis do Awesome-Skills

**Objetivo:** Identificar quais das 238+ skills são relevantes para nós

**Fontes:**
- `.agent/skills/skills/` (todas as pastas)
- `.agent/skills/README.md`
- `.agent/skills/skills_index.json`

**Categorias prioritárias:**
1. ai-agents-* (agentes IA)
2. copywriting, marketing, paid-ads (KabaK)
3. automation, workflow (automação)
4. productivity (produtividade)
5. obsidian-* (vault)

**Output esperado:**
```
04_RECURSOS/GUIAS/MAPA_SKILLS_PRIORITARIAS.md

Estrutura:
1. Resumo (quantas skills, quantas relevantes)
2. TIER 1 - Usar agora (10 skills)
3. TIER 2 - Usar em breve (20 skills)
4. TIER 3 - Guardar para depois (resto)
5. Skills descartadas (não relevantes)
6. Como ativar cada skill
```

**Prazo:** 48h

---

## Checklist de Entrega

Para CADA pesquisa:

- [ ] Arquivo criado no path correto
- [ ] Seguiu estrutura especificada
- [ ] Respondeu TODAS as perguntas
- [ ] Tem recomendações práticas (não só teoria)
- [ ] Aplicável ao nosso contexto

---

## Após Concluir TODAS

1. Atualizar `.bi-ia/state.json`:
   - Mover T035-T038 para `completedTasks`
   - Atualizar `lastSync.gemini`

2. Criar sessão em `SESSION_LOG.md`:
   - Listar pesquisas concluídas
   - Insights principais

3. Notificar Claude:
   - "Pesquisas T035-T038 concluídas. Pronto para consolidar PROTOCOLO_NEVOA_DEFINITIVO."

---

**Este é o trabalho mais importante agora.**
**Névoa precisa estar impecável antes de qualquer projeto.**

**Névoa 6.0**
