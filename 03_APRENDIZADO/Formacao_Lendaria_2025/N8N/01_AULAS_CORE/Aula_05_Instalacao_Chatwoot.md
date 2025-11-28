---
criado: 2025-07-22T10:43:18-03:00
atualizado: 2025-07-22T10:43:18-03:00
---
# AULA 05 - INSTALAÇÃO E CONFIGURAÇÃO CHATWOOT

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 05/11  
**DURAÇÃO**: 75min  
**PREREQUISITOS**: Evolution API funcionando (Aula 04)  
**CRIADO**: 10/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO

Esta aula instala o **Chatwoot** - o centralizador de comunicação que unifica WhatsApp, email, webchat e outros canais. É o painel de controle que transforma comunicação fragmentada em **experiência unificada** para seus projetos.

**O QUE VOCÊ VAI DOMINAR:**
- Instalação completa Chatwoot no stack
- Integração com Evolution API (WhatsApp)
- Configuração multicanal unificada
- Interface única para todos os projetos

## 🎯 CONCEITOS-CHAVE

### **Chatwoot - Centralizador Universal:**
- **Função**: Hub único para todas as comunicações
- **Integração**: WhatsApp + Email + Webchat + SMS
- **Vantagem**: Uma interface para gerenciar tudo
- **Resultado**: Eficiência operacional máxima

### **Arquitetura Multicanal:**
```
WhatsApp (via Evolution) ↘
Email Marketing         → CHATWOOT → Equipe/Automação
Webchat Site           ↗
SMS/Telegram          ↗
```

### **Componentes Chatwoot:**
- **Application**: Interface web principal
- **Database**: PostgreSQL para dados
- **Redis**: Cache e processamento background
- **Storage**: Arquivos e mídias

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **PASSO 1: PostgreSQL Chatwoot**
```yaml
# EasyPanel → Add Service → PostgreSQL
Name: chatwoot-postgres
Database: chatwoot_db
Username: chatwoot_user
Password: [senha-forte-chatwoot]
Port: 5432
Volume: chatwoot_postgres_data
```

### **PASSO 2: Redis Chatwoot**
```yaml
# EasyPanel → Add Service → Redis
Name: chatwoot-redis
Password: [senha-forte-redis-chatwoot]
Port: 6379
Volume: chatwoot_redis_data
```

### **PASSO 3: Chatwoot Application**
```yaml
# Docker Image: chatwoot/chatwoot:latest
Environment Variables:
- DATABASE_URL=postgresql://chatwoot_user:[senha]@chatwoot-postgres:5432/chatwoot_db
- REDIS_URL=redis://:[senha-redis]@chatwoot-redis:6379
- SECRET_KEY_BASE=[chave-secreta-longa]
- RAILS_ENV=production
- INSTALLATION_ENV=docker
- FRONTEND_URL=https://[seu-dominio-chatwoot]
- DEFAULT_LOCALE=pt_BR
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**
- **Unificação**: Todas as conversas IA em uma interface
- **Histórico**: Contexto completo de interações
- **Equipe**: Colaboradores podem acompanhar IA
- **Métricas**: Analytics detalhadas de performance

### **EVANGELISMO DIGITAL:**
- **Multicanal**: WhatsApp + Email + Site unificados
- **Pastoral**: Acompanhamento espiritual centralizado
- **Eventos**: Coordenação de atividades da igreja
- **Comunidade**: Gestão de grupos e células

### **GABRIELE CONFECÇÕES/KABAK:**
- **Atendimento**: Suporte unificado para clientes
- **Vendas**: Pipeline comercial integrado
- **Marketing**: Campanhas multicanal coordenadas
- **Operação**: Logística e pós-venda centralizados

## 🔗 CONEXÕES

### **BUILDS SOBRE:**
- Aula 04: Evolution API agora tem interface visual
- Aula 03: N8N ganha painel de comunicação

### **PREPARA PARA:**
- Aula 06: Funcionamento detalhado Evolution
- Aula 07: Sincronização WhatsApp via QR
- Aula 08+: Workflows práticos no stack completo

### **INTEGRAÇÃO CRÍTICA:**
- Chatwoot + Evolution = WhatsApp visual
- Chatwoot + N8N = automação com oversight
- PostgreSQL compartilhado = dados unificados

## ✅ CHECKLIST AULA 05

### **INFRAESTRUTURA:**
- [ ] PostgreSQL Chatwoot instalado e funcionando
- [ ] Redis Chatwoot operacional com persistência
- [ ] Volumes de dados configurados corretamente
- [ ] Rede entre serviços estabelecida

### **CHATWOOT INSTALAÇÃO:**
- [ ] Aplicação acessível via navegador
- [ ] Interface responsiva e estável
- [ ] Login funcionando sem erros
- [ ] Dashboard principal carregando

### **CONFIGURAÇÃO INICIAL:**
- [ ] Conta Super Admin criada
- [ ] Organização configurada
- [ ] Timezone e idioma ajustados (pt_BR)
- [ ] Primeiros canais adicionados

### **INTEGRAÇÃO:**
- [ ] Evolution API detectado pelo Chatwoot
- [ ] WhatsApp Business channel configurado
- [ ] Teste de mensagem funcionando
- [ ] Pronto para workflows N8N

---

**STATUS**: ✅ Chatwoot operacional como centralizador  
**RESULTADO**: Comunicação multicanal unificada  
**PRÓXIMO**: Aula 06 - Como Funciona Evolution API

*"Chatwoot: onde comunicação fragmentada vira experiência unificada"*