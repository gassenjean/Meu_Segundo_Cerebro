---
criado: 2026-01-16T12:49:45-03:00
atualizado: 2026-01-16T12:49:45-03:00
---
# 🌟 GUIDELINES: PESSOAL

**Diretrizes Específicas - Notas Pessoais e Reflexões**

**Categoria:** 05_PESSOAL
**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

---

## 🎯 O QUE PERTENCE AQUI

### Sim, Vai em PESSOAL

- ✅ Journal/diário pessoal (reflexões diárias/semanais)
- ✅ Ideias brutas (ainda não desenvolvidas ou validadas)
- ✅ Reflexões pessoais e autoconhecimento
- ✅ Brainstorms e pensamentos aleatórios
- ✅ Notas sobre si mesmo (valores, personalidade, forças/fraquezas)
- ✅ Finanças pessoais (não de projeto/empresa)
- ✅ Metas e objetivos pessoais (não de projeto)
- ✅ Listas de desejos (wishlist, bucket list)
- ✅ Tracking pessoal (hábitos, humor, energia)
- ✅ Revisões pessoais (semanal, mensal, anual)

### Não, Vai em Outro Lugar

- ❌ Conhecimento consolidado → `01_CONHECIMENTO/`
- ❌ Ideias que viraram projeto → `02_PROJETOS/`
- ❌ Notas de curso → `03_APRENDIZADO/`
- ❌ Templates/prompts reutilizáveis → `04_RECURSOS/`
- ❌ Tarefas de projeto → `02_PROJETOS/[Projeto]/tarefas/`
- ❌ Metas de projeto → `02_PROJETOS/[Projeto]/planejamento/`

**Princípio:** Pessoal = Privado, em processo, não estruturado (ainda), sobre VOCÊ (não sobre trabalho/projetos).

---

## 📛 NOMENCLATURA ESPECÍFICA

### Journal (Diário)

```
Journal_DDMMMYYYY.md

Regras:
- Prefixo Journal_ obrigatório (CamelCase)
- Data: DDMMMYYYY (17JAN2026)
- Ano com 4 dígitos
- Mês com 3 letras UPPERCASE

Exemplos corretos:
✅ Journal_17JAN2026.md
✅ Journal_25FEV2026.md
✅ Journal_31DEZ2026.md

Exemplos errados:
❌ Diario_17-01-2026.md  (formato errado, português)
❌ Journal_17-01-26.md   (formato de data errado)
❌ journal_17jan2026.md  (lowercase)
```

### Ideias

```
Idea_[Titulo_Curto].md

Regras:
- Prefixo Idea_ obrigatório (CamelCase)
- Título: Descritivo mas curto
- Máximo 40 caracteres
- CamelCase

Exemplos corretos:
✅ Idea_App_Produtividade_TDAH.md
✅ Idea_Negocio_IA_Consultoria.md
✅ Idea_Curso_PKM_Para_Devs.md
✅ Idea_Plugin_Obsidian_AutoTag.md

Exemplos errados:
❌ ideia_app.md           (lowercase, sem prefixo correto)
❌ App_Produtividade.md   (sem prefixo Idea_)
❌ Idea_App_Produtividade_TDAH_Com_Gamificacao_E_IA.md  (muito longo)
```

### Metas e Objetivos

```
Metas_[Periodo].md

Exemplos:
✅ Metas_2026.md
✅ Metas_Q1_2026.md
✅ Metas_Janeiro_2026.md
```

### Finanças

```
Financas_[Periodo].md OU Financas_[Categoria].md

Exemplos:
✅ Financas_2026.md
✅ Financas_Janeiro_2026.md
✅ Financas_Investimentos.md
✅ Financas_Orcamento_Pessoal.md
```

### Revisões Pessoais

```
Revisao_[Tipo]_[Periodo].md

Exemplos:
✅ Revisao_Semanal_Semana_03_2026.md
✅ Revisao_Mensal_Janeiro_2026.md
✅ Revisao_Anual_2026.md
```

---

## 🗂️ ORGANIZAÇÃO POR SUBPASTA

### Estrutura Recomendada

```
05_PESSOAL/
│
├── _MOC_Pessoal.md          # MOC master (índice) - opcional
│
├── Journal/                 # Diário pessoal
│   ├── 2026/
│   │   ├── Journal_01JAN2026.md
│   │   ├── Journal_02JAN2026.md
│   │   └── ...
│   ├── 2025/
│   │   └── ...
│   └── README.md            # Sobre o journal (opcional)
│
├── Ideas/                   # Ideias brutas
│   ├── Idea_App_X.md
│   ├── Idea_Negocio_Y.md
│   ├── Idea_Curso_Z.md
│   └── _ARQUIVO/            # Ideias descartadas
│       └── ...
│
├── Metas/                   # Metas e objetivos
│   ├── Metas_2026.md
│   ├── Metas_Q1_2026.md
│   ├── Metas_Janeiro_2026.md
│   └── Revisoes/
│       ├── Revisao_Mensal_Janeiro_2026.md
│       ├── Revisao_Anual_2025.md
│       └── ...
│
├── Financas/                # Finanças pessoais
│   ├── Financas_2026.md
│   ├── Financas_Investimentos.md
│   ├── Financas_Orcamento.md
│   └── Historico/
│       └── Financas_2025.md
│
├── Sobre_Mim/               # Autoconhecimento
│   ├── Valores_Pessoais.md
│   ├── Forcas_Fraquezas.md
│   ├── Personalidade.md
│   ├── TDAH_Estrategias.md
│   └── Plano_Vida.md
│
├── Tracking/                # Tracking pessoal (opcional)
│   ├── Habitos_2026.md
│   ├── Humor_Tracker.md
│   └── Energia_Tracker.md
│
├── Listas/                  # Listas diversas (opcional)
│   ├── Wishlist.md
│   ├── Bucket_List.md
│   └── Livros_Para_Ler.md
│
└── README.md                # Visão geral da categoria (opcional)
```

**Nota:** Subpastas são opcionais. Crie conforme necessidade.

---

## 📝 TEMPLATES COMPLETOS

### Template: Journal (Diário Pessoal)

**Versão Completa (Reflexiva):**

```markdown
# Journal - DD/MMM/YYYY

**Humor:** 😊 Ótimo | 😐 Neutro | 😢 Ruim
**Energia:** ⚡⚡⚡ Alta | ⚡⚡ Média | ⚡ Baixa
**Foco:** ⭐⭐⭐ Excelente | ⭐⭐ Bom | ⭐ Difícil

---

## 🌅 Como Foi o Dia

[Resumo livre do dia em 2-4 parágrafos]

---

## ✅ Conquistas do Dia

- Conquista 1
- Conquista 2
- Conquista 3

---

## 🎓 O Que Aprendi Hoje

**Insight principal:**
[Aprendizado mais importante do dia]

**Outros aprendizados:**
- Aprendizado 1
- Aprendizado 2

---

## 💭 Reflexões

[Pensamentos, reflexões, questionamentos]

---

## 🙏 Gratidão

Hoje sou grato por:
1. Gratidão 1
2. Gratidão 2
3. Gratidão 3

---

## ⚠️ Desafios / Problemas

**Desafio principal:**
[O que foi difícil hoje?]

**Como lidei:**
[O que fiz a respeito]

**Lição:**
[O que aprendi com isso]

---

## 🎯 Amanhã

**Prioridade #1:** [A coisa mais importante para amanhã]

**Outras tarefas:**
- [ ] Tarefa 1
- [ ] Tarefa 2

**Mindset para amanhã:**
[Como quero me sentir/agir amanhã]

---

**Tags:** #journal #[tema1] #[tema2]
```

**Versão Rápida (TDAH-Friendly - 2 minutos):**

```markdown
# Journal - DD/MMM/YYYY

😊/😐/😢 | ⚡⚡⚡/⚡⚡/⚡

## Hoje
- Fiz: [X]
- Aprendi: [Y]
- Senti: [Z]

## Gratidão
1. A
2. B
3. C

## Amanhã
- Prioridade: [X]

---
#journal #quick
```

### Template: Idea (Ideia Bruta)

```markdown
# IDEA - [Título da Ideia]

**Criado:** DD/MMM/YYYY
**Status:** 💡 Bruta | 🔍 Pesquisando | 🚀 Pronto para Virar Projeto | ⏸️ Pausado | ❌ Descartado
**Tipo:** [App, Negócio, Curso, Conteúdo, Produto, Serviço]

---

## 🎯 O Que É (Em 1 Frase)

[Descrição ultra-concisa da ideia]

---

## 💡 Descrição

[Descrição completa da ideia - o que é, como funciona, para quem]

---

## 🔥 Por Que Isso Importa

**Problema que resolve:**
[Que dor/problema esta ideia ataca?]

**Para quem:**
[Público-alvo]

---

## 💰 Potencial

**Monetização:**
[Como poderia gerar renda? ou "Não aplicável"]

**Impacto pessoal:**
[Como isso me beneficia? Aprendizado? Portfólio?]

---

## 🚧 Próximos Passos (Se Avançar)

- [ ] Passo 1: [Pesquisar X]
- [ ] Passo 2: [Validar Y]
- [ ] Passo 3: [Criar MVP Z]

---

## 🔗 Conexões

**Similar a:**
- [[Idea_Outra.md]] - [Como se relaciona]

**Inspirado em:**
- [Fonte, pessoa, produto]

**Poderia usar conhecimento de:**
- [[01_CONHECIMENTO/Categoria/Topico.md]]

---

## 📊 Decisão

**Data revisão:** [DD/MMM/YYYY]

**Destino:**
- [ ] Virar projeto → Mover para `02_PROJETOS/`
- [ ] Consolidar conhecimento → `01_CONHECIMENTO/`
- [ ] Manter incubando em `Ideas/`
- [ ] Arquivar → `Ideas/_ARQUIVO/`

---

**Última atualização:** DD/MMM/YYYY
**Tags:** #idea #[categoria] #[tema]
```

### Template: Metas (Anuais/Mensais)

```markdown
# METAS - [Período: 2026, Q1 2026, Janeiro 2026]

**Período:** [Data início] - [Data fim]
**Criado:** DD/MMM/YYYY
**Status:** 🟢 Ativo | 🟡 Pausado | ✅ Concluído

---

## 🎯 Grandes Objetivos

### 1. [Nome do Objetivo]

**O que:** [Descrição clara]
**Por que:** [Motivação, razão]
**Como medir:** [Métrica de sucesso]
**Prazo:** [DD/MMM/YYYY]

**Ações:**
- [ ] Ação 1
- [ ] Ação 2
- [ ] Ação 3

### 2. [Nome do Objetivo]

[mesmo padrão]

---

## 📊 Áreas da Vida

### 💼 Profissional / Carreira
- [ ] Meta 1
- [ ] Meta 2

### 💰 Financeiro
- [ ] Meta 1
- [ ] Meta 2

### 🧠 Aprendizado / Crescimento
- [ ] Meta 1
- [ ] Meta 2

### 💪 Saúde / Fitness
- [ ] Meta 1
- [ ] Meta 2

### 👨‍👩‍👧 Relacionamentos / Social
- [ ] Meta 1
- [ ] Meta 2

### 🎨 Hobbies / Diversão
- [ ] Meta 1
- [ ] Meta 2

---

## 📈 Progresso

**Atualizado em:** [DD/MMM/YYYY]

| Meta | Progresso | Status |
|------|-----------|--------|
| Meta 1 | XX% | 🟢/🟡/🔴 |
| Meta 2 | XX% | 🟢/🟡/🔴 |

---

## 💭 Reflexões

[Atualizações, aprendizados, ajustes de rota]

---

**Última revisão:** DD/MMM/YYYY
**Próxima revisão:** DD/MMM/YYYY
```

---

## 📝 JOURNALING: ESTRATÉGIA

### Frequência Recomendada

**Ideal:**
- Diário (todos os dias, mesmo que 2 minutos)

**Realista:**
- 3-4x por semana (Segunda, Quarta, Sexta, Domingo)

**Mínimo viável:**
- Semanal (domingo à noite / segunda de manhã)

**Regra:** Frequência consistente > Conteúdo perfeito.

### Formatos de Journal (Escolha o Seu)

#### 1. Journal Tradicional (Reflexivo)

**Melhor para:** Introspecção profunda, processar emoções
**Tempo:** 10-20 minutos
**Template:** Versão completa acima

#### 2. Journal Rápido (TDAH-Friendly)

**Melhor para:** Quem tem pouco tempo/foco
**Tempo:** 2-5 minutos
**Template:** Versão rápida acima

#### 3. Bullet Journal Style

**Melhor para:** Visual, listas, tracking
**Tempo:** 5-10 minutos
**Formato:**
```
# Journal - DD/MMM/YYYY

• Evento importante
○ Tarefa completada
- Nota/pensamento
× Tarefa cancelada

→ Migrado para amanhã
```

#### 4. Gratitude Journal (Só Gratidão)

**Melhor para:** Mindset positivo
**Tempo:** 1-2 minutos
**Formato:**
```
# Journal - DD/MMM/YYYY

Grato por:
1. [A]
2. [B]
3. [C]
```

#### 5. One Line a Day

**Melhor para:** Máxima simplicidade
**Tempo:** 30 segundos
**Formato:**
```
DD/MMM/YYYY: [Uma frase resumindo o dia]
```

**Dica:** Escolha 1 formato e teste por 30 dias. Depois ajuste se necessário.

---

## 💡 IDEIAS: ESTRATÉGIA COMPLETA

### 1. Captura Rápida (Zero Fricção)

**Princípio:** Capturar IMEDIATAMENTE, organizar DEPOIS.

**Workflow:**
```
Ideia surge (a qualquer momento)
↓
Abrir Obsidian (ou _inbox/)
↓
Criar: Idea_[Titulo].md
↓
Escrever: Título + 1 parágrafo descritivo
↓
PRONTO! (não estruturar agora)
```

**Tempo total:** 1-2 minutos

### 2. Revisão Mensal de Ideias

**Frequência:** 1x por mês (ex: último domingo do mês)
**Tempo:** 30-60 min

**Processo:**
```
1. LISTAR
   Abrir todas as ideias de Ideas/

2. PARA CADA IDEIA, PERGUNTAR:
   - Ainda faz sentido?
   - Tenho energia/tempo para isso?
   - Vale a pena explorar?

3. DECISÃO (4 opções):

   A. 🚀 VIRAR PROJETO
      → Criar projeto em 02_PROJETOS/
      → Mover arquivo para 02_PROJETOS/Nome/planejamento/IDEIA_ORIGINAL.md
      → Remover de Ideas/

   B. 📚 VIRAR CONHECIMENTO
      → Consolidar em 01_CONHECIMENTO/
      → Remover de Ideas/

   C. ⏸️ MANTER INCUBANDO
      → Deixar em Ideas/
      → Adicionar nota de revisão

   D. ❌ DESCARTAR
      → Mover para Ideas/_ARQUIVO/
      → Anotar razão do descarte
```

### 3. Ideias → Projetos (Critérios)

**Quando transformar ideia em projeto?**

Responda:
1. Tenho clareza do objetivo? (Sim/Não)
2. Tenho tempo/energia nos próximos 3 meses? (Sim/Não)
3. Preciso fazer para validar ou posso só pesquisar? (Fazer/Pesquisar)
4. O retorno (financeiro/aprendizado/impacto) compensa? (Sim/Não)

**Se 3+ Sim → VIRAR PROJETO**

**Caso contrário:** Manter incubando ou descartar.

---

## ⚠️ ANTI-PADRÕES (EVITAR)

### ❌ Erro 1: Tentar Estruturar Demais

```
❌ Errado:
Criar estrutura perfeita para ideias brutas:
Ideas/
├── Categorias/
│   ├── Apps/
│   ├── Negocios/
│   ├── Cursos/
├── Status/
│   ├── Validando/
│   ├── Pausadas/

Resultado: Paralisia por organização

✅ Correto:
Ideas/ (flat, sem subpastas)
├── Idea_App_X.md
├── Idea_Negocio_Y.md
├── Idea_Curso_Z.md

Resultado: Captura rápida, organização mensal
```

**Regra:** Simplicidade > Estrutura perfeita.

### ❌ Erro 2: Deixar Ideias Apodrecerem

```
❌ Errado:
100+ ideias em Ideas/ sem revisão há 6+ meses
Resultado: Ideias esquecidas, informação morta

✅ Correto:
Revisão mensal obrigatória
Decidir destino de cada ideia:
- Virar projeto
- Consolidar
- Manter incubando
- Arquivar
```

**Regra:** Ideia sem revisão = ideia morta.

### ❌ Erro 3: Journal Como Transcrição do Dia

```
❌ Errado:
# Journal - 17/Jan/2026

Acordei 7h. Tomei café. Fui trabalhar. Almoço 12h.
Reunião 14h. Voltei 18h. Jantar 19h. TV 20h. Dormi 23h.

Problemas:
- Zero insights
- Zero emoções
- Zero valor futuro

✅ Correto:
# Journal - 17/Jan/2026

😊 | ⚡⚡

Hoje percebi que trabalho melhor de manhã. Fiz X sem esforço
antes do almoço, mas depois das 14h meu foco caiu muito.

Aprendizado: Agendar tarefas complexas para manhã.

Gratidão: Pela reunião boa com time, pelo feedback positivo.

Amanhã: Testar técnica Pomodoro pela manhã.
```

**Regra:** Journal = Emoções + Insights + Aprendizados, NÃO transcrição.

### ❌ Erro 4: Metas Vagas

```
❌ Errado:
- Melhorar saúde
- Ganhar mais dinheiro
- Ser mais produtivo

Problemas:
- Impossível medir
- Impossível saber se atingiu

✅ Correto:
- Saúde: Fazer exercício 3x/semana (medir: app de tracking)
- Financeiro: Aumentar renda mensal em 30% (medir: R$ real)
- Produtividade: Completar 3 projetos em Q1 (medir: checkpoints)
```

**Regra:** Meta sem métrica = desejo vago.

### ❌ Erro 5: Journal Inconsistente

```
❌ Errado:
Janeiro: 20 entradas de journal
Fevereiro: 2 entradas
Março: 0 entradas
Abril: 15 entradas

Problema: Padrão quebrado, hábito não formado

✅ Correto:
Escolher frequência realista (ex: 3x/semana)
Manter CONSISTÊNCIA > volume

3x/semana toda semana > 7x/semana 1 mês e depois parar
```

**Regra:** Consistência > Volume.

### ❌ Erro 6: Informações Sensíveis em Journal

```
❌ Errado (se vault é sincronizado):
Senhas, dados bancários, informações médicas sensíveis,
conflitos com nomes reais de pessoas

✅ Correto:
- Senhas → Gerenciador de senhas (1Password, Bitwarden)
- Dados bancários → App próprio ou offline
- Informações sensíveis → Vault local NÃO sincronizado
- Conflitos → Usar iniciais ou pseudônimos
```

**Regra:** Vault sincronizado = assumir que pode vazar.

---

## ✅ CHECKLIST DE MANUTENÇÃO

### Semanal (5-10 min - domingo)

- [ ] Revisar semana no journal (se não fez diário)
- [ ] Atualizar Metas/ (progresso semanal)
- [ ] Planejar prioridades da próxima semana

### Mensal (1h - último domingo)

- [ ] Revisão mensal completa (usar template Revisao_Mensal)
- [ ] Revisar TODAS as ideias em Ideas/ (decidir destino)
- [ ] Atualizar Metas_Mes.md (progresso mensal)
- [ ] Arquivar journals antigos (mover mês anterior para subpasta)
- [ ] Atualizar Financas/ (se aplicável)

### Trimestral (2h)

- [ ] Revisão trimestral (usar template Revisao_Trimestral)
- [ ] Revisar Sobre_Mim/ (valores/objetivos mudaram?)
- [ ] Atualizar Metas_Q[N].md
- [ ] Limpar Ideas/_ARQUIVO/ (deletar ideias antigas descartadas)

### Anual (4h - 31 dez ou 1 jan)

- [ ] Revisão anual completa (template Revisao_Anual_YYYY)
- [ ] Criar Metas_[ANO_NOVO].md
- [ ] Revisar e atualizar Sobre_Mim/ completamente
- [ ] Arquivar journal do ano anterior (mover 2025/ para subpasta)
- [ ] Limpar Financas/ antigas (>2 anos)

---

## 🔗 LINKS RELACIONADOS

- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Padrões gerais de nomenclatura
- [[_MOC_Pessoal.md]] - MOC master desta categoria (se existir)
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Protocolo geral
- [[01_CONHECIMENTO/DevPessoal/]] - Conhecimento sobre desenvolvimento pessoal
- [[02_PROJETOS/]] - Onde ideias viram projetos

---

**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

**CLAREZA PESSOAL = DECISÕES MELHORES! 🌟**
