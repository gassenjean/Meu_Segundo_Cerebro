# M03 A02 - Pixel e Eventos: O Informante da Meta

## Conceito Central

Pixel é um informante espião que reporta tudo pro Zuckerberg. Eventos são as ações específicas que você quer rastrear pra criar públicos e treinar o algoritmo.

## As 3 Funções do Pixel (que importam)

### 1. **Transportador de Dados**

Leva informações do seu site pra Meta sobre o que usuários fazem

### 2. **Cérebro da Conta**

Afina segmentação e direcionamento com base no comportamento

### 3. **Criador de Públicos**

Permite criar segmentações baseadas em ações específicas no site

## O Que São Eventos (sem drama)

**Evento = Ação do usuário no site**

Simples assim. Pode ser:

- Clicar num botão
- Chegar numa página
- Fazer compra
- Adicionar ao carrinho
- Scrollar até X%
- Assistir vídeo
- Qualquer coisa que você queira trackear

## Para Que Servem (só 2 coisas)

### 1. **Criar Públicos**

Segmentar quem fez ações específicas:

- Quem adicionou ao carrinho
- Quem comprou
- Quem scrollou até 50% da página
- Quem clicou em botão específico

### 2. **Otimizar Campanhas**

Meta treina pra buscar pessoas similares:

- Similar a quem compra
- Similar a quem adiciona carrinho
- Similar a quem se cadastra

## Os 3 Tipos de Eventos

### 1. **Eventos Padrão**

Meta já definiu, você só copia/cola:

- ViewContent (visualizou conteúdo)
- AddToCart (adicionou carrinho)
- Purchase (comprou)
- Lead (cadastrou)
- InitiateCheckout (iniciou checkout)

**Como fazer:** Ctrl+C no código da Meta, Ctrl+V no seu site. Ou Shopify/WooCommerce fazem sozinho.

### 2. **Eventos Personalizados**

Você inventa o nome e cria:

- ScrolledTo50Percent
- WatchedFullVideo
- ClickedSizeChart
- DownloadedCatalog

**Como fazer:** Mesmo esquema mas você define o nome do evento.

### 3. **Conversões Personalizadas**

Baseadas em URL específica:

- URL contém "/obrigado"
- URL contém "/thank-you"
- URL contém "/cadastro-sucesso"

**ATENÇÃO CRÍTICA:** Conversão personalizada NÃO cria público diretamente! Só eventos padrão e personalizados criam.

## Aplicação Real (sem bullshit)

### Para KabaK

```javascript
// Eventos Padrão (já prontos)
fbq("track", "ViewContent", {
  content_type: "product",
  content_ids: ["legging-123"],
  value: 89.9,
});

fbq("track", "AddToCart", {
  content_ids: ["legging-123"],
  value: 89.9,
});

fbq("track", "Purchase", {
  value: 89.9,
  currency: "BRL",
});

// Eventos Personalizados (você cria)
fbq("trackCustom", "ViuTabelaMedidas");
fbq("trackCustom", "ScrollouAte50");
fbq("trackCustom", "AssistiuVideoCompleto");
```

### Para Gabriele

```javascript
// B2B específicos
fbq("trackCustom", "SolicitouOrcamento");
fbq("trackCustom", "PersonalizouProduto");
fbq("trackCustom", "BaixouCatalogo");
fbq("trackCustom", "ContatouVendedor");
```

## Implementação Prática (verdade nua)

### Opção 1: Plataforma faz sozinha

- Shopify, WooCommerce, Nuvemshop = eventos padrão automáticos
- Você só coloca ID do Pixel

### Opção 2: Google Tag Manager

- Interface visual, não precisa código
- Cria triggers baseados em ações
- Dispara eventos quando trigger ativa

### Opção 3: Manual (raro precisar)

- Copia código da documentação Meta
- Cola no site onde quer disparar
- Ajusta parâmetros se necessário

## Realidade vs Hype do Pedro

**Pedro diz:** "Não é muito fácil, precisa 5 contatos pra aprender"

**Realidade:**

- Shopify = 2 cliques
- GTM = arrastar e soltar
- Manual = copiar e colar

**Pedro diz:** "Pixel foi bicho de 7 cabeças pra mim"

**Realidade:** É literalmente um código de rastreamento como Google Analytics

## Checklist de Implementação

### ✅ Básico Obrigatório

- [ ] Pixel base instalado em todas páginas
- [ ] ID do Pixel salvo no Business Manager
- [ ] Evento PageView funcionando
- [ ] Evento ViewContent nos produtos
- [ ] Evento Purchase na confirmação

### 🎯 Intermediário Recomendado

- [ ] AddToCart configurado
- [ ] InitiateCheckout ativo
- [ ] Lead para cadastros
- [ ] Search para buscas

### 🚀 Avançado (quando escalar)

- [ ] Eventos personalizados de engajamento
- [ ] Scroll tracking
- [ ] Video tracking
- [ ] Micro-conversões mapeadas

## Observação Crítica da Névoa

Pedro transformando Ctrl+C/Ctrl+V em curso de 15 anos. A parte técnica real:

1. **Pegar ID do Pixel** = copiar número do Business Manager
2. **Instalar Pixel base** = colar no header do site
3. **Adicionar eventos** = copiar código onde quer trackear

O resto é ele inflando complexidade pra parecer guru. Google Tag Manager resolve 95% sem tocar em código.

**Próximo passo real:** Instalar Pixel Helper (extensão Chrome) e verificar se tá trackeando. Pronto.

---

_Processado sem romantização às 23:30h de 08/08/2025_
_Duração real pra implementar: 30 minutos no Shopify, 2 horas no GTM_
