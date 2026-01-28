---
created: 2026-01-28T11:05
updated: 2026-01-28T11:21
---
# 🦅 Moltbot Pilot (Docker)

Este diretório contém a infraestrutura para rodar o **Moltbot** (antigo Clawdbot) de forma segura e isolada, integrada ao ecossistema do Segundo Cérebro.

## ⚠️ Aviso de Segurança

O Moltbot roda isolado em container Docker.

- **Acesso ao Disco:** Limitado à pasta `./data` (interna) e `../../../_inbox` (externa).
- **Não exponha** este container à internet pública sem configurar autenticação adequada.

## 🚀 Como Instalar

### 1. Preparar o Repositório

Você precisa clonar o código fonte do Moltbot dentro da pasta `src`:

```bash
cd 00_SISTEMA/Infra/Moltbot
git clone https://github.com/moltbot/moltbot.git src
```

### 2. Configurar Variáveis

Copie o exemplo e adicione suas chaves:

```bash
cp .env.example .env
# Edite o arquivo .env com sua ANTHROPIC_API_KEY
```

### 3. Iniciar o Piloto

Use o Docker Compose para construir e subir o container:

```bash
docker-compose up -d --build
```

### 4. Verificar

- Logs: `docker logs -f moltbot_pilot`
- Status: `docker ps`

## 📂 Estrutura

- `docker-compose.yml`: Definição do serviço e volumes.
- `.env`: (Você cria) Suas chaves secretas.
- `src/`: (Você clona) O código fonte do bot.
- `data/`: (Automático) Onde o bot guarda a memória persistente.
