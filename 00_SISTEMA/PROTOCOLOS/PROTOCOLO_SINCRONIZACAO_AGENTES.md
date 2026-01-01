# Protocolo de Sincronização - Claude ↔ Gemini

**Criado:** 28/Nov/2025
**Versão:** 1.0
**Tipo:** Protocolo de Comunicação entre Agentes

---

## 🎯 OBJETIVO

Manter **Claude Code** e **Antigravity/Gemini 3 Pro** sincronizados quando trabalhando no mesmo vault, evitando:
- ❌ Conflitos de edição
- ❌ Trabalho duplicado
- ❌ Perda de contexto
- ❌ Tarefas esquecidas

E garantindo:
- ✅ Continuidade entre sessões
- ✅ Comunicação clara
- ✅ Colaboração eficiente
- ✅ Histórico completo

---

## 📋 ARQUIVO CENTRAL

**Arquivo:** `SESSION_LOG.md` (raiz do vault)

**Função:** Canal de comunicação bidirecional

**Leitura:** OBRIGATÓRIA ao iniciar sessão
**Atualização:** OBRIGATÓRIA ao finalizar trabalho significativo

---

## 🔄 FLUXO DE TRABALHO

### Ao Iniciar Sessão

**Para ambos os agentes (Claude e Gemini):**

1. **Abrir** `SESSION_LOG.md`
2. **Ler** seção "ÚLTIMAS MUDANÇAS" completamente
3. **Identificar** o que o outro agente fez desde última vez
4. **Verificar** se há "MENSAGEM PARA [SEU NOME]"
5. **Checar** "CONTEXTO ATUAL DO VAULT"
6. **Decidir** se vai continuar tarefa pendente ou iniciar nova

**Exemplo Claude Code:**
```markdown
Ao iniciar, você lê:
- Gemini processou 3 lives do Alan Nicolas
- Gemini criou notas em 03_APRENDIZADO/Alan_Nicolas_Academia_Lendaria/notas/
- Gemini deixou mensagem: "Claude, valide nomenclatura das 3 notas criadas"
→ Você então valida antes de fazer outra coisa
```

**Exemplo Gemini:**
```markdown
Ao iniciar, você lê:
- Claude otimizou comandos (13 → 8)
- Claude criou GUIA_RAPIDO_COMANDOS.md
- Claude deixou mensagem: "Gemini, quando processar próximas lives, use apenas os 8 comandos listados no guia"
→ Você então consulta o guia antes de continuar
```

---

### Durante o Trabalho

**Não precisa atualizar constantemente**, mas:

**✅ Atualize SESSION_LOG.md quando:**
- Completar tarefa significativa
- Criar/modificar múltiplos arquivos
- Mudar estrutura do vault
- Encontrar problema importante
- Precisar que o outro agente faça algo específico

**❌ Não precisa atualizar para:**
- Edições menores
- Correções de typo
- Leitura de arquivos (sem modificação)
- Trabalho ainda em andamento

---

### Ao Finalizar Sessão

**SEMPRE atualizar antes de encerrar!**

1. **Copiar template** do SESSION_LOG.md
2. **Preencher** suas ações
3. **Adicionar** na seção "ÚLTIMAS MUDANÇAS" (no topo)
4. **Deixar mensagem** para outro agente se necessário
5. **Atualizar** "CONTEXTO ATUAL DO VAULT"
6. **Verificar** se deixou tarefas pendentes documentadas

---

## 📝 TEMPLATE DE ATUALIZAÇÃO

### Claude Code
```markdown
### 🔵 Claude Code - [DATA] ([HORA])
**Ações realizadas:**
- ✅ [Ação 1 - específica e clara]
- ✅ [Ação 2]
- ✅ [Ação 3]

**Arquivos modificados:**
- `caminho/arquivo.md` (descrição da mudança)
- `outro/arquivo.md` (o que foi feito)

**Próximos passos sugeridos:**
- [ ] [Tarefa que ficou pendente]
- [ ] [Outra tarefa]

**Estado do vault:**
- [Informação importante sobre estado atual]
- [Exemplo: "8 comandos ativos", "52 arquivos totais"]

**Mensagem para Gemini:**
> [Instrução direta se necessário]
> [Exemplo: "Valide nomenclatura dos arquivos criados em X"]
```

### Antigravity/Gemini
```markdown
### 🟢 Antigravity/Gemini - [DATA] ([HORA])
**Ações realizadas:**
- ✅ [Ação 1 - específica e clara]
- ✅ [Ação 2]
- ✅ [Ação 3]

**Arquivos criados/modificados:**
- `caminho/arquivo.md` (descrição da mudança)
- `outro/arquivo.md` (o que foi feito)

**Próximos passos sugeridos:**
- [ ] [Tarefa que ficou pendente]
- [ ] [Outra tarefa]

**Estado do vault:**
- [Informação importante sobre estado atual]

**Mensagem para Claude:**
> [Instrução direta se necessário]
> [Exemplo: "Integre essas notas ao MOC de Aprendizado"]
```

---

## 🎯 CASOS DE USO

### Caso 1: Processamento de Conteúdo Longo (Gemini → Claude)

**Fluxo:**
1. 🟢 **Gemini:** Processa 5 lives do Alan Nicolas (1M tokens, 2h de trabalho)
2. 🟢 **Gemini:** Cria 5 notas estruturadas em `03_APRENDIZADO/.../notas/`
3. 🟢 **Gemini:** Atualiza SESSION_LOG.md:
   ```markdown
   **Mensagem para Claude:**
   > Criei 5 notas de lives. Validar:
   > 1. Nomenclatura está correta?
   > 2. Localização em 03_APRENDIZADO ok?
   > 3. Precisa atualizar _MOC_Aprendizado.md com essas notas
   ```
4. 🔵 **Claude:** Inicia sessão, lê SESSION_LOG.md
5. 🔵 **Claude:** Valida nomenclatura (corrige se necessário)
6. 🔵 **Claude:** Atualiza MOC de Aprendizado
7. 🔵 **Claude:** Atualiza SESSION_LOG.md confirmando validação

---

### Caso 2: Criação de Estrutura (Claude → Gemini)

**Fluxo:**
1. 🔵 **Claude:** Cria novo projeto em `02_PROJETOS/Novo_Projeto/`
2. 🔵 **Claude:** Define estrutura de pastas padrão
3. 🔵 **Claude:** Atualiza SESSION_LOG.md:
   ```markdown
   **Mensagem para Gemini:**
   > Criei projeto "Novo_Projeto" em 02_PROJETOS/
   > Precisa popular README.md com conteúdo inicial
   > Usar estrutura definida em ESTRUTURA_PROJETOS.md
   ```
4. 🟢 **Gemini:** Inicia sessão, lê SESSION_LOG.md
5. 🟢 **Gemini:** Gera conteúdo para README.md do projeto
6. 🟢 **Gemini:** Atualiza SESSION_LOG.md confirmando criação

---

### Caso 3: Sincronização Diária

**Cenário:** Gassen trabalha com Claude de manhã e Gemini à tarde

**Manhã (Claude):**
- Planeja estrutura de novo curso
- Cria pastas e templates
- Documenta no SESSION_LOG.md

**Tarde (Gemini):**
- Lê o que Claude fez
- Processa aulas do curso
- Popula usando templates criados
- Documenta no SESSION_LOG.md

**Noite (Claude ou Gemini):**
- Qualquer um pode continuar
- Contexto completo disponível

---

## ⚠️ REGRAS IMPORTANTES

### ✅ SEMPRE:
1. Ler SESSION_LOG.md ao iniciar
2. Atualizar ao finalizar trabalho significativo
3. Deixar mensagens claras para o outro agente
4. Documentar mudanças estruturais
5. Manter template consistente

### ❌ NUNCA:
1. Ignorar mensagens deixadas pelo outro agente
2. Modificar/deletar entradas anteriores
3. Fazer mudanças conflitantes sem coordenar
4. Esquecer de documentar trabalho importante
5. Sobrescrever trabalho do outro agente

---

## 🔍 DETECTANDO CONFLITOS

### Sinais de Problema:
- Arquivo modificado por ambos sem sincronização
- Tarefas duplicadas
- Estruturas inconsistentes
- Links quebrados após mudanças

### Como Resolver:
1. **Parar** trabalho imediatamente
2. **Ler** SESSION_LOG.md completamente
3. **Identificar** o que cada agente fez
4. **Resolver** conflito (preservar melhor versão ou mesclar)
5. **Documentar** resolução no SESSION_LOG.md
6. **Continuar** trabalho sincronizado

---

## 📊 MÉTRICAS DE SUCESSO

**Sistema funcionando bem quando:**
- ✅ Zero conflitos de edição
- ✅ Tarefas continuam fluidamente entre agentes
- ✅ Contexto nunca é perdido
- ✅ Comunicação clara e eficiente
- ✅ Histórico completo de mudanças

**Sistema precisa ajuste quando:**
- ❌ Conflitos frequentes
- ❌ Trabalho duplicado
- ❌ Contexto perdido entre sessões
- ❌ Confusão sobre quem fez o quê

---

## 🛠️ FERRAMENTAS DE APOIO

### Comando /sync (Claude Code)
```
/sync
→ Atualiza SESSION_LOG.md automaticamente com trabalho da sessão
```

### Visualização Rápida
```bash
# Ver últimas 50 linhas do log
tail -50 SESSION_LOG.md

# Ver apenas mensagens
grep "Mensagem para" SESSION_LOG.md

# Ver últimas ações
grep "Ações realizadas:" SESSION_LOG.md -A 5
```

---

## 📚 INTEGRAÇÃO COM OUTROS PROTOCOLOS

Este protocolo trabalha em conjunto com:
- [[PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Para criar arquivos corretamente
- [[PROTOCOLO_REVISAO_SEMANAL.md]] - Para manutenção periódica
- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Para nomenclatura consistente

---

## 🎓 TREINAMENTO

### Para Novo Agente
1. Ler este protocolo completamente
2. Ler exemplos de uso em SESSION_LOG.md
3. Fazer primeiro update (supervised)
4. Revisar com usuário
5. Continuar autonomamente

### Para Usuário (Gassen)
1. Consulte SESSION_LOG.md quando trocar de agente
2. Deixe instruções explícitas se necessário
3. Valide sincronização periodicamente
4. Relate problemas para ajuste do protocolo

---

**Status:** ✅ Ativo desde 28/Nov/2025
**Versão:** 1.0
**Revisão:** Mensal (ou quando houver problemas)

---

**Este protocolo garante que Claude e Gemini trabalhem como uma equipe sincronizada, não como indivíduos isolados.** 🤝
