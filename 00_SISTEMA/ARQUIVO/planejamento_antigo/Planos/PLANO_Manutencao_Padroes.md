---
criado: 2025-11-27T13:47:13-03:00
atualizado: 2025-11-27T13:47:13-03:00
---

# PLANO: Manutenção de Padrões e Organização

**Data:** 27/Nov/2025
**Status:** 🟢 Ativo
**Contexto:** Garantir que o Segundo Cérebro permaneça organizado a cada interação.

## 🎯 Objetivo

Estabelecer um protocolo rígido e rotinas automáticas para que a entropia (desorganização) não se acumule no vault.

## 🔄 O Ciclo de Manutenção Contínua

### 1. Pré-Interação (Check-in)

Antes de começar qualquer tarefa complexa:

- [ ] Verificar `STATUS_VAULT.md` para entender o contexto.
- [ ] Se for criar arquivos, rodar `/validate` (Modo 1).

### 2. Durante a Execução (Anti-Entropia)

- **Regra de Ouro:** Nunca criar arquivo sem saber onde ele vai.
- **Nomenclatura:** Validar contra `NOMENCLATURA.md` em tempo real.
- **Estrutura:** Se criar projeto, usar `ESTRUTURA_PROJETOS.md`.

### 3. Pós-Interação (Check-out)

Ao finalizar uma sessão ou tarefa:

- [ ] Atualizar `STATUS_ATUAL.md` do projeto (se aplicável).
- [ ] Atualizar MOCs se houve criação de arquivos.
- [ ] Rodar `/validate` (Modo 2 - Auditoria) para garantir que nada ficou fora do lugar.

## 🛠️ Ferramentas de Apoio

### Workflows Automatizados

- **/validate:** Auditoria instantânea de estrutura e nomes.
- **/system:** Manutenção geral e limpeza.

### Checkpoints

- **Semanal:** Sexta-feira 17h (Protocolo existente).
- **Sessão:** Ao final de cada grande implementação.

## 📋 Ações Imediatas (Plano de Ação)

1. **Auditoria Geral:**
   - Rodar `/validate` em todo o vault (Feito parcialmente).
   - Corrigir desvios encontrados (Ex: `DeFi_Verso_2025` corrigido).

2. **Limpeza da Raiz:**
   - Manter apenas `CLAUDE.md`, `README.md`, `STATUS_VAULT.md`.
   - Mover ou deletar arquivos temporários (`_ul`, etc).

3. **Padronização de Projetos:**
   - Garantir que todos em `02_PROJETOS` tenham `README.md` e `STATUS_ATUAL.md`.

## 📊 Métricas de Sucesso

- Zero arquivos na raiz (exceto permitidos).
- 100% dos projetos com estrutura padrão.
- MOCs sincronizados com a estrutura de pastas.
