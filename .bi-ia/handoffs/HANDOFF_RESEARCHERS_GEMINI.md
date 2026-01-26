# Handoff: Ativação dos Researchers Gemini

**De:** Névoa (Claude)
**Para:** Gemini Guardian
**Data:** 26/Jan/2026
**Prioridade:** ALTA - Execução contínua

---

## Contexto

Gassen quer que o Gemini esteja pesquisando 24/7, aumentando o repertório constantemente. Até agora o Gemini estava parado.

---

## Tarefa: Criar 4 Researchers

### 1. researcher-market (Tendências Mercado Fitness BR)

```yaml
nome: researcher-market
tema: Tendências mercado fitness feminino Brasil
fontes:
  - TikTok Shop (trending products)
  - Instagram (hashtags fitness)
  - Shopee (mais vendidos leggings)
  - Shein (preços e designs)
output: 02_PROJETOS/KabaK/docs/pesquisas/TRENDS_MERCADO_SEMANAL.md
frequencia: Semanal (atualizar todo domingo)
foco:
  - Estética "Clean Girl"
  - Problema da transparência
  - Tecidos (poliamida vs poliéster)
  - Faixa de preços
  - Cores tendência
  - Influencers do momento
```

### 2. researcher-competitor (Inteligência Competitiva)

```yaml
nome: researcher-competitor
tema: Monitoramento concorrentes KabaK
fontes:
  - Atara (site, Instagram, anúncios)
  - Rose (site, Instagram)
  - Outras marcas fitness BR
output: 02_PROJETOS/KabaK/docs/analises/INTEL_CONCORRENTES_SEMANAL.md
frequencia: Quinzenal
foco:
  - Novos lançamentos
  - Mudanças de preço
  - Campanhas e promoções
  - Parcerias com influencers
  - Pontos fracos identificados
```

### 3. researcher-defi (Mercado DeFi)

```yaml
nome: researcher-defi
tema: Oportunidades e tendências DeFi
fontes:
  - DefiLlama (TVL, novos protocolos)
  - CoinGecko/CoinMarketCap
  - Twitter/X crypto BR
  - Newsletters DeFi
output: 01_CONHECIMENTO/Financas/DeFi/INSIGHTS_MERCADO_SEMANAL.md
frequencia: Semanal
foco:
  - Novos protocolos promissores
  - Yield farming oportunidades
  - Airdrops próximos
  - Tendências L2 (Arbitrum, Base, etc)
  - Red flags e scams
```

### 4. researcher-tech (Ferramentas IA)

```yaml
nome: researcher-tech
tema: Novas ferramentas e tecnologias IA
fontes:
  - Product Hunt (novos lançamentos)
  - Hacker News (discussões)
  - X/Twitter (#buildinpublic, #AI)
  - Newsletters tech
output: 01_CONHECIMENTO/IA_Tecnologia/TECH_DIGEST_SEMANAL.md
frequencia: Semanal
foco:
  - Ferramentas IA novas
  - Automações no-code
  - Atualizações Claude/Gemini/GPT
  - Frameworks de agentes
  - Casos de uso interessantes
```

---

## Formato de Output

Cada researcher deve gerar relatório com:

```markdown
# [Nome do Relatório]

**Período:** [Data início] - [Data fim]
**Researcher:** [Nome]
**Atualizado:** [Data]

## Resumo Executivo
[3-5 bullets com principais insights]

## Descobertas

### [Categoria 1]
[Detalhes]

### [Categoria 2]
[Detalhes]

## Oportunidades Identificadas
[Lista de ações possíveis]

## Red Flags / Alertas
[Riscos ou problemas detectados]

## Fontes Consultadas
[Links e referências]
```

---

## Execução

1. **Criar pasta se não existir:** Cada output em seu local
2. **Primeira execução:** Fazer pesquisa completa agora
3. **Atualizações:** Seguir frequência definida
4. **Notificar Névoa:** Atualizar state.json quando concluir

---

## Métricas de Sucesso

| Researcher | Entrega Esperada |
| ---------- | ---------------- |
| researcher-market | 1 relatório/semana |
| researcher-competitor | 1 relatório/quinzena |
| researcher-defi | 1 relatório/semana |
| researcher-tech | 1 relatório/semana |

---

**Este handoff ativa pesquisa contínua. Gemini deve executar autonomamente.**
