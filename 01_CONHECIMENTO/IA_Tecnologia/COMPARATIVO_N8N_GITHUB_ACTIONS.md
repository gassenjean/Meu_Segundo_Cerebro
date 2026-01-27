---
created: 2026-01-26T11:56
updated: 2026-01-26T11:56
---
# COMPARATIVO: n8n vs GitHub Actions

**Contexto:** Decisão de Stack de Automação (T037)
**Researcher:** Gemini Guardian
**Data:** 26/Jan/2026

## 1. Resumo Executivo (Qual usar?)

* **Use GitHub Actions (GHA) se:** A automação for sobre **CÓDIGO**. (CI/CD, testes, deploy, code review, linting). É o padrão da indústria para dev.
* **Use n8n se:** A automação for sobre **NEGÓCIO/DADOS**. (Integrar WhatsApp, Notion, Gmail, CRM, Agentes de IA). É o rei do Low-Code/No-Code com poder de Python.

**Para a Névoa/Gassen:** Precisamos de **AMBOS**, mas para fins diferentes.

## 2. Tabela Comparativa (2026)

| Critério | n8n (Self-Hosted) | GitHub Actions |
| :--- | :--- | :--- |
| **Foco** | Processos, Integrações, Agentes IA | CI/CD, DevSecOps, Builds |
| **Interface** | Visual (Nós e setas) | Código (YAML) |
| **Curva de Aprendizado** | Baixa/Média (Intuitivo) | Média/Alta (Requer dev knowledge) |
| **IA Nativa** | **Excelente** (Nodes de IA nativos - LangChain) | Limitada (Via scripts externos) |
| **Trigger** | Webhooks, Cron, Eventos de Apps | Pushes, PRs, Issues no Git |
| **Custo** | Zero (Self-hosted) + Server | Cobrado por minuto (Free tier generoso) |
| **Debug** | Visual (Vê o dado passar) | Logs de texto (Console) |
| **Persistência** | Ótima (Wait for webhook) | Limitada (Timeout de jobs) |

## 3. n8n - Prós e Contras

### ✅ Prós (Poder da Névoa)

1. **Orquestrador de IA Visual:** O n8n virou a melhor ferramenta para criar fluxos de IA (RAG, Agentes) visualmente.
2. **Conectividade Total:** Conecta fácil com Notion, Google, WhatsApp API. No GHA isso exige muita configuração de secrets/scripts.
3. **Human-in-the-loop:** Fácil criar fluxos que "param e esperam" você aprovar no Telegram.

### ❌ Contras

1. **Gestão de Infra:** Se rodar self-hosted, VOCÊ é o suporte. Se o servidor cair, a automação para.
2. **Segurança:** Recentemente teve um CVE crítico (Jan 2026). Exige ficar atento a updates.

## 4. GitHub Actions - Prós e Contras

### ✅ Prós (Robustez)

1. **Indestrutível:** Roda na infra da Microsoft. Zero manutenção de servidor.
2. **Versionado:** Toda a automação fica no git. Se quebrar, dá rollback.
3. **Segurança:** Secrets management de nível enterprise.

### ❌ Contras

1. **Dev-Centric demais:** Para fazer algo simples (ex: "se receber email, salve no notion") é um inferno de scripts e APIs no YAML.
2. **Difícil de Debugar:** Você só vê o erro depois que rodou e falhou.

## 5. Recomendação para Nosso Caso

### Cenário 1: "Quero que o Vault arrume os links automaticamente"

-> **Use GitHub Actions.** É manipulação de arquivo, roda no repo.
-> *Exemplo:* Linter de Markdown, Verificador de Links quebrados.

### Cenário 2: "Quero receber um resumo das News de IA no meu Telegram"

-> **Use n8n.** É integração de sistemas externos + IA.
-> *Exemplo:* RSS -> n8n (Resumo Gemini) -> Telegram.

### Cenário 3: "Quero que a Névoa lembre dos compromissos"

-> **Use n8n (Brain).** O n8n gerencia a memória e o fluxo de dados.
-> **Use GHA (Body).** O GHA faz o backup do Vault toda noite.

## 6. Plano de Implementação

1. **Manter GitHub Actions para:** Sync, Backup, Linting, Validação de Nomenclatura (CI do Vault).
2. **Subir n8n (Local ou VPS) para:** Agentes de pesquisa (Ralphs), Integração com WhatsApp/Telegram, Processamento de e-mail.
