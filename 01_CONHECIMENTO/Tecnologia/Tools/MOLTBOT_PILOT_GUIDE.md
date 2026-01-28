---
created: 2026-01-28T11:05
updated: 2026-01-28T11:23
---
# 🦅 Guia Piloto: Moltbot (Docker Edition)

**Status:** Piloto (Beta)
**Versão:** 1.0
**Instalação:** `00_SISTEMA/Infra/Moltbot`

---

## 🎯 O que é?

O **Moltbot** (antigo Clawdbot) é o seu "Funcionário Digital Residente".
Diferente do Claude (Cérebro Estratégico) ou do n8n (Fábrica de Automação), o Moltbot é quem **executa tarefas humanas** no seu computador.

### O que ele FAZ

- **Navegação Web:** "Entre no site do banco e baixe o PDF."
- **WhatsApp:** "Mande mensagem pro Dr. Alexandre cobrando o documento." (Se configurado)
- **Agenda:** "Me lembre de beber água a cada 2 horas."

### O que ele NÃO faz

- **Processamento Pesado:** Não peça para ele resumir um livro (Use o Gemini).
- **Código Complexo:** Não peça para ele refatorar o sistema (Use o Claude).

---

## 🔒 Segurança (Regras do Piloto)

Este piloto roda em **Docker** para proteção.

1. **Sandbox:** Ele só enxerga a pasta interna dele e a pasta `_inbox` do Vault.
2. **Sem Acesso Root:** Ele não pode deletar arquivos do seu Windows.
3. **Memória Local:** Tudo o que ele "aprende" fica salvo em `00_SISTEMA/Infra/Moltbot/data`.

---

## 🚀 Como Usar

### 1. Iniciar

Abra o terminal na pasta `00_SISTEMA/Infra/Moltbot` e rode:

```bash
docker-compose up -d
```

### 2. Interagir

Se você configurou o Telegram/WhatsApp, chame ele por lá.
Se estiver usando via CLI (shim), use o comando no terminal do container.

### 3. Parar

```bash
docker-compose down
```

---

## 🛠️ Manutenção

**Atualizar:**

```bash
cd src
git pull
cd ..
docker-compose build --no-cache
docker-compose up -d
```

**Ver Logs:**

```bash
docker logs -f moltbot_pilot
```
