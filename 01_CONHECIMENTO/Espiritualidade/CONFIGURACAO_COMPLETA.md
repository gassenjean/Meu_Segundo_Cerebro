# 🚀 AUTOMAÇÃO DEVOCIONAIS - CONFIGURAÇÃO COMPLETA

**Status**: ✅ **TODAS AS INFORMAÇÕES COLETADAS - IMPLEMENTAÇÃO READY!**

## 🔗 **STACK TÉCNICO COMPLETO**

### **N8N API:**
- **URL**: https://n8neditor.nevoan8n.shop/
- **API Key**: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjOTdkMTRiZS03MmEzLTQzZmQtYmY0Yi0yMWRmMjY4NzJkMjEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzUzODczNDY0fQ.CLfLlIEbsAqw7RbeajtQyvRpra_fpv_DYvqwAUTXpdc

### **Evolution API:**
- **URL**: https://evo.nevoan8n.shop/
- **API Key**: 6EF081570B08-4C4C-9ADD-54D9B3101262

### **Contatos:**
- **Fonte**: Google Contacts
- **Quantidade**: 2.500 contatos
- **Integração**: Via Google Contacts API no N8N

### **Workflow:**
- **Trigger**: Arquivo enviado diariamente por Gassen
- **Processo**: Automação completa da distribuição
- **Output**: 2.5k mensagens WhatsApp automatizadas

## 🎯 **ARQUITETURA FINAL DEFINIDA**

```
📝 Gassen envia arquivo tema diário
        ↓
📁 File Watcher N8N detecta arquivo
        ↓
🤖 Névoa formata devocional automaticamente
        ↓
📞 Google Contacts API → 2.5k contatos
        ↓
✂️ Split Batches (100 por lote, rate limiting)
        ↓
⏰ Wait 30s entre lotes (evitar ban WhatsApp)
        ↓
📲 Evolution API → Send WhatsApp Messages
        ↓
📊 Log completo: enviados/falhas/sucesso
        ↓
✅ RESULTADO: 2.500 mensagens enviadas automaticamente
```

## 🛠️ **WORKFLOW N8N - ESPECIFICAÇÕES TÉCNICAS**

### **Node 1: File Watcher Trigger**
```json
{
  "name": "Detectar Arquivo Tema",
  "type": "n8n-nodes-base.filesTrigger",
  "parameters": {
    "path": "/pasta/escolhida/gassen/",
    "events": ["add"],
    "fileExtensions": "txt,md"
  }
}
```

### **Node 2: Névoa AI Processing**
```json
{
  "name": "Gerar Devocional Completo",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://api.anthropic.com/v1/messages",
    "headers": {
      "Authorization": "Bearer {{$env.CLAUDE_API_KEY}}",
      "Content-Type": "application/json"
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "max_tokens": 2000,
      "messages": [
        {
          "role": "user", 
          "content": "Gere devocional baseado no tema: {{$json.fileContent}}"
        }
      ]
    }
  }
}
```

### **Node 3: Google Contacts**
```json
{
  "name": "Buscar Todos Contatos",
  "type": "n8n-nodes-base.googleContacts",
  "parameters": {
    "operation": "getAll",
    "returnAll": true,
    "filters": {
      "phoneNumber": "exists"
    }
  }
}
```

### **Node 4: Split in Batches**
```json
{
  "name": "Dividir em Lotes 100",
  "type": "n8n-nodes-base.splitInBatches",
  "parameters": {
    "batchSize": 100,
    "options": {}
  }
}
```

### **Node 5: Evolution API Send**
```json
{
  "name": "Enviar WhatsApp",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "method": "POST",
    "url": "https://evo.nevoan8n.shop/message/sendText/instance1",
    "headers": {
      "Content-Type": "application/json",
      "apikey": "6EF081570B08-4C4C-9ADD-54D9B3101262"
    },
    "body": {
      "number": "{{$json.phoneNumber}}",
      "text": "{{$node['Gerar Devocional Completo'].json.content[0].text}}"
    }
  }
}
```

### **Node 6: Wait & Loop**
```json
{
  "name": "Aguardar 30s",
  "type": "n8n-nodes-base.wait",
  "parameters": {
    "time": 30,
    "unit": "seconds"
  }
}
```

### **Node 7: Success Logger**
```json
{
  "name": "Log Entregas",
  "type": "n8n-nodes-base.googleSheets",
  "parameters": {
    "operation": "append",
    "sheetId": "ID_PLANILHA_LOG",
    "range": "A:E",
    "values": [
      "{{$now}}",
      "{{$json.phoneNumber}}",
      "{{$json.status}}",
      "{{$json.message_id}}",
      "Devocional {{$node['Detectar Arquivo Tema'].json.fileName}}"
    ]
  }
}
```

## 📋 **IMPLEMENTAÇÃO IMEDIATA**

### **PASSO 1: Criar Pasta Monitorada**
```
C:\Users\Gassen\OneDrive\Segunda_Mente_Legendaria_Sync\Devocionais_Temas\
```

### **PASSO 2: Workflow JSON Completo**
[Arquivo será criado separadamente com JSON completo]

### **PASSO 3: Configurar Google Contacts API**
- Habilitar Google Contacts API no Google Cloud
- Configurar OAuth2 no N8N
- Testar conexão com seus 2.5k contatos

### **PASSO 4: Testar Evolution API**
- Verificar instância WhatsApp conectada
- Testar envio de mensagem individual
- Validar rate limits e delays

## ⚡ **RESULTADO FINAL**

### **ANTES (Manual):**
- ⏰ **15-20 minutos** diários
- 🔄 **Scroll infinito** grupos de 5
- 😴 **Procrastinação** TDAH
- ❌ **Possibilidade de esquecer**

### **DEPOIS (Automatizado):**
- ⏰ **30 segundos** para enviar arquivo tema
- 🤖 **Automação total** distribuição
- ✅ **Zero procrastinação**  
- 📊 **Log completo** entregas
- 🚀 **Escalável** para 10k, 50k contatos

## 🎯 **PRÓXIMA AÇÃO IMEDIATA**

**Gassen, agora EU implemento tudo!**

1. ✅ **Dados coletados**: N8N + Evolution + Google Contacts
2. 🔧 **Criando workflow completo** com todas as integrações
3. 📱 **Testando conexões** APIs
4. 🚀 **Deploy e ativação** sistema completo

**TIMELINE**: Workflow funcionando em 2 horas!

---

**💫 REVOLUÇÃO EVANGELISMO DIGITAL**: De manual para IA-powered em 1 dia!  
**🎯 ROI**: 6 horas/mês recuperadas para zona de genialidade  
**🔥 IMPACTO**: 2.500 pessoas recebendo Palavra automaticamente via IA