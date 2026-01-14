# AULA 17 - Implementação Projeto Final

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 17/11  
**DURAÇÃO**: 90min  
**PREREQUISITOS**: Aulas 1-16 completas  
**CRIADO**: 31/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

- Implementação prática completa do sistema de classificação de leads com IA
- Construção passo a passo: Formulário → IA → CRM → WhatsApp automatizado
- Sistema final operacional pronto para uso em projetos reais

## 🎯 CONCEITOS-CHAVE

### 1. **Arquitetura de Implementação**

- **Node 1**: Webhook Trigger (recebe formulário)
- **Node 2**: IA Classificadora (OpenAI/GPT-4)
- **Node 3**: Switch condicional (3 branches)
- **Nodes 4-6**: IAs especializadas (ChatGPT, Gemini, DeepSeek)
- **Nodes 7-9**: CRM automation (Airtable/Notion/Mock)
- **Nodes 10-12**: WhatsApp personalizados (Evolution API)

### 2. **Estrutura de Dados Padronizada**

```javascript
// Formulário Input
{
  "nome": "string",
  "empresa": "string",
  "porte": "Micro/Pequeno/Médio/Grande",
  "urgencia": "Imediata/30 dias/Pesquisando",
  "volume": "<50/50-200/>200 por dia",
  "orcamento": "<2k/2-5k/5-15k/>15k"
}

// Output Classificação
{
  "tipo": "quente/morno/frio",
  "score": 1-10,
  "prioridade": "alta/media/baixa",
  "proxima_acao": "string"
}
```

### 3. **Prompts de Classificação**

```javascript
// Prompt Master para Node 2
"Analise o lead e classifique como:
- QUENTE: Orçamento >5k + urgência imediata + grande porte
- MORNO: Orçamento 2-5k + urgência 30 dias + médio porte
- FRIO: Orçamento <2k + apenas pesquisando + pequeno porte

Responda APENAS: quente, morno ou frio"
```

### 4. **Sistema de Fallback Inteligente**

- Timeout de 30s por request
- Retry automático 3x em caso de falha
- Fallback GPT-3.5 se GPT-4 indisponível
- Log completo de erros para debugging

## 💻 IMPLEMENTAÇÃO PRÁTICA

### FASE 1: Setup Inicial

#### 1.1 Preparação N8N

```bash
# Verificar N8N rodando
curl http://n8neditor.nevoan8n.shop/healthz

# Verificar API Keys
- OpenAI: sk-...
- Google AI Studio: AIza...
- DeepSeek: sk-...
```

#### 1.2 Webhook de Entrada

```javascript
// Node 1: Webhook Trigger
{
  "httpMethod": "POST",
  "path": "lead-classifier",
  "responseMode": "responseNode",
  "options": {}
}

// URL resultado:
// https://n8neditor.nevoan8n.shop/webhook/lead-classifier
```

#### 1.3 Teste do Formulário

```html
<!-- Formulário HTML simples para teste -->
<form action="https://n8neditor.nevoan8n.shop/webhook/lead-classifier" method="POST">
  <input name="nome" placeholder="Nome" required>
  <input name="empresa" placeholder="Empresa" required>
  <select name="porte">
    <option value="Micro">Micro (até 5 funcionários)</option>
    <option value="Pequeno">Pequeno (até 20 funcionários)</option>
    <option value="Médio">Médio (até 50 funcionários)</option>
    <option value="Grande">Grande (50+ funcionários)</option
```
