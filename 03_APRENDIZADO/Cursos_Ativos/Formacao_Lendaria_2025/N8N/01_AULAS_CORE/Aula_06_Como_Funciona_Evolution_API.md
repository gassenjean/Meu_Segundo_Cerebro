---
criado: 2025-07-22T10:43:48-03:00
atualizado: 2025-07-22T10:43:48-03:00
---

# AULA 06 - COMO FUNCIONA EVOLUTION API

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 06/11  
**DURAÇÃO**: 60min  
**PREREQUISITOS**: Chatwoot instalado (Aula 05)  
**CRIADO**: 11/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

Esta aula **desmistifica** o funcionamento interno da Evolution API. Você vai compreender a arquitetura PostgreSQL + Redis + Core, dominar o Manager Evolution e preparar o sistema para automações WhatsApp avançadas.

**O QUE VOCÊ VAI DOMINAR:**

- Arquitetura interna PostgreSQL + Redis + Core Evolution
- Interface Manager Evolution para controle total
- Configuração avançada para performance máxima
- Troubleshooting completo para problemas comuns

## 🎯 CONCEITOS-CHAVE

### **Arquitetura Evolution - 3 Camadas:**

```
CAMADA 1: PostgreSQL (Persistência)
├── Instâncias WhatsApp
├── Histórico de mensagens
├── Configurações de webhook
└── Dados de autenticação

CAMADA 2: Redis (Cache + Performance)
├── Sessões ativas WhatsApp
├── Fila de mensagens
├── Cache de contatos
└── Estado real-time

CAMADA 3: Core API (Processamento)
├── Endpoints REST
├── Webhook dispatcher
├── WhatsApp Web interface
└── Manager de instâncias
```

### **Evolution Manager - Painel de Controle:**

- **Função**: Interface visual para gerenciar instâncias
- **Recursos**: Criar, deletar, monitorar WhatsApp
- **Integração**: Conecta com N8N via webhooks
- **Monitoramento**: Status real-time das conexões

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **ACESSANDO EVOLUTION MANAGER:**

```bash
# URL padrão:
http://[SEU-IP]:3000

# Login inicial:
- Sem autenticação por padrão
- Acesso direto ao dashboard
- Interface em português disponível
```

### **CRIANDO PRIMEIRA INSTÂNCIA:**

```javascript
// Manager Evolution → Nova Instância
{
  "instanceName": "nevoa-principal",
  "webhook": "http://n8n:5678/webhook/whatsapp",
  "events": [
    "MESSAGES_UPSERT",
    "MESSAGES_UPDATE",
    "MESSAGES_DELETE",
    "SEND_MESSAGE"
  ],
  "qrcode": true,
  "markMessagesRead": false
}
```

### **CONFIGURAÇÃO WEBHOOK N8N:**

```yaml
# N8N Webhook Node Configuration:
HTTP Method: POST
Path: /webhook/whatsapp
Response Mode: Respond to Webhook
Response Data: JSON
Response Code: 200
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**

- **Instância Dedicada**: "nevoa-ia" para processamento IA
- **Webhook Especializado**: Captura apenas mensagens de texto/áudio
- **Performance**: Redis cache para respostas <3 segundos
- **Monitoramento**: Logs detalhados via Manager

### **EVANGELISMO DIGITAL:**

- **Instância Pastoral**: "evangelismo-digital" para leads espirituais
- **Eventos Filtrados**: Foco em MESSAGES_UPSERT + novos contatos
- **Integração CRM**: Webhook direto para sistema de discipulado
- **Backup**: PostgreSQL com retenção 1 ano

### **GABRIELE CONFECÇÕES/KABAK:**

- **Instância Comercial**: "comercial-gabriele" para vendas
- **Catálogo Integrado**: Webhook para sistema de estoque
- **Múltiplos Atendentes**: Distribuição via Chatwoot
- **Analytics**: Métricas de conversão em tempo real

## 🔗 CONEXÕES

### **BUILDS SOBRE:**

- Aula 04: Evolution agora é compreendido internamente
- Aula 05: Chatwoot integra via Manager Evolution

### **PREPARA PARA:**

- Aula 07: QR Code e sincronização prática
- Aula 08: Workflows avançados de transcrição
- Aula 09: Produção 24/7 baseada nesta base

### **DEPENDÊNCIAS TÉCNICAS:**

- PostgreSQL estável = instâncias persistentes
- Redis ativo = performance otimizada
- Manager funcionando = controle total

## ✅ CHECKLIST AULA 06

### **COMPREENSÃO ARQUITETURAL:**

- [ ] Entendo função PostgreSQL na Evolution
- [ ] Compreendo papel do Redis para performance
- [ ] Vejo como Core API processa requisições
- [ ] Distingo Manager de API Core

### **MANAGER EVOLUTION:**

- [ ] Acesso Manager via navegador funcionando
- [ ] Interface responsiva e estável
- [ ] Dashboard mostrando status serviços
- [ ] Pronto para criar instâncias WhatsApp

### **CONFIGURAÇÃO AVANÇADA:**

- [ ] Compreendo configuração de webhooks
- [ ] Sei filtrar eventos por necessidade
- [ ] Entendo impacto de cada configuração
- [ ] Posso troubleshooting problemas básicos

### **INTEGRAÇÃO N8N:**

- [ ] Webhook N8N configurado corretamente
- [ ] Teste de comunicação Evolution → N8N
- [ ] Logs mostrando fluxo de dados
- [ ] Pronto para automações avançadas

---

**STATUS**: ✅ Evolution API completamente compreendido  
**RESULTADO**: Domínio total da arquitetura para automações  
**PRÓXIMO**: Aula 07 - Sincronização WhatsApp via QR Code

_"Compreender a arquitetura é dominar as possibilidades"_
