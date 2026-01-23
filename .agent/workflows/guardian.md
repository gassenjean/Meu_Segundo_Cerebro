---
description: Guardian - Agente de Manutenção Automática do Vault
---

# Guardian - Zelador Inteligente

Orquestra skills existentes para manter o vault organizado automaticamente.

## Contexto Obrigatório

**SEMPRE carregar antes de qualquer ação:**
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_GUARDIAN.md` (protocolo completo)
- `00_SISTEMA/PADROES/NOMENCLATURA.md` (lei do Guardian)

## Filosofia

```
"Guardian ORQUESTRA, não duplica."
"NOMENCLATURA.md é lei."
"Começa propondo, ganha confiança para executar."
```

## Comandos Disponíveis

### `/guardian` ou `/guardian help`
Mostra ajuda e status atual do vault.

### `/guardian audit`
**Nível 1 (READ)** - Auditoria completa sem modificar nada.

**Workflow:**
1. Carregar NOMENCLATURA.md
2. Executar varredura do vault (simular vault-auditor)
3. Verificar:
   - Nomenclatura (prefixos, CamelCase, underscores)
   - Localização (arquivos na pasta certa)
   - Raiz (apenas arquivos permitidos)
   - Links quebrados (wikilinks inválidos)
4. Gerar relatório em `00_SISTEMA/RELATORIOS/AUDITORIA_VAULT_[DATA].md`
5. Exibir resumo ao usuário

**Output:** Relatório detalhado + resumo

### `/guardian fix`
**Nível 2 (PROPOSE)** - Propõe correções e aguarda aprovação.

**Workflow:**
1. Executar `/guardian audit` primeiro
2. Para cada problema encontrado:
   - Mostrar: arquivo atual → correção proposta
   - Gerar comando pronto para executar
3. Perguntar: "Aprovar correções? (y/n/selecionar)"
4. Se aprovado:
   - Criar backup
   - Executar correções
   - Atualizar MOCs afetados
   - Registrar em SESSION_LOG
5. Exibir relatório de execução

**Output:** Lista de propostas → Confirmação → Execução

### `/guardian auto`
**Nível 3 (EXECUTE)** - Execução automática com backup.

**Pré-requisito:** Só usar após 10+ execuções de `/guardian fix` sem erros.

**Workflow:**
1. Verificar permissão Nível 3 (perguntar usuário se primeira vez)
2. Criar backup completo em `.guardian_backup_[DATA]/`
3. Executar auditoria
4. Executar correções automaticamente
5. Loop Ralph: verificar cada correção
   - Se falhou → reverter + alertar
6. Atualizar MOCs
7. Atualizar STATUS_VAULT.md
8. Registrar em SESSION_LOG
9. Exibir relatório final

**Output:** Relatório completo + backup

### `/guardian clean-root`
**Nível 2 (PROPOSE)** - Limpa arquivos invasores da raiz.

**Arquivos PERMITIDOS na raiz:**
- `CLAUDE.md`
- `README.md`
- `STATUS_VAULT.md`
- `SESSION_LOG.md`
- `PC_SYNC_LOG.md`
- `.gitignore`
- Pastas: `.claude/`, `.gemini/`, `.obsidian/`, `.git/`, `.agent/`, `.venv/`
- Pastas numeradas: `00_SISTEMA/` até `05_PESSOAL/`

**Workflow:**
1. Listar todos os arquivos na raiz
2. Identificar invasores (não estão na lista permitida)
3. Para cada invasor:
   - Detectar tipo (template, prompt, checkpoint, etc)
   - Propor destino correto
4. Mostrar lista de movimentações propostas
5. Aguardar aprovação
6. Se aprovado → mover + atualizar MOCs

### `/guardian status`
**Nível 1 (READ)** - Estatísticas rápidas do vault.

**Exibe:**
- Total de arquivos
- Arquivos com problemas de nomenclatura
- Arquivos fora de lugar
- Última auditoria realizada
- Saúde geral (%)

### `/guardian restore [ID]`
**Nível 3** - Reverte execução anterior.

**Workflow:**
1. Listar backups disponíveis em `.guardian_backup_*/`
2. Se ID fornecido → restaurar específico
3. Se não → mostrar lista para escolher
4. Confirmar antes de restaurar
5. Executar restauração
6. Registrar em SESSION_LOG

## Skills Orquestradas

Guardian usa estas skills existentes (não duplica):

| Skill | Quando Usar | Localização |
|-------|-------------|-------------|
| vault-auditor | audit, fix, auto | `.gemini/skills/vault-auditor/` |
| architect-linter | audit (verificações mecânicas) | `.gemini/skills/architect-linter/` |
| validate | fix (validar antes de mover) | `.gemini/skills/validate/` |
| vault-organizer | fix, auto (mover/renomear) | `.gemini/skills/vault-organizer/` |
| session-logger | fix, auto (registrar ações) | `.gemini/skills/session-logger/` |
| status-updater | auto (atualizar métricas) | `.gemini/skills/status-updater/` |

## Regras de Nomenclatura (Resumo)

**Prefixos obrigatórios (MAIÚSCULAS):**
- `MOC_` ou `_MOC_` - Maps of Content
- `PLANO_` - Planejamento
- `TEMPLATE_` - Templates
- `CHECKPOINT_` - Snapshots
- `STATUS_` - Status
- `GUIA_` - Guias

**Formato de datas:** `DDMMMYYYY` (ex: 22JAN2026)

**Regras gerais:**
- CamelCase: `Categoria_Subcategoria`
- Underscores para espaços (nunca espaços reais)
- Máximo 60 caracteres
- Sem caracteres especiais: `/ \ : * ? " < > |`

## Níveis de Permissão

```
Nível 1 (READ):     Auditar, gerar relatórios
Nível 2 (PROPOSE):  Propor + aguardar aprovação ← COMEÇA AQUI
Nível 3 (EXECUTE):  Executar automaticamente ← GANHAR CONFIANÇA
```

**Evolução:** Após 10+ execuções de `/guardian fix` sem problemas, usuário pode habilitar Nível 3.

## Loop Ralph

Após cada ação de modificação, verificar:
- [ ] Arquivo de destino existe?
- [ ] Arquivo de origem foi removido?
- [ ] Nome está correto?
- [ ] MOC foi atualizado?
- [ ] Backup existe?

Se qualquer verificação falhar → REVERTER + ALERTAR.

## Exemplos de Uso

```
# Ver problemas no vault
/guardian audit

# Corrigir com aprovação
/guardian fix

# Limpar raiz
/guardian clean-root

# Depois de ganhar confiança
/guardian auto

# Ver estatísticas
/guardian status
```

## Anti-Patterns

**NUNCA:**
- Pular direto para Nível 3 sem testar Nível 2
- Ignorar NOMENCLATURA.md
- Executar sem backup
- Aprovar em massa sem revisar

**SEMPRE:**
- Ler NOMENCLATURA.md antes de decidir
- Criar backup antes de modificar
- Verificar resultado após cada ação (Loop Ralph)
- Registrar ações em SESSION_LOG

## Troubleshooting

**"Não sei onde mover arquivo X"**
1. Ler NOMENCLATURA.md
2. Identificar tipo do arquivo (template, plano, checkpoint, etc)
3. Consultar tabela de localizações no PROTOCOLO_GUARDIAN.md
4. Se ainda não souber → perguntar ao usuário

**"Correção falhou"**
1. Loop Ralph detectou problema
2. Reverter automaticamente
3. Exibir erro ao usuário
4. Sugerir ação manual

**"Muitos problemas encontrados"**
1. Priorizar por tipo (nomenclatura > localização > links)
2. Executar em lotes de 10
3. Checkpoint entre lotes
4. Pausar se erro crítico

---

**Versão:** 1.0
**Criado:** 22/JAN/2026
**Protocolo:** [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GUARDIAN.md]]

**"Gassen odeia organizar manualmente. Guardian automatiza o tédio."**
