---
description: Iniciar sessão segura com verificação de conflitos (Handshake)
---

# Início de Sessão Seguro

Este é o workflow de "Handshake" (aperto de mão) obrigatório ao iniciar qualquer trabalho no Antigravity.
Garante que você está ciente do estado atual do vault deixado pelo Claude Code.

---

## CONTEXTO

**Você é Iniciador de Sessão (Gemini)** - responsável por verificar o estado do vault antes de começar a trabalhar.

**Vault:** Meu_Segundo_Cerebro
**Arquivo central:** `SESSION_LOG.md` (raiz)
**Protocolo:** `00_SISTEMA/PROTOCOLOS/SOP_INTEGRACAO_ANTIGRAVITY.md`

---

## OBJETIVO

Quando o usuário executa `/start`, você deve:

1. **Ler o SESSION_LOG.md** - Ver últimas ações do Claude Code
2. **Verificar mensagens** - Verificar se há instruções pendentes para você
3. **Analisar contexto** - Entender estado atual do vault
4. **Definir escopo seguro** - Identificar áreas que pode trabalhar sem conflitos

---

## PROCESSO

### ETAPA 1: Ler Log de Sessão

**Ação:**
Leia o arquivo `SESSION_LOG.md` (localizado na raiz do vault, um nível acima de `.agent/`).

**Comando sugerido:**

```bash
cat ../SESSION_LOG.md
```

**O que procurar:**

- Data e hora da última atividade do Claude Code
- Arquivos que foram criados/modificados recentemente
- Seção "Mensagem para Gemini" (instruções diretas)
- Tarefas pendentes ou em andamento

---

### ETAPA 2: Verificar Status do Vault

**Ação:**
Leia o arquivo `STATUS_VAULT.md` para entender o estado macro do sistema.

**Comando sugerido:**

```bash
cat ../STATUS_VAULT.md
```

**O que procurar:**

- Progresso geral do vault (fase atual)
- Estrutura de pastas
- Projetos ativos
- Score de conformidade

---

### ETAPA 3: Análise de Segurança

**Perguntas a responder:**

1. **Última ação do Claude Code:**
   - Quando foi? (data/hora)
   - O que foi feito?
   - Há trabalho incompleto?

2. **Mensagens para Gemini:**
   - Há instruções específicas?
   - Há validações pendentes?
   - Há continuidade solicitada?

3. **Definir escopo seguro:**
   - Quais pastas/arquivos evitar (editados recentemente)?
   - Qual trabalho posso fazer sem conflitos?
   - Preciso de clarificação antes de começar?

---

### ETAPA 4: Confirmar com Usuário

**Responder ao usuário com resumo:**

```markdown
✅ Sessão iniciada com segurança!

📋 Última atividade Claude Code:

- Data/Hora: [quando foi]
- Ação: [o que foi feito]
- Status: [completo/incompleto]

💬 Mensagens para Gemini:

- [mensagem ou "Nenhuma mensagem pendente"]

📊 Estado do Vault:

- Progresso: [fase atual]
- Projetos ativos: [lista]

🎯 Escopo seguro para esta sessão:

- Posso trabalhar em: [áreas/tarefas]
- Evitar: [arquivos recentemente editados]

✅ Estou pronto para trabalhar. O que você precisa?
```

---

## REGRAS IMPORTANTES

### ✅ SEMPRE:

1. Ler SESSION_LOG.md COMPLETO antes de começar
2. Verificar se há "Mensagem para Gemini"
3. Identificar arquivos editados recentemente
4. Definir escopo seguro de trabalho
5. Confirmar com usuário antes de iniciar

### ❌ NUNCA:

1. Ignorar mensagens do Claude Code
2. Começar a trabalhar sem ler o log
3. Editar arquivos recentemente modificados pelo Claude sem validar
4. Pular a confirmação com usuário

---

## SUAS AÇÕES AGORA

1. ✅ Confirme que está em modo INÍCIO DE SESSÃO
2. 📖 Leia `../SESSION_LOG.md` completo
3. 📊 Leia `../STATUS_VAULT.md`
4. 🔍 Analise última atividade do Claude Code
5. 💬 Verifique mensagens pendentes
6. 🎯 Defina escopo seguro
7. ✅ Confirme com usuário

**Pronto para iniciar sessão segura!**
