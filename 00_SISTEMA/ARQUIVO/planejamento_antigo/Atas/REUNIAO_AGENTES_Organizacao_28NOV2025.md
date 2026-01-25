---
criado: 2025-11-28
tipo: reuniao_agentes
participantes:
  - Névoa
  - Elena
  - Alan
objetivo: Criar plano de organização do vault
atualizado: 2025-11-28T11:02:45-03:00
---

# 🤝 REUNIÃO DE AGENTES: ORGANIZAÇÃO DO VAULT

**Convocada por:** Gassen
**Data:** 28/Nov/2025 - 11:00
**Participantes:** Névoa (Orquestração), Elena (Produtividade), Alan (Sistemas)

---

## 🎯 PROBLEMA IDENTIFICADO

Após a migração de ~1500 arquivos, o vault apresenta:

1.  **Arquivos soltos na raiz** de pastas (ex: `Cursos_*.md` em `03_APRENDIZADO`)
2.  **Pastas com nomes inconsistentes** (ex: `Alan_Nicolas_Academia_Lendaria` vs padrão)
3.  **Duplicatas potenciais** (ex: 3 pastas do Alan)
4.  **Falta de estrutura interna** nas pastas migradas

---

## 💬 DISCUSSÃO DOS AGENTES

### 🌫️ NÉVOA (Orquestração):

> "Precisamos de um agente especializado em organização de vaults. Alguém que entenda tanto os padrões do sistema quanto a metodologia do Alan Nicolas. Elena, você tem experiência com organização pessoal. Alan, você conhece a estrutura técnica. Vamos criar esse agente juntos?"

### 🧠 ELENA (Produtividade):

> "Concordo. O problema não é só técnico - é cognitivo. O Gassen tem TDAH. Se ele abrir o Obsidian e ver bagunça, vai travar. Precisamos de:
>
> 1. **Inbox de Migração:** Pasta temporária para processar aos poucos
> 2. **Regras claras:** O que vai onde
> 3. **Automação:** Scripts para renomear em massa"

### 🤖 ALAN (Sistemas):

> "Do ponto de vista técnico, sugiro:
>
> 1. **Auditoria:** Listar todos os arquivos fora do padrão
> 2. **Mapeamento:** Criar um 'De-Para' (Origem → Destino)
> 3. **Execução em lotes:** Mover 50 arquivos por vez, não tudo de uma vez
> 4. **Validação:** Verificar links quebrados após cada lote"

---

## 🎨 PROPOSTA: AGENTE "MARIE KONDO"

**Nome:** Marie Kondo (Especialista em Organização de Vaults)
**Função:** Auditar, mapear e organizar arquivos seguindo os padrões do sistema

**Princípios:**

1.  **Spark Joy (Digital):** Se o arquivo não tem propósito claro, vai para `_Arquivo_Morto`
2.  **Tudo Tem um Lugar:** Nenhum arquivo na raiz, tudo em pastas categorizadas
3.  **Visibilidade:** Criar dashboards visuais do progresso

**Ferramentas:**

- Scripts PowerShell para renomeação em massa
- Checklist de conformidade com `NOMENCLATURA.md`
- Templates de estrutura interna para cursos

---

## 📋 PLANO DE AÇÃO PROPOSTO

### FASE 1: Auditoria (1h)

- [ ] Listar todos os arquivos `.md` soltos na raiz de `01_CONHECIMENTO` e `03_APRENDIZADO`
- [ ] Identificar pastas com nomes fora do padrão
- [ ] Criar `RELATORIO_AUDITORIA_ORGANIZACAO.md`

### FASE 2: Mapeamento (30min)

- [ ] Criar `MAPA_REORGANIZACAO.md` (De-Para)
- [ ] Validar com Gassen antes de mover qualquer arquivo

### FASE 3: Execução (2-3h)

- [ ] Criar estrutura interna para cursos (notas/, recursos/, README.md)
- [ ] Mover arquivos soltos para pastas apropriadas
- [ ] Renomear pastas para seguir padrão

### FASE 4: Validação (30min)

- [ ] Verificar links quebrados
- [ ] Atualizar MOCs
- [ ] Criar checkpoint

---

## ✅ DECISÃO FINAL

**NÉVOA:** "Vamos criar a Marie Kondo e executar a Fase 1 agora. Gassen, você aprova?"

**Próximo Passo:** Criar `PROMPT_AGENTE_MARIE_KONDO.md` e iniciar auditoria.
