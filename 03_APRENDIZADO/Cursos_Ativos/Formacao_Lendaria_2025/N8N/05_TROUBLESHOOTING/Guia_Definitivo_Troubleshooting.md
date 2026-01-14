# 🛠️ TROUBLESHOOTING N8N - GUIA DEFINITIVO

## 🎯 FILOSOFIA DO TROUBLESHOOTING

**MINDSET**: "Fundamento, não ferramenta. Conceito, não clique."

- Identifique o PADRÃO por trás do problema
- Entenda o FLUXO de dados, não apenas o erro
- Documente SOLUÇÕES para problemas recorrentes

---

## 🚨 PROBLEMAS DE INFRAESTRUTURA (VPS + EasyPanel)

### **🔴 CRÍTICO - VPS Não Acessa**

#### **Sintomas**:

- Site não carrega
- Timeout na conexão
- "Site não encontrado"

#### **Diagnóstico**:

```bash
# 1. Teste de ping
ping seudominio.com

# 2. Verificação DNS
nslookup easypanel.seudominio.com

# 3. Teste porta específica
telnet IP_VPS 80
```

#### **Soluções por Ordem**:

1. **DNS não propagou**: dnschecker.org → aguardar até 48h
2. **IP errado no DNS**: Hostinger → DNS → verificar IP atual VPS
3. **VPS offline**: Hostinger → VPS → verificar status/reiniciar
4. **Firewall bloqueando**: EasyPanel → configurações de rede

### **🟡 MÉDIO - EasyPanel Inacessível**

#### **Sintomas**:

- DNS funciona mas EasyPanel não abre
- Erro SSL/certificado
- Login não aceita credenciais

#### **Soluções**:

```
1. Certificado SSL:
   - Acesso: https://easypanel.seudominio.com
   - Clique: "Avançados" → "Continuar mesmo assim"
   - Motivo: SSL demora para configurar automaticamente

2. Credenciais perdidas:
   - Use email/senha do PRIMEIRO CADASTRO no EasyPanel
   - NÃO confundir com credenciais da Hostinger
   - Recuperar: função "Esqueci senha" na tela login

3. Domínio personalizado:
   - EasyPanel → Configurações → Geral
   - Verificar: easypanel.SEUDOMINIO correto
   - Salvar novamente se necessário
```

---

## 🔧 PROBLEMAS DE INSTALAÇÃO N8N

### **🔴 CRÍTICO - N8N Não Instala**

#### **Sintomas**:

- Erro durante instalação via EasyPanel
- Aplicação não aparece na lista
- Status "Failed" na instalação

#### **Diagnóstico e Soluções**:

```
1. Recursos VPS insuficientes:
   - EasyPanel → Monitor → verificar RAM/CPU
   - Solução: Upgrade VPS ou liberar recursos

2. Porta já em uso:
   - Verificar aplicações instaladas
   - Usar porta diferente (5678 padrão N8N)

3. Dependências ausentes:
   - Reinstalar aplicação
   - Aguardar processo completo (pode demorar 10-15min)

4. Logs de erro:
   - EasyPanel → Aplicações → N8N → Logs
   - Buscar por: "ERROR", "FAILED", "Cannot"
```

### **🟡 MÉDIO - N8N Instalado mas Inacessível**

#### **Sintomas**:

- Instalação bem-sucedida
- URL não carrega
- Erro 502/503

#### **Soluções Sequenciais**:

```
1. Verificar status aplicação:
   - EasyPanel → Aplicações → N8N → Status: "Running"
   - Se "Stopped": clicar "Start"

2. Configurar domínio personalizado:
   - EasyPanel → N8N → Settings → Domain
   - Inserir: n8n.seudominio.com
   - Adicionar DNS: mesmo processo Aula 02

3. Aguardar inicialização:
   - N8N demora 2-5 minutos para carregar completamente
   - Monitorar logs para "Server started"

4. Verificar porta/proxy:
   - Porta padrão: 5678
   - EasyPanel faz proxy automático via domínio
```

---

## 🤖 PROBLEMAS DE WORKFLOWS

### **🔴 CRÍTICO - Workflow Não Executa**

#### **Sintomas**:

- Workflow salvo mas não ativa
- Trigger não dispara
- Dados não fluem entre nodes

#### **Diagnóstico**:

```json
{
  "verificações": {
    "workflow_ativo": "Botão 'Active' deve estar ON",
    "trigger_configurado": "Webhook/Timer/Manual configurado corretamente",
    "conexões": "Todas as linhas entre nodes conectadas",
    "credenciais": "APIs externas autenticadas"
  }
}
```

#### **Soluções por Tipo de Trigger**:

**WEBHOOK**:

```
1. URL correta:
   - Copiar URL exata do node Webhook
   - Testar com Postman/curl primeiro

2. Método HTTP:
   - GET/POST conforme esperado pela fonte
   - Headers corretos se necessário

3. Teste manual:
   - Node Webhook → "Listen for test event"
   - Enviar dados → verificar recepção
```

**SCHEDULE/TIMER**:

```
1. Timezone:
   - N8N → Settings → Timezone
   - Verificar se coincide com servidor

2. Formato cron:
   - Usar gerador online: crontab.guru
   - Testar com intervalo curto primeiro

3. Execution mode:
   - N8N → Settings → Execution
   - Verificar se não está em "Manual only"
```

### **🟡 MÉDIO - Workflow Executa com Erro**

#### **Sintomas**:

- Execution inicia mas falha em node específico
- Dados não chegam no destino final
- Timeout em integrações

#### **Debugging Sistemático**:

```
1. Ativar modo debug:
   - Node com erro → "Show details"
   - Verificar input/output de cada step

2. Testar node isoladamente:
   - Desconectar node problemático
   - Executar até node anterior
   - Verificar dados que chegam

3. Logs detalhados:
   - N8N → Executions → selecionar execução
   - Expandir cada node para ver logs

4. Timeout issues:
   - Node → Settings → Timeout
   - Aumentar para integrações lentas (APIs externas)
```

---

## 🔗 PROBLEMAS DE INTEGRAÇÃO

### **WhatsApp (Evolution API)**

#### **Erros Comuns**:

```
1. "Instance not found":
   - Verificar nome da instância
   - Recriar instância se necessário

2. "Unauthorized":
   - Renovar token de acesso
   - Verificar headers da requisição

3. "Message not delivered":
   - Número em formato internacional (+55)
   - WhatsApp do destinatário ativo
```

### **CRM (RD Station, HubSpot)**

#### **Erros Comuns**:

```
1. "Invalid API key":
   - Regenerar API key
   - Verificar permissões do token

2. "Rate limit exceeded":
   - Adicionar delay entre requests
   - Implementar retry com backoff

3. "Field validation error":
   - Verificar campos obrigatórios
   - Mapear dados corretamente
```

### **IA (OpenAI, Claude)**

#### **Erros Comuns**:

```
1. "Token limit exceeded":
   - Reduzir max_tokens
   - Dividir prompt em chunks menores

2. "Model not found":
   - Verificar nome do modelo (gpt-4, claude-3)
   - Confirmar acesso ao modelo na conta

3. "Content policy violation":
   - Revisar prompt por conteúdo inadequado
   - Usar system prompt para contexto
```

---

## 📊 MONITORAMENTO E PREVENÇÃO

### **Métricas Essenciais**

#### **Infraestrutura**:

```
VPS Health Check:
- CPU < 80%
- RAM < 85%
- Disk < 90%
- Uptime > 99%
```

#### **Aplicações**:

```
N8N Monitor:
- Executions/hour
- Success rate > 95%
- Average execution time
- Failed workflows alert
```

### **Alertas Automáticos**

#### **EasyPanel Monitoring**:

```
1. Resource alerts:
   - CPU > 80% por 5min
   - RAM > 90% por 5min
   - Disk > 85%

2. Application alerts:
   - Service down
   - HTTP errors > 5%
   - Response time > 10s
```

#### **N8N Internal Monitoring**:

```json
{
  "workflow_monitor": {
    "failed_executions": "webhook_alert",
    "execution_time": "> 30s = warning",
    "daily_summary": "email_report"
  }
}
```

---

## 🚀 OTIMIZAÇÃO E PERFORMANCE

### **VPS Performance**

#### **Otimizações Básicas**:

```bash
# 1. Limpeza de cache
sudo apt clean
sudo apt autoremove

# 2. Reiniciar serviços pesados
sudo systemctl restart docker
sudo systemctl restart nginx

# 3. Monitorar processos
htop
```

#### **Upgrade Planejado**:

```
Sinais para upgrade VPS:
- CPU > 80% constante
- RAM > 85% constante
- Workflows executando > 30s
- Múltiplas aplicações instaladas
```

### **N8N Performance**

#### **Otimizações de Workflow**:

```
1. Batch processing:
   - Processar múltiplos items por execução
   - Usar "Split in Batches" node

2. Async operations:
   - Usar HTTP Request assíncrono
   - Implementar callbacks para long-running tasks

3. Error handling:
   - Try/catch em nodes críticos
   - Retry automático com backoff

4. Data efficiency:
   - Limitar campos retornados em APIs
   - Usar filtros antes de processamento pesado
```

---

## 📚 RECURSOS DE APOIO

### **Documentação Oficial**:

- N8N Docs: docs.n8n.io
- Evolution API: evolution-api.com/docs
- EasyPanel: easypanel.io/docs

### **Comunidades**:

- N8N Community: community.n8n.io
- Discord Servers: [específicos por integração]
- Stack Overflow: tag "n8n"

### **Ferramentas de Debug**:

- **Postman**: Testar webhooks e APIs
- **dnschecker.org**: Verificar propagação DNS
- **crontab.guru**: Validar expressões cron
- **jsonlint.com**: Validar formato JSON

---

## 🎯 PROTOCOLO DE EMERGÊNCIA

### **Sistema Down Completo**:

```
1. Verificar Hostinger dashboard (VPS status)
2. Ping direto no IP da VPS
3. Acessar via SSH se necessário
4. Reiniciar VPS como último recurso
5. Backup de workflows salvos localmente
```

### **Backup de Workflows**:

```json
{
  "backup_schedule": "daily",
  "location": "Google Drive + Local",
  "format": "JSON export",
  "versioning": "git repository"
}
```

### **Contatos de Emergência**:

- **Hostinger Support**: [link/telefone]
- **N8N Community**: Para problemas específicos
- **Gassen Network**: Backup de especialistas técnicos

---

**🎖️ LEMBRETE**: Sempre documente soluções encontradas. Cada problema resolvido é conhecimento acumulado para o futuro.

**⚡ MANTRA**: "Erro não é falha, é aprendizado. Debug sistemático, solução lendária."
