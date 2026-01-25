# ⚙️ Especificação Técnica: Workflows n8n (Secretária Biônica)

**Versão:** 1.0
**Status:** Especificação para Implementação

---

## 1. Workflow: Injestão de Contexto (Ouvido Biorgânico)

**Objetivo:** Capturar mensagens do usuário (Áudio/Texto) via WhatsApp/Telegram, transcrever se necessário, e salvar estruturado na Inbox do Vault.

### 🔌 Gatilhos (Triggers)

1.  **Webhook (EvolutionAPI):** Evento `messages.upsert` (Nova mensagem recebida).
2.  **Webhook (Telegram):** Evento `message` (Nova mensagem).

### ⚡ Fluxo Lógico (Steps)

1.  **Filtro de Origem:** Verificar `remoteJid` (WhatsApp) ou `chatId` (Telegram) para garantir que é o Gassen.
2.  **Router (Tipo de Mídia):**
    - **Caso Áudio:**
      - Baixar arquivo de mídia.
      - Enviar para OpenAI Whisper (Transcrever).
      - Output: `text_transcribed`.
    - **Caso Texto:**
      - Manter `text_body`.
3.  **Formatação Markdown:**
    - Criar frontmatter:
      ```yaml
      ---
      data: { { $now } }
      origem: whatsapp
      tipo: captura_rapida
      status: processar
      ---
      ```
    - Corpo: `{{ $json.text_transcribed || $json.text_body }}`
4.  **Gravação (File System):**
    - Node: `Write Binary File` (ou Antigravity API se disponível remotamente).
    - Caminho: `C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\_inbox\captura_{{ $now.format('YYYYMMDD_HHmm') }}.md`

### 📤 Saída Esperada

Um arquivo Markdown na pasta `_inbox` pronto para ser processado pela Névoa.

---

## 2. Workflow: Assistente Cognitivo (Gestão de Energia)

**Objetivo:** Monitorar o "nível de bateria" do usuário e sugerir tarefas adequadas.

### 🔌 Gatilhos (Triggers)

1.  **Schedule:** A cada 4 horas (08:00, 12:00, 16:00, 20:00).
2.  **Webhook Manual:** "Estou cansado" (via botão no Whats).

### ⚡ Fluxo Lógico (Steps)

1.  **Determinar Fase do Dia:**
    - 08:00 - 12:00: **Alta Energia (Criar)** -> Foco em Deep Work.
    - 13:00 - 17:00: **Média Energia (Gerenciar)** -> Reuniões, Emails.
    - 18:00 - 22:00: **Baixa Energia (Consumir/Planejar)** -> Estudos, Leitura leve.
2.  **Ler Contexto (Opcional - Complexo):**
    - Consultar `STATUS_VAULT.md` para ver projetos ativos.
3.  **Gerar Sugestão (LLM):**
    - Prompt: "São {{ $hour }} horas. Fase: {{ $fase }}. Usuário Gassen (TDAH). Sugira uma única ação alinhada com a fase."
4.  **Notificar:**
    - Enviar mensagem no WhatsApp: "🔋 Energia {{ $fase }}. Que tal focar em [SUGESTÃO] agora?"

---

## 3. Workflow: Orquestrador de Agentes (Névoa Dispatcher)

**Objetivo:** Processar o arquivo da Inbox e chamar o agente especialista.

### 🔌 Gatilhos (Triggers)

1.  **File Watcher (Local):** Monitorar pasta `_inbox`.
2.  **Webhook (Antigravity):** Chamada de ferramenta.

### ⚡ Fluxo Lógico (Steps)

1.  **Ler Arquivo:** Obter conteúdo do Markdown.
2.  **Classificar Intenção (LLM):**
    - Categorias: `TRAFEGO`, `DEFI`, `CODIGO`, `GERAL`.
3.  **Roteamento:**
    - Se `TRAFEGO` -> Adicionar tag `#pedro-sobral`, mover para `02_PROJETOS/Mkt`.
    - Se `DEFI` -> Adicionar tag `#lucas-amoedo`, mover para `02_PROJETOS/DeFi`.
    - Se `GERAL` -> Mover para `00_SISTEMA/processamento`.

---

## 📦 Requisitos de Instalação

- **Docker:** Container n8n oficial.
- **Credenciais:**
  - OpenAI API Key (Whisper/GPT-4o).
  - EvolutionAPI Token.
  - Acesso de escrita ao OneDrive/Filesystem local.
