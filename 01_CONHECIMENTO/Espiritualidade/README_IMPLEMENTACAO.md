---
criado: 2026-01-14T12:22:26-03:00
atualizado: 2026-01-14T12:22:26-03:00
---
# 🚀 AUTOMAÇÃO DEVOCIONAIS N8N - FASE 1

**Criado**: 29/07/2025 por Névoa  
**Status**: 🟡 Implementação em andamento  
**Objetivo**: Eliminar 15-20min diários de envio manual  

## ✅ PROGRESSO ATUAL

### **CONECTIVIDADE ESTABELECIDA:**
- ✅ **N8N VPS**: https://n8neditor.nevoan8n.shop/
- ✅ **API Key**: Criada e configurada
- ✅ **Domínio**: nevoan8n.shop (personalizado)
- ✅ **Evolution API**: Presumidamente configurada

### **PRÓXIMOS PASSOS:**
1. **Testar conexão API** via JavaScript
2. **Listar workflows existentes** 
3. **Criar workflow base** automação devocionais
4. **Configurar contatos** Google Contacts
5. **Implementar rate limiting** WhatsApp
6. **Teste completo** com devocional real

## 🎯 ARQUITETURA PLANEJADA

```
📱 Névoa → Devocional (Obsidian)
        ↓
🔔 File Watcher (N8N detecta arquivo novo)
        ↓
📖 Read File → Format WhatsApp
        ↓
📞 Google Contacts → Get 2.5k contatos
        ↓
✂️ Split Batches (100 por lote)
        ↓
⏰ Wait 30s (rate limiting)
        ↓
📲 Evolution API → WhatsApp send
        ↓
📊 Log success/failures
```

## 🛠️ CONFIGURAÇÕES TÉCNICAS

### **API N8N:**
```javascript
const API_KEY = "eyJhbGci..."; // JWT token
const N8N_URL = "https://n8neditor.nevoan8n.shop";
```

### **Headers Necessários:**
```javascript
{
    'X-N8N-API-KEY': API_KEY,
    'Content-Type': 'application/json'
}
```

### **Endpoints Principais:**
- **GET** `/api/v1/workflows` - Listar workflows
- **POST** `/api/v1/workflows` - Criar workflow
- **GET** `/api/v1/workflows/{id}/execute` - Executar workflow

## 📋 WORKFLOW TEMPLATE

```json
{
  "name": "Automacao-Devocionais-WhatsApp-Nevoa",
  "active": true,
  "nodes": [
    {
      "name": "File Watcher Trigger",
      "type": "n8n-nodes-base.filesTrigger",
      "parameters": {
        "path": "/caminho/obsidian/devocionais/",
        "events": ["add"]
      }
    },
    {
      "name": "Read Devocional",
      "type": "n8n-nodes-base.readFile"
    },
    {
      "name": "Google Contacts",
      "type": "n8n-nodes-base.googleContacts",
      "parameters": {
        "operation": "getAll",
        "returnAll": true
      }
    },
    {
      "name": "Split in Batches",
      "type": "n8n-nodes-base.splitInBatches",
      "parameters": {
        "batchSize": 100
      }
    },
    {
      "name": "Send WhatsApp",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "POST",
        "url": "http://evolution-api/message/sendText",
        "headers": {
          "apikey": "{{$env.EVOLUTION_API_KEY}}"
        }
      }
    }
  ]
}
```

## 🚨 PENDÊNCIAS CRÍTICAS

### **INFORMAÇÕES NECESSÁRIAS:**
- [ ] **Contatos**: Confirmação se estão no Google Contacts
- [ ] **Evolution API**: URL e API key
- [ ] **Horário**: Quando enviar automaticamente?
- [ ] **Pasta**: Onde salvar devocionais no Obsidian?

### **TESTES NECESSÁRIOS:**
- [ ] Conexão N8N API funcionando
- [ ] Google Contacts acessível
- [ ] Evolution API operacional
- [ ] Rate limiting WhatsApp testado

## ⚡ AÇÃO IMEDIATA

**Gassen, preciso de você:**

1. **Confirme onde estão os 2.5k contatos** (Google Contacts?)
2. **URL da Evolution API** do seu VPS
3. **Pasta preferida** para salvar devocionais no Obsidian

Com essas 3 informações, finalizo o workflow em 1 hora!

---

**💫 OBJETIVO**: De 20 minutos manuais → 30 segundos automáticos  
**🎯 RESULTADO**: 6 horas/mês recuperadas para zona de genialidade  
**🚀 TIMELINE**: Primeira automação funcionando hoje!