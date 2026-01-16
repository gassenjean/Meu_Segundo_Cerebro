---
description: Iniciar sessão segura com verificação de conflitos e contexto arquitetural (Handshake)
---

# Início de Sessão Seguro (Architecture-Aware)

Este é o workflow de "Handshake" (aperto de mão) obrigatório ao iniciar qualquer trabalho no Antigravity.
**Versão 2.0 (Enhanced):** Agora inclui verificação profunda de mudanças arquiteturais e protocolos.

---

## CONTEXTO

**Você é Iniciador de Sessão (Gemini)** - responsável por verificar o estado do vault antes de começar a trabalhar.

**Vault:** Meu_Segundo_Cerebro
**Arquivo central:** `SESSION_LOG.md` (raiz)
**Protocolo:** `00_SISTEMA/PROTOCOLOS/SOP_INTEGRACAO_ANTIGRAVITY.md`

---

## OBJETIVO

Quando o usuário executa `/start`, você deve:

1. **Ler o SESSION_LOG.md** - Ver últimas ações do Claude Code e buscar por *mudanças estruturais*.
2. **Identificar Padrões de Arquitetura** - Verificar se novas regras (ex: "Architecture Guidelines", "RPI") foram implementadas.
3. **Verificar mensagens** - Verificar se há instruções pendentes para você.
4. **Validar Status Macro** - STATUS_VAULT.md e PC_SYNC_LOG.md.
5. **Definir escopo seguro** - Identificar áreas que pode trabalhar sem conflitos.

---

## PROCESSO

### ETAPA 1: Ler Log de Sessão e Analisar Contexto

**Ação:**
Leia o arquivo `SESSION_LOG.md` e busque ativamente por palavras-chave de mudança estrutural.

**Comando sugerido:**

```bash
cat ../SESSION_LOG.md
```

**O que procurar (Análise Profunda):**

- **Atividade Recente:** O que o Claude Code fez?
- **Keywords de Alerta:** "ARCHITECTURE", "OVERHAUL", "PROTOCOL", "RPI", "SMART ZONE".
- **Instruções Diretas:** Seção "Mensagem para Gemini" ou "TAREFA PARA GEMINI".

---

### ETAPA 2: Verificar Diretrizes Arquiteturais (Condicional)

**Ação:**
Se na Etapa 1 você detectou menção a novos padrões (especialmente `ARCHITECTURE_GUIDELINES.md` ou novos Protocolos), **VOCÊ DEVE LÊ-LOS AGORA**.

**Comando sugerido (se aplicável):**

```bash
# Se o log citar Architecture Guidelines:
cat ../00_SISTEMA/PADROES/ARCHITECTURE_GUIDELINES.md
```

**Por que isso é crítico?**
Ignorar novas diretrizes arquiteturais pode fazer com que você crie arquivos fora do padrão (ex: sem seguir RPI ou Nomenclatura), gerando conflitos imediatos.

---

### ETAPA 3: Verificar Status e Sync

**Ação:**
Leia `STATUS_VAULT.md` e `PC_SYNC_LOG.md` para triangulação de estado.

**Comando sugerido:**

```bash
cat ../STATUS_VAULT.md
cat ../PC_SYNC_LOG.md
```

**Verificação:**
- O `STATUS_VAULT.md` está alinhado com o `SESSION_LOG.md`? Se não, note essa divergência.
- O `PC_SYNC_LOG.md` mostra pendências de outro computador?

---

### ETAPA 4: Análise de Segurança e Escopo

**Perguntas a responder:**

1.  **Architecture Check:** Estou ciente das novas regras (ex: Smart Zone, RPI)?
2.  **Task Check:** Existe alguma tarefa de manutenção "URGENTE" atribuída a mim no log?
3.  **Scope Check:** Onde posso trabalhar sem violar os novos padrões?

---

### ETAPA 5: Confirmar com Usuário

**Responder ao usuário com resumo detalhado:**

```markdown
✅ Sessão iniciada com segurança (Architecture-Aware)!

📋 Contexto Arquitetural Identificado:
- Mudanças Recentes: [ex: Architecture Overhaul, RPI Framework]
- Novos Padrões: [ex: Smart Zone 40%]
- Arquivos de Referência: [quais diretrizes regem esta sessão]

💬 Mensagens e Tarefas (Gemini):
- Instrução Principal: [ex: "Alinhar .gemini/ com padrões"]
- Urgência: [Alta/Média/Baixa]

📊 Estado do Vault & Sync:
- Status Vault: [Atualizado/Desatualizado]
- PC Sync: [ex: Pendência de envio KabaK]

🎯 Escopo Seguro Definido:
- AÇÃO IMEDIATA: [ex: Ler ARCHITECTURE_GUIDELINES.md e corrigir .gemini/]
- Evitar: [ex: Criar arquivos sem RPI]

✅ Estou pronto e alinhado com as novas regras. Prossigo com a [AÇÃO IMEDIATA]?
```

---

## REGRAS IMPORTANTES

### ✅ SEMPRE:

1.  **Ler SESSION_LOG.md COMPLETO** antes de começar.
2.  **Buscar proativamente** por mudanças de arquitetura.
3.  **Ler os GUIDELINES** se mencionados como novos.
4.  **Priorizar tarefas de manutenção/alinhamento** solicitadas pelo Claude.

### ❌ NUNCA:

1.  Ignorar avisos de "OVERHAUL" ou "NEW PROTOCOL".
2.  Começar a trabalhar com "regras antigas" na cabeça.
3.  Pular a leitura de diretrizes críticas citadas no log.

---

## SUAS AÇÕES AGORA

1.  ✅ Confirme que leu o workflow atualizado.
2.  🔍 Execute a **ETAPA 1** (Re-ler SESSION_LOG com foco em Arquitetura).
3.  📖 Execute a **ETAPA 2** (Ler `ARCHITECTURE_GUIDELINES.md` se detectado).
4.  🎯 Redefina o escopo da sessão baseado nas novas regras.
5.  ✅ Reporte ao usuário com o novo formato "Architecture-Aware".
