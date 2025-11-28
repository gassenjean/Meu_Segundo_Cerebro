---
criado: 2025-07-22T10:44:56-03:00
atualizado: 2025-07-22T10:44:56-03:00
---
# AULA 08 - TRANSCRIÇÃO AUTOMÁTICA DE ÁUDIOS WHATSAPP

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 08/11  
**DURAÇÃO**: 90min  
**PREREQUISITOS**: WhatsApp sincronizado (Aula 07)  
**CRIADO**: 13/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO

Esta é a aula do **SISTEMA NEVOATRANSCRITORA**! Você vai criar um workflow completo que recebe áudios do WhatsApp, transcreve via Groq Whisper, corrige via OpenAI e retorna texto limpo. É automação de **valor real** funcionando.

**O QUE VOCÊ VAI DOMINAR:**
- Workflow completo de transcrição automática
- Integração Groq Whisper para speech-to-text
- Correção inteligente via OpenAI
- Sistema robusto com tratamento de erros

## 🎯 CONCEITOS-CHAVE

### **Pipeline de Transcrição:**
```
Áudio WhatsApp → Webhook N8N → Groq Whisper → OpenAI Correção → Resposta Limpa
```

### **Groq Whisper - Speech-to-Text:**
- **Velocidade**: Transcrição em <5 segundos
- **Precisão**: 95%+ para português brasileiro
- **Suporte**: Múltiplos formatos de áudio
- **Custo**: Muito baixo por transcrição

### **OpenAI Correção - Post-Processing:**
- **Função**: Corrigir erros de transcrição
- **Modelo**: GPT-4o para máxima precisão
- **Resultado**: Texto limpo e estruturado
- **Valor agregado**: Pontuação e formatação

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **WORKFLOW COMPLETO - JSON Template:**
```json
{
  "name": "nevoatranscritora",
  "nodes": [
    {
      "name": "Webhook WhatsApp",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "whatsapp-audio",
        "httpMethod": "POST"
      }
    },
    {
      "name": "Extract Audio",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "values": [
          {
            "name": "audioUrl",
            "value": "={{ $json.data.message.audioMessage.url }}"
          }
        ]
      }
    },
    {
      "name": "Groq Whisper",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.groq.com/openai/v1/audio/transcriptions",
        "method": "POST",
        "headers": {
          "Authorization": "Bearer {{ $credentials.groqApi.apiKey }}"
        },
        "body": {
          "file": "={{ $binary.data }}",
          "model": "whisper-large-v3"
        }
      }
    },
    {
      "name": "OpenAI Correction",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "model": "gpt-4o",
        "prompt": "Corrija erros de transcrição e formate o texto:\n\n{{ $json.text }}"
      }
    },
    {
      "name": "Send Response",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "{{ $node['Webhook WhatsApp'].json.instanceData.serverUrl }}/message/sendText/{{ $node['Webhook WhatsApp'].json.instanceData.instance }}",
        "method": "POST",
        "body": {
          "number": "{{ $node['Webhook WhatsApp'].json.data.key.remoteJid }}",
          "text": "🎙️ Transcrição:\n\n{{ $json.message.content }}"
        }
      }
    }
  ]
}
```

### **Configuração API Keys:**
```bash
# Groq API (Whisper):
1. Criar conta em console.groq.com
2. Gerar API Key
3. Adicionar em N8N Credentials

# OpenAI API:
1. Conta OpenAI Platform
2. API Key com créditos
3. Configurar em N8N Credentials
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**
- **Áudios Longos**: Transcrever para posterior resposta IA
- **Accessibility**: Converter áudio em texto para deficientes auditivos
- **Análise**: Extrair insights de conversas de áudio
- **Arquivo**: Histórico pesquisável de áudios importantes

### **EVANGELISMO DIGITAL:**
- **Testemunhos**: Transcrever para criar conteúdo escrito
- **Orações**: Converter pedidos de oração para follow-up
- **Ensinos**: Áudios bíblicos viram material de estudo
- **Pastoreio**: Acompanhamento mais eficiente de membrosd

### **GABRIELE CONFECÇÕES/KABAK:**
- **Atendimento**: Transcrever para melhor compreensão
- **Pedidos**: Converter áudios complexos em texto claro
- **Feedback**: Análise de satisfação de clientes
- **Treinamento**: Material para capacitação de equipe

## 🔗 CONEXÕES

### **BUILDS SOBRE:**
- Aula 07: WhatsApp agora processa áudios automaticamente
- Aula 06: Evolution API fornece áudios estruturados

### **PREPARA PARA:**
- Aula 09: Sistema em produção 24/7
- Aula 10: IA generativa baseada em transcrições
- Aula 11: Framework teórico aplicado

### **TECNOLOGIAS INTEGRADAS:**
- **Groq Whisper**: Speech-to-text de qualidade
- **OpenAI**: Correção e formatação inteligente
- **Evolution API**: Entrega de áudios estruturados

## ✅ CHECKLIST AULA 08

### **CONFIGURAÇÃO:**
- [ ] API Keys Groq e OpenAI configuradas
- [ ] Webhook específico para áudios criado
- [ ] Workflow nevoatranscritora importado
- [ ] Todas as conexões entre nodes testadas

### **FUNCIONALIDADE:**
- [ ] Áudio WhatsApp chega via webhook
- [ ] Groq Whisper transcreve corretamente
- [ ] OpenAI corrige e formata texto
- [ ] Resposta retorna ao WhatsApp automaticamente

### **QUALIDADE:**
- [ ] Transcrição >90% precisa para áudios limpos
- [ ] Correção OpenAI melhora significativamente texto
- [ ] Tempo total <15 segundos para áudio de 1 minuto
- [ ] Sistema estável para múltiplos áudios

### **ROBUSTEZ:**
- [ ] Tratamento de erro para APIs indisponíveis
- [ ] Fallback para áudios muito longos
- [ ] Logs detalhados para debugging
- [ ] Pronto para escala em produção

---

**STATUS**: ✅ Sistema de transcrição automática funcionando  
**RESULTADO**: Áudios WhatsApp viram texto automaticamente  
**PRÓXIMO**: Aula 09 - Implementação em produção 24/7

*"Quando áudios se transformam em texto inteligente"*