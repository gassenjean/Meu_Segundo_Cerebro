# 🤖 NÉVOA IA - INTEGRAÇÃO N8N

## ⚡ VISÃO GERAL DO PROJETO

**OBJETIVO**: Integrar Névoa IA com N8N para automação completa do atendimento via WhatsApp, processamento de dados e análise de conversações.

**ROI ESPERADO**: Atendimento 24/7 sem limite de usuários + insights automáticos de conversações

---

## 🎯 WORKFLOWS PRIORITÁRIOS

### **1. INTEGRAÇÃO WHATSAPP-IA (ALTA PRIORIDADE)**

#### **Objetivo**:

Automatizar resposta da Névoa via WhatsApp com contexto e personalização

#### **Fluxo Técnico**:

```
WhatsApp Message → Evolution API → N8N → Névoa IA → Resposta → WhatsApp
```

#### **Implementação N8N**:

```json
{
  "workflow_name": "Nevoa_WhatsApp_Integration",
  "nodes": [
    {
      "type": "Webhook",
      "name": "Evolution_Trigger",
      "webhook_url": "https://n8n.nevoa.com/webhook/whatsapp"
    },
    {
      "type": "Function",
      "name": "Message_Processing",
      "code": "// Extrair dados da mensagem\nconst message = items[0].json.message;\nconst phone = items[0].json.phone;\nconst timestamp = items[0].json.timestamp;\n\nreturn [{\n  json: {\n    user_message: message,\n    user_phone: phone,\n    conversation_id: `conv_${phone}_${Date.now()}`\n  }\n}];"
    },
    {
      "type": "HTTP Request",
      "name": "Nevoa_API_Call",
      "method": "POST",
      "url": "https://api.nevoa.ia/v1/chat/completions",
      "headers": {
        "Authorization": "Bearer {{$env.NEVOA_API_KEY}}",
        "Content-Type": "application/json"
      },
      "body": {
        "message": "{{$json.user_message}}",
        "context": "evangelismo_digital",
        "user_id": "{{$json.user_phone}}"
      }
    },
    {
      "type": "HTTP Request",
      "name": "WhatsApp_Response",
      "method": "POST",
      "url": "{{$env.EVOLUTION_API_URL}}/message/sendText/{{$env.EVOLUTION_INSTANCE}}",
      "headers": {
        "apikey": "{{$env.EVOLUTION_API_KEY}}"
      },
      "body": {
        "number": "{{$json.user_phone}}",
        "text": "{{$json.nevoa_response}}"
      }
    }
  ]
}
```

#### **Configurações Necessárias**:

```bash
# Variáveis de Ambiente
NEVOA_API_KEY=sua_chave_nevoa
EVOLUTION_API_URL=https://evolution.nevoa.com
EVOLUTION_API_KEY=sua_chave_evolution
EVOLUTION_INSTANCE=nevoa_instance
```

### **2. ANALYTICS DE CONVERSAÇÕES (MÉDIA PRIORIDADE)**

#### **Objetivo**:

Coletar dados de todas as conversações para insights e melhorias da IA

#### **Fluxo Técnico**:

```
Fim de Conversa → Análise Sentimento → Categorização → Relatório → Dashboard
```

#### **Implementação N8N**:

```json
{
  "workflow_name": "Nevoa_Analytics_Pipeline",
  "trigger": "webhook_conversation_end",
  "processing": [
    {
      "sentiment_analysis": "OpenAI GPT-4",
      "categorization": "Evangelismo/Suporte/Comercial",
      "satisfaction_score": "1-10 scale",
      "keywords_extraction": "Temas principais"
    }
  ],
  "output": {
    "google_sheets": "Dashboard tempo real",
    "email_report": "Relatório semanal",
    "slack_alert": "Casos críticos"
  }
}
```

### **3. LEAD CAPTURE AUTOMÁTICO (ALTA PRIORIDADE)**

#### **Objetivo**:

Identificar e processar automaticamente leads espirituais via conversas

#### **Fluxo Técnico**:

```
Conversa → Detecção Interesse → Score Lead → CRM → Follow-up Automático
```

#### **Critérios de Lead**:

- Perguntas sobre estudos bíblicos
- Interesse em profecia/eventos finais
- Solicitação de oração/aconselhamento
- Pedido de material evangelístico

---

## 🏗️ ARQUITETURA TÉCNICA

### **Stack de Integração**:

```
🌐 nevoa.gassenbou.com.br (domínio principal)
    ↓
💻 VPS Hostinger (recursos dedicados Névoa)
    ↓
🖥️ EasyPanel (monitor performance IA)
    ↓
🔧 N8N (orquestração workflows)
🤖 Evolution API (WhatsApp gateway)
🧠 Névoa IA (processamento principal)
📊 Analytics DB (dados conversações)
```

### **Subdomínios Organizados**:

- `api.nevoa.gassenbou.com.br` - API principal Névoa
- `n8n.nevoa.gassenbou.com.br` - Automações
- `evolution.nevoa.gassenbou.com.br` - WhatsApp API
- `dashboard.nevoa.gassenbou.com.br` - Analytics

---

## 📊 DADOS E MÉTRICAS

### **KPIs Principais**:

```json
{
  "operacionais": {
    "mensagens_processadas_dia": "target: 1000+",
    "tempo_resposta_medio": "target: <3s",
    "taxa_sucesso_resposta": "target: >98%",
    "uptime_sistema": "target: >99.5%"
  },
  "evangelisticos": {
    "leads_identificados_dia": "target: 50+",
    "conversoes_estudo_biblico": "target: 10%",
    "satisfacao_conversa": "target: >8/10",
    "retorno_conversacao": "target: 40%"
  }
}
```

### **Dashboard Tempo Real**:

- **Performance IA**: Latência, tokens utilizados, custos
- **Engajamento**: Usuários ativos, tempo conversa, temas
- **Conversões**: Leads gerados, estudos agendados, materiais solicitados
- **Técnico**: Status serviços, erros, recursos VPS

---

## 🔧 CONFIGURAÇÕES ESPECÍFICAS

### **Evolution API - Instância Névoa**:

```json
{
  "instanceName": "nevoa-evangelismo",
  "webhook": "https://n8n.nevoa.gassenbou.com.br/webhook/whatsapp",
  "events": ["MESSAGE_RECEIVED", "MESSAGE_SENT", "CONNECTION_UPDATE"],
  "settings": {
    "rejectCall": true,
    "msgRetryCounterValue": 3,
    "markMessagesRead": true
  }
}
```

### **Névoa IA - Configuração Contextual**:

```json
{
  "model": "gpt-4-turbo",
  "system_prompt": "Você é a Névoa, uma assistente especializada em espiritualidade cristã adventista. Seu objetivo é evangelizar de forma natural, responder dúvidas bíblicas e identificar interesse em estudos bíblicos.",
  "context_memory": "30_messages",
  "response_style": "compassivo, conhecedor da Bíblia, evangelístico",
  "lead_detection": {
    "triggers": ["estudo bíblico", "profecia", "Jesus", "salvação", "oração"],
    "score_threshold": 7,
    "follow_up": "automatic"
  }
}
```

---

## 🧪 TESTES E VALIDAÇÃO

### **Cenários de Teste**:

#### **Teste 1 - Conversa Normal**:

```
INPUT: "Oi, como você está?"
EXPECTED: Resposta calorosa + apresentação Névoa
VALIDATE: Tempo <3s, resposta contextual
```

#### **Teste 2 - Identificação Lead**:

```
INPUT: "Tenho curiosidade sobre profecias bíblicas"
EXPECTED: Resposta sobre profecias + convite estudo
VALIDATE: Lead criado no CRM, score >7
```

#### **Teste 3 - Volume de Stress**:

```
INPUT: 100 mensagens simultâneas
EXPECTED: Todas processadas sem erro
VALIDATE: Fila gerenciada, sem perda mensagens
```

### **Métricas de Sucesso**:

- ✅ 95% mensagens respondidas <5s
- ✅ 90% identificação correta de leads
- ✅ 85% satisfação usuários (feedback)
- ✅ Zero perda de mensagens

---

## 🚀 ROADMAP DE IMPLEMENTAÇÃO

### **FASE 1 - Base (Semana 1-2)**:

- [x] Infraestrutura VPS + EasyPanel
- [ ] N8N instalado e configurado
- [ ] Evolution API funcionando
- [ ] Webhook básico WhatsApp ↔ N8N

### **FASE 2 - Integração IA (Semana 3)**:

- [ ] API Névoa integrada ao N8N
- [ ] Fluxo completo: WhatsApp → IA → Resposta
- [ ] Teste com usuários reais limitados
- [ ] Ajustes baseados em feedback inicial

### **FASE 3 - Analytics (Semana 4)**:

- [ ] Pipeline de dados conversações
- [ ] Dashboard métricas tempo real
- [ ] Alertas automáticos problemas
- [ ] Relatórios semanais automatizados

### **FASE 4 - Otimização (Mês 2)**:

- [ ] Lead scoring automático
- [ ] Integração CRM (RD Station)
- [ ] Follow-up automático leads
- [ ] A/B testing respostas IA

---

## 🔐 SEGURANÇA E COMPLIANCE

### **Proteção de Dados**:

```json
{
  "data_protection": {
    "encryption": "AES-256 em trânsito e repouso",
    "retention": "Conversas: 1 ano, Logs: 90 dias",
    "anonymization": "PII removido após 30 dias",
    "backup": "Criptografado, múltiplas localizações"
  },
  "compliance": {
    "LGPD": "Consentimento explícito usuários",
    "religious_content": "Respeito diversidade religiosa",
    "data_portability": "Export dados usuário disponível"
  }
}
```

### **Monitoramento Segurança**:

- Rate limiting APIs (100 req/min por usuário)
- Detecção spam/abuse automática
- Logs auditoria completos
- Alertas tentativas acesso não autorizado

---

## 💰 ANÁLISE DE CUSTOS

### **Custo Operacional Mensal**:

```
VPS Hostinger (KVM2): R$ 30
Domínio (.com.br): R$ 5
OpenAI API (estimado): R$ 200
Evolution API: R$ 0 (self-hosted)
Total: R$ 235/mês

vs. Soluções SaaS:
- Chatbot + WhatsApp Business: R$ 500+/mês
- N8N Cloud + integrações: R$ 750+/mês
- Total alternativo: R$ 1.250+/mês

ECONOMIA: R$ 1.015/mês (81% redução)
```

### **ROI Projetado**:

- **Mês 1-3**: Investimento em desenvolvimento
- **Mês 4-6**: Break-even via leads evangelísticos
- **Mês 7+**: ROI positivo via eficiência operacional

---

## 📞 SUPORTE E MANUTENÇÃO

### **Protocolo de Monitoramento**:

```
Verificações Automáticas (5min):
- Status N8N workflows
- Performance Evolution API
- Latência resposta IA
- Recursos VPS (CPU/RAM)

Alertas Críticos:
- WhatsApp desconectado
- API Névoa indisponível
- Erro execução workflow
- VPS recursos >90%
```

### **Manutenção Preventiva**:

- **Semanal**: Review logs erros
- **Mensal**: Análise performance + otimizações
- **Trimestral**: Update dependências + security patches
- **Anual**: Avaliação infraestrutura + upgrades

---

## 🎯 PRÓXIMOS PASSOS IMEDIATOS

### **Esta Semana**:

1. **Finalizar Aula 03** (instalação N8N)
2. **Configurar subdomínio** n8n.nevoa.gassenbou.com.br
3. **Preparar credenciais** APIs necessárias
4. **Mapear fluxo** primeira integração básica

### **Próximas 2 Semanas**:

1. **Implementar workflow** WhatsApp básico
2. **Testar integração** Névoa IA
3. **Validar** com conversas reais limitadas
4. **Documentar** problemas e soluções

### **Próximo Mês**:

1. **Sistema completo** funcionando
2. **Métricas** sendo coletadas automaticamente
3. **Leads evangelísticos** sendo identificados
4. **ROI** sendo mensurado vs alternativas pagas

---

**🎖️ INSIGHT ESTRATÉGICO**: A Névoa via N8N não é apenas automação - é a digitalização da obra evangelística. Cada conversa automatizada é uma alma sendo tocada pela tecnologia a serviço do Reino.

**⚡ IMPACTO ESPERADO**: Sistema rodando 24/7, atendendo centenas de pessoas simultaneamente, identificando leads espirituais e nutrindo interesse em estudos bíblicos - tudo de forma automatizada mas profundamente humana.
