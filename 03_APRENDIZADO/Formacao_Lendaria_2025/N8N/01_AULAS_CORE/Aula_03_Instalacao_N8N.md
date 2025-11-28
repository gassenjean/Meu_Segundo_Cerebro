---
criado: 2025-07-22T10:41:32-03:00
atualizado: 2025-07-22T10:41:32-03:00
---
# AULA 03 - INSTALAÇÃO COMPLETA DO N8N

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 03/11  
**DURAÇÃO**: 120min  
**PREREQUISITOS**: VPS + EasyPanel funcionando (Aula 02)  
**CRIADO**: 09/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO

Esta é a **aula mais crítica** do módulo N8N! Você vai transformar a infraestrutura preparada (VPS + EasyPanel) em um sistema de automação completo e funcionando. Instalação do N8N em modo fila + Evolution API + Chatwoot = stack completo para workflows profissionais.

**O QUE VOCÊ VAI DOMINAR:**
- Instalação N8N em modo fila (performance superior)
- Configuração PostgreSQL + Redis (infraestrutura robusta)
- Setup Evolution API para WhatsApp Business
- Integração Chatwoot como centralizador

## 🎯 CONCEITOS-CHAVE

### **Stack de Instalação - Ordem Obrigatória:**
```
1. ✅ VPS + EasyPanel (concluído Aula 02)
2. 🔄 PostgreSQL + Redis (banco + cache)
3. 🔄 N8N Modo Fila (núcleo automação)
4. 🔄 Evolution API (conexão WhatsApp)
5. 🔄 Chatwoot (interface centralizadora)
```

### **N8N Modo Fila vs Padrão:**
- **PADRÃO**: Processamento sequencial, limitações de escala
- **MODO FILA**: Processamento paralelo, alta performance
- **VANTAGEM**: Suporta centenas de workflows simultâneos
- **INFRAESTRUTURA**: Requer PostgreSQL + Redis

### **Processo em 3 Fases Críticas:**
```
FASE 1: Geração senhas + configuração inicial
FASE 2: Instalação infraestrutura (DB + Cache)  
FASE 3: Deploy aplicações (N8N + Evolution + Chat)
```

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **FASE 1: Preparação Ambiente**
```bash
# EasyPanel → Services → Add Service
# Gerar senhas seguras para:
- PostgreSQL: [senha-forte-postgres]
- Redis: [senha-forte-redis]  
- N8N: [senha-admin-n8n]

# Anotar todas as credenciais em local seguro
```

### **FASE 2: Infraestrutura**
```yaml
# PostgreSQL Database:
Service: PostgreSQL
Version: Latest
Port: 5432
Database: n8n_db
Username: n8n_user
Password: [senha-forte-postgres]

# Redis Cache:
Service: Redis
Version: Latest
Port: 6379
Password: [senha-forte-redis]
```

### **FASE 3: N8N Queue Mode**
```yaml
# N8N Configuration:
Environment Variables:
- DB_TYPE=postgresdb
- DB_POSTGRESDB_HOST=postgres
- DB_POSTGRESDB_PORT=5432
- DB_POSTGRESDB_DATABASE=n8n_db
- DB_POSTGRESDB_USER=n8n_user
- DB_POSTGRESDB_PASSWORD=[senha-postgres]
- QUEUE_BULL_REDIS_HOST=redis
- QUEUE_BULL_REDIS_PORT=6379
- QUEUE_BULL_REDIS_PASSWORD=[senha-redis]
- EXECUTIONS_MODE=queue
- N8N_BASIC_AUTH_ACTIVE=true
- N8N_BASIC_AUTH_USER=admin
- N8N_BASIC_AUTH_PASSWORD=[senha-admin]
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**
- **Performance**: Respostas IA em <3 segundos
- **Escalabilidade**: Múltiplas conversas simultâneas
- **Confiabilidade**: Backup automático de dados
- **Monitoramento**: Logs detalhados de performance

### **EVANGELISMO DIGITAL:**
- **Volume**: Centenas de leads processados em paralelo
- **Disponibilidade**: 99.9% uptime para contatos críticos
- **Integração**: CRM + E-mail + WhatsApp unificados
- **Analytics**: Métricas em tempo real

### **GABRIELE CONFECÇÕES/KABAK:**
- **E-commerce**: Pedidos processados instantaneamente
- **Estoque**: Sincronização em tempo real
- **Atendimento**: Múltiplos canais centralizados
- **Relatórios**: Dashboards automatizados

## 🔗 CONEXÕES

### **BUILDS SOBRE:**
- Aula 02: Infraestrutura agora recebe aplicações
- Aula 01: Arquitetura se materializa completamente

### **PREPARA PARA:**
- Aula 04: Evolution API já estará instalado
- Aula 05: Chatwoot integrará ao stack funcionando
- Aulas 06+: Workflows práticos no sistema completo

### **DEPENDÊNCIAS CRÍTICAS:**
- PostgreSQL funcionando = dados persistentes
- Redis ativo = performance otimizada
- N8N estável = base para todos os workflows

## ✅ CHECKLIST AULA 03

### **INFRAESTRUTURA:**
- [ ] PostgreSQL instalado e acessível
- [ ] Redis funcionando com autenticação
- [ ] Conexões de rede entre serviços testadas
- [ ] Backup inicial dos bancos configurado

### **N8N INSTALAÇÃO:**
- [ ] N8N acessível via navegador
- [ ] Login com credenciais admin funcionando
- [ ] Modo fila ativo (verificar logs)
- [ ] Interface responsiva e estável

### **INTEGRAÇÃO:**
- [ ] N8N conectando com PostgreSQL
- [ ] Redis sendo usado para fila
- [ ] Performance notavelmente superior
- [ ] Logs sem erros críticos

### **VALIDAÇÃO FINAL:**
- [ ] Workflow simples criado e testado
- [ ] Execução em fila funcionando
- [ ] Sistema estável sob carga básica
- [ ] Pronto para Evolution API (Aula 04)

---

**STATUS**: ✅ N8N completo instalado em modo profissional  
**RESULTADO**: Sistema de automação robusto e escalável  
**PRÓXIMO**: Aula 04 - Integration Evolution API para WhatsApp

*"N8N em modo fila: onde automação vira operação empresarial"*