# 🏗️ Arquitetura do Sistema: Secretária Biônica (GAIA)

**Versão:** 1.0
**Data:** 17/Dez/2025
**Status:** Em Implementação

---

## 🎯 Objetivo Core

Prover um sistema de assistência virtual híbrido (IA + Automação) projetado especificamente para um usuário com **TDAH e Altas Habilidades**, eliminando a carga cognitiva de tarefas repetitivas e gerenciando ativamente o foco e a energia.

## 🧠 Princípios de Design (Elena Vasquez)

1.  **Scaffolding Cognitivo:** A assistente nunca entrega uma "parede de texto". Tudo é estruturado (Bullet points, Leituras guiadas).
2.  **Gestão de Energia:** O sistema reconhece o ciclo do usuário. Tarefas criativas de manhã, tarefas burocráticas à tarde/noite.
3.  **Consumo vs. Criação:** O sistema monitora ativamente se o usuário está apenas consumindo informação (passivo) e o empurra para a criação (ativo).
4.  **Zero Atrito:** Interfaces via WhatsApp/Telegram para captura rápida. Backend (Vault) para organização estruturada.

---

## 🧩 Componentes da Arquitetura

### 1. Módulo de Contexto Persistente (Memória)

_Onde as informações vivem e se conectam._

- **Estrutura no Vault:** `00_SISTEMA/memoria/`
- **Tipos de Memória:**
  - **Curto Prazo:** Logs de interação diária (`SESSION_LOG.md`).
  - **Longo Prazo:** MOCs e Base de Conhecimento (`01_CONHECIMENTO`).
  - **Episódica:** Diário de bordo e decisões (`02_PROJETOS/*/decisoes/`).
- **Tecnologia:** Obsidian (Frontend da Memória) + Busca Semântica (futuro: Vector DB local/remoto).

### 2. Módulo Assistente Cognitivo (O "Cérebro")

_Quem pensa, planeja e decide._

- **Persona:** Névoa 3.0 (GAIA - Generative Artificial Intelligence Assistant).
- **Motor:** Antigravity (Gemini 3 Pro) e Claude Code (Claude 3.5 Sonnet).
- **Função:** Processar entradas desestruturadas (voice dumps, textos rápidos) e transformá-las em ações estruturadas no Vault.

### 3. Módulo de Interface (A "Face")

_Como o usuário interage._

- **Canais:** WhatsApp e Telegram.
- **Gateway:** EvolutionAPI (WhatsApp) / Telegram Bot API.
- **Funcionalidades:**
  - Envio de áudio (transcrição automática via n8n).
  - Envio de imagens/textos.
  - Recebimento de "Daily Briefings".

### 4. Módulo de Orquestração (Os "Braços")

_Quem executa as tarefas repetitivas._

- **Motor:** n8n (Self-hosted).
- **Workflows Principais:**
  - **Injestão:** Receber msg -> Transcrever -> Salvar no Inbox do Vault.
  - **Rituais:** Script matinal que lê calendário e tarefas -> Gera Briefing.
  - **Sanidade:** Script semanal que verifica "links quebrados" ou projetos estagnados.

---

## 🔄 Fluxo de Dados (Exemplo)

1.  **Captura:** Usuário manda áudio no WhatsApp: "Tive uma ideia para a KabaK, fazer um anúncio estilo X."
2.  **Injestão (n8n):** Recebe áudio -> Transcreve (OpenAI Whisper) -> Envia para Webhook Antigravity (ou salva direto em Markdown).
3.  **Processamento (Névoa):** Lê o novo arquivo na Inbox -> Identifica projeto "KabaK" -> Move para `02_PROJETOS/KabaK/ideias/`.
4.  **Feedback:** Envia msg no WhatsApp: "Ideia salva em KabaK. Quer detalhar o roteiro agora?"

## 🛠️ Stack Tecnológico

- **Core:** Obsidian (Vault Local)
- **IA:** Gemini 1.5 Pro (Processamento Massivo) + Claude 3.5 Sonnet (Raciocínio)
- **Automação:** n8n (Docker)
- **Mensageria:** EvolutionAPI (Docker)

---

## ⚠️ Limites e Restrições

- **Tokens:** Respeitar limite de 30KB para processamento seguro no Gemini.
- **Privacidade:** Dados sensíveis ficam no Vault Local, não em clouds públicas desnecessárias.
