# AULA 15 - ECOSSISTEMA LLMS E REQUISIÇÕES HTTP

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 15/11  
**DURAÇÃO**: 45min  
**PREREQUISITOS**: Aula 14 - HTTP Request  
**CRIADO**: 28/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO
- **Dominará todos os LLMs**: ChatGPT, Claude, Gemini, Groq, Perplexity e outros
- **Mestre das requisições HTTP**: estrutura, headers, body para cada modelo
- **Integração N8N universal**: conectar qualquer LLM em automações

## 🎯 CONCEITOS-CHAVE

### **Anatomia Requisição HTTP para LLMs**
- **URL**: Endpoint específico de cada provedor
- **Headers**: Autenticação (Bearer, API-Key) + Content-Type
- **Body**: Payload JSON com modelo, mensagens e parâmetros

### **Diferenças Entre Provedores**
- **OpenAI**: `/v1/chat/completions` + Bearer token
- **Claude**: `/v1/messages` + x-api-key header  
- **Gemini**: `/v1beta/models/{model}:generateContent` + key param
- **Groq**: `/openai/v1/chat/completions` + Bearer token
- **Perplexity**: `/chat/completions` + Bearer token

### **Estruturas de Mensagem**
- **Padrão**: `{"role": "user", "content": "texto"}`
- **Claude**: `{"role": "user", "content": [{"type": "text", "text": "..."}]}`
- **Sistema**: role "system" para contexto/personalidade

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **Template Básico N8N - HTTP Request LLM**
```json
{
  "method": "POST",
  "url": "https://api.openai.com/v1/chat/completions",
  "headers": {
    "Authorization": "Bearer {{$env.OPENAI_API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "Você é um assistente especializado"},
      {"role": "user", "content": "{{$node.Webhook.json.text}}"}
    ],
    "max_tokens": 1000,
    "temperature": 0.7
  }
}
```

### **Workflow Multi-LLM Inteligente**
1. **Node Webhook**: Recebe input do usuário
2. **Node Switch**: Escolhe LLM baseado em critério
3. **Nodes HTTP Request**: Um para cada LLM
4. **Node Merge**: Combina respostas
5. **Node Response**: Retorna resultado final

### **Gestão de API Keys**
- Usar variáveis de ambiente: `{{$env.OPENAI_API_KEY}}`
- Configurar em Settings > Environment variables
- Nunca hardcoded no workflow

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA**:
- **Fallback inteligente**: OpenAI principal → Claude backup → Groq emergencial
- **Especialização por modelo**: GPT-4 (texto), Claude (análise), Groq (velocidade)
- **Cost optimization**: Groq para respostas simples, GPT-4 para complexas

### **EVANGELISMO DIGITAL**:
- **Geração conteúdo**: Claude para reflexões profundas
- **Imagens**: DALL-E para ilustrações bíblicas
- **Velocidade**: Groq para respostas rápidas em lives

### **GABRIELE CONFECÇÕES/KABAK**:
- **Atendimento**: Groq para respostas instantâneas
- **Copywriting**: GPT-4 para descrições de produtos
- **Análise feedback**: Claude para insights de clientes

## 🔗 CONEXÕES

### **BUILDS SOBRE**:
- Aula 14: HTTP Request fundamentals
- Aula 10: IA Generativa básica
- Aula 08: Integração WhatsApp

### **PREPARA PARA**:
- Próxima: Orquestração avançada de múltiplos LLMs
- Pipeline de IA distribuída
- Otimização de custos automatizada

## ✅ CHECKLIST AULA 15

### **CONCEITUAL**:
- [ ] Entendo diferenças entre provedores LLM
- [ ] Sei estruturar requisições HTTP para cada um
- [ ] Compreendo vantagens/desvantagens de cada modelo

### **PRÁTICO**:
- [ ] Configurei pelo menos 3 LLMs diferentes no N8N
- [ ] Criei workflow com fallback automático
- [ ] Testei geração de texto e imagem

### **APLICAÇÃO**:
- [ ] Implementei multi-LLM em projeto real
- [ ] Configurei otimização de custos
- [ ] Documentei performance de cada modelo

---
**STATUS**: ✅ Ecossistema LLM dominado - requisições HTTP universais
**PRÓXIMO**: Orquestração avançada e otimização de custos