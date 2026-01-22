---
criado: 2026-01-22T11:30:00-03:00
atualizado: 2026-01-22T12:00:00-03:00
tipo: plano
status: em_andamento
prioridade: alta
created: 2026-01-22T11:25
updated: 2026-01-22T12:37
---

# PLANO: Reorganização Projeto KabaK + Skill v2.0

**Data:** 22/Jan/2026
**Sessão Origem:** `01e190bd-4561-4d87-93ee-9041b3fff1bb`
**Objetivo:** Limpar, organizar e evoluir o projeto KabaK e a skill de gerenciamento
**Recurso Chave:** Vault Alan Nicolas (mentelendaria.com) via Gemini

---

## CONTEXTO E PROBLEMA

### Varredura Completa Realizada (Sessão Anterior)

| Métrica | Valor |
|---------|-------|
| **Pastas** | 23 |
| **Arquivos totais** | 87 |
| **Arquivos .md** | 64 |
| **Scripts Python** | 25 (sem documentação!) |
| **Linhas de conteúdo** | 18.573 |

### 10 Problemas Críticos Identificados

| # | Problema | Impacto |
|---|----------|---------|
| 1 | 8 versões de planilha financeira | Qual é a oficial? |
| 2 | 7 documentos sobre mesma reunião | Confusão total |
| 3 | 3 versões de briefing Dr. Alexandre | Desatualizado |
| 4 | Investimento conflitante | R$ 2.096.300 vs R$ 2.106.300 |
| 5 | SEM MOC (índice master) | Impossível navegar |
| 6 | Nomenclatura inconsistente | Viola NOMENCLATURA.md |
| 7 | 25 scripts Python sem documentação | Ninguém sabe qual usar |
| 8 | READMEs com links mortos | Mencionam arquivos inexistentes |
| 9 | Arquivo vazio | PLANILHA_KABAK_SANSOM.xlsx.md (0 bytes) |
| 10 | Frontmatter misto | PT vs EN (criado vs created) |

### Recurso Disponível: Vault Alan Nicolas

- **URL:** https://mentelendaria.com (vault público)
- **Acesso:** Gemini tem acesso direto
- **Conteúdo relevante:**
  - Sistema 5C (Capturar, Conectar, Criar, Compartilhar, Consolidar)
  - Workflows de automação
  - Templates estruturados
  - Integrações Claude ↔ Gemini
  - Boas práticas PKM

### Skills Gemini Existentes (12)

| Skill | Função | Útil para |
|-------|--------|-----------|
| kabak | Gestão projeto | FASE 2-3 |
| validate | Validação arquivos | FASE 2-3 |
| vault-organizer | Organização | FASE 2 |
| vault-auditor | Auditoria | FASE 2 |
| mapa | Índice vault | FASE 2 |
| session-logger | Log sessões | FASE 4 |
| session-log-archiver | Arquivamento | FASE 4 |
| context-manager | Gestão contexto | FASE 4 |
| architect-linter | Validação padrões | FASE 3 |
| gemini-handoff | Delegação Claude→Gemini | FASE 4 |
| status-updater | Atualização status | FASE 2 |

### Comunicação Bi-IA (A Melhorar)

**Arquivos atuais:**
- `SESSION_LOG.md` - Comunicação principal (precisa melhorar estrutura)
- `PC_SYNC_LOG.md` - Sync multi-PC

**Problemas:**
- Formato pouco estruturado
- Difícil de parsear automaticamente
- Falta protocolo claro de handoff

### Agentes Envolvidos no Planejamento

| Agente | Contribuição |
|--------|--------------|
| **Skill Creator** | Arquitetura e estrutura da skill v2.0 |
| **Alan Nicolas** | Automação, workflows eficientes, pesquisa mentelendaria.com |
| **KabaK Agent** | Conhecimento do domínio e necessidades |
| **Gemini** | Execução bulk e processamento pesado |

---

## FASES DO PLANO

### FASE 1: PESQUISA VAULT ALAN NICOLAS (Gemini)

**Responsável:** Gemini 3 Pro
**Objetivo:** Pesquisar boas práticas no vault do Alan Nicolas (mentelendaria.com)

| # | Tarefa | Status | Comando/Ação |
|---|--------|--------|--------------|
| 1.1 | Executar comando Gemini: pesquisar estrutura mentelendaria.com | [ ] | `gemini "analise estrutura mentelendaria.com"` |
| 1.2 | Executar comando Gemini: extrair templates e padrões do Alan | [ ] | `gemini "extraia templates skills Alan Nicolas"` |
| 1.3 | Executar comando Gemini: buscar integrações Claude + Gemini do Alan | [ ] | `gemini "como Alan Nicolas integra Claude e Gemini"` |
| 1.4 | Criar skill `alan-researcher` no Gemini para pesquisas futuras | [ ] | Nova skill Gemini |

**Entregáveis:**
- [ ] Documento com padrões extraídos do Alan
- [ ] Lista de boas práticas aplicáveis ao KabaK
- [ ] Skill Gemini para pesquisas futuras

---

### FASE 2: REORGANIZAÇÃO PROJETO KABAK

**Responsável:** Claude Code (com Gemini para bulk)
**Objetivo:** Limpar, consolidar e padronizar a estrutura do projeto

| # | Tarefa | Status | Prioridade |
|---|--------|--------|------------|
| 2.1 | Criar `_MOC_KabaK.md` (índice master do projeto) | [x] ✅ | ALTA |
| 2.2 | Consolidar planilhas financeiras (arquivar antigas) | [x] ✅ | ALTA |
| 2.3 | Validar docs reunião Sansom (sem redundância real) | [x] ✅ | MÉDIA |
| 2.4 | Deletar `BRIEFING_DR_ALEXANDRE.md` obsoleto | [x] ✅ | BAIXA |
| 2.5 | Resolver conflito R$ 2.096.300 vs R$ 2.106.300 | [x] ✅ | ALTA |
| 2.6 | Deletar arquivo vazio `PLANILHA_KABAK_SANSOM.xlsx.md` | [x] ✅ | BAIXA |
| 2.7 | Corrigir nomenclatura 5 arquivos | [x] ✅ | MÉDIA |
| 2.8 | Documentar scripts Python (`scripts/README.md`) | [x] ✅ | MÉDIA |
| 2.9 | Atualizar MOC com nomes renomeados | [x] ✅ | BAIXA |
| 2.10 | Frontmatter (delegado Gemini - bulk) | [~] | MÉDIA |

**Entregáveis:**
- [x] MOC master do projeto (`_MOC_KabaK.md`)
- [x] Valores oficiais consolidados (R$ 2.096.300 é oficial)
- [x] Estrutura limpa (arquivos deletados/renomeados)
- [x] Scripts documentados (`scripts/README.md`)
- [~] Frontmatter (20 arquivos com EN - delegar Gemini)

---

### FASE 3: REESTRUTURAÇÃO SKILL KABAK v2.0

**Responsável:** Claude Code + Skill Creator
**Objetivo:** Criar skill robusta que previne erros e escala
**Status:** ✅ CONCLUÍDA (22/Jan/2026)

| # | Tarefa | Status | Descrição |
|---|--------|--------|-----------|
| 3.1 | Definir nova arquitetura skill (baseada em boas práticas Alan) | [x] ✅ | ARQUITETURA_V2.md criado |
| 3.2 | Criar sistema de validação automática antes de criar arquivos | [x] ✅ | validate_before_create.py + nomenclatura_kabak.md |
| 3.3 | Criar templates padronizados com frontmatter obrigatório | [x] ✅ | 7 templates UPPERCASE |
| 3.4 | Implementar nomenclatura automática (prefixos corretos) | [x] ✅ | Script valida prefixos/locais |
| 3.5 | Criar workflow de atualização de MOCs automático | [x] ✅ | update_moc.py funcional |
| 3.6 | Sincronizar skills Claude e Gemini (mesma versão) | [x] ✅ | Ambas em v2.0 |

**Entregáveis:**
- [x] Skill KabaK v2.0 com validação (SKILL.md 143 linhas, -54%)
- [x] Templates padronizados (7 templates UPPERCASE)
- [x] Sistema de nomenclatura automática (validate_before_create.py)
- [x] Workflow MOC automático (update_moc.py)
- [x] Skills Claude/Gemini sincronizadas (v2.0)

---

### FASE 4: INTEGRAÇÃO BI-IA AVANÇADA

**Responsável:** Claude Code
**Objetivo:** Melhorar comunicação e handoff entre Claude e Gemini

| # | Tarefa | Status | Descrição |
|---|--------|--------|-----------|
| 4.1 | Melhorar SESSION_LOG.md (formato mais estruturado) | [ ] | Seções claras, timestamps, status |
| 4.2 | Criar protocolo de handoff Claude → Gemini para tarefas longas | [ ] | Quando e como delegar |
| 4.3 | Implementar contexto compartilhado entre agentes | [ ] | Arquivos de estado comum |
| 4.4 | Configurar autonomia de execução prolongada (horas) | [ ] | Tarefas que rodam sem intervenção |

**Entregáveis:**
- [ ] SESSION_LOG.md v2.0
- [ ] Protocolo de handoff documentado
- [ ] Sistema de contexto compartilhado
- [ ] Guia de execução autônoma

---

### FASE 5: TESTES E VALIDAÇÃO

**Responsável:** Claude Code + Gemini
**Objetivo:** Validar que tudo funciona corretamente

| # | Tarefa | Status | Descrição |
|---|--------|--------|-----------|
| 5.1 | Testar skill KabaK v2.0 com caso real (nova reunião) | [ ] | Simular processamento de reunião |
| 5.2 | Validar integração Claude ↔ Gemini | [ ] | Testar handoff completo |
| 5.3 | Documentar lições aprendidas | [ ] | O que funcionou, o que não funcionou |

**Entregáveis:**
- [ ] Skill testada e validada
- [ ] Integração funcionando
- [ ] Documento de lições aprendidas

---

## CRITÉRIOS DE SUCESSO

1. **Projeto organizado:** Zero arquivos duplicados, todos com nomenclatura correta
2. **MOC funcional:** `_MOC_KabaK.md` com links para todos arquivos importantes
3. **Skill robusta:** Valida antes de criar, segue padrões automaticamente
4. **Bi-IA integrado:** Claude e Gemini trabalham em sincronia
5. **Documentação atualizada:** READMEs, scripts, frontmatter padronizados

---

## ORDEM DE EXECUÇÃO RECOMENDADA

```
FASE 1 (Gemini)  →  FASE 2 (Paralelo)  →  FASE 3  →  FASE 4  →  FASE 5
     ↓                    ↓
 Pesquisa Alan     Reorganização
                   (pode usar Gemini
                    para bulk ops)
```

**Estimativa:**
- Fase 1: Gemini executa comandos
- Fase 2: Claude/Gemini executam limpeza
- Fase 3: Claude Code implementa
- Fase 4: Claude Code implementa
- Fase 5: Testes finais

---

## SKILL ALAN-RESEARCHER (A CRIAR NO GEMINI)

**Proposta:** Skill para pesquisar profundamente o vault do Alan Nicolas

```
📁 .gemini/skills/alan-researcher/
├── SKILL.md (definição)
├── references/
│   └── mentelendaria_map.md (mapa do vault Alan)
├── scripts/
│   └── deep_search.py (pesquisa automatizada)
└── templates/
    └── RESEARCH_REPORT.md
```

**Comandos para executar no Antigravity (FASE 1):**

```bash
# Comando 1: Pesquisar estrutura
gemini "Acesse https://mentelendaria.com e analise:
1. ESTRUTURA DO VAULT: pastas, categorias, padrões de nomenclatura
2. METODOLOGIAS: Sistema 5C, workflows, templates
3. SKILLS E AUTOMAÇÕES: documentadas, integrações, N8N
4. BOAS PRÁTICAS PKM: projetos, reuniões, consistência
Retorne relatório DETALHADO em markdown."

# Comando 2: Extrair templates
gemini "De https://mentelendaria.com extraia TODOS os templates:
1. TEMPLATES DE ARQUIVOS: estrutura, campos, exemplos
2. PADRÕES DE NOMENCLATURA: prefixos, convenções
3. WORKFLOWS AUTOMATIZADOS: quais, como funcionam
Formato: Markdown estruturado."

# Comando 3: Integrações Claude + Gemini
gemini "De https://mentelendaria.com analise integrações Claude/Gemini:
1. Como usa os dois agentes juntos?
2. Divisão de tarefas?
3. Sincronização?
4. Skills compartilhadas vs específicas?
Documente padrões para replicar no KabaK."
```

---

## LISTA COMPLETA DE TAREFAS (PRÓXIMA JANELA)

### FASE 1: PESQUISA ALAN NICOLAS (Gemini)
- [ ] 1.1 Executar comando 1: pesquisar estrutura mentelendaria.com
- [ ] 1.2 Executar comando 2: extrair templates e padrões
- [ ] 1.3 Executar comando 3: buscar integrações Claude + Gemini
- [ ] 1.4 Criar skill `alan-researcher` no Gemini
- [ ] 1.5 Documentar descobertas em `references/mentelendaria_map.md`

### FASE 2: REORGANIZAÇÃO PROJETO KABAK
- [ ] 2.1 Criar `_MOC_KabaK.md` (índice master)
- [ ] 2.2 Consolidar 8 planilhas financeiras → 1 fonte única
- [ ] 2.3 Consolidar 7 docs reunião Sansom → 2-3 essenciais
- [ ] 2.4 Deletar briefings obsoletos (manter apenas 19JAN)
- [ ] 2.5 Resolver conflito R$ 2.096.300 vs R$ 2.106.300
- [ ] 2.6 Deletar arquivo vazio `PLANILHA_KABAK_SANSOM.xlsx.md`
- [ ] 2.7 Corrigir nomenclatura 5 arquivos (`Reuniao_*` → `RESUMO_REUNIAO_*`)
- [ ] 2.8 Criar `scripts/README.md` documentando 25 scripts Python
- [ ] 2.9 Atualizar READMEs com links mortos
- [ ] 2.10 Padronizar frontmatter (PT único: criado/atualizado)

### FASE 3: SKILL KABAK v2.0
- [ ] 3.1 Definir nova arquitetura (baseada em Alan Nicolas)
- [ ] 3.2 Criar validação automática antes de criar arquivos
- [ ] 3.3 Criar templates padronizados com frontmatter obrigatório
- [ ] 3.4 Implementar nomenclatura automática (prefixos corretos)
- [ ] 3.5 Criar workflow de atualização de MOCs automático
- [ ] 3.6 Sincronizar skills Claude e Gemini

### FASE 4: INTEGRAÇÃO BI-IA AVANÇADA
- [ ] 4.1 Redesenhar SESSION_LOG.md (formato mais estruturado)
- [ ] 4.2 Criar protocolo de handoff Claude → Gemini
- [ ] 4.3 Implementar contexto compartilhado entre agentes
- [ ] 4.4 Configurar autonomia de execução prolongada

### FASE 5: TESTES E VALIDAÇÃO
- [ ] 5.1 Testar skill KabaK v2.0 com caso real (nova reunião)
- [ ] 5.2 Validar integração Claude ↔ Gemini
- [ ] 5.3 Documentar lições aprendidas

---

## PRÓXIMA AÇÃO

**Abrir nova janela limpa com este plano.**

### Passo a Passo:
1. Fechar esta janela (contexto atual será perdido)
2. Abrir nova sessão Claude Code
3. Comando inicial:
```
Leia: 02_PROJETOS/KabaK/planejamento/PLANO_REORGANIZACAO_KABAK_SKILL_22JAN2026.md
Leia: 00_SISTEMA/CHECKPOINTS/CHECKPOINT_22JAN2026_Reorganizacao_KabaK_Skill.md
Vamos executar o plano começando pela FASE [1 ou 2]
```

### Recomendação de Início:
- **Se Gemini disponível:** FASE 1 primeiro (pesquisa informará decisões)
- **Se só Claude:** FASE 2.1 primeiro (criar MOC dá visão clara)

---

## ARQUIVOS RELACIONADOS

**Projeto KabaK:**
- [[STATUS_ATUAL.md]] - Estado atual do projeto
- [[VALORES_OFICIAIS.md]] - Fonte única valores financeiros
- [[_MOC_KabaK.md]] - (A CRIAR) Índice master

**Skills:**
- `.claude/skills/kabak/` - Skill Claude atual
- `.gemini/skills/kabak/` - Skill Gemini atual
- `.gemini/skills/alan-researcher/` - (A CRIAR) Pesquisador Alan

**Comunicação Bi-IA:**
- `SESSION_LOG.md` - Comunicação Claude ↔ Gemini
- `PC_SYNC_LOG.md` - Sync multi-PC

**Checkpoint:**
- `00_SISTEMA/CHECKPOINTS/CHECKPOINT_22JAN2026_Reorganizacao_KabaK_Skill.md`

---

**Criado por:** Claude Code (Opus 4.5)
**Sessão:** 22/Jan/2026 - Recuperação de contexto
**Total de tarefas:** 26 itens em 5 fases
