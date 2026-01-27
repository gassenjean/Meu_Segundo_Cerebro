# DOSSIÊ TÉCNICO: ClawdBot

**Data:** 27/Jan/2026
**Analista:** Alan Nicolas (Gemini Guardian)
**Tipo:** Open Source AI Agent Framework
**Repo:** `clawdbot/clawdbot`
**Licença:** MIT

---

## 1. Identity Core (O que é *realmente*?)

ClawdBot não é apenas um "chatbot". É um **Funcionário Digital Autônomo (AI Employee)** que vive no seu hardware local (Local-First) e se comunica com o mundo via gateways de mensageria (WhatsApp, Telegram, iMessage).

**A Diferença Vital:**
Enquanto o Claude (Anthropic) é o *cérebro* (API), o ClawdBot é o *corpo*. Ele dá ao LLM mãos (Shell, Browser, Filesystem) e ouvidos (Polling de mensagens), permitindo que ele inicie interações (Proatividade) em vez de apenas reagir.

---

## 2. Arquitetura do Sistema

O sistema opera sobre **Node.js (v22+)** e segue uma arquitetura modular de 4 pilares:

### A. The Gateway (O Hub)

O centro nervoso que conecta o AI Agent às interfaces humanas.

* **Canais Suportados:** WhatsApp, Telegram, Discord, Slack, Signal, iMessage.
* **Função:** Roteia mensagens, gerencia autenticação e mantém o "state" da conexão.

### B. The Agent (O Cérebro)

Onde reside a lógica de raciocínio.

* **LLMs:** Agnostico (Claude 3.5 Sonnet recomendado, GPT-4o suportado).
* **Contexto:** Gerencia a janela de contexto e decisão de uso de ferramentas.

### C. The Skills (As Mãos)

Módulos de execução que dão poder real ao agente:

* **System Control:** Execução de Shell Scripts (Bash/Zsh).
* **Browser Control:** Navegação web headless (Puppeteer/Playwright) para preencher formulários e extrair dados.
* **File I/O:** Leitura e escrita direta no disco local.

### D. The Memory (A Alma - `SOUL.md`)

Diferente de sessões efêmeras (Chat), o ClawdBot tem **Memória Persistente Baseada em Arquivos**.

* **Formato:** Markdown/JSON locais.
* **Arquivos Críticos:**
  * `SOUL.md`: A personalidade e diretrizes core.
  * `MEMORY.md`: Fatos aprendidos sobre o usuário (long-term).
  * `history/*.json`: Logs de conversas passadas.

---

## 3. Tech Stack & Requisitos

* **Runtime:** Node.js >= 22.0.0
* **Package Manager:** pnpm (recomendado), npm, bun.
* **OS:** macOS (nativo), Linux (Debian/Ubuntu), Windows (via WSL2).
* **Deployment:** Docker (recomendado para segurança) ou Bare Metal.

---

## 4. Análise de Segurança (The "Honey Pot" Risk)

**⚠️ ALERTA CRÍTICO:** O modelo "Local-First" do ClawdBot é uma faca de dois gumes.

1. **Superfície de Ataque:** Como o bot tem permissão de Shell e File System, um prompt injection ou comando malicioso via chat pode comprometer a máquina inteira (RCE - Remote Code Execution).
2. **Dados em Plaintext:** Memórias e tokens são armazenados localmente sem criptografia por padrão. Malware de roubo de info (InfoStealers) adoraria encontrar a pasta do ClawdBot.
3. **Sandboxing:** É **obrigatório** rodar via Docker com flags de restrição (`--read-only`, usuário non-root) se for expor publicamente.
4. **DM Pairing:** O sistema usa um mecanismo de pareamento para impedir que estranhos mandem comandos via Telegram/WhatsApp. Nunca desative isso.

---

## 5. Implementação "Alan Nicolas Style"

Para integrar ao nosso ecossistema (Segundo Cérebro):

1. **Instalação Segura:**

    ```bash
    git clone https://github.com/clawdbot/clawdbot.git
    cd clawdbot
    pnpm install
    cp .env.example .env # Configurar API keys Anthropic
    ```

2. **Configuração da Alma (`SOUL.md`):**
    Configurar o arquivo para adotar a persona de um "Gerente de Execução" que obedece aos protocolos do Vault (NOMENCLATURA.md).

3. **Skills Customizadas:**
    Criar scripts Node.js em `./skills` que permitam ao bot ler/escrever diretamente na pasta do Vault (`Meu_Segundo_Cerebro`), transformando-o em um "Bibliotecário Ativo".

---

## 6. Veredito Final

* **Robustez:** Alta (Comunidade ativa 20k+ stars).
* **Complexidade:** Média/Alta (Exige conhecimento de Node e Docker).
* **Utilidade:** **Extrema**. É o elo perdido para automação proativa (ex: ele te manda mensagem no WhatsApp cobrando uma tarefa atrasada).

**Recomendação:** Implementar em ambiente isolado (Docker) para testar como "Secretário Executivo" via WhatsApp.

---
*Gerado via Deep Research por Alan Nicolas.*
