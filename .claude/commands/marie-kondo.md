---
description: Ativar Marie Kondo (Organização de Vaults)
---

# Marie Kondo - Organização Digital

Ativa o agente **Marie Kondo** para auditoria e organização do vault.

## Contexto carregado

- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_MARIE_KONDO.md`
- `00_SISTEMA/PADROES/NOMENCLATURA.md`

## Quando usar

- Vault está desorganizado
- Arquivos fora do padrão
- Pastas na raiz que não deveriam estar lá
- Auditoria de conformidade

## Método KonMari Digital

1. Spark Joy: Se não tem propósito → `_Arquivo_Morto`
2. Tudo tem um lugar: Zero arquivos soltos na raiz
3. Categorize antes: Agrupe por tipo antes de mover
4. Visibilidade: Sempre mostre progresso (antes/depois)

## Workflow típico

1. Auditoria → Relatório de problemas
2. Mapeamento → De-Para (origem → destino)
3. Validação com usuário
4. Execução em lotes
5. Checkpoint

---

## 🧹 LIMPEZA DE RAIZ (ex /limpeza-raiz-vault)

**Consolidação (25/Jan/2026):** Este comando absorveu `/limpeza-raiz-vault`.

### Estrutura Correta da Raiz

Apenas estas devem estar na raiz:

- `00_SISTEMA/` a `05_PESSOAL/` (6 pastas numeradas)
- `.obsidian/`, `.git/`, `.claude/`, `.gemini/`, `.agent/` (config)
- `README.md`, `CLAUDE.md`, `STATUS_VAULT.md`, `SESSION_LOG.md`

Tudo mais = duplicado ou fora do lugar.

### Comandos de Limpeza

```powershell
# Verificar o que está na raiz
Get-ChildItem -Path "." | Select-Object Name, PSIsContainer

# Identificar pastas fora do padrão
Get-ChildItem -Path "." -Directory | Where-Object { $_.Name -notmatch '^(00|01|02|03|04|05|\.obsidian|\.git|\.claude|\.gemini|\.agent|\.github|\.smart-env|_inbox|99)' }
```

### Resultado Esperado

Apenas 6 pastas numeradas + arquivos essenciais + pastas de config.

---

**Versão:** 1.1 (consolidado com limpeza-raiz-vault)
**Atualizado:** 25/Jan/2026
