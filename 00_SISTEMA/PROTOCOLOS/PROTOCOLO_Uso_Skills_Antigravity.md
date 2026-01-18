# 📄 PROTOCOLO: Uso de Skills Antigravity

**Responsável:** Antigravity (Gemini) / Claude Code
**Versão:** 1.0
**Ultima Atualização:** 18/JAN/2026

---

## 🎯 Visão Geral

Este protocolo define como utilizar as "Antigravity Skills", automações em Python que o Gemini 3 Pro executa diretamente no sistema de arquivos do usuário. Diferente das skills do Claude (que usam tools), estas são scripts standalone que rodam localmente.

### Quando Usar Skills Antigravity?

Use quando precisar de:

1. **Bulk Operations:** Mexer em centenas de arquivos de uma vez.
2. **Automação Repetitiva:** Coisas que você faz todo dia (sync, status).
3. **Execução Rápida:** Scripts Python rodam em milissegundos.
4. **Análise de Dados:** Coletar métricas do vault inteiro.

---

## 🤖 Skill #1: vault-organizer

### 📋 Visão Rápida

- **Função:** Organiza a raiz do vault e pastas de inbox.
- **Trigger:** "organizar vault", "marie kondo".
- **Local:** `.gemini/skills/vault-organizer/`

### Quando Usar

* ✅ Quando a raiz do vault estiver bagunçada (imagens, zips, PDFs soltos).
- ✅ Após baixar muitos arquivos da internet.
- ✅ Durante faxina semanal (Sexta-feira).
- ✅ Se houver uma pasta `Inbox_Migracao` cheia.

### Quando NÃO Usar

* ❌ Em pastas de projetos complexos (pode mover arquivos que deveriam ficar juntos).
- ❌ Se você não sabe o que os arquivos são (valide antes).
- ❌ Em arquivos de sistema ou configuração (`.git`, `node_modules`).

### 🔄 Como Usar

**Trigger Natural:**
> "Gemini, organize o vault por favor."
> "Pode rodar o marie kondo na raiz?"

**Workflow Automático:**

1. Gemini detecta a intenção.
2. Executa `scripts/organizer.py`.
3. Script move:
    - `.jpg`, `.png` → `04_RECURSOS/Assets/` ou conforme contexto.
    - `.zip` → `04_RECURSOS/Arquivos/`.
    - `.pdf` (se parecer livro) → `01_CONHECIMENTO/Biblioteca/`.
4. Gera relatório final.

**Exemplo Real:**

```text
Usuário: "A raiz ta uma bagunça, organiza aí"
Gemini: [Executa vault-organizer]
        Resultado:
        - Movidos 5 arquivos PNG para 04_RECURSOS/Assets
        - Movido 1 ZIP para 04_RECURSOS/Arquivos
        - Raiz limpa! ✨
```

---

## 📊 Skill #2: status-updater

### 📋 Visão Rápida

- **Função:** Atualiza `STATUS_VAULT.md` com métricas reais.
- **Trigger:** "atualizar status", "status vault".
- **Local:** `.gemini/skills/status-updater/`

### Quando Usar

* ✅ Após criar novos projetos ou skills.
- ✅ Ao finalizar uma sessão de trabalho longa.
- ✅ Quando quiser ver o progresso das fases (1-7).
- ✅ Para verificar estatísticas do vault (total arquivos, etc).

### Como Usar

**Trigger Natural:**
> "Atualize o status do vault."
> "Como está o progresso geral?" (pode disparar update antes de responder)

**Workflow Automático:**

1. Gemini detecta intenção.
2. Executa `scripts/updater.py`.
3. Script:
    - Conta arquivos em cada pasta.
    - Verifica fases completas baseadas em heurísticas.
    - Calcula % total.
    - Atualiza `STATUS_VAULT.md` preservando seu texto manual.
4. Confirmação visual.

**Exemplo Real:**

```text
Usuário: "Status update"
Gemini: [Executa status-updater]
        [Lê STATUS_VAULT.md]
        [Calcula novas métricas]
        [Escreve no arquivo]
        "Status atualizado! Estamos em 55% da Fase 7."
```

---

## 📝 Skill #3: session-logger

### 📋 Visão Rápida

- **Função:** Registra a sessão atual no `SESSION_LOG.md`.
- **Trigger:** "sync", "registrar sessão".
- **Local:** `.gemini/skills/session-logger/`

### Quando Usar

* ✅ **SEMPRE** ao finalizar seu trabalho no Gemini.
- ✅ Antes de passar a bola para o Claude ("Handoff").
- ✅ Se fez muitas alterações e quer garantir que fiquem registradas.

### Como Usar

**Trigger Natural:**
> "Sync."
> "Registrar sessão e encerrar."

**Workflow Automático:**

1. Gemini detecta "sync".
2. Executa `scripts/logger.py`.
3. Script:
    - Roda `git status` para ver o que mudou.
    - Gera um resumo formatado com emojis (🟣).
    - Insere no topo de `SESSION_LOG.md`.
4. Confirmação.

**Exemplo Real:**

```text
Usuário: "Sync"
Gemini: [Executa logger]
        [Detecta: criou 3 arquivos, modificou 1]
        [Escreve no SESSION_LOG.md]
        "Sessão registrada com sucesso! 🟣"
```

---

## 🛠️ Boas Práticas Gerais

1. **Confie, mas verifique:** Sempre leia a saída da skill. Se o `vault-organizer` diz que moveu 50 arquivos, veja para onde.
2. **Backups são vida:** Todas as skills fazem backup automático (`.bak`) dos arquivos que tocam. Se algo der errado, restaure o `.bak`.
3. **Use Triggers Claros:** Embora a IA entenda intenção, usar as palavras-chave ("organizar", "status", "sync") garante execução mais rápida.
4. **Git:** Mantenha seu git limpo (`git status` clean) antes de rodar operações massivas como `vault-organizer`, para facilitar o rollback se necessário.

---

## ✅ Checklist de Uso

**Antes de Executar:**

- [ ] O vault está em um estado estável?
- [ ] (Se Marie Kondo) Eu revisei o que está na raiz? Tem algo que NÃO deve ser movido?
- [ ] `SESSION_LOG.md` foi lido no início da sessão?

**Após Executar:**

- [ ] A skill reportou sucesso?
- [ ] O resultado visual parece correto?
- [ ] Se foi `status-updater`, o arquivo Markdown quebrou ou manteve formatação?
- [ ] Se foi `session-logger`, a entrada apareceu no topo do arquivo?

---

**Fim do Protocolo**
