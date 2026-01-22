---
criado: 2025-11-27T00:00:00-03:00
tipo: workflow
categoria: comercial
ferramentas: [Gemini 3 Pro, Banana Nano Pro, N8N, Google Sheets]
baseado-em: Alan Nicolas - Serviços Comerciais com IA
---
# 🎨 WORKFLOW: Geração Automatizada de Banners

**Objetivo:** Criar banners profissionais em escala automaticamente
**Ferramentas:** Gemini 3 + Banana Pro + N8N + Google Sheets
**ROI:** R$5.000-10.000 setup + R$1.000/mês manutenção
**Economia:** 90% tempo vs designer manual

---

## 📊 VISÃO GERAL

```
Planilha (dados) → N8N (trigger) → Gemini (copy) → Banana Pro (imagem) → Drive (entrega)
```

**Serviço completo de geração de banners para:**
- E-commerce (produtos)
- Redes sociais (posts)
- Marketing (anúncios)
- Eventos (divulgação)

---

## 🎯 CASOS DE USO

### 1. E-commerce - Banners de Produtos
**Input:** Planilha com produtos
**Output:** Banner personalizado por produto
**Valor:** R$50/banner vs R$200 designer

### 2. Redes Sociais - Carrosséis Instagram
**Input:** Tema + pontos-chave
**Output:** 10 slides consistentes
**Valor:** R$500/carrossel vs R$2.000 designer

### 3. Campanha de Marketing - Anúncios
**Input:** Briefing da campanha
**Output:** 20+ variações para A/B test
**Valor:** R$2.000 vs R$5.000 agência

---

## 🔄 SETUP INICIAL (Uma Vez)

### 1. Estrutura Google Sheets

```
Colunas obrigatórias:
- A: status (novo/processando/concluido)
- B: id_unico
- C: titulo_banner
- D: texto_principal
- E: call_to_action
- F: cor_predominante
- G: estilo (minimalista/moderno/corporativo)
- H: dimensoes (1200x628/1080x1080/etc)
- I: url_imagem_output (preenchido automaticamente)
```

### 2. Setup N8N

**Node 1: Google Sheets Trigger**
```json
{
  "trigger": "onRowAdded",
  "filter": "status == 'novo'",
  "poll_interval": "5min"
}
```

**Node 2: Gemini API - Gerar Copy**
```javascript
// Prompt otimizado
const prompt = `Criar copy persuasivo para banner:
Título: {{$json["titulo_banner"]}}
Texto principal: {{$json["texto_principal"]}}
CTA: {{$json["call_to_action"]}}
Estilo: {{$json["estilo"]}}

Gere:
1. Headline impactante (max 40 chars)
2. Subheadline (max 60 chars)
3. CTA otimizado (max 20 chars)
4. Hierarquia visual (onde colocar cada elemento)

Formato JSON.`;
```

**Node 3: Banana Pro API - Gerar Imagem**
```javascript
// Prompt para Banana Pro
const imagePrompt = `Professional banner ${$json["dimensoes"]}:
- Background: ${$json["cor_predominante"]} gradient
- Style: ${$json["estilo"]}, clean, modern
- Text layers:
  * Headline: "${geminiOutput.headline}" (bold, large)
  * Subheadline: "${geminiOutput.subheadline}" (medium)
  * CTA: "${geminiOutput.cta}" (button-style)
- Layout: ${geminiOutput.hierarquia}
- High quality, professional, ready for social media`;
```

**Node 4: Google Drive - Salvar**
```json
{
  "folder_id": "ID_PASTA_CLIENTE",
  "filename": "{{$json["id_unico"]}}_{{$json["titulo_banner"]}}.png",
  "convert_to": "png"
}
```

**Node 5: Google Sheets - Atualizar Status**
```json
{
  "update_row": "{{$json["row_id"]}}",
  "set": {
    "status": "concluido",
    "url_imagem_output": "{{driveUrl}}"
  }
}
```

### 3. Configuração API Keys

```bash
# .env do N8N
GEMINI_API_KEY=sua_chave_aqui
GOOGLE_SHEETS_OAUTH=oauth_token
GOOGLE_DRIVE_OAUTH=oauth_token
```

---

## 🚀 USO DIÁRIO

### Fluxo Cliente

1. **Cliente preenche planilha:**
```
| status | id | titulo | texto | cta | cor | estilo | dimensao |
|--------|-----|--------|-------|-----|-----|--------|----------|
| novo   | 001 | Black Friday | Até 70% OFF | Compre Agora | azul | moderno | 1200x628 |
```

2. **N8N detecta (em 5 min)**
3. **Gemini cria copy otimizado**
4. **Banana Pro gera imagem**
5. **Salva em Drive do cliente**
6. **Atualiza status: concluído**

**Tempo total:** 2-5 minutos por banner
**Zero intervenção manual**

---

## 💡 TEMPLATES PRÉ-CONFIGURADOS

### Template 1: E-commerce Produto
```javascript
{
  "tipo": "produto",
  "elementos": ["foto_produto", "preco", "desconto", "cta"],
  "layout": "produto_esquerda_texto_direita",
  "cores": ["cor_marca", "branco", "destaque_cta"]
}
```

### Template 2: Redes Sociais Quote
```javascript
{
  "tipo": "quote",
  "elementos": ["citacao", "autor", "logo"],
  "layout": "centralizado",
  "cores": ["gradiente_marca", "texto_branco"]
}
```

### Template 3: Evento/Webinar
```javascript
{
  "tipo": "evento",
  "elementos": ["titulo", "data_hora", "speakers", "cta_inscricao"],
  "layout": "header_footer",
  "cores": ["cor_tema", "contraste_high"]
}
```

---

## 📊 PRECIFICAÇÃO SERVIÇO

### Setup Inicial
- **Configuração N8N:** R$2.000
- **Templates customizados:** R$1.000
- **Integração Google Workspace:** R$1.000
- **Treinamento cliente:** R$1.000
- **TOTAL SETUP:** R$5.000

### Manutenção Mensal
- **Monitoramento:** R$300
- **Ajustes e melhorias:** R$400
- **Suporte:** R$300
- **TOTAL MENSAL:** R$1.000

### Por Banner Adicional
- **Preço por unidade:** R$50
- **Custo real:** R$0 (APIs gratuitas)
- **Margem:** 100%

### Pacotes
- **Básico:** 50 banners/mês = R$2.500
- **Pro:** 200 banners/mês = R$8.000
- **Enterprise:** Ilimitado = R$15.000/mês

---

## 🎯 ROI PARA CLIENTE

**Antes (designer manual):**
- Custo por banner: R$200-500
- Tempo de entrega: 24-48h
- Revisões: 2-3 rounds
- 50 banners/mês: R$10.000-25.000

**Depois (sistema automatizado):**
- Custo: R$2.500/mês (50 banners)
- Tempo: 5 minutos por banner
- Revisões: Editar planilha e regerar
- **Economia: 75-90%**

---

## 🔧 MONITORAMENTO E OTIMIZAÇÃO

### KPIs Dashboard

```javascript
// Métricas automáticas
{
  "banners_gerados_mes": count,
  "tempo_medio_geracao": avg_time,
  "taxa_sucesso": (concluidos / total) * 100,
  "banners_por_categoria": group_by_estilo,
  "cliente_mais_ativo": top_user
}
```

### Notificações

- **Slack:** Banner concluído
- **Email:** Relatório semanal
- **SMS:** Erro crítico

---

## 📚 RECURSOS

### Exemplos de Prompts

**Salvos em:** `04_RECURSOS/PROMPTS/Gemini/Banner_*.md`
**Salvos em:** `04_RECURSOS/PROMPTS/BananaPro/Image_*.md`

### Links

- N8N: https://n8n.io
- Banana Pro: Via Gemini interface
- Google Sheets API: https://developers.google.com/sheets

---

**Versão:** 1.0
**Status:** ✅ PRONTO PARA IMPLEMENTAÇÃO
**ROI Esperado:** R$10.000-50.000/ano