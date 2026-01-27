---
created: 2026-01-25
updated: 2026-01-26T11:16
tags:
  - protocolo
  - session-log
  - rotacao
---

# PROTOCOLO: Rotação do SESSION_LOG

## Objetivo

Manter o `SESSION_LOG.md` leve (< 500 linhas / < 15k tokens) para não estourar limite de leitura do Claude Code.

## Regra de Rotação

**Manter apenas sessões dos últimos 7 dias.**

Sessões mais antigas devem ser arquivadas em:

```text
00_SISTEMA/ARQUIVO/LOGS/SESSION_LOG_ARQUIVO_[MES]_[ANO].md
```

## Quando Rotacionar

| Gatilho | Ação |
| ------- | ---- |
| SESSION_LOG > 500 linhas | Rotacionar imediatamente |
| SESSION_LOG > 20k tokens | Rotacionar imediatamente |
| Erro de leitura "exceeds maximum" | Rotacionar imediatamente |
| Primeira sessão do mês | Verificar e rotacionar se necessário |

## Como Rotacionar (Manual)

### Passo 1: Identificar ponto de corte

Buscar última sessão dentro dos 7 dias:

```bash
# No SESSION_LOG.md, encontrar linha da sessão mais antiga a manter
grep -n "^## " SESSION_LOG.md | tail -20
```

### Passo 2: Criar arquivo de histórico

Copiar sessões antigas para:

```text
00_SISTEMA/ARQUIVO/LOGS/SESSION_LOG_ARQUIVO_[MES]_[ANO].md
```

Se arquivo do mês já existir, fazer append.

### Passo 3: Reescrever SESSION_LOG

Manter apenas:

- Frontmatter
- Aviso de rotação
- Sessões dos últimos 7 dias
- Rodapé com link para arquivo

### Passo 4: Verificar tamanho

```bash
wc -l SESSION_LOG.md  # Deve ser < 500 linhas
```

## Template do SESSION_LOG Rotacionado

```markdown
---
criado: [data original]
atualizado: [data atual]
---

# SESSION_LOG

> **Rotação automática:** Sessões com mais de 7 dias são arquivadas em `00_SISTEMA/ARQUIVO/LOGS/`

## [Sessões recentes aqui...]

---

> **Arquivo histórico:** Sessões anteriores estão em `00_SISTEMA/ARQUIVO/LOGS/SESSION_LOG_ARQUIVO_[MES]_[ANO].md`
```

## Responsabilidade

| Agente | Ação |
| ------ | ---- |
| Claude Code | Verificar tamanho ao carregar `/nevoa` |
| Gemini | Executar rotação se solicitado |
| Guardian | Alertar se SESSION_LOG > 500 linhas |

## Métricas de Saúde

| Métrica | Saudável | Atenção | Crítico |
| ------- | -------- | ------- | ------- |
| Linhas | < 300 | 300-500 | > 500 |
| Tokens | < 10k | 10k-20k | > 20k |
| Dias | 7 | 10 | > 14 |

## Histórico de Rotações

| Data | Antes | Depois | Arquivado |
| ---- | ----- | ------ | --------- |
| 25/Jan/2026 | 2558 linhas | 300 linhas | SESSION_LOG_ARQUIVO_JAN_2026.md |

---

**Criado por:** Névoa
**Versão:** 1.0
