# TEMPLATE: Estrutura de Projeto

> **Como usar:** Copie esta estrutura para criar novo projeto
> Remova este bloco de instruções após criar

---

## Criar Pasta do Projeto

```bash
mkdir -p "02_PROJETOS/[Nome_Projeto]/{planejamento,checkpoints,docs,recursos,tarefas,metricas}"
```

## Estrutura Resultante

```
[Nome_Projeto]/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
├── checkpoints/
├── docs/
├── recursos/
├── tarefas/
└── metricas/
```

---

# README.md (copiar abaixo)

```markdown
# [Nome do Projeto]

**Status:** [Planejamento/Ativo/Pausado/Concluído]
**Início:** [Data]
**Prazo:** [Data ou "Ongoing"]
**Prioridade:** [Alta/Média/Baixa]

---

## 🎯 Objetivo

[Descrição concisa: o que é e por que existe]

## 📊 Progresso Atual

**Fase:** [Nome da fase atual]
**Progresso:** ░░░░░░░░░░ 0%

## 🔗 Links Importantes

- [[STATUS_ATUAL.md]] - Status detalhado
- [[planejamento/PLANO_Principal.md]] - Plano principal

## 📁 Estrutura

- `planejamento/` - Planos e estratégias
- `checkpoints/` - Snapshots de progresso
- `docs/` - Documentação técnica
- `recursos/` - Assets e materiais
- `tarefas/` - Task management
- `metricas/` - KPIs e analytics

---

**Última atualização:** [Data]
```

---

# STATUS_ATUAL.md (copiar abaixo)

```markdown
# STATUS ATUAL - [Nome Projeto]

**Última atualização:** [Data e hora]

---

## ✅ ONDE ESTAMOS

**Fase Atual:** [Nome da fase]
**Progresso:** [Percentual]

### Última Ação
[O que foi feito]

### Estado Atual
[Descrição]

---

## 🎯 PRÓXIMAS AÇÕES

### Imediato
1. [ ] [Ação 1]
2. [ ] [Ação 2]

### Esta Semana
- [ ] [Meta 1]
- [ ] [Meta 2]

---

## 📋 DECISÕES RECENTES

### [Data] - [Decisão]
**Contexto:** [Por quê]
**Decisão:** [O quê]
**Motivo:** [Justificativa]

---

## 🚨 NÃO MUDAR

- [Item protegido 1]
- [Item protegido 2]

---

**Próxima revisão:** [Data]
```

---

**Template criado:** 17/Jan/2025
**Versão:** 1.0
