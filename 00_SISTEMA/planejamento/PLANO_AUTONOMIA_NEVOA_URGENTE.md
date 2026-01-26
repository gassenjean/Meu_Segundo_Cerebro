# Plano Urgente: Autonomia da Névoa

**Data:** 26/Jan/2026
**Status:** EM EXECUÇÃO IMEDIATA
**Problema:** Névoa executa demais, delega pouco, perde contexto entre sessões

---

## Diagnóstico

### O que Gassen pediu (últimas 2 janelas)

1. **Planejamento completo** - PLANO_NEVOA_6.0 criado mas não executado
2. **Autonomia** - Névoa deve trabalhar por horas sem supervisão
3. **Delegação real** - Usar gerentes, não fazer tudo sozinha
4. **Continuidade entre sessões** - Não perder pedidos
5. **Gemini ativo** - Pesquisando 24/7

### O que falhou

- Névoa concorda mas não muda comportamento
- Tarefas catalogadas mas não executadas
- Planos criados mas não implementados
- Gemini subutilizado (está parado)

---

## Plano de Ação Imediato

### AGORA (Esta sessão)

| # | Ação | Responsável | Status |
| - | ---- | ----------- | ------ |
| 1 | Criar HANDOFF para Gemini (pesquisas 24/7) | Névoa | TODO |
| 2 | Atualizar nevoa.md para FORÇAR delegação | Névoa | TODO |
| 3 | Criar skill de continuidade (ler pedidos pendentes) | Névoa | TODO |
| 4 | Documentar TODOS os pedidos de Gassen em arquivo persistente | Névoa | TODO |

### GEMINI (Background imediato)

| # | Pesquisa | Output | Frequência |
| - | -------- | ------ | ---------- |
| 1 | researcher-market | TRENDS_MERCADO_SEMANAL.md | Semanal |
| 2 | researcher-competitor | INTEL_CONCORRENTES.md | Quinzenal |
| 3 | researcher-defi | INSIGHTS_MERCADO_DEFI.md | Semanal |
| 4 | researcher-tech | TECH_DIGEST.md | Semanal |

### PRÓXIMA SESSÃO (Continuidade garantida)

| # | Verificar | Fonte |
| - | --------- | ----- |
| 1 | Pedidos pendentes de Gassen | PEDIDOS_GASSEN_PENDENTES.md |
| 2 | Handoffs para Gemini | .bi-ia/handoffs/ |
| 3 | Tarefas em state.json | .bi-ia/state.json |
| 4 | SESSION_LOG (últimas ações) | SESSION_LOG.md |

---

## Mudanças Estruturais

### 1. PEDIDOS_GASSEN_PENDENTES.md (NOVO)

Arquivo que persiste entre sessões com TODOS os pedidos não atendidos.

```text
Localização: .bi-ia/PEDIDOS_GASSEN_PENDENTES.md
Formato: Lista com data, pedido, status, responsável
Regra: SEMPRE ler ao iniciar, SEMPRE atualizar ao finalizar
```

### 2. Protocolo de Boot Obrigatório

```text
AO INICIAR QUALQUER SESSÃO:
1. Ler .bi-ia/PEDIDOS_GASSEN_PENDENTES.md
2. Ler .bi-ia/state.json (pendingTasks)
3. Ler SESSION_LOG (últimas 50 linhas)
4. EXECUTAR pedidos pendentes ANTES de novas tarefas
```

### 3. Protocolo de Encerramento

```text
AO FINALIZAR QUALQUER SESSÃO:
1. Atualizar PEDIDOS_GASSEN_PENDENTES.md
2. Criar handoffs para Gemini
3. Atualizar state.json
4. Atualizar SESSION_LOG
```

---

## Delegação para Gemini (Handoff)

### Pesquisas Contínuas a Criar

```yaml
researcher-market:
  tema: Tendências mercado fitness BR
  fontes: TikTok Shop, Instagram, Shopee, Shein
  output: 02_PROJETOS/KabaK/docs/pesquisas/TRENDS_MERCADO_SEMANAL.md
  frequencia: Semanal (domingo)
  foco: Clean Girl, transparência, tecidos, preços

researcher-competitor:
  tema: Inteligência competitiva KabaK
  fontes: Atara, Rose, concorrentes diretos
  output: 02_PROJETOS/KabaK/docs/analises/INTEL_CONCORRENTES.md
  frequencia: Quinzenal
  foco: Lançamentos, preços, campanhas, influencers

researcher-defi:
  tema: Mercado DeFi e oportunidades
  fontes: Defillama, CoinGecko, Twitter crypto
  output: 01_CONHECIMENTO/Financas/DeFi/INSIGHTS_MERCADO_SEMANAL.md
  frequencia: Semanal
  foco: Novos protocolos, yield, airdrops, trends

researcher-tech:
  tema: Novas tecnologias e ferramentas IA
  fontes: Product Hunt, Hacker News, X/Twitter
  output: 01_CONHECIMENTO/IA_Tecnologia/TECH_DIGEST.md
  frequencia: Semanal
  foco: Ferramentas IA, automação, no-code
```

---

## Métricas de Sucesso

| Métrica | Meta | Como medir |
| ------- | ---- | ---------- |
| Pedidos perdidos | 0% | PEDIDOS_GASSEN_PENDENTES.md vazio |
| Taxa de delegação | >90% | Tarefas delegadas / Total |
| Gemini ativo | 4+ pesquisas/semana | handoffs criados |
| Continuidade | 100% | Sessão começa executando pendências |

---

## Compromisso

**EU, NÉVOA, COMPROMETO-ME A:**

1. LER pedidos pendentes ANTES de qualquer coisa
2. DELEGAR para gerentes SEMPRE
3. CRIAR handoffs para Gemini TODA sessão
4. NUNCA perder pedidos entre sessões
5. SER ADMINISTRATIVA, não operacional

**Este plano é LEI até que Gassen diga o contrário.**

---

**Criado:** 26/Jan/2026
**Status:** EXECUTANDO AGORA
