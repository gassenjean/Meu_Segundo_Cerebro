---
created: 2026-01-22T11:58
updated: 2026-01-22T11:58
---
# Plano de Implementação: Investigação Contínua Alan Nicolas

**Objetivo:** Transformar o vault em um organismo vivo que aprende continuamente com o "Universo Alan Nicolas" e aplica esse conhecimento automaticamente (Relógio Suíço).

## Contexto

O usuário deseja que Gemini (Antigravity) e Claude Code trabalhem por horas em segundo plano, com total contexto, para "não errar" e ter "cartas na manga".

## Estrutura do Projeto

Local: `02_PROJETOS/Estudo_Alan_Nicolas/`

## Fases de Implementação

### FASE 1: Estruturação (Imediata)

1. **Fundação:** Criar pastas e arquivos de controle (`PLANO`, `MOC`, `CHECKPOINT`).
2. **Mapeamento:** Identificar onde *exatamente* estão os "tesouros" do Alan no vault (já sabemos que estão em `03_APRENDIZADO` e `04_RECURSOS`).

### FASE 2: Evolução da Skill `alan-researcher` (Motor de Busca)

Transformar a skill de uma busca simples para um **Indexador Semântico**.

- **Script `index_alan.py`:**
  - Não apenas busca palavras-chave.
  - Lê cada arquivo encontrado.
  - Extrai: Princípios, Regras de Automação, Prompts.
  - Gera um `CONHECIMENTO_CONSOLIDADO.md`.

### FASE 3: Protocolo "Relógio Suíço" (Autonomia)

Definir como o Gemini e Claude operam em loop:

1. **Ciclo de Leitura:** O script roda a cada X tempo (ou sob comando) para re-ler o vault.
2. **Ciclo de Aplicação:** Quando o usuário pede algo no KabaK, o agente consulta o `CONHECIMENTO_CONSOLIDADO.md` obrigatoriamente.
3. **Memória Compartilhada:** O arquivo gerado fica em `00_SISTEMA/MEMORIA/` acessível a ambos.

## Entregáveis

- [ ] Projeto `Estudo_Alan_Nicolas` configurado.
- [ ] Skill `alan-researcher` v2.0 com capacidade de leitura massiva.
- [ ] Relatório inicial: "O que o Alan faria no KabaK agora?".
