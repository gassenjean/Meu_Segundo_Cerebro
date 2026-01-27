---
criado: 2026-01-25
atualizado: 2026-01-25
baseado_em: Alan_Nicolas_O_Fim_dos_Cursos_e_Ascensao_dos_Sistemas.md
tags:
  - protocolo
  - agentes
  - ios-framework
  - alan-nicolas
created: 2026-01-26T08:44
updated: 2026-01-26T11:16
---

# PROTOCOLO: Criação de Agentes (Framework iOS)

**Blueprint Técnico para Construção de Agentes**

**Status:** ✅ ATIVO
**Versão:** 1.0
**Baseado em:** Live "O Fim dos Cursos" - Alan Nicolas

---

## Referência Obrigatória

Antes de criar qualquer agente, consultar:

```text
02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_O_Fim_dos_Cursos_e_Ascensao_dos_Sistemas.md
```

---

## 1. Framework iOS (Intelligence Operating System)

### Estrutura de Clusters

```text
┌─────────────────────────────────────────┐
│           iOS MASTER                    │
│      (Orquestrador Central)             │
├─────────────────────────────────────────┤
│                                         │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│   │ Líder 1 │  │ Líder 2 │  │ Líder N │ │
│   └────┬────┘  └────┬────┘  └────┬────┘ │
│        │            │            │      │
│   ┌────┴────┐  ┌────┴────┐  ┌────┴────┐ │
│   │Operários│  │Operários│  │Operários│ │
│   └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

**Regra:** Você não gerencia 200 agentes. Você gerencia 1 Orquestrador → 5 Líderes → N Operários.

### Roles Padrão

| Role | Função | Comportamento |
| ---- | ------ | ------------- |
| **Master** | Orquestrador | Ponto de entrada, decide quem chamar |
| **Dev (James)** | Implementador | Executa sem inventar, segue padrão |
| **Arquiteto (Whistle)** | Designer | Visão holística, desenha antes de codar |
| **QA (Kim/Queen)** | Validador | Critica, emite reports de risco |
| **DevOps (Dave)** | Infraestrutura | Ambiente, CI/CD, configuração |
| **PM (John)** | Produto | Visão de produto |
| **PO (Sarah)** | Priorização | Backlog e prioridades |
| **SM (Bob)** | Facilitador | Remove impedimentos |

---

## 2. Conceito Ralph (Loop de Execução)

### O que é

Executor incansável de tarefas repetitivas. Um script "burro" que garante qualidade.

### Implementação

```text
LOOP RALPH:
┌──────────────────────────────────┐
│ 1. Executar tarefa               │
│ 2. Verificar checklist           │
│ 3. Passou? ───┬─── SIM → PARA   │
│               └─── NÃO → REPETE  │
└──────────────────────────────────┘
```

### Quando Usar

- Tarefas que você faz mais de 3x
- Processos que precisam de validação
- Qualquer coisa que pode ser automatizada

### Filosofia

> "Não seja o imbecil que aperta sim. Tenha um Ralph para apertar sim por você."

---

## 3. Code Above LLM

### Regra de Ouro

```text
DETERMINÍSTICO = CÓDIGO
COGNITIVO = LLM
```

### Exemplos

| Tarefa | Usar |
| ------ | ---- |
| Extrair URLs de texto | Código (regex) |
| Calcular métricas | Código (math) |
| Validar formato | Código (if/else) |
| Analisar sentimento | LLM |
| Criar conteúdo | LLM |
| Interpretar nuance | LLM |

### Implementação

```text
1. Tarefa é repetitiva e previsível? → Código
2. Tarefa requer criatividade/interpretação? → LLM
3. Pode ser determinístico? → Código primeiro
```

---

## 4. Quality Gates (Checklists)

### Estrutura Obrigatória

Todo agente deve ter um Quality Gate com:

```text
QUALITY GATE: [Nome do Agente]
├── Checklist de N pontos
├── Nota mínima (ex: 95/100)
├── Critérios de aprovação
└── Ação se reprovado (Loop Ralph)
```

### Exemplo

```markdown
## Quality Gate: Resumo de Livro

- [ ] Tem 10+ citações?
- [ ] Tem analogias práticas?
- [ ] Aplicável ao contexto do leitor?
- [ ] Estrutura lógica (não ordem do livro)?
- [ ] Nota > 95?

**Se NÃO:** Volta para reescrever (Ralph Loop)
```

---

## 5. Metodologia A-to-O (Caos → Ordem)

### Fluxo

```text
CAOS (Ideia)
    │
    ▼
1. DECOMPOSIÇÃO (AOC)
   └── Ação (Verbo) + Objeto (Alvo) + Condição (Contexto)
    │
    ▼
2. FRICÇÃO (UX)
   └── Caixa aberta → Opção binária
    │
    ▼
3. ARQUITETURA
   └── Fluxo lógico: entrada → processamento → saída
    │
    ▼
4. ORQUESTRAÇÃO
   └── Quem faz o quê (Agentes)
    │
    ▼
5. PROTOTIPAGEM
   └── MVP em 48h ("Feito > Perfeito, mas funciona")
    │
    ▼
6. REFINAMENTO
   └── Quality Gates + Métricas
    │
    ▼
ORDEM (Sistema)
```

---

## 6. Template de Agente

### Estrutura Mínima

```markdown
# Agente: [Nome]

## Role

[Função específica - 1 linha]

## Comportamento

[Como age - 2-3 bullets]

## Inputs

[O que recebe]

## Outputs

[O que entrega]

## Quality Gate

[Checklist de validação]

## Integração

[Com quem trabalha]
```

### Exemplo Completo

```markdown
# Agente: Kim (QA)

## Role

Validadora de qualidade. Impede que lixo vá para produção.

## Comportamento

- Critica sem piedade (construtivamente)
- Emite reports de risco
- Nunca aprova sem checklist completo

## Inputs

- Output de outros agentes
- Critérios de aceitação
- Checklist de qualidade

## Outputs

- Aprovação / Reprovação
- Report de problemas
- Sugestões de melhoria

## Quality Gate

- [ ] Todos os critérios atendidos?
- [ ] Riscos documentados?
- [ ] Nota > 95?

## Integração

- Recebe de: James (Dev), Whistle (Arquiteto)
- Envia para: Master (aprovação final)
```

---

## 7. Filosofia Mente Lendária

### Princípios Obrigatórios

| Princípio | Descrição |
| --------- | --------- |
| **Automatize o Chato** | >3x = trabalho de Ralph |
| **Velocidade = Segurança** | Adaptação rápida > planejamento infinito |
| **Orquestrador > Operador** | Desenhe o sistema, não aperte o botão |
| **Human First** | Experiência humana antes do código |
| **Abundância** | Compartilhe conhecimento |

---

## 8. Checklist de Criação

Antes de criar um novo agente:

```text
[ ] 1. Role definido (1 função clara)
[ ] 2. Comportamento descrito (2-3 bullets)
[ ] 3. Inputs/Outputs especificados
[ ] 4. Quality Gate criado
[ ] 5. Integração mapeada (com quem trabalha)
[ ] 6. Segue estrutura iOS (Master → Líderes → Operários)
[ ] 7. Código para determinístico, LLM para cognitivo
[ ] 8. Loop Ralph se necessário
```

---

## Referências

- Blueprint: `02_PROJETOS/Estudo_Alan_Nicolas/conceitos/Alan_Nicolas_O_Fim_dos_Cursos_e_Ascensao_dos_Sistemas.md`
- Agentes atuais: `04_RECURSOS/PROMPTS/Agentes_Sistema/`
- Névoa (Orquestrador): `.claude/commands/nevoa.md`

---

**Versão:** 1.0
**Criado:** 25/Jan/2026
**Autor:** Bi-IA (Claude + Gemini)
