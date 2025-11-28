# GUIA DE IMPLEMENTAÇÃO - PROJETO FINAL N8N

---
**BASEADO EM**: Material do curso + Aula 17  
**CRIADO**: 31/07/2025  
**STATUS**: Guia prático passo a passo  
---

## 📋 RESUMO DO MATERIAL ORIGINAL

O material que você compartilhou mostra o processo EXATO de configuração do projeto final, incluindo:

1. **Download do arquivo base** com workflow pré-configurado
2. **Preenchimento das seções em vermelho** (APIs e configurações)
3. **Teste passo a passo** com dados fictícios
4. **Integração com Trello** para CRM
5. **Configuração WhatsApp** via Evolution API

## 🔴 SEÇÕES VERMELHAS PARA PREENCHER

### 1. FORMULÁRIO
- Já vem configurado, apenas testar com "Test Step"
- Dados de exemplo: Academia Lendária, José Carlos, etc.

### 2. CHAVE API OPENAI
```
Local: Node de IA Principal
Como: 
1. Acessar platform.openai.com
2. Gerar nova API Key
3. Substituir texto "PREENCHA_CHAVE_API"
```

### 3. CHAVE API GEMINI
```
Local: Node de Lead Morno
Como:
1. Acessar Google AI Studio
2. Gerar API Key
3. Substituir no node correspondente
```

### 4. CHAVE API DEEPSEEK
```
Local: Node de Lead Frio
Como:
1. Acessar platform.deepseek.com
2. Gerar API Key
3. Substituir no node correspondente
```

### 5. CONFIGURAÇÃO TRELLO

#### 5.1 Criar Quadro CRM
```
Nome: CRM
Listas:
- Lead Quente (verde)
- Lead Morno (amarelo)
- Lead Frio (vermelho)
```

#### 5.2 Obter Código do Board
```
1. Abrir URL do Trello
2. Copiar código entre /b/ e /crm
3. Substituir em 3 nodes: "CODIGO_DO_BOARD"
```

#### 5.3 Gerar Chave e Token
```
1. Acessar trello.com/app-key
2. Gerar API Key
3. Gerar Token manualmente
4. Substituir em TODOS os nodes Trello
```

### 6. CONFIGURAÇÃO WHATSAPP

```
1. Copiar URL do Evolution: tudo antes de /manager
2. Remover barra extra (deixar apenas uma /)
3. Copiar nome da instância
4. Copiar API Key da linha 106 do .env
```

## 🚀 FLUXO DE EXECUÇÃO

### PASSO 1: Pin dos Dados
```javascript
// Clicar em "Test Step" no formulário
// Preencher com dados de teste
// Clicar no pin para salvar dados
```

### PASSO 2: Testar Node por Node
```javascript
// Play em cada node sequencialmente
// Verificar saída no painel direito
// Corrigir erros antes de prosseguir
```

### PASSO 3: Test Workflow Completo
```javascript
// Clicar em "Test Workflow"
// Acompanhar execução completa
// Verificar:
  - Card criado no Trello
  - Mensagem enviada no WhatsApp
```

## ⚡ DICAS DO MATERIAL

### FORMATAÇÃO IMPORTANTE
- Número WhatsApp: código do país + DDD + número
- Brasil: 55 + DDD + número (sem o 9 extra)
- Exemplo: 5511999999999

### ORDEM DE CONFIGURAÇÃO
1. OpenAI primeiro (node principal)
2. Trello (criar quadro → pegar código → APIs)
3. Gemini e DeepSeek (nodes secundários)
4. WhatsApp por último (Evolution)

### ERROS COMUNS
- Duas barras na URL (remover uma)
- Esquecer de substituir TODAS ocorrências
- Não pinar os dados antes de testar
- API Keys com espaços extras

## 📱 APLICAÇÃO NOS SEUS PROJETOS

### NÉVOA IA
```javascript
// Formulário adaptado:
- "Maturidade em IA" no lugar de "porte"
- "Budget mensal IA" no lugar de "orçamento"
- "Volume de automações" no lugar de "volume"
```

### EVANGELISMO DIGITAL
```javascript
// Formulário adaptado:
- "Tamanho da igreja" no lugar de "porte"
- "Verba para tecnologia" no lugar de "orçamento"
- "Membros ativos online" no lugar de "volume"
```

### GABRIELE/KABAK
```javascript
// Formulário adaptado:
- "Volume de compra mensal" no lugar de "porte"
- "Ticket médio" no lugar de "orçamento"
- "SKUs de interesse" no lugar de "volume"
```

## ✅ CHECKLIST FINAL

### ANTES DE RODAR
- [ ] Todas as APIs configuradas
- [ ] Trello com 3 listas criadas
- [ ] WhatsApp conectado no Evolution
- [ ] Dados de teste pinados

### DURANTE EXECUÇÃO
- [ ] Formulário recebe dados
- [ ] IA classifica corretamente
- [ ] Switch direciona para branch certo
- [ ] CRM cria card com tasks
- [ ] WhatsApp envia mensagem

### DEPOIS DE FUNCIONAR
- [ ] Salvar workflow
- [ ] Documentar customizações
- [ ] Criar formulário real
- [ ] Ativar para produção

---

**LEMBRETE**: O sistema já vem 80% pronto. Você só precisa:
1. Preencher as chaves de API
2. Configurar Trello
3. Conectar WhatsApp
4. Testar e ajustar

**TEMPO ESTIMADO**: 45-60 minutos seguindo o passo a passo