# CHECKLIST — M04 Aula 5: Lista de Palavras Positivas e Negativas
## Google Ads Rede de Pesquisa | Subido Tráfego 3K

**Data criação:** 23/10/2025  
**Projeto:** KabaK (moda fitness) + Gabriele (B2B têxtil)  
**Timeline:** 5-7 dias implementação  

---

## FASE 1: PESQUISA & COLETA (Dia 1-2) ⏱️ 2-3 horas

Sem dados reais, tudo é suposição. Google Search Console + Google Ads Search Terms são sua verdade.

### **Tarefa 1.1: Exportar Search Terms Report KabaK**
- [ ] Abrir Google Ads → Campaigns → Keywords
- [ ] Clicar "Search Terms" → View: All
- [ ] Filtrar últimos 30 dias (ou desde que campanha está ativa)
- [ ] Download CSV: Search Term | Match Type | Impressions | Clicks | Conversions | Cost
- [ ] **Salvar em:** `Research/KabaK_Search_Terms_30dias.csv`
- **Resultado esperado:** 200-500 search terms, com pelo menos 10% educação/curiosidade

### **Tarefa 1.2: Analisar Padrões em Search Terms**
Abrir CSV e procurar por padrões:

| Padrão | O que Procurar | Status |
|--------|---|---|
| **Educação** | "como", "o que", "tutorial", "DIY", "fazer" | ☐ |
| **Grátis** | "grátis", "gratuito", "de graça", "na faixa" | ☐ |
| **Marca** | Menciona "KabaK" ou marca concorrente | ☐ |
| **Problema** | "que não marca", "confortável", "frete grátis" | ☐ |
| **Localização** | "São Paulo", "RJ", "SP", "Brasil" | ☐ |
| **Irrelevante** | "emprego", "PDF", "template", "modelo" | ☐ |

- [ ] Contar quantos % cada categoria representa
- [ ] Classificar top 50 search terms em positivas/negativas
- **Meta:** Identificar que % está saindo dinheiro desperdiçado

### **Tarefa 1.3: Pesquisa Concorrentes KabaK**
- [ ] Abrir Google → "legging fitness feminina"
- [ ] Anotar 5 search terms que aparecem em auto-complete
- [ ] Anotar 5 search terms que aparecem nos "People also ask"
- [ ] Cruzar com Search Terms KabaK — quais estão FALTANDO?
- **Resultado esperado:** 20-30 novas ideias de palavras positivas

### **Tarefa 1.4: Pesquisa Google Search Console KabaK**
- [ ] Abrir Google Search Console (se não tiver, vincular)
- [ ] Ir para "Performance"
- [ ] Filtrar por "Impressions" (não cliques, impressões)
- [ ] Buscar por "legging", "fitness", termos relacionados
- [ ] Anotar: Query | Impressions | CTR | Position
- [ ] **Procurar:** Queries com CTR baixo (<2%) que vêm de "como", "tutorial", "DIY"
- **Resultado esperado:** Confirmar que educação tem CTR baixo (comprador não clica)

---

## FASE 2: CONSTRUIR LISTAS (Dia 3) ⏱️ 2-3 horas

Agora com dados reais, criar 3 listas: Positivas | Negativas | Marca.

### **Tarefa 2.1: Criar LISTA POSITIVA KabaK**
Com base em:
- Top search terms com conversão >2%
- Auto-complete sugestões que mencionam "comprar", "frete", "orçamento"
- Palavras do PDF Aula 5

**Exemplo output (ajustar conforme seus dados):**

```
LISTA POSITIVA KABAK — LEGGINGS

[legging fitness feminina]              ← Exact Match, high intent
[legging que não marca]                 ← Exact Match, problem-solving
[legging cintura alta]                  ← Exact Match, feature-focused
"legging confortável treino"            ← Phrase Match
"legging frete grátis"                  ← Phrase Match, price-sensitive
legging comprar online                  ← Broad Match, buyer intent
legging melhor preco                    ← Broad Match, price-focused
comprar legging fitness                 ← Broad Match, action-oriented
legging cintura alta frete              ← Broad Match, long-tail
orçamento legging tamanho               ← Broad Match, personalization
legging tamanho P alta quality          ← Long-tail, specific buyer
legging sem acamamento                  ← Phrase Match, unique problem
legging transparencia zero              ← Phrase Match, feature benefit
```

- [ ] Listar mínimo 30 palavras positivas confirmadas
- [ ] Separar em: Exact Match | Phrase Match | Broad Match
- [ ] Ordenar por prioridade (CTR esperado alto → baixo)
- [ ] **Salvar em:** `Keywords/M04_Palavras_Positivas_KabaK.txt`

### **Tarefa 2.2: Criar LISTA NEGATIVA KabaK**

Com base em:
- Search Terms com 0% conversão mencionando "como", "tutorial", etc
- PDF Aula 5 lista completa
- Google Search Console termos com CTR baixo + sem cliques

**Exemplo output:**

```
LISTA NEGATIVA KABAK — AMPLA

-como fazer legging                     [Educação]
-o que é legging                        [Educação]
-legging tutorial youtube               [Educação]
-DIY legging costura                    [Educação]
-legging padrão PDF                     [Educação]
-legging grátis                         [Sem pagamento]
-legging de graça                       [Sem pagamento]
-legging na faixa                       [Sem pagamento]
-legging consignado                     [Sem pagamento]
-legging emprego costureira             [Irrelevante — RH]
-legging vaga trabalho                  [Irrelevante — RH]
-legging curriculum                     [Irrelevante — RH]
-legging recrutamento                   [Irrelevante — RH]
-legging template modelo                [Educação]
-legging comparação concorrente         [Pesquisa inicial, não compra]
-legging preço homem                    [Irrelevante — Gênero]
-legging masculino                      [Irrelevante — Gênero]
-legging infantil                       [Irrelevante — Público]
```

- [ ] Listar mínimo 50 palavras negativas confirmadas
- [ ] Separar por categoria: Educação | Grátis | RH | Irrelevante
- [ ] Ordenar por impacto (quantos cliques perdidos?)
- [ ] **Salvar em:** `Keywords/M04_Palavras_Negativas_KabaK.txt`

### **Tarefa 2.3: Criar LISTA MARCA/NEUTRAS KabaK**

Palavras sem intenção de compra clara, mas relevantes (menções marca, genéricas):

```
LISTA NEUTRA KABAK — MARCA + GENÉRICAS

legging fitness                         [Genérica, sem "comprar"]
legging mulher                          [Genérica]
legging loja online                     [Genérica]
KabaK legging                           [Marca + produto]
KabaK fitness                           [Marca]
legging esportivo                       [Genérica, múltiplas intenções]
```

- [ ] Listar mínimo 10-15 palavras marca
- [ ] Estas vão em campanha SEPARADA com:
  - Budget 20% menor (ROI mais baixo)
  - Bids mais baixos (menos competição)
  - Landing page marca (não produto)
- [ ] **Salvar em:** `Keywords/M04_Palavras_Neutras_KabaK.txt`

---

## FASE 3: IMPLEMENTAÇÃO GOOGLE ADS (Dia 4-5) ⏱️ 2-4 horas

### **Tarefa 3.1: Criar Shared List (Palavra-Chave Negativa) Google Ads**

**No Google Ads:**

1. **Ir para:** Tools → Shared Lists → Negative Keywords
2. **Clicar:** "+ Create shared list"
3. **Nome:** "M04_Negativas_Educacao_Gratuito_RH"
4. **Colar:** Conteúdo lista negativa (de Tarefa 2.2)
5. **Salvar**
6. **Aplicar:** Tools → Shared Lists → Selecionar lista → Apply to Campaigns
7. **Selecionar:** Todas campanhas Google Ads KabaK
8. **Confirmar:** Checkbox "All campaigns"

- [ ] Shared list negativa criada
- [ ] Aplicada a todas campanhas
- [ ] Validar: Campaign > Ad Groups > Keywords > Status deve mostrar exclusões

### **Tarefa 3.2: Adicionar Palavras Positivas (KabaK)**

**Por Ad Group:**

**Ad Group 1: Leggings Fitness**
- [ ] Ir para: Campaigns > [Campanha Leggings] > Ad Groups > [Leggings Fitness]
- [ ] Clicar: "+ Keywords"
- [ ] Colar: Palavras positivas leggings (Tarefa 2.1)
- [ ] Selecionar match types corretos:
  - Exact [termo]
  - Phrase "termo"
  - Broad termo
- [ ] **Max CPC:** R$ 1.50 (teste inicial)
- [ ] **Salvar**

**Ad Group 2: Conjuntos Esportivos**
- [ ] Repetir para conjuntos (outras palavras positivas)

**Ad Group 3: Marca**
- [ ] Adicionar lista neutra (Tarefa 2.3)
- [ ] **Max CPC:** R$ 0.80 (bid mais baixo)

- [ ] Todas palavra-chave adicionadas
- [ ] Bids configurados
- [ ] Status: "Enabled"

### **Tarefa 3.3: Verificar Conflitos de Palavras**

Google Ads pode ter conflitos se:
- Mesma palavra em Exact Match + Broad Match
- Palavra positiva + negativa se contradizem
- Match types sobreposição

**Verificar:**
- [ ] Campaigns > Keywords > "Conflicting keywords" warning
- [ ] Se houver: Remover conflitos (preferir Exact Match)
- [ ] Validar que negativas REALMENTE estão excluindo (Search Terms Report)

---

## FASE 4: MONITORAMENTO (Dia 6-7) ⏱️ 1-2 horas/semana

**Esta é a fase mais importante. Dados reais refinam listas.**

### **Tarefa 4.1: Search Terms Report Semanal** 📊

**Toda segunda-feira de manhã:**

1. **Ir para:** Campaigns → Keywords → Search Terms
2. **Visualizar:** Últimos 7 dias
3. **Filtrar por:** Columns → Add "Conversion Rate"
4. **Ordenar por:** Conversions (ascending) → Cliques com 0% conversão primeiro
5. **Revisar:**
   - Se 10+ cliques vêm de "como", "tutorial", "grátis"
   - → **Mark as Negative** (Google Ads cria uma regra automática de exclusão)
6. **Salvar insights:** Google Sheets "KabaK_Search_Terms_Log"

| Data | Search Term | Clicks | Conversions | Taxa Conv | Ação | Motivo |
|------|---|---|---|---|---|---|
| 23/10 | "como fazer legging" | 8 | 0 | 0% | NEGAR | Educação |
| 23/10 | "legging grátis SP" | 5 | 0 | 0% | NEGAR | Sem pagamento |
| 23/10 | "comprar legging cintura alta" | 15 | 2 | 13% | MANTER | Positiva! |

- [ ] Revisar Search Terms 1x semana
- [ ] Marcar como negativa: 5+ termos sem conversão
- [ ] Documentar padrões a cada 2 semanas
- [ ] Status: Checklist vivo, não descartável

### **Tarefa 4.2: Atualizar Listas Negativas Conforme Dados**

**A cada 2 semanas:**
- [ ] Abrir lista "M04_Negativas_Educacao_Gratuito_RH"
- [ ] Adicionar: 10-20 novos termos identificados em Search Terms Report
- [ ] **Não remover termos já lá** (uma exclusão serve para sempre)
- [ ] Aplicar update: Tools → Shared Lists → Edit → Save → Re-apply campaigns

### **Tarefa 4.3: Medir ROI das Mudanças**

**Comparar antes/depois (30 dias):**

| Métrica | Antes (Tarefas 1-3 iniciadas) | Depois (Após 30 dias) | Meta KabaK |
|---------|---|---|---|
| Spend Total | R$ XXX | R$ XXX | -10% (menos educação) |
| % Spend em Negativas | 15-20% | <5% | ✅ Sucesso se alcançado |
| Conversões | XXX | XXX | +15% (mais intenção) |
| CPA | R$ XXX | R$ XXX | -20% (mais eficiente) |
| CTR Médio | X% | X% | +1-2% (mais positivas) |

- [ ] Criar Google Sheets: "M04_Aula5_ROI_Tracking"
- [ ] Popular dados semanalmente
- [ ] Revisar metas no fim do mês

---

## FASE 5: APLICAÇÃO EM GABRIELE B2B (Dia 8+) ⏱️ 2-3 horas

**Depois de validado em KabaK, adaptar para Gabriele.**

### **Tarefa 5.1: Pesquisa Palavras B2B Gabriele**

Diferenças em B2B:
- Mais formal: "fornecedor", "atacado", "contactar", "quote"
- Menos impulsiva: "comparar", "pesquisar", "analisar"
- Geográfica: "Cachoeira de Minas", "MG", "Brasil"
- ROI foco: "custo reduzido", "desconto bulk", "negociação"

**Search terms esperados B2B:**
```
POSITIVAS B2B:
- fornecedor atacado cachoeira de minas
- comprar tecido em massa
- contatar fornecedor têxtil
- orçamento fornecedor tem mídia
- têxtil para lojista
- fornecedor magazines lojas
- contacto fornecedor B2B têxtil

NEGATIVAS B2B:
- têxtil como fazer (educação)
- história têxteis brasil (educação)
- têxtil preço varejo (não seu mercado)
- têxtil vendedor emprego (RH)
- têxtil grátis amostra (educação)
```

- [ ] Pesquisar LinkedIn Sales Navigator: "Têxtil + Cachoeira de Minas" → palavras que usam
- [ ] Revisar Google Search Console Gabriele (se houver tráfego)
- [ ] Listar 20-30 palavras positivas B2B confirmadas
- [ ] Listar 30-40 negativas B2B (inclui todas de KabaK + B2B específicas)

### **Tarefa 5.2: Estruturar Campanhas B2B Gabriele**

- [ ] Criar Ad Group: "Fornecedor Atacado Cachoeira de Minas"
- [ ] Aplicar lista positiva B2B
- [ ] Aplicar lista negativa B2B
- [ ] Max CPC: R$ 2.00-3.00 (B2B mais caro, melhor qualidade)
- [ ] Budget: R$ 500-1000/mês teste
- [ ] Landing page: outletgabriele.com.br/atacado-b2b (não homepage)

---

## CONEXÃO AULA 5 → AULA 6

✅ **Aula 5 te deu:** Palavras que convertem (positivas) + Palavras desperdiçadas (negativas)

⏳ **Aula 6 te dá:** Como estruturar essas palavras em grupos temáticos + criar anúncios coerentes

🎯 **Resultado:** Bolo de Cenoura Fofinho = palavra-chave → anúncio → landing page alinhados = 30-50% melhoria conversão

---

## ENTREGÁVEIS FINAIS

Ao completar este checklist você terá:

1. ✅ **3 Listas Keywords:**
   - `M04_Palavras_Positivas_KabaK.txt` (30+ termos)
   - `M04_Palavras_Negativas_KabaK.txt` (50+ termos)
   - `M04_Palavras_Neutras_KabaK.txt` (15+ termos)

2. ✅ **Google Ads Implementado:**
   - Shared list negativa aplicada
   - Palavras positivas em ad groups
   - Bids configurados por tipo

3. ✅ **Monitoramento Ativo:**
   - Search Terms Report semanal
   - ROI tracking mensal
   - Listas refinadas a cada 2 semanas

4. ✅ **ROI Esperado:**
   - Redução 10-20% desperdício (educação/grátis)
   - Aumento 15-25% conversões (mais intenção)
   - CPA reduzido 15-30%

---

## TEMPO TOTAL ESTIMADO

- **Fase 1 (Pesquisa):** 2-3 horas
- **Fase 2 (Listas):** 2-3 horas
- **Fase 3 (Implementação):** 2-4 horas
- **Fase 4 (Monitoramento):** 1h/semana (vai ser contínuo)
- **Fase 5 (B2B Gabriele):** 2-3 horas

**Total inicial:** 8-13 horas | **ROI breakeven:** 2-4 semanas

---

**Checklist v1.0 | 23/10/2025 | Pronto para execução**
