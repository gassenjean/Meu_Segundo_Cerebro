---
criado: 2025-07-22T10:42:15-03:00
atualizado: 2025-07-22T10:42:15-03:00
---

# AULA 04 - INSTALAÇÃO E CONFIGURAÇÃO EVOLUTION API

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 04/11  
**DURAÇÃO**: 90min  
**PREREQUISITOS**: N8N modo fila funcionando (Aula 03)  
**CRIADO**: 10/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

Esta aula instala o **Evolution API** - a ponte crítica entre WhatsApp e N8N. Com este componente, você terá controle total sobre comunicação automatizada em seus projetos. É a diferença entre ter um cérebro digital e ter um cérebro digital que **fala com o mundo**.

**O QUE VOCÊ VAI DOMINAR:**

- Instalação completa Evolution API no EasyPanel
- Configuração PostgreSQL + Redis para Evolution
- Integração com N8N para automações WhatsApp
- Setup inicial para receber mensagens

## 🎯 CONCEITOS-CHAVE

### **Evolution API - Gateway WhatsApp:**

- **Função**: Conecta N8N ↔ WhatsApp Business
- **Poder**: Automação completa de conversas, leads, atendimento
- **Diferencial**: API robusta vs soluções amadoras
- **Aplicação**: Base para evangelismo digital e comercial

### **Arquitetura de Comunicação:**

```
WhatsApp Business ↔ Evolution API ↔ N8N
                          ↓
                PostgreSQL + Redis
                          ↓
                   Seus Projetos
```

### **Componentes Evolution:**

- **Core**: Servidor principal da API
- **Manager**: Interface web para gerenciamento
- **Database**: PostgreSQL para persistência
- **Cache**: Redis para performance

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **PASSO 1: PostgreSQL Evolution**

```yaml
# EasyPanel → Add Service → PostgreSQL
Name: evolution-postgres
Database: evolution_db
Username: evolution_user
Password: [senha-forte-evolution]
Port: 5432
Volume: evolution_postgres_data
```

### **PASSO 2: Redis Evolution**

```yaml
# EasyPanel → Add Service → Redis
Name: evolution-redis
Password: [senha-forte-redis-evolution]
Port: 6379
Volume: evolution_redis_data
```

### **PASSO 3: Evolution API Core**

```yaml
# Docker Image: atendai/evolution-api:latest
Environment Variables:
  - DATABASE_URL=postgresql://evolution_user:[senha]@evolution-postgres:5432/evolution_db
  - REDIS_URI=redis://:[senha-redis]@evolution-redis:6379
  - AUTHENTICATION_API_KEY=[chave-api-forte]
  - SERVER_PORT=8080
  - DEL_INSTANCE=false
  - WEBHOOK_GLOBAL_URL=
  - WEBHOOK_GLOBAL_ENABLED=false
```

### **PASSO 4: Evolution Manager**

```yaml
# Docker Image: atendai/evolution-manager:latest
Environment Variables:
  - DATABASE_URL=postgresql://evolution_user:[senha]@evolution-postgres:5432/evolution_db
  - NEXT_PUBLIC_MANAGER_PORT=3000
  - NEXT_PUBLIC_EVOLUTION_API_URL=http://evolution-api:8080
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**

- **Conversas**: WhatsApp como canal principal
- **Processamento**: Mensagens → Evolution → N8N → IA → Resposta
- **Escalabilidade**: Múltiplos números WhatsApp
- **Monitoramento**: Logs completos de interações

### **EVANGELISMO DIGITAL:**

- **Lead Capture**: WhatsApp como porta de entrada
- **Nurturing**: Sequências automáticas espirituais
- **Follow-up**: Acompanhamento personalizado
- **Analytics**: Métricas de engajamento espiritual

### **GABRIELE CONFECÇÕES/KABAK:**

- **Atendimento**: WhatsApp Business automatizado
- **Vendas**: Catálogo e pedidos via WhatsApp
- **Suporte**: Resolução automática dúvidas
- **Remarketing**: Campanhas via WhatsApp

## 🔗 CONEXÕES

### **BUILDS SOBRE:**

- Aula 03: N8N agora tem canal de comunicação
- PostgreSQL/Redis já configurados

### **PREPARA PARA:**

- Aula 05: Chatwoot centralizará as conversas
- Aula 06: Funcionamento detalhado da Evolution
- Aula 07: Sincronização WhatsApp via QR Code

### **INTEGRAÇÃO CRÍTICA:**

- Evolution + N8N = automações WhatsApp
- PostgreSQL = persistência de conversas
- Redis = performance em tempo real

## ✅ CHECKLIST AULA 04

### **INFRAESTRUTURA:**

- [ ] PostgreSQL Evolution instalado e acessível
- [ ] Redis Evolution funcionando com autenticação
- [ ] Rede entre serviços configurada corretamente
- [ ] Volumes persistentes criados

### **EVOLUTION API:**

- [ ] Evolution Core rodando sem erros
- [ ] API respondendo em http://evolution-api:8080
- [ ] Logs indicando conexão com banco
- [ ] Manager interface acessível

### **CONFIGURAÇÃO:**

- [ ] Variáveis de ambiente corretas
- [ ] Chave API segura definida
- [ ] Conexão PostgreSQL testada
- [ ] Redis cache funcionando

### **INTEGRAÇÃO:**

- [ ] Evolution Manager acessível via navegador
- [ ] Interface responsiva e estável
- [ ] Pronto para sincronização WhatsApp
- [ ] Aguardando configuração N8N (próximas aulas)

---

**STATUS**: ✅ Evolution API operacional e integrado  
**RESULTADO**: WhatsApp Business pronto para automações  
**PRÓXIMO**: Aula 05 - Chatwoot como centralizador de comunicação

_"Evolution API: transformando WhatsApp em ferramenta empresarial"_
