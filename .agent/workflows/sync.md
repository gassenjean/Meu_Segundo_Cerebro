---
description: Sincronizar com Claude Code (Atualizar SESSION_LOG)
---

# Sincronizar com Claude Code

Atualiza o SESSION_LOG.md com o trabalho realizado nesta sessão do Antigravity/Gemini para comunicação com Claude Code.

---

## CONTEXTO

**Você é Sincronizador de Sessão (Gemini)** - responsável por documentar o trabalho do Antigravity/Gemini para Claude Code ler.

**Vault:** Meu_Segundo_Cerebro
**Arquivo central:** `SESSION_LOG.md` (raiz)
**Protocolo:** `00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md`

---

## OBJETIVO

Quando o usuário executa `/sync`, você deve:

1. **Revisar a sessão atual** - O que foi feito desde que Gemini iniciou
2. **Identificar mudanças significativas** - Arquivos criados/modificados, decisões tomadas
3. **Atualizar SESSION_LOG.md** - Seguindo template específico
4. **Deixar mensagens** para Claude Code se necessário

---

## PROCESSO SEGMENTADO

### ETAPA 0: Pré-Sync (Segurança)

Antes de começar a escrever o log, faça uma auto-análise rápida:

1. **Verifique** se você seguiu os padrões de nomenclatura.
2. **Confirme** se não sobrepôs nenhuma mudança recente do Claude (lida no início).
3. Se houver dúvida, avise o usuário antes de consolidar.

---

## PROCESSO

### ETAPA 1: Análise da Sessão

**Perguntas a responder:**

- Quais arquivos foram criados?
- Quais arquivos foram modificados?
- Qual foi o trabalho principal realizado?
- Há tarefas que ficaram pendentes?
- Claude precisa fazer algo como continuação?

### ETAPA 2: Preparar Atualização

**Estrutura obrigatória:**

```markdown
### 🟢 Antigravity/Gemini - [DATA ATUAL] ([HORA ATUAL])

**Ações realizadas:**

- ✅ [Ação 1 específica]
- ✅ [Ação 2 específica]
- ✅ [Ação 3 específica]

**Arquivos modificados:**

- `caminho/arquivo.md` (descrição clara da mudança)
- `caminho/outro.md` (o que foi feito)

**Próximos passos sugeridos:**

- [ ] [Tarefa pendente 1]
- [ ] [Tarefa pendente 2]

**Estado do vault:**

- [Informação importante sobre estado atual]
- [Exemplo: Estatísticas, estrutura, progresso]

**Mensagem para Claude:**

> [Deixar mensagem APENAS se Claude precisar fazer algo específico]
> [Se não houver nada específico, colocar: "Nenhuma ação necessária"]
```

### ETAPA 3: Ler SESSION_LOG.md

**Antes de atualizar:**

1. Ler arquivo atual
2. Verificar seção "ÚLTIMAS MUDANÇAS"
3. Verificar se há "Mensagem para Gemini" não lida
4. Identificar onde inserir nova entrada

### ETAPA 4: Atualizar Arquivo

**Onde inserir:**

- Na seção "ÚLTIMAS MUDANÇAS"
- **NO TOPO** (entrada mais recente primeiro)
- Manter últimas 10 entradas (apagar mais antigas)

**Também atualizar:**

- Seção "ÚLTIMA SESSÃO ATIVA"
- Seção "CONTEXTO ATUAL DO VAULT" (se mudou significativamente)
- Seção "CANAL DE COMUNICAÇÃO DIRETA" (se há mensagem para Claude)

### ETAPA 5: Confirmar com Usuário

**Mostrar resumo:**

```markdown
✅ SESSION_LOG.md atualizado!

📝 Registrado:

- [Resumo das ações]
- [Arquivos modificados]

💬 Mensagem para Claude:

- [Mensagem deixada, ou "Nenhuma"]

🔄 Próxima vez que Claude iniciar:

- Ele verá todo este contexto
- Poderá continuar trabalho pendente
```

---

## REGRAS IMPORTANTES

### ✅ SEMPRE:

1. Usar data e hora REAIS do sistema
2. Ser específico nas descrições
3. Listar TODOS os arquivos importantes modificados
4. Manter formato consistente (template)
5. Perguntar ao usuário se incerto sobre algo

### ❌ NUNCA:

1. Inventar informações
2. Omitir mudanças importantes
3. Quebrar o formato do template
4. Deletar entradas anteriores (exceto se > 10)
5. Sobrescrever mensagens de Claude

---

## SUAS AÇÕES AGORA

1. ✅ Confirme que está em modo SINCRONIZAÇÃO
2. 🔍 Analise a sessão atual (o que foi feito?)
3. 📝 Prepare atualização seguindo template
4. 📖 Leia SESSION_LOG.md atual
5. ✏️ Atualize arquivo com nova entrada
6. 💬 Deixe mensagem para Claude se necessário
7. ✅ Confirme com usuário

**Pronto para sincronizar! O que foi trabalhado nesta sessão?**
