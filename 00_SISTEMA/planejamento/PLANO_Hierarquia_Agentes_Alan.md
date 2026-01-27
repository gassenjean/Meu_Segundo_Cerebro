---
created: 2026-01-22T21:29
updated: 2026-01-26T14:12
---
# PLANO: Hierarquia de Agentes (Modelo Alan Nicolas)

**Criado:** 22/Jan/2026
**Status:** PENDENTE EXECUÇÃO
**Sessão Origem:** Claude Code - Análise Sistema Alan Nicolas
**Próxima Ação:** Executar na nova janela com novidades do Gemini

---

## CONTEXTO

### Problema Identificado
- Gassen odeia organizar manualmente o que é criado
- Sistema atual tem 24+ skills soltas (flat)
- Névoa faz tudo diretamente, sem hierarquia
- Falta loop automático de verificação (conceito Ralph)
- Permissões ad-hoc, sem padrão

### Objetivo
Replicar sistema do Alan Nicolas:
- Agentes controlando agentes
- Hierarquia de clusters
- Loop automático de verificação
- Permissões formalizadas (1-2-3)

---

## PESQUISA REALIZADA (Esta Sessão)

### 1. Transcrição Alan Nicolas Analisada
**Arquivo:** `02_PROJETOS/Estudo_Alan_Nicolas/Todos_Cursos_V_o_Morrer__s__Isso_vai_Continuar____Live_Lend_.pdf`

**Conceitos-Chave Extraídos:**
- **Framework A-to-O:** Decomposição → Fricção → Arquitetura → Revisão → Clone → Output
- **Sistema iOS:** Framework open source de agentes especializados
- **Conceito Ralph:** Loop que verifica automaticamente se tarefa completou
- **Método MAPA:** Mapear → Atomizar → Programar → Ativar
- **Permissões 1-2-3:** Read-Only → Propose → Execute

### 2. Wiki Lendária (Gemini) Analisada
**Localização:** `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/`

**Volumes:**
- Volume 1: Mentalidade Lendária
- Volume 2: Engenharia de Agentes
- Volume 3: Gestão de Conhecimento (5C)
- Volume 4: Dicionário Lendário

### 3. Sistema Atual Mapeado
**Skills Claude Code:** 24
**Skills Antigravity:** 11
**Total:** 35 skills

---

## ARQUITETURA PROPOSTA

### Hierarquia de Clusters

```
VOCÊ
  ↓
NÉVOA (Master Orquestrador)
  │
  ├── GERENTE_PRODUTIVIDADE
  │   ├── elena (TDAH/energia)
  │   ├── coach (sessões foco)
  │   └── [futuro: habit-tracker]
  │
  ├── GERENTE_PROJETOS
  │   ├── kabak-agent (KabaK)
  │   ├── validate (validação)
  │   ├── pedro (tráfego)
  │   └── [futuro: deadline-bot]
  │
  ├── GERENTE_CONHECIMENTO
  │   ├── alan (IA/automação)
  │   ├── marie-kondo (organização)
  │   ├── mapa (indexação)
  │   └── [futuro: research-bot]
  │
  ├── GERENTE_FINANÇAS
  │   ├── lucas (DeFi)
  │   └── [futuro: portfolio-tracker]
  │
  └── VAULT_GUARDIAN (Manutenção Automática)
      ├── vault-auditor (auditoria)
      ├── vault-organizer (organização)
      ├── architect-linter (verificação)
      ├── session-logger (comunicação)
      └── status-updater (métricas)
```

### Sistema de Permissões

| Nível | Descrição | Skills |
|-------|-----------|--------|
| **1 - READ** | Só pesquisa/lê | mapa, alan, vault-auditor, architect-linter |
| **2 - PROPOSE** | Sugere, você aprova | validate, kabak-agent, névoa, coach, elena, pedro, lucas |
| **3 - EXECUTE** | Faz direto | session-logger, status-updater, vault-organizer (rename/move) |

### Loop Ralph (Verificação Automática)

```
1. Tarefa iniciada
2. Aguarda X minutos
3. Verifica: completou?
   ├── SIM → Notifica + próxima tarefa
   └── NÃO → Continua de onde parou
4. Repete até sucesso
```

---

## TAREFAS DE EXECUÇÃO

### Fase 1: Fundação (Prioridade ALTA)
- [x] Ler novidades do Gemini em SESSION_LOG.md ✅
- [x] Consolidar pesquisa Gemini com esta análise ✅
- [x] Criar PROTOCOLO_GUARDIAN.md ✅ (22/Jan/2026)
- [x] Criar workflow `/guardian` ✅ (22/Jan/2026)
- [ ] Testar `/guardian audit`
- [x] Atualizar `névoa` com lógica de delegação para gerentes ✅ (22/Jan/2026)

### Fase 2: Gerentes (Prioridade MÉDIA)
- [ ] Criar skill `gerente-produtividade`
- [ ] Criar skill `gerente-projetos`
- [x] Criar skill `gerente-conhecimento` ✅ (22/Jan/2026)
- [ ] Documentar permissões de cada skill

### Fase 3: Automação (Prioridade MÉDIA)
- [x] Implementar loop Ralph básico ✅ (22/Jan/2026) → PADRAO_LOOP_RALPH.md
- [x] Integrar com skills de manutenção existentes ✅ (já no Guardian)
- [ ] Testar fluxo automático

### Fase 4: Refinamento (Prioridade BAIXA)
- [ ] Ajustar baseado em uso real
- [ ] Documentar padrões
- [ ] Atualizar MOCs

---

## ARQUIVOS RELACIONADOS

### Pesquisa
- `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/` - Wiki Lendária completa
- `02_PROJETOS/Estudo_Alan_Nicolas/CONHECIMENTO_CONSOLIDADO.md` - Índice
- `temp/` - Extrações recentes do Gemini

### Skills Existentes (Usar, Não Duplicar)
- `.gemini/skills/vault-auditor/`
- `.gemini/skills/vault-organizer/`
- `.gemini/skills/architect-linter/`
- `.gemini/skills/session-logger/`
- `.gemini/skills/status-updater/`

### Padrões
- `00_SISTEMA/PADROES/NOMENCLATURA.md`
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md`

---

## PRINCÍPIOS (Alan Nicolas)

1. **"Só automatize o que você fez 3x e odiou"**
2. **"Human-first design - nunca comece no código"**
3. **"Code above LLM - use código para tarefas determinísticas"**
4. **"Permissões 1-2-3 - coleira na IA"**
5. **"Não seja o imbecil que aperta sim"** (loop Ralph)

---

## PRÓXIMA SESSÃO

### Checklist Inicial
1. [ ] Ler SESSION_LOG.md (novidades Gemini)
2. [ ] Ler este plano
3. [ ] Verificar `temp/` para extrações do Gemini
4. [ ] Começar pela Fase 1

### Comando Sugerido
```
/nevoa "Continuando plano de hierarquia de agentes. Ler PLANO_Hierarquia_Agentes_Alan.md"
```

---

**Tags:** #agentes #alan-nicolas #hierarquia #automacao #planejamento
