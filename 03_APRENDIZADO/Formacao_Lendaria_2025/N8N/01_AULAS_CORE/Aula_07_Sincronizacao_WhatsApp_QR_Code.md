---
criado: 2025-07-22T10:44:21-03:00
atualizado: 2025-07-22T10:44:21-03:00
---
# AULA 07 - SINCRONIZAÇÃO WHATSAPP VIA QR CODE

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 07/11  
**DURAÇÃO**: 45min  
**PREREQUISITOS**: Evolution Manager funcionando (Aula 06)  
**CRIADO**: 12/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO

Esta é a aula do **PRIMEIRO MILAGRE**! Você vai conectar seu WhatsApp pessoal/business ao Evolution API via QR Code e ver sua primeira automação funcionando. É o momento onde teoria vira **automação real**.

**O QUE VOCÊ VAI DOMINAR:**
- Sincronização WhatsApp via QR Code no Manager
- Configuração webhook Evolution → N8N
- Primeiro workflow automatizado funcionando
- Troubleshooting de conexão WhatsApp

## 🎯 CONCEITOS-CHAVE

### **QR Code - Ponte WhatsApp Web:**
- **Tecnologia**: Mesmo sistema do WhatsApp Web
- **Segurança**: Conexão criptografada end-to-end
- **Persistência**: Sessão mantida no PostgreSQL
- **Renovação**: QR expira em 60 segundos, auto-renova

### **Fluxo de Sincronização:**
```
WhatsApp Mobile → QR Code → Evolution API → PostgreSQL
                                   ↓
                              Webhook N8N
                                   ↓
                            Automação Ativa
```

### **Estados de Conexão:**
- **DISCONNECTED**: Aguardando QR Code
- **CONNECTING**: QR escaneado, sincronizando
- **CONNECTED**: Operacional, recebendo mensagens
- **LOST**: Conexão perdida, necessita re-sync

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **PASSO 1: Criar Instância WhatsApp**
```javascript
// Evolution Manager → Nova Instância
{
  "instanceName": "minha-primeira-automacao",
  "webhook": "http://n8n:5678/webhook-test/whatsapp",
  "events": ["MESSAGES_UPSERT"],
  "qrcode": true,
  "markMessagesRead": false,
  "alwaysOnline": true
}
```

### **PASSO 2: Escanear QR Code**
```bash
# No Manager Evolution:
1. Clicar em "Connect" na instância criada
2. QR Code aparece na tela
3. WhatsApp → Aparelhos Conectados → Conectar Aparelho
4. Escanear QR Code com celular
5. Aguardar status "CONNECTED"
```

### **PASSO 3: N8N Webhook Simples**
```json
{
  "nodes": [
    {
      "name": "Webhook WhatsApp",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "whatsapp",
        "httpMethod": "POST",
        "responseMode": "respondToWebhook"
      }
    },
    {
      "name": "Debug Message",
      "type": "n8n-nodes-base.noOp",
      "parameters": {}
    }
  ],
  "connections": {
    "Webhook WhatsApp": {
      "main": [["Debug Message"]]
    }
  }
}
```

### **PASSO 4: Teste de Comunicação**
```bash
# Enviar mensagem para o WhatsApp conectado
# Verificar se chegou no N8N via webhook
# Logs do Evolution Manager mostram atividade
# PostgreSQL registra a mensagem
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**
- **Instância Pessoal**: WhatsApp principal para IA
- **Webhook Dedicado**: `/webhook/nevoa-ia`
- **Eventos**: Apenas MESSAGES_UPSERT (mensagens recebidas)
- **Auto-resposta**: Sistema responde automaticamente

### **EVANGELISMO DIGITAL:**
- **WhatsApp Pastoral**: Número dedicado para ministério
- **Webhook Pastoral**: `/webhook/evangelismo`
- **Filtros**: Mensagens com palavras-chave espirituais
- **Follow-up**: Sequências automáticas de discipulado

### **GABRIELE CONFECÇÕES/KABAK:**
- **WhatsApp Business**: Atendimento comercial
- **Webhook Comercial**: `/webhook/comercial`
- **Horário**: Automação apenas horário comercial
- **Escalação**: Humano assume se necessário

## 🔗 CONEXÕES

### **BUILDS SOBRE:**
- Aula 06: Manager Evolution agora é usado na prática
- Aula 04: Evolution API finalmente conectado

### **PREPARA PARA:**
- Aula 08: Transcrição automática de áudios
- Aula 09: Sistema completo em produção 24/7
- Aula 10+: IA generativa e casos avançados

### **MARCO CRÍTICO:**
- **Primeira automação funcionando**
- **WhatsApp integrado ao N8N**
- **Base para todos os workflows futuros**

## ✅ CHECKLIST AULA 07

### **SINCRONIZAÇÃO:**
- [ ] Instância WhatsApp criada no Manager
- [ ] QR Code gerado e visível
- [ ] WhatsApp mobile escaneou QR com sucesso
- [ ] Status "CONNECTED" confirmado

### **INTEGRAÇÃO N8N:**
- [ ] Webhook N8N criado e ativo
- [ ] URL webhook configurada na instância
- [ ] Teste de envio de mensagem realizado
- [ ] N8N recebeu dados via webhook

### **FUNCIONAMENTO:**
- [ ] Mensagens chegando em tempo real
- [ ] Logs Evolution mostrando atividade
- [ ] PostgreSQL registrando dados
- [ ] Sistema estável por 15+ minutos

### **VALIDAÇÃO COMPLETA:**
- [ ] Múltiplas mensagens testadas
- [ ] Diferentes tipos (texto, emoji, etc.)
- [ ] Performance consistente
- [ ] Pronto para workflows avançados

---

**STATUS**: ✅ WhatsApp sincronizado e automação funcionando  
**RESULTADO**: Primeira ponte real entre WhatsApp e N8N  
**PRÓXIMO**: Aula 08 - Transcrição automática de áudios

*"O momento onde teoria vira automação real"*