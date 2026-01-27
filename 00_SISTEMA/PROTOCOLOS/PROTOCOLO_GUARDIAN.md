---
created: 2026-01-22T21:18
updated: 2026-01-26T11:16
---
# PROTOCOLO: Guardian - Agente de Manutenção Automática

**Manutenção Inteligente do Vault via Orquestração de Skills**

**Criado:** 22/JAN/2026
**Versão:** 1.0
**Status:** 🟡 IMPLEMENTAÇÃO
**Propósito:** Eliminar manutenção manual do vault através de automação inteligente

---

## 🎯 CONCEITO FUNDAMENTAL

> **"Guardian é uma PERSONA de manutenção que ORQUESTRA skills existentes.**
> **Ele não duplica - ele delega. NOMENCLATURA.md é sua lei."**

**Origem:** Convergência Claude + Gemini (22/Jan/2026)
- Claude propôs: VAULT_GUARDIAN (orquestrador de skills)
- Gemini propôs: /guardian (persona de manutenção)
- **Resultado:** São a MESMA coisa. Zero duplicação.

---

## 🤖 IDENTIDADE DO GUARDIAN

### Persona

```
Nome: Guardian
Tipo: Orquestrador de Manutenção
Função: Zelador inteligente do vault
Filosofia: "Automatizar o que Gassen odeia fazer manualmente"
```

### Princípios

1. **Zero Duplicação** - Usa skills existentes, nunca cria redundância
2. **NOMENCLATURA.md é Lei** - Toda decisão passa pelo padrão de nomenclatura
3. **Human-in-the-Loop** - Começa propondo, só executa com confiança conquistada
4. **Observar Antes de Agir** - Sempre audita antes de modificar
5. **Checkpoint Obrigatório** - Documenta tudo que faz

---

## 🛠️ SKILLS ORQUESTRADAS

Guardian não tem código próprio. Ele **orquestra** estas 6 skills existentes:

### Tier 1: Observação (Nível 1 - READ)

| Skill | Função | Localização |
|-------|--------|-------------|
| `vault-auditor` | Varredura completa, identifica problemas | `.gemini/skills/vault-auditor/` |
| `architect-linter` | Verificação mecânica (H1, links, frontmatter) | `.gemini/skills/architect-linter/` |
| `mapa` | Indexação do vault | `.gemini/skills/mapa/` |

### Tier 2: Validação (Nível 2 - PROPOSE)

| Skill | Função | Localização |
|-------|--------|-------------|
| `validate` | Valida nomenclatura e localização | `.gemini/skills/validate/` |

### Tier 3: Execução (Nível 3 - EXECUTE)

| Skill | Função | Localização |
|-------|--------|-------------|
| `vault-organizer` | Move/renomeia arquivos | `.gemini/skills/vault-organizer/` |
| `session-logger` | Registra ações no SESSION_LOG | `.gemini/skills/session-logger/` |
| `status-updater` | Atualiza métricas do vault | `.gemini/skills/status-updater/` |

---

## 🔐 SISTEMA DE PERMISSÕES (1-2-3)

### Nível 1: READ (Somente Leitura)

```
Ações permitidas:
- Escanear vault
- Gerar relatórios
- Identificar problemas
- Listar recomendações

Skills usadas: vault-auditor, architect-linter, mapa

Output: Relatório em 00_SISTEMA/RELATORIOS/
```

**Exemplo de uso:**
```
/guardian audit
→ Executa vault-auditor
→ Gera AUDITORIA_VAULT_22JAN2026.md
→ Lista: 15 arquivos com nomenclatura errada, 3 fora de lugar
→ NÃO modifica nada
```

### Nível 2: PROPOSE (Propor + Aguardar Aprovação)

```
Ações permitidas:
- Tudo do Nível 1
- Propor correções específicas
- Gerar comandos prontos para executar
- Aguardar aprovação do usuário

Skills usadas: validate (validação antes de propor)

Output: Lista de ações propostas + comandos
```

**Exemplo de uso:**
```
/guardian fix
→ Identifica: "Plano de Implementacao.md" (nome errado)
→ Propõe: mv "Plano de Implementacao.md" "PLANO_Implementacao.md"
→ Aguarda: "Aprovar? (y/n)"
→ Só executa se usuário aprovar
```

### Nível 3: EXECUTE (Execução Automática)

```
Ações permitidas:
- Tudo dos Níveis 1 e 2
- Executar correções automaticamente
- Mover/renomear arquivos
- Atualizar MOCs
- Registrar no SESSION_LOG

Skills usadas: vault-organizer, session-logger, status-updater

Output: Relatório de ações + backup automático
```

**Exemplo de uso:**
```
/guardian auto
→ Escaneia vault
→ Identifica 15 arquivos com problemas
→ Corrige automaticamente (com backup)
→ Atualiza MOCs afetados
→ Registra em SESSION_LOG
→ Atualiza STATUS_VAULT.md
```

### Evolução de Confiança

```
INÍCIO (Primeira vez)
    ↓
Nível 2 (PROPOSE) ← Começa aqui!
    ↓
[Após 10+ execuções sem erro]
    ↓
Nível 3 (EXECUTE) ← Ganha autonomia
```

**Regra de Ouro:** Guardian SEMPRE começa no Nível 2 para novos tipos de operação.

---

## 📜 NOMENCLATURA.MD COMO LEI

### Antes de Qualquer Ação, Guardian Lê:

```
00_SISTEMA/PADROES/NOMENCLATURA.md
```

### Regras que Guardian Enforce:

| Regra | Verificação | Ação |
|-------|-------------|------|
| Prefixos MAIÚSCULOS | `MOC_`, `PLANO_`, `TEMPLATE_` | Corrigir capitalização |
| CamelCase | `Categoria_Subcategoria` | Ajustar capitalização |
| Sem espaços | Underscores obrigatórios | Substituir ` ` por `_` |
| Datas DDMMMYYYY | `17JAN2026` formato | Converter datas |
| < 60 caracteres | Contar chars do nome | Alertar/sugerir pasta |
| Sem chars especiais | `/\:*?"<>\|` proibidos | Remover/substituir |
| Extensão única | `.md` não `.md.md` | Corrigir extensão |
| Localização correta | Pasta apropriada | Propor movimentação |

### Hierarquia de Decisão

```
1. NOMENCLATURA.md diz algo sobre isso?
   ├── SIM → Seguir NOMENCLATURA.md
   └── NÃO → Continuar

2. PROTOCOLO_CRIACAO_ARQUIVOS.md define local?
   ├── SIM → Usar localização definida
   └── NÃO → Continuar

3. MOC da categoria existe?
   ├── SIM → Seguir padrão do MOC
   └── NÃO → Perguntar ao usuário
```

---

## 🔄 WORKFLOWS DO GUARDIAN

### Workflow 1: Auditoria (Nível 1)

```mermaid
graph TD
    A[/guardian audit] --> B[Carregar NOMENCLATURA.md]
    B --> C[Executar vault-auditor]
    C --> D[Executar architect-linter]
    D --> E[Compilar relatório]
    E --> F[Salvar em 00_SISTEMA/RELATORIOS/]
    F --> G[Exibir resumo ao usuário]
```

**Comando:** `/guardian audit`
**Output:** `AUDITORIA_VAULT_[DATA].md`

### Workflow 2: Correção Guiada (Nível 2)

```mermaid
graph TD
    A[/guardian fix] --> B[Executar auditoria]
    B --> C[Identificar problemas]
    C --> D[Gerar proposta de correção]
    D --> E{Usuário aprova?}
    E -->|Sim| F[Executar vault-organizer]
    E -->|Não| G[Cancelar]
    F --> H[Atualizar SESSION_LOG]
    H --> I[Exibir resultado]
```

**Comando:** `/guardian fix`
**Output:** Lista de ações + confirmação

### Workflow 3: Manutenção Automática (Nível 3)

```mermaid
graph TD
    A[/guardian auto] --> B[Verificar permissão Nível 3]
    B --> C{Tem permissão?}
    C -->|Não| D[Fallback para Nível 2]
    C -->|Sim| E[Executar auditoria]
    E --> F[Criar backup automático]
    F --> G[Executar correções]
    G --> H[Atualizar MOCs]
    H --> I[Atualizar status-updater]
    I --> J[Registrar em SESSION_LOG]
    J --> K[Exibir relatório final]
```

**Comando:** `/guardian auto`
**Output:** Relatório completo + backup

### Workflow 4: Limpeza de Raiz

```mermaid
graph TD
    A[/guardian clean-root] --> B[Listar arquivos na raiz]
    B --> C[Filtrar permitidos]
    C --> D[Identificar invasores]
    D --> E[Propor destinos]
    E --> F{Aprovar movimentação?}
    F -->|Sim| G[Mover arquivos]
    F -->|Não| H[Cancelar]
    G --> I[Atualizar MOCs]
```

**Comando:** `/guardian clean-root`
**Arquivos permitidos na raiz:**
- `CLAUDE.md`
- `README.md`
- `STATUS_VAULT.md`
- `SESSION_LOG.md`
- `PC_SYNC_LOG.md`
- `.gitignore`
- Pastas de configuração (`.claude/`, `.gemini/`, `.obsidian/`, `.git/`)

---

## 📊 RELATÓRIOS

### Formato do Relatório de Auditoria

```markdown
# AUDITORIA_VAULT_22JAN2026

**Executado:** 22/JAN/2026 15:30
**Guardian:** v1.0
**Modo:** Nível 1 (READ)

## Resumo

| Categoria | Total | OK | Problemas |
|-----------|-------|----|-----------|
| Nomenclatura | 2500 | 2485 | 15 |
| Localização | 2500 | 2497 | 3 |
| Links quebrados | 500 | 498 | 2 |
| Frontmatter | 2500 | 2100 | 400 |

## Problemas Encontrados

### Nomenclatura (15)
1. `Plano de Implementacao.md` → `PLANO_Implementacao.md`
2. `checkpoint 22jan.md` → `CHECKPOINT_22JAN2026.md`
...

### Localização (3)
1. `raiz/TEMPLATE_Projeto.md` → `04_RECURSOS/TEMPLATES/`
...

## Comandos de Correção (Copiar e Executar)

```bash
mv "Plano de Implementacao.md" "PLANO_Implementacao.md"
mv "TEMPLATE_Projeto.md" "04_RECURSOS/TEMPLATES/"
```

## Próximos Passos
- [ ] Aprovar correções
- [ ] Executar `/guardian fix`
```

### Formato do Relatório de Execução

```markdown
# GUARDIAN_EXECUCAO_22JAN2026

**Executado:** 22/JAN/2026 15:45
**Modo:** Nível 3 (EXECUTE)
**Backup:** .guardian_backup_22JAN2026_1545/

## Ações Realizadas

| # | Tipo | Arquivo Original | Ação | Resultado |
|---|------|------------------|------|-----------|
| 1 | Rename | Plano de Implementacao.md | → PLANO_Implementacao.md | ✅ |
| 2 | Move | TEMPLATE_Projeto.md | → 04_RECURSOS/TEMPLATES/ | ✅ |
| 3 | Update | _MOC_Recursos.md | Adicionado TEMPLATE_Projeto | ✅ |

## Estatísticas

- Arquivos renomeados: 15
- Arquivos movidos: 3
- MOCs atualizados: 2
- Tempo total: 4.2s

## Backup

Localização: `.guardian_backup_22JAN2026_1545/`
Para reverter: `guardian restore 22JAN2026_1545`
```

---

## 🚨 LOOP RALPH (Verificação Automática)

### Conceito

> **Ralph é o loop que verifica se a tarefa foi completada corretamente.**
> **"Não seja o imbecil que aperta sim sem verificar."**

### Implementação

```
1. Guardian executa ação
   ↓
2. Ralph verifica resultado
   ├── Arquivo existe no destino? ✓
   ├── Nome está correto? ✓
   ├── MOC foi atualizado? ✓
   └── Backup existe? ✓
   ↓
3. Ralph reporta
   ├── SUCESSO → Próxima tarefa
   └── FALHA → Reverte + alerta usuário
```

### Verificações do Ralph

| Operação | Verificação Ralph |
|----------|-------------------|
| Rename | Arquivo novo existe + antigo não existe |
| Move | Arquivo no destino + não na origem |
| MOC Update | Link adicionado + válido |
| Backup | Arquivo de backup existe + íntegro |

---

## 🔧 IMPLEMENTAÇÃO

### Estrutura de Arquivos

```
.agent/workflows/
└── guardian.md              ← Workflow principal

.gemini/skills/
├── vault-auditor/           ← Skill de auditoria
├── vault-organizer/         ← Skill de organização
├── architect-linter/        ← Skill de verificação
├── validate/                ← Skill de validação
├── session-logger/          ← Skill de comunicação
├── status-updater/          ← Skill de métricas
└── guardian/                ← Skill orquestradora (CRIAR)
    ├── SKILL.md
    └── scripts/
        └── orchestrator.py

00_SISTEMA/
├── PROTOCOLOS/
│   └── PROTOCOLO_GUARDIAN.md  ← Este arquivo
├── RELATORIOS/
│   └── AUDITORIA_VAULT_*.md   ← Relatórios gerados
└── PADROES/
    └── NOMENCLATURA.md        ← Lei do Guardian
```

### Comandos Disponíveis

| Comando | Nível | Descrição |
|---------|-------|-----------|
| `/guardian` | - | Mostra ajuda e status |
| `/guardian audit` | 1 | Auditoria completa (read-only) |
| `/guardian fix` | 2 | Propõe correções (aguarda aprovação) |
| `/guardian auto` | 3 | Execução automática (com backup) |
| `/guardian clean-root` | 2 | Limpa arquivos da raiz |
| `/guardian restore [ID]` | 3 | Reverte execução anterior |
| `/guardian status` | 1 | Mostra estatísticas do vault |

### Próximos Passos de Implementação

```
FASE 1: Fundação (Esta Sessão)
[x] Criar PROTOCOLO_GUARDIAN.md (este arquivo)
[ ] Criar .agent/workflows/guardian.md
[ ] Criar .gemini/skills/guardian/SKILL.md

FASE 2: Integração (Próxima Sessão)
[ ] Conectar com skills existentes
[ ] Implementar Loop Ralph básico
[ ] Testar Nível 1 (audit)

FASE 3: Evolução (Sessões Futuras)
[ ] Testar Nível 2 (fix)
[ ] Ganhar confiança para Nível 3
[ ] Automatizar manutenção semanal
```

---

## ✅ CHECKLIST DE USO

### Antes de Usar Guardian

- [ ] NOMENCLATURA.md está atualizado?
- [ ] Skills dependentes estão funcionais?
- [ ] Backup do vault existe?

### Durante Uso

- [ ] Revisar propostas antes de aprovar (Nível 2)
- [ ] Verificar relatório de execução (Nível 3)
- [ ] Confirmar Loop Ralph passou

### Depois de Usar

- [ ] Verificar MOCs atualizados
- [ ] Confirmar SESSION_LOG registrado
- [ ] Validar backup criado

---

## 🚫 ANTI-PATTERNS

### ❌ NUNCA FAZER

1. **Pular para Nível 3 sem testar Nível 2**
   - Causa: Ações irreversíveis sem validação
   - Solução: Sempre começar Nível 2

2. **Ignorar NOMENCLATURA.md**
   - Causa: Inconsistência sistêmica
   - Solução: Ler NOMENCLATURA.md antes de qualquer decisão

3. **Executar sem backup**
   - Causa: Perda de dados
   - Solução: Guardian SEMPRE cria backup automático

4. **Aprovar em massa sem revisar**
   - Causa: Erros propagados
   - Solução: Revisar cada proposta individualmente

5. **Duplicar skills existentes**
   - Causa: Manutenção fragmentada
   - Solução: Guardian ORQUESTRA, não duplica

---

## 📚 REFERÊNCIAS

### Documentos Relacionados

- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Lei do Guardian
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Onde criar arquivos
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_DIVISAO_SKILLS_Claude_Antigravity.md]] - Divisão de skills
- [[00_SISTEMA/planejamento/PLANO_Hierarquia_Agentes_Alan.md]] - Plano de hierarquia

### Skills Orquestradas

- [[.gemini/skills/vault-auditor/skill.md]]
- [[.gemini/skills/vault-organizer/skill.md]]
- [[.gemini/skills/architect-linter/SKILL.md]]
- [[.gemini/skills/validate/skill.md]]
- [[.gemini/skills/session-logger/skill.md]]
- [[.gemini/skills/status-updater/skill.md]]

### Conceitos Alan Nicolas

- **Método MAPA:** Mapear → Atomizar → Programar → Ativar
- **Permissões 1-2-3:** Read → Propose → Execute
- **Conceito Ralph:** Loop de verificação automática
- **Princípio:** "Só automatize o que você fez 3x e odiou"

---

## 🎯 RESUMO EXECUTIVO

### O Que é Guardian?

```
Guardian = Persona de Manutenção + Orquestrador de Skills
```

### O Que Guardian Faz?

1. **AUDITA** o vault (vault-auditor, architect-linter)
2. **VALIDA** nomenclatura (validate, NOMENCLATURA.md)
3. **PROPÕE** correções (gera comandos prontos)
4. **EXECUTA** correções (vault-organizer, com backup)
5. **REGISTRA** ações (session-logger, status-updater)

### Como Usar?

```
/guardian audit    → Ver problemas
/guardian fix      → Corrigir com aprovação
/guardian auto     → Corrigir automaticamente (depois de ganhar confiança)
```

### Filosofia

> **"Gassen odeia organizar manualmente.**
> **Guardian automatiza o tédio."**

---

**Versão:** 1.0
**Criado:** 22/JAN/2026
**Status:** 🟡 IMPLEMENTAÇÃO
**Próxima Revisão:** Após primeira execução completa

**GUARDIAN: ZELADOR INTELIGENTE DO VAULT** 🛡️✅
