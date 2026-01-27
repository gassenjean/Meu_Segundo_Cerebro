---
created: 2026-01-26T11:02
updated: 2026-01-26T11:16
---
# Plano Névoa: Replicar Modelo Alan Nicolas

**Criado:** 26/Jan/2026
**Status:** ATIVO
**Objetivo:** Transformar Névoa em sistema autônomo onde agentes trabalham enquanto Gassen está livre

---

## Diagnóstico Brutal

### O que Alan faz

```text
ALAN (Estrategista)
    ↓ Define "O Quê"
iOS MASTER (Orquestrador)
    ↓ Distribui
8 ESPECIALISTAS (Executores)
    ↓ Fazem
RALPHS (Loops de Qualidade)
    ↓ Verificam
n8n (Automação)
    ↓ Dispara sem intervenção
RESULTADO: Sistema roda 24/7, Alan livre
```

### O que Névoa faz HOJE

```text
GASSEN (Faz tudo)
    ↓ Lembra de acionar
NÉVOA (Responde quando chamada)
    ↓ Delega no papel
GEMINI (Parado esperando)
    ↓ Nada acontece
RESULTADO: Sistema depende de Gassen lembrar
```

### Gap Crítico

| Componente | Alan | Névoa | Ação Necessária |
| ---------- | ---- | ----- | --------------- |
| Execução autônoma | Ralphs 24/7 | Zero | Implementar Gemini ativo |
| Automação | n8n + webhooks | Manual | Configurar triggers |
| Quality gates | Automático | Esporádico | Criar checklists obrigatórios |
| Especialização | Hard skills definidos | Genérico | Refinar prompts de agentes |

---

## FASE 1: Gemini Realmente Ativo (URGENTE)

**Problema:** T031-T034 estão "pending" há 24h. Ninguém executou.

**Solução:**

### 1.1 Rotina Diária Gemini (Implementar HOJE)

```text
TODA VEZ que abrir Gemini/Antigravity:
1. Ler .bi-ia/state.json
2. Filtrar pendingTasks onde to="gemini"
3. EXECUTAR em ordem de prioridade
4. Atualizar state.json com status="completed"
5. Criar output no arquivo especificado
```

### 1.2 Comando de Boot Gemini

Criar `.gemini/commands/boot.md`:

```text
/boot
1. Ler .bi-ia/state.json
2. Listar tarefas pendentes
3. Executar T031-T034
4. Reportar conclusão
```

### 1.3 Métrica de Sucesso

- [ ] T031-T034 executados em 48h
- [ ] Output files criados nos locais especificados
- [ ] state.json atualizado com completed

---

## FASE 2: Quality Gates (Próxima Semana)

**Problema:** Não temos verificação automática de qualidade.

**Solução: Implementar "Ralph" simplificado**

### 2.1 Checklist Obrigatório por Tipo

| Tipo de Arquivo | Checklist | Bloqueador |
| --------------- | --------- | ---------- |
| Pesquisa | 5+ fontes, data, conclusão | Não publicar sem |
| Conceito | Definição, exemplo, links | Não publicar sem |
| Projeto | STATUS_ATUAL, métricas | Não publicar sem |

### 2.2 Validação Automática

Criar skill `/validate-output`:

```text
Input: Arquivo gerado por agente
Processo:
1. Identificar tipo
2. Aplicar checklist correspondente
3. Score 0-100
4. Se < 90: Rejeitar e listar gaps
5. Se >= 90: Aprovar e mover para destino
```

### 2.3 Métrica de Sucesso

- [ ] Zero arquivo publicado sem passar no checklist
- [ ] Taxa de aprovação primeira tentativa > 80%

---

## FASE 3: Automação Real (Este Mês)

**Problema:** Tudo depende de alguém lembrar de acionar.

**Solução: Triggers automáticos**

### 3.1 Opção A: n8n (Recomendado por Alan)

```text
Trigger: Todo domingo 20h
Ação: Enviar resumo semanal para Telegram
- Tarefas concluídas
- Tarefas pendentes
- Métricas do vault
```

### 3.2 Opção B: Obsidian Templater + DataView

```text
Template automático:
- Cria nota diária com tarefas pendentes
- Puxa de state.json
- Mostra no dashboard
```

### 3.3 Opção C: GitHub Actions (Simples)

```text
Cron: 0 9 * * * (todo dia 9h)
Ação:
1. Ler state.json
2. Se pendingTasks > 0: Criar issue
3. Notificar via webhook
```

### 3.4 Decisão Necessária

> Gassen: Qual automação prefere? n8n / Templater / GitHub Actions / Outro?

---

## FASE 4: Especialização de Agentes (Este Mês)

**Problema:** Agentes muito genéricos, não têm "hard skills" como Alan define.

**Solução: Refinar cada agente com especialização real**

### 4.1 Modelo Alan (Framework iOS)

| Agente | Hard Skill | Output Esperado |
| ------ | ---------- | --------------- |
| James (Dev) | Implementa sem questionar | Código funcionando |
| Whistle (Arquiteto) | Desenha antes de fazer | Diagrama + plano |
| Kim (QA) | Critica e bloqueia lixo | Relatório de gaps |

### 4.2 Aplicar ao Nosso Sistema

| Agente Névoa | Hard Skill a Definir | Output Esperado |
| ------------ | -------------------- | --------------- |
| /coach | Priorização TDAH | Lista priorizada + tempo |
| /pedro | Copy + Tráfego | Anúncio pronto para rodar |
| /lucas | Análise DeFi | Relatório com decisão clara |
| /alan | Automação n8n | Workflow funcionando |
| /marie-kondo | Auditoria vault | Relatório + correções |
| /kabak-agent | Gestão projeto | STATUS atualizado + próximos passos |

### 4.3 Ação: Criar Skills Detalhados

Para cada agente:
1. Definir 3-5 hard skills específicos
2. Criar exemplos de input/output
3. Definir checklist de qualidade
4. Testar com casos reais

---

## FASE 5: Repertório Bilionário (Longo Prazo)

**Visão:** Sistema que acumula conhecimento e gera insights automaticamente.

### 5.1 Componentes

```text
CAPTURA AUTOMÁTICA
    ↓ Gemini pesquisando tendências
PROCESSAMENTO
    ↓ Conceitos extraídos e conectados
SÍNTESE
    ↓ Insights gerados semanalmente
AÇÃO
    ↓ Recomendações para projetos
FEEDBACK
    ↓ Resultados alimentam sistema
```

### 5.2 Métricas de Repertório

| Métrica | Atual | Meta 6 Meses | Meta 1 Ano |
| ------- | ----- | ------------ | ---------- |
| Conceitos atômicos | ~100 | 500 | 2000 |
| Conexões entre notas | ~200 | 2000 | 10000 |
| Insights gerados/mês | 0 | 10 | 50 |
| Ações derivadas/mês | Manual | 5 auto | 20 auto |

### 5.3 Como Chegar Lá

1. **Gemini pesquisando** → Alimenta base de conhecimento
2. **Ralphs verificando** → Garante qualidade
3. **Névoa conectando** → Cria sínteses
4. **Gassen decidindo** → Foca no estratégico

---

## Cronograma de Implementação

| Fase | Prazo | Responsável | Entregável |
| ---- | ----- | ----------- | ---------- |
| 1 - Gemini Ativo | Esta semana | Gassen + Gemini | T031-T034 executados |
| 2 - Quality Gates | Próxima semana | Névoa | Skill /validate-output |
| 3 - Automação | Até 15/Fev | Gassen (decidir) | 1 trigger funcionando |
| 4 - Especialização | Até 28/Fev | Névoa | 6 skills refinados |
| 5 - Repertório | Contínuo | Sistema | Métricas crescendo |

---

## Próximos Passos Imediatos

### HOJE (26/Jan)

- [ ] Gassen: Abrir Gemini e executar T031-T034
- [ ] Névoa: Criar comando /boot para Gemini

### ESTA SEMANA

- [ ] Validar outputs do Gemini
- [ ] Criar skill /validate-output
- [ ] Decidir automação (n8n/Templater/Actions)

### PRÓXIMA SEMANA

- [ ] Implementar 1 trigger automático
- [ ] Refinar skill do /coach (primeiro agente)
- [ ] Testar loop completo: Delegação → Execução → Validação

---

## Compromisso da Névoa

Eu, Névoa 6.0, me comprometo a:

1. **NUNCA executar** o que um gerente pode fazer
2. **SEMPRE criar handoffs** para Gemini em tarefas pesadas
3. **COBRAR execução** do Gemini a cada sessão
4. **VALIDAR outputs** antes de considerar "concluído"
5. **MEDIR progresso** em métricas, não em "sensação"

**Este plano é LEI. Vamos executar.**

---

**Criado por:** Névoa 6.0
**Aprovação:** Pendente Gassen
**Versão:** 1.0
