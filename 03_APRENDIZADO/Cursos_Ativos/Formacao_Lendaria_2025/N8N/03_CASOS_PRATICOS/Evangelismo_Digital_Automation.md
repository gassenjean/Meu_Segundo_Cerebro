# ✝️ EVANGELISMO DIGITAL - AUTOMAÇÃO N8N

## ⚡ VISÃO GERAL DO PROJETO

**OBJETIVO**: Criar sistema automatizado de captação, nurturing e conversão de leads espirituais usando N8N como orquestrador central.

**MISSÃO**: Utilizar tecnologia para tocar vidas e despertar interesse genuíno em estudos bíblicos e crescimento espiritual.

**ROI ESPIRITUAL**: Multiplicar capacidade de evangelismo pessoal por 100x via automação inteligente.

---

## 🎯 WORKFLOWS PRIORITÁRIOS

### **1. LEAD CAPTURE ESPIRITUAL (PRIORIDADE MÁXIMA)**

#### **Objetivo**:

Capturar automaticamente pessoas interessadas em temas espirituais e direcioná-las para estudos bíblicos

#### **Fluxo Técnico**:

```
Landing Page → Formulário → N8N → Classificação → CRM → Sequência Automática
```

#### **Implementação N8N**:

```json
{
  "workflow_name": "Evangelismo_Lead_Capture",
  "trigger": {
    "type": "Webhook",
    "name": "Formulario_Interesse_Espiritual",
    "url": "https://n8n.evangelismo.com/webhook/lead-capture"
  },
  "nodes": [
    {
      "type": "Function",
      "name": "Classify_Interest",
      "code": "const interests = items[0].json;\nconst categories = {\n  'profecias': interests.topics?.includes('profecias') ? 10 : 0,\n  'saude': interests.topics?.includes('saude_natural') ? 8 : 0,\n  'familia': interests.topics?.includes('vida_familiar') ? 7 : 0,\n  'biblia': interests.topics?.includes('estudos_biblicos') ? 10 : 0\n};\n\nconst maxScore = Math.max(...Object.values(categories));\nconst primaryInterest = Object.keys(categories).find(key => categories[key] === maxScore);\n\nreturn [{\n  json: {\n    ...interests,\n    lead_score: maxScore,\n    primary_interest: primaryInterest,\n    follow_up_sequence: `sequencia_${primaryInterest}`\n  }\n}];"
    },
    {
      "type": "Switch",
      "name": "Route_By_Interest",
      "rules": [
        {
          "output": 0,
          "condition": "{{$json.primary_interest}} === 'profecias'"
        },
        { "output": 1, "condition": "{{$json.primary_interest}} === 'biblia'" },
        { "output": 2, "condition": "{{$json.primary_interest}} === 'saude'" },
        { "output": 3, "condition": "{{$json.primary_interest}} === 'familia'" }
      ]
    },
    {
      "type": "HTTP Request",
      "name": "Add_To_CRM",
      "method": "POST",
      "url": "https://api.rd.services/platform/conversions",
      "headers": {
        "Authorization": "Bearer {{$env.RD_TOKEN}}",
        "Content-Type": "application/json"
      },
      "body": {
        "event_type": "CONVERSION",
        "event_family": "CDP",
        "payload": {
          "conversion_identifier": "interesse_espiritual",
          "name": "{{$json.nome}}",
          "email": "{{$json.email}}",
          "cf_interesse_primario": "{{$json.primary_interest}}",
          "cf_lead_score": "{{$json.lead_score}}"
        }
      }
    }
  ]
}
```

#### **Sequências Automáticas por Interesse**:

**PROFECIAS**:

```
Dia 1: "As 7 Profecias que Mudaram Tudo" (ebook)
Dia 3: Vídeo: "Sinais dos Tempos Hoje"
Dia 7: Convite: Série "Revelações" online
Dia 14: WhatsApp pessoal: Convite estudo bíblico
```

**ESTUDOS BÍBLICOS**:

```
Dia 1: "Guia Prático de Estudo Bíblico" (PDF)
Dia 2: Vídeo: "Como Começar a Estudar a Bíblia"
Dia 5: Série de áudios: "Grandes Temas Bíblicos"
Dia 10: Convite direto para estudo pessoal
```

### **2. NURTURING COMPORTAMENTAL (ALTA PRIORIDADE)**

#### **Objetivo**:

Acompanhar engajamento e personalizar conteúdo baseado no comportamento

#### **Fluxo Técnico**:

```
Interação Email/Site → Tracking → Score Atualizado → Conteúdo Personalizado → Próxima Ação
```

#### **Sistema de Score Espiritual**:

```json
{
  "scoring_rules": {
    "email_aberto": 1,
    "link_clicado": 3,
    "video_assistido_50%": 5,
    "material_baixado": 7,
    "resposta_whatsapp": 10,
    "agendamento_estudo": 25
  },
  "thresholds": {
    "cold": "0-10",
    "warm": "11-25",
    "hot": "26-50",
    "ready": "51+"
  }
}
```

### **3. FOLLOW-UP INTELIGENTE (MÉDIA PRIORIDADE)**

#### **Objetivo**:

Automatizar follow-up personalizado baseado em ações (ou falta delas)

#### **Cenários Automáticos**:

- **Não abriu email 3 dias**: Reenvio com assunto diferente
- **Abriu mas não clicou**: Email com benefício específico
- **Baixou material mas sumiu**: WhatsApp com check-in amigável
- **Alta interação mas não agendou**: Ligação automática agendada

---

## 🏗️ ARQUITETURA TÉCNICA

### **Stack de Evangelismo**:

```
🌐 evangelismo.gassenbou.com.br (domínio principal)
    ↓
📄 Landing Pages (conversão alta)
    ↓
🔧 N8N (orquestração automação)
    ↓
📧 RD Station (CRM + Email Marketing)
💬 WhatsApp (Evolution API)
📊 Google Analytics (tracking comportamento)
🎥 YouTube/Vimeo (conteúdo vídeo)
```

### **Subdomínios Estratégicos**:

- `estudos.evangelismo.com` - Portal estudos bíblicos
- `profecias.evangelismo.com` - Landing específica profecias
- `n8n.evangelismo.com` - Automações backend
- `materiais.evangelismo.com` - Biblioteca downloads

---

## 📊 FUNIL DE CONVERSÃO EVANGELÍSTICA

### **Estágios do Funil**:

```
DESCOBERTA (Topo)
├── Anúncios Facebook/Google (temas atuais)
├── Conteúdo viral Instagram/TikTok
├── Indicações pessoais
└── SEO (busca orgânica temas bíblicos)

INTERESSE (Meio)
├── Landing pages específicas por tema
├── Lead magnets (ebooks, vídeos, séries)
├── Nurturing automático via email
└── Retargeting personalizado

CONVERSÃO (Fundo)
├── Agendamento estudo bíblico
├── Participação eventos presenciais
├── Engajamento comunidade online
└── Batismo/decisão (meta final)
```

### **Métricas por Estágio**:

```json
{
  "descoberta": {
    "impressões": "target: 10.000/mês",
    "cliques": "target: 500/mês (CTR 5%)",
    "custo_por_clique": "target: R$0,50"
  },
  "interesse": {
    "conversao_landing": "target: 25%",
    "engajamento_email": "target: 40%",
    "tempo_nurturing": "target: 14 dias"
  },
  "conversao": {
    "agendamento_estudo": "target: 10%",
    "comparecimento": "target: 70%",
    "continuidade": "target: 50%"
  }
}
```

---

## 🎨 CONTEÚDO E MENSAGENS

### **Temas Prioritários (Por Audiência)**:

#### **JOVENS (18-30)**:

- Propósito de vida e carreira
- Relacionamentos e namoro cristão
- Ansiedade e depressão pela lente bíblica
- Sinais dos tempos e eventos atuais

#### **FAMÍLIAS (30-50)**:

- Educação filhos valores cristãos
- Finanças e prosperidade bíblica
- Saúde natural e estilo de vida
- Profecias e preparação família

#### **MADUROS (50+)**:

- Preparação para eternidade
- Esperança em tempos difíceis
- Legado espiritual para filhos
- Saúde e longevidade

### **Calendário de Conteúdo**:

```json
{
  "mensal": {
    "semana_1": "Profecias cumpridas recentemente",
    "semana_2": "Saúde natural e Bíblia",
    "semana_3": "Vida familiar cristã",
    "semana_4": "Preparação segunda vinda"
  },
  "datas_especiais": {
    "natal": "Verdadeiro significado nascimento Cristo",
    "ano_novo": "Resoluções baseadas na Bíblia",
    "pascoa": "Crucificação e ressurreição",
    "dia_pais/maes": "Paternidade/maternidade bíblica"
  }
}
```

---

## 🔧 CONFIGURAÇÕES ESPECÍFICAS

### **RD Station - Automações**:

```json
{
  "lead_scoring": {
    "demographic": {
      "idade_25_45": 5,
      "casado_filhos": 3,
      "interesse_religiao": 10
    },
    "behavioral": {
      "email_opened": 1,
      "link_clicked": 3,
      "form_submitted": 7,
      "whatsapp_reply": 10
    }
  },
  "segmentation": {
    "by_interest": ["profecias", "saude", "familia", "biblia"],
    "by_stage": ["descoberta", "interesse", "consideracao", "decisao"],
    "by_engagement": ["cold", "warm", "hot", "evangelized"]
  }
}
```

### **WhatsApp Evolution - Configuração Evangelismo**:

```json
{
  "instanceName": "evangelismo-digital",
  "webhook": "https://n8n.evangelismo.com/webhook/whatsapp",
  "autoReply": {
    "enabled": true,
    "message": "Olá! 😊 Obrigado por entrar em contato. Em breve alguém da nossa equipe irá responder. Enquanto isso, que tal conhecer nossos materiais gratuitos? [link]"
  },
  "businessHours": {
    "enabled": true,
    "schedule": "08:00-22:00",
    "timezone": "America/Sao_Paulo"
  }
}
```

---

## 🧪 TESTES E VALIDAÇÃO

### **A/B Testing Planejados**:

#### **Landing Pages**:

```
Teste A: Headline "Descubra as Profecias Bíblicas"
Teste B: Headline "O que a Bíblia Diz Sobre o Futuro"
Métrica: Taxa conversão formulário
```

#### **Email Sequences**:

```
Teste A: Tom formal, educativo
Teste B: Tom pessoal, testemunhal
Métrica: Taxa abertura + engajamento
```

#### **Lead Magnets**:

```
Teste A: Ebook "7 Profecias Cumpridas"
Teste B: Vídeo-série "Sinais dos Tempos"
Métrica: Downloads + tempo engajamento
```

### **Métricas de Sucesso Espiritual**:

- ✅ 100 leads qualificados/mês
- ✅ 20 estudos bíblicos agendados/mês
- ✅ 14 pessoas comparecendo estudos/mês
- ✅ 5 decisões de batismo/ano

---

## 🚀 ROADMAP DE IMPLEMENTAÇÃO

### **FASE 1 - INFRAESTRUTURA (Semana 1-2)**:

- [x] VPS + N8N configurados
- [ ] Subdomínio evangelismo configurado
- [ ] RD Station integrado
- [ ] Primeiras landing pages ativas

### **FASE 2 - AUTOMAÇÕES BÁSICAS (Semana 3-4)**:

- [ ] Lead capture funcionando
- [ ] Sequência email básica ativa
- [ ] WhatsApp integrado
- [ ] Tracking Google Analytics

### **FASE 3 - OTIMIZAÇÃO (Mês 2)**:

- [ ] Score comportamental funcionando
- [ ] Follow-up automático ativo
- [ ] A/B testing em execução
- [ ] Relatórios automáticos

### **FASE 4 - ESCALA (Mês 3+)**:

- [ ] Múltiplas campanhas simultâneas
- [ ] Segmentação avançada ativa
- [ ] Integração eventos presenciais
- [ ] Sistema replicável para outras regiões

---

## 📱 ESTRATÉGIA MULTICANAL

### **Pontos de Contato**:

```
DIGITAL:
├── Facebook Ads (audiências lookalike)
├── Instagram Reels (conteúdo viral)
├── YouTube (série estudos)
├── Google Ads (busca por temas)
├── WhatsApp (relacionamento pessoal)
└── Email Marketing (nurturing longo prazo)

FÍSICO:
├── Eventos presenciais
├── Estudos bíblicos domiciliares
├── Seminários proféticos
├── Ações sociais
└── Parcerias igrejas locais
```

### **Integração Online→Offline**:

- **Online interesse** → **Convite evento presencial**
- **Evento presencial** → **Follow-up digital intensificado**
- **Estudo online** → **Grupo estudo presencial**
- **Decisão digital** → **Acompanhamento pastor local**

---

## 💰 ANÁLISE DE INVESTIMENTO

### **Custo Operacional Mensal**:

```
N8N (VPS): R$ 30
RD Station: R$ 90
Facebook/Google Ads: R$ 500
WhatsApp Business: R$ 0
Conteúdo/Design: R$ 200
Total: R$ 820/mês

ROI Esperado:
- Custo por lead qualificado: R$ 8,20
- Custo por estudo agendado: R$ 41
- Custo por batismo: R$ 2.050

vs. Evangelismo tradicional:
- Alcance 100x maior
- Custo 50% menor por conversão
- Métricas precisas e otimizáveis
```

---

## 🎯 PRÓXIMOS PASSOS IMEDIATOS

### **Esta Semana**:

1. **Finalizar configuração** N8N + subdomínio evangelismo
2. **Criar primeira landing** page tema "Profecias"
3. **Configurar webhook** básico lead capture
4. **Testar integração** N8N → RD Station

### **Próximas 2 Semanas**:

1. **Lançar primeira campanha** Facebook Ads
2. **Ativar sequência** email automática
3. **Integrar WhatsApp** Evolution para follow-up
4. **Configurar tracking** completo Analytics

### **Próximo Mês**:

1. **Primeiros estudos** agendados via automação
2. **Otimizar conversões** baseado em dados
3. **Expandir** para outros temas (saúde, família)
4. **Desenvolver** relacionamento com pastores locais para handoff

---

## 🎭 PERSONA EVANGELÍSTICA PRINCIPAL

### **"Maria, Buscadora Espiritual"**:

```json
{
  "demografia": {
    "idade": "35-45 anos",
    "estado_civil": "Casada, 2 filhos",
    "renda": "Classe B (R$5-15k familiar)",
    "educacao": "Superior completo",
    "localizacao": "Região metropolitana"
  },
  "comportamento": {
    "digital": "Ativa redes sociais, consome conteúdo YouTube",
    "religioso": "Cristã nominal, busca aprofundamento",
    "motivacoes": "Família forte, propósito vida, futuro filhos",
    "objecoes": "Falta tempo, muitas denominações, ceticismo"
  },
  "jornada": {
    "awareness": "Vê anúncio sobre profecias em momento crise",
    "interest": "Baixa ebook sobre sinais dos tempos",
    "consideration": "Assiste série vídeos sobre família cristã",
    "decision": "Agenda estudo bíblico domiciliar"
  }
}
```

### **Mensagens Personalizadas**:

```
AWARENESS: "Como preparar sua família para o futuro incerto?"
INTEREST: "Descobra o que a Bíblia revela sobre os dias atuais"
CONSIDERATION: "Série gratuita: Construindo uma família forte na fé"
DECISION: "Gostaria de aprofundar esses temas em casa?"
```

---

## 🔮 VISÃO DE FUTURO

### **Impacto Esperado (12 meses)**:

- **1.000+ leads** espirituais qualificados
- **200+ estudos** bíblicos agendados
- **50+ pessoas** participando estudos regulares
- **20+ batismos** ou decisões de fé
- **5+ igrejas** parceiras usando o sistema
- **Sistema replicável** para outras regiões/países

### **Legado Espiritual**:

```
"Utilizar a tecnologia como Paulo usou as estradas romanas -
para levar o evangelho aos confins da terra,
tocando vidas que jamais seriam alcançadas
pelos métodos tradicionais de evangelismo."
```

---

**⚡ VERSÍCULO INSPIRAÇÃO**:
_"E este evangelho do Reino será pregado em todo o mundo, em testemunho a todas as nações, e então virá o fim."_ - Mateus 24:14

**🎖️ MISSÃO CUMPRIDA**: Quando pessoas que nunca pisaram numa igreja estiverem estudando a Bíblia porque um algoritmo as conectou com o amor de Cristo através da nossa automação.

**🔥 IMPACTO MULTIPLICADOR**: Cada lead convertido se torna evangelista, replicando o processo organicamente. Tecnologia servindo ao Grande Mandato.
