---
description: Workflow para criar e implantar a Secretária Biônica (Assistente Virtual)
---

# 🤖 Workflow: Criação da Secretária Biônica

Este workflow guia o processo de instanciar a "Secretária Biônica" (GAIA/Névoa 3.0), integrando n8n, Antigravity e o Vault.

## 1. Preparação e Diagnóstico

- [ ] Verificar acesso ao n8n
- [ ] Verificar acesso ao Antigravity (Google IDE)
- [ ] Validar existência dos arquivos de arquitetura (Baseado em `CATALOGO_Secretaria_Bionica_Arquitetura_Completa.md`)

## 2. Definição da Arquitetura (Blueprint)

- [ ] Criar/Validar `ARQUITETURA_SECRETARIA_BIONICA.md` com os 4 Pilares:
  1.  **Contexto Persistente:** Memória Híbrida (Vector + Graph)
  2.  **Assistente Cognitivo:** Gestão de Energia e Decisão (n8n)
  3.  **Interface:** WhatsApp/Telegram via EvolutionAPI
  4.  **Orquestração:** Sistema de Eventos (BionicOrchestrator)

## 3. Implementação dos Módulos

### Módulo 1: Cérebro (Névoa/Antigravity)

- [ ] Consolidar prompts da Névoa para "Névoa 3.0"
- [ ] Criar arquivo de Persona `PROMPT_NEVOA_3.0.md`
- [ ] Definir regras de interação com TDAH (Scaffolding, brevidade)

### Módulo 2: Braços (n8n)

- [ ] Importar/Criar workflow de "Injestão de Contexto" (Telegram -> Vault)
- [ ] Importar/Criar workflow de "Gestão de Energia" (Algoritmo Consumir vs Criar)
- [ ] Configurar Webhooks para comunicação Antigravity <-> n8n

### Módulo 3: Memória (Contexto)

- [ ] Estruturar pasta de memória no Vault (`00_SISTEMA/memoria/`)
- [ ] Definir formato de logs de interação

## 4. Validação e Teste

- [ ] **Teste de Fluxo:** Enviar mensagem no Telegram -> Ver refletido no Vault
- [ ] **Teste de Cognição:** Pedir tarefa complexa -> Ver Antigravity planejar
- [ ] **Walkthrough:** Gerar relatório de status do sistema

## 5. Manutenção

- [ ] Estabelecer rotina semanal de revisão de logs
- [ ] Atualizar "Lista Negra" de ações automatizadas
