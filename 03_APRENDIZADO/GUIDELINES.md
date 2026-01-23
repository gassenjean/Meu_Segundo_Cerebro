---
criado: 2026-01-16T12:44:43-03:00
atualizado: 2026-01-16T12:44:43-03:00
---
# 🎓 GUIDELINES: APRENDIZADO

**Diretrizes Específicas - Cursos e Estudos**

**Categoria:** 03_APRENDIZADO
**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

---

## 🎯 O QUE PERTENCE AQUI

### Sim, Vai em APRENDIZADO

- ✅ Cursos em andamento (online ou presencial)
- ✅ Bootcamps e formações estruturadas
- ✅ Livros sendo estudados ativamente (com notas progressivas)
- ✅ Tutoriais estruturados multi-parte
- ✅ Mentoria/coaching recebido (sessões documentadas)
- ✅ Lives de aprendizado (em processo de estudo)
- ✅ Certificações profissionais (em preparação)
- ✅ Workshops e treinamentos
- ✅ Séries educacionais (YouTube, podcasts) sendo acompanhadas

### Não, Vai em Outro Lugar

- ❌ Conhecimento consolidado → `01_CONHECIMENTO/`
- ❌ Livros já lidos e resumidos → `01_CONHECIMENTO/Livros/`
- ❌ Aplicação prática do aprendizado → `02_PROJETOS/`
- ❌ Templates criados a partir do curso → `04_RECURSOS/TEMPLATES/`
- ❌ Prompts desenvolvidos durante estudo → `04_RECURSOS/PROMPTS/`
- ❌ Conteúdo que você criou (não está aprendendo) → `02_PROJETOS/`
- ❌ Lives concluídas e consolidadas → `01_CONHECIMENTO/`

**Princípio:** Aprendizado = Processo **ativo** de estudo com estrutura, progressão e status "em andamento" ou "pausado". Quando concluído e consolidado → move para `01_CONHECIMENTO/`.

---

## 📛 NOMENCLATURA ESPECÍFICA

### Padrão de Nome de Curso

```
[Nome_Curso] OU [Autor_Nome_Curso]

Regras:
- CamelCase obrigatório
- Incluir autor/instrutor SE relevante
- Descritivo mas conciso
- Máximo 40 caracteres

Exemplos corretos:
✅ Alan_Nicolas_Academia_Lendaria
✅ JavaScript_Full_Stack_Udemy
✅ DeFi_Master_Class
✅ Python_Data_Science_Alura
✅ TDAH_Produtividade_Curso
```

### Nomenclatura de Arquivos Internos

#### README.md
```
✅ README.md (sempre na raiz do curso)
```

#### Notas (notas/)
```
notas/
├── M01_Introducao.md                # Módulo 01
├── M02_Fundamentos.md               # Módulo 02
├── M03_Avancado.md                  # Módulo 03
├── L01_Aula_Inaugural.md            # Live 01
├── L02_Deep_Dive_Feature_X.md       # Live 02
└── NOTAS_GERAIS.md                  # Notas não organizadas por aula

Padrões:
- Módulos: M[NN]_Titulo.md (M01, M02, etc)
- Lives: L[NN]_Titulo.md (L01, L02, etc)
- Aulas: Aula_[NN]_Titulo.md
- Capítulos: Cap_[NN]_Titulo.md (para livros)
- Sessões: Sessao_[NN]_Titulo.md (para mentorias)
```

#### Recursos (recursos/)
```
recursos/
├── slides/                          # PDFs, apresentações
├── codigo/                          # Exemplos de código
├── exercicios/                      # Exercícios práticos
├── certificados/                    # Certificados obtidos
└── extras/                          # Materiais complementares

Arquivos:
- Manter nomes originais quando possível
- Se renomear: usar CamelCase + descrição clara
```

---

## 🗂️ ESTRUTURA OBRIGATÓRIA

### Template Base (SIMPLES: 2 pastas apenas)

```
Nome_Curso/
├── README.md                    # ✅ OBRIGATÓRIO - Visão geral e progresso
├── notas/                       # ✅ OBRIGATÓRIO - Notas de aulas/módulos
│   ├── M01_Introducao.md
│   ├── M02_Fundamentos.md
│   └── NOTAS_GERAIS.md          # Notas avulsas
└── recursos/                    # ✅ OBRIGATÓRIO - Materiais de apoio
    ├── slides/
    ├── codigo/
    └── exercicios/
```

**IMPORTANTE: APENAS 2 PASTAS (notas + recursos)**

❌ **NÃO criar:** checkpoints/, planejamento/, docs/, tarefas/, metricas/

**Motivo:** Curso não é projeto. Curso é **input** (Sistema 5C: Consumir/Capturar). Projeto é **output** (Criar/Compartilhar).

**Se curso gerar projeto:** Criar projeto separado em `02_PROJETOS/` e linkar no README.md do curso.

---

## 📝 TEMPLATES COMPLETOS

### Template: README.md

```markdown
# [Nome do Curso]

**Status:** [🟢 Em andamento | 🟡 Pausado | ✅ Concluído]
**Início:** [DD/MMM/YYYY]
**Conclusão prevista:** [DD/MMM/YYYY ou "Sem prazo"]
**Instrutor:** [Nome do instrutor/autor]
**Plataforma:** [Udemy, YouTube, Livro, Mentoria, etc]

---

## 🎯 Objetivo do Curso

[Por que estou fazendo este curso? O que quero aprender?]

### Aplicação Esperada

[Onde vou usar este conhecimento? Em qual projeto/área?]

---

## 📊 Progresso

**Conclusão:** [XX%] ████████░░

**Módulos:**
- [x] M01 - Introdução (DD/MMM)
- [ ] M02 - Fundamentos
- [ ] M03 - Avançado
- [ ] M04 - Prática

**Total:** [X de Y] módulos completados

---

## 📚 Estrutura do Curso

### Módulos

**M01 - Introdução**
- Aula 1: [Título]
- Aula 2: [Título]
- Status: ✅ Concluído

**M02 - Fundamentos**
- Aula 1: [Título]
- Aula 2: [Título]
- Status: 🟢 Em andamento

**M03 - Avançado**
- Status: ⏸️ Não iniciado

---

## 🔑 Principais Aprendizados

[Atualizar conforme avança no curso]

**Conceitos Chave:**
- Conceito 1: [Resumo em 1 linha]
- Conceito 2: [Resumo em 1 linha]
- Conceito 3: [Resumo em 1 linha]

**Ferramentas/Técnicas:**
- Ferramenta 1: [Para que serve]
- Técnica 1: [Quando usar]

---

## 🎯 Ações Práticas

**Exercícios completados:**
- [ ] Exercício 1 - [Título]
- [ ] Exercício 2 - [Título]

**Projetos criados a partir deste curso:**
- [[02_PROJETOS/Nome_Projeto/]] - [Descrição]

---

## 🔗 Próximos Passos

**Após concluir este curso:**
1. Consolidar conhecimento em [[01_CONHECIMENTO/]]
2. Aplicar em [[02_PROJETOS/Nome_Projeto/]]
3. Próximo curso: [Nome se já souber]

---

## 📁 Organização de Arquivos

```
Nome_Curso/
├── README.md (este arquivo)
├── notas/
│   ├── M01_Introducao.md
│   ├── M02_Fundamentos.md
│   └── NOTAS_GERAIS.md
└── recursos/
    ├── slides/
    ├── codigo/
    └── exercicios/
```

---

## 🔗 Links Relacionados

- [Link para plataforma do curso]
- [[01_CONHECIMENTO/[Categoria]/]] - Conhecimento relacionado
- [[_MOC_Aprendizado.md]] - Voltar ao MOC

---

**Última atualização:** [DD/MMM/YYYY]
**Próxima revisão:** [DD/MMM/YYYY]
```

### Template: Nota de Módulo/Aula

```markdown
# [Módulo/Aula] - [Título]

**Data:** [DD/MMM/YYYY]
**Duração:** [Xh ou X aulas]
**Status:** [✅ Concluído | 🟢 Em andamento | ⏸️ Pausado]

---

## 🎯 Objetivo da Aula

[O que esta aula ensina? Qual o foco?]

---

## 📝 Notas Principais

### Conceito 1: [Nome]

**O que é:**
[Explicação simples]

**Por que importa:**
[Relevância, aplicação]

**Como usar:**
[Passo a passo ou exemplo]

### Conceito 2: [Nome]

[mesmo padrão]

---

## 💡 Insights Pessoais

[Suas reflexões, conexões com conhecimento anterior, ideias de aplicação]

---

## 🔑 Pontos Chave (TL;DR)

- **Ponto 1:** [Resumo]
- **Ponto 2:** [Resumo]
- **Ponto 3:** [Resumo]

---

## 💻 Exemplos Práticos / Código

```[linguagem]
// Exemplo de código relevante
// Com comentários explicativos
```

**Explicação:**
[O que o código faz, por que é importante]

---

## ✅ Exercícios / Tarefas

- [ ] Exercício 1: [Descrição]
- [ ] Exercício 2: [Descrição]
- [ ] Aplicar em projeto: [[02_PROJETOS/Nome/]]

---

## 🔗 Conexões

### Relacionado a:
- [[notas/M01_Introducao.md]] - Conceito base
- [[01_CONHECIMENTO/Categoria/Topico.md]] - Conhecimento prévio
- [[02_PROJETOS/Nome/]] - Onde aplicar

### Próximos passos:
- [[notas/M03_Avancado.md]] - Continuar aprendizado

---

## 📚 Referências

- Link 1: [Título do recurso]
- Link 2: [Artigo complementar]
- [[recursos/slides/Aula_X.pdf]]

---

**Revisado:** [DD/MMM/YYYY]
**Consolidado em 01_CONHECIMENTO/:** [ ] Sim [ ] Não [ ] Parcial
```

---

## 🔄 WORKFLOW DE APRENDIZADO

### Do Curso à Consolidação (Sistema 5C Completo)

```
1. CONSUMIR (Input)
   ↓
   Assistir aula/ler capítulo/participar de live

2. CAPTURAR (Registro)
   ↓
   Criar nota em notas/M[NN]_Titulo.md
   - Usar template de nota de módulo
   - Capturar APENAS conceitos novos, insights, ações
   - NÃO transcrever aula inteira

3. CONECTAR (Relações)
   ↓
   Adicionar wikilinks para:
   - Outras notas do curso
   - Conhecimento existente em 01_CONHECIMENTO/
   - Projetos onde aplicar em 02_PROJETOS/

4. CRIAR (Output - Opcional)
   ↓
   OPÇÃO A: Exercício prático → recursos/exercicios/
   OPÇÃO B: Nota consolidada → 01_CONHECIMENTO/
   OPÇÃO C: Projeto aplicando conceito → 02_PROJETOS/

5. COMPARTILHAR (Aplicação)
   ↓
   Aplicar em projeto real em 02_PROJETOS/
   OU
   Ensinar/compartilhar (blog, vídeo, mentoria)
```

### Checklist de Cada Aula

Após assistir cada aula/módulo:

- [ ] Criar nota em notas/ (usando template)
- [ ] Capturar conceitos chave (3-5 principais)
- [ ] Adicionar pelo menos 2 wikilinks
- [ ] Marcar exercícios propostos
- [ ] Atualizar README.md (progresso %)
- [ ] Se conceito importante → considerar consolidar em 01_CONHECIMENTO/

---

## 🔄 INTEGRAÇÃO COM SISTEMA 5C

### Sistema 5C Aplicado ao Aprendizado

**Alan Nicolas - Sistema 5C:**

```
CONSUMIR → Input de conhecimento
├── Assistir aula
├── Ler capítulo
├── Participar de workshop
└── FOCO: Absorver sem interrupção

CAPTURAR → Registro estruturado
├── notas/M01_Introducao.md
├── Usar templates
├── APENAS conceitos relevantes
└── FOCO: Seletividade, não volume

CONECTAR → Criar relações
├── Wikilinks para notas anteriores
├── Links para 01_CONHECIMENTO/
├── Tags relevantes
└── FOCO: Rede de conhecimento

CRIAR → Gerar output
├── Exercício prático
├── Nota consolidada em 01_CONHECIMENTO/
├── Projeto em 02_PROJETOS/
└── FOCO: Transformar input em output

COMPARTILHAR → Aplicar e ensinar
├── Aplicar em projeto real
├── Ensinar a alguém
├── Publicar conteúdo
└── FOCO: Validar aprendizado
```

**Regra 80/20:**
- 80% do valor vem de 20% do conteúdo
- Capture APENAS os 20% mais valiosos
- Ignore detalhes que pode buscar depois

---

## 🎯 PROGRESSÃO DO CURSO

### Estados do Curso

```
1. 🟢 EM ANDAMENTO
   ├── Aulas sendo assistidas regularmente
   ├── Notas sendo criadas
   ├── README.md atualizado semanalmente
   └── Progresso visível

2. 🟡 PAUSADO
   ├── Temporariamente interrompido
   ├── Atualizar README.md com razão da pausa
   ├── Marcar última aula/módulo completado
   └── Definir quando pretende retomar (se souber)

3. ✅ CONCLUÍDO
   ├── Todas as aulas/módulos finalizados
   ├── README.md marcado como concluído
   ├── PRÓXIMO PASSO: Consolidar em 01_CONHECIMENTO/
   └── Certificado em recursos/certificados/ (se houver)

4. 📦 ARQUIVADO
   ├── Concluído há >6 meses E consolidado
   ├── Conhecimento extraído para 01_CONHECIMENTO/
   ├── Mover para 00_SISTEMA/ARQUIVO/
   └── Manter link em _MOC_Aprendizado.md
```

### Quando Consolidar em 01_CONHECIMENTO/

**Consolidar DURANTE o curso (progressivamente):**
- Conceito importante surge → criar nota em 01_CONHECIMENTO/
- NÃO esperar curso terminar para consolidar
- Vantagem: Conhecimento disponível imediatamente

**Consolidar AO FINAL do curso (global):**
- Revisar TODAS as notas do curso
- Extrair os 10-20% mais valiosos
- Criar notas consolidadas em 01_CONHECIMENTO/
- Linkar de volta para curso (fonte)

**Recomendação:** Fazer AMBOS
- Durante: Conceitos críticos
- Ao final: Revisão e consolidação global

---

## ⚠️ ANTI-PADRÕES (EVITAR)

### ❌ Erro 1: Transcrição Completa

```
❌ Errado:
# M01 - Introdução

[Transcrição palavra por palavra da aula de 2 horas]
[20 páginas de texto copiado]
[Detalhes irrelevantes incluídos]

✅ Correto:
# M01 - Introdução

## 🎯 Objetivo: Entender fundamentos de X

## 📝 Conceitos Chave

1. **Conceito A:** [Explicação simples em 2-3 linhas]
2. **Conceito B:** [Explicação simples em 2-3 linhas]

## 💡 Insight: [Sua conexão pessoal]

## ✅ Ação: Aplicar conceito A em [[02_PROJETOS/Nome/]]
```

**Regra:** Captura seletiva > Transcrição completa. Qualidade > Quantidade.

### ❌ Erro 2: Criar Estrutura de Projeto

```
❌ Errado:
Nome_Curso/
├── README.md
├── checkpoints/          ← ERRO! Curso não precisa
├── planejamento/         ← ERRO!
├── tarefas/              ← ERRO!
├── metricas/             ← ERRO!
├── notas/
└── recursos/

✅ Correto:
Nome_Curso/
├── README.md
├── notas/                ← APENAS estas 2 pastas
└── recursos/
```

**Regra:** Curso = INPUT simples. Projeto = OUTPUT complexo. Não misturar.

### ❌ Erro 3: Notas Sem Conexões

```
❌ Errado:
# M02 - Fundamentos

[Conteúdo isolado, sem links]

✅ Correto:
# M02 - Fundamentos

## 🔗 Conexões
- Baseado em [[M01_Introducao.md]]
- Relacionado a [[01_CONHECIMENTO/IA/Prompts.md]]
- Aplicar em [[02_PROJETOS/KabaK/]]
```

**Regra:** Conhecimento conectado = memorização 10x melhor.

### ❌ Erro 4: README.md Desatualizado

```
❌ Errado:
README.md mostra:
- Progresso: 10%
- Última atualização: 01/Jan/2026
Realidade: Já está em 50%, hoje é 16/Jan

✅ Correto:
Atualizar README.md:
- Após cada módulo completado
- Mínimo semanal se curso ativo
- Ao pausar (atualizar status)
```

**Regra:** README = Dashboard do curso. Deve refletir realidade.

### ❌ Erro 5: Curso Fantasma

```
❌ Errado:
Curso criado há 3 meses
- README.md = template vazio
- notas/ = 1 nota incompleta
- Progresso: 5%
- Status: Ainda marcado como "Em andamento"

✅ Correto:
Se curso não decolou:
1. Atualizar README.md → Status: 🟡 Pausado ou 📦 Arquivado
2. Adicionar razão (ex: "Não é prioridade agora")
3. Atualizar _MOC_Aprendizado.md
4. Se vai desistir → Arquivar
```

**Regra:** Honestidade > Aparências. Pausar/arquivar é OK.

### ❌ Erro 6: Duplicação com 01_CONHECIMENTO/

```
❌ Errado:
03_APRENDIZADO/Curso_IA/notas/M02_Prompts.md (10 páginas)
01_CONHECIMENTO/IA_Prompts_Engineering.md (mesmo conteúdo)

✅ Correto:
03_APRENDIZADO/Curso_IA/notas/M02_Prompts.md (notas brutas do contexto do curso)
01_CONHECIMENTO/IA_Prompts_Engineering.md (conhecimento consolidado e refinado)
+ Linkar um ao outro (nota consolidada referencia fonte)
```

**Regra:**
- 03_APRENDIZADO/ = Notas no contexto do curso (podem ser brutas)
- 01_CONHECIMENTO/ = Conhecimento consolidado e permanente
- Um referencia o outro

---

## 📊 ESTRATÉGIAS DE ORGANIZAÇÃO

### 1. Cursos Longos (>20 aulas)

**Organizar notas por módulos:**

```
notas/
├── M01_Introducao.md
├── M02_Fundamentos.md
├── M03_Intermediario.md
├── M04_Avancado.md
└── M05_Projeto_Final.md
```

**README.md detalhado:**
- Lista completa de módulos
- % de progresso por módulo
- Tempo estimado restante

### 2. Cursos Curtos (<10 aulas)

**Nota única ou por aula:**

```
notas/
├── Aula_01_Intro.md
├── Aula_02_Conceito_X.md
├── Aula_03_Pratica.md
└── NOTAS_GERAIS.md         ← Pode consolidar tudo aqui se preferir
```

### 3. Livros (Capítulos)

```
notas/
├── Cap_01_Introducao.md
├── Cap_02_Metodo_PARA.md
├── Cap_03_Sistema_CODE.md
└── RESUMO_GERAL.md          ← Resumo do livro completo ao final
```

### 4. Lives / Workshops (Eventos)

```
notas/
├── L01_16JAN2026_Tema_Principal.md
├── L02_23JAN2026_Deep_Dive_X.md
├── L03_30JAN2026_QA_Especial.md
└── INSIGHTS_ACUMULADOS.md   ← Consolidação cross-lives
```

**Nomenclatura de lives:**
- `L[NN]_DDMMMYYYY_Titulo.md`
- Data ajuda a localizar e ordenar

### 5. Mentorias (Sessões)

```
notas/
├── Sessao_01_16JAN2026_Planejamento.md
├── Sessao_02_23JAN2026_Revisao.md
├── Sessao_03_30JAN2026_Estrategia.md
└── ACOES_PRIORITARIAS.md    ← Lista consolidada de ações
```

---

## ✅ CHECKLIST DE MANUTENÇÃO

### Por Aula/Módulo (15-30 min)

- [ ] Assistir/ler conteúdo (Consumir)
- [ ] Criar nota usando template (Capturar)
- [ ] Adicionar 2+ wikilinks (Conectar)
- [ ] Marcar exercícios propostos
- [ ] Atualizar README.md (% progresso)

### Semanal (30 min - se curso ativo)

- [ ] Revisar notas da semana
- [ ] Consolidar conceitos importantes → 01_CONHECIMENTO/
- [ ] Fazer exercícios pendentes
- [ ] Atualizar README.md (progresso detalhado)
- [ ] Atualizar _MOC_Aprendizado.md (se necessário)

### Mensal (1h)

- [ ] Revisar progresso geral
- [ ] Avaliar: curso ainda é prioridade?
- [ ] Se não → marcar como 🟡 Pausado
- [ ] Consolidar conhecimento acumulado → 01_CONHECIMENTO/
- [ ] Limpar recursos/ (remover downloads desnecessários)

### Ao Concluir Curso (2-3h)

- [ ] Marcar README.md como ✅ Concluído
- [ ] Revisar TODAS as notas
- [ ] Consolidar os 20% mais valiosos → 01_CONHECIMENTO/
- [ ] Criar projeto aplicando conhecimento (se aplicável) → 02_PROJETOS/
- [ ] Adicionar certificado em recursos/certificados/
- [ ] Atualizar _MOC_Aprendizado.md
- [ ] Agendar arquivamento (6 meses)
- [ ] Celebrar! 🎉

---

## 🔗 LINKS RELACIONADOS

- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Padrões gerais de nomenclatura
- [[_MOC_Aprendizado.md]] - MOC master desta categoria
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Protocolo geral
- [[01_CONHECIMENTO/]] - Para consolidar conhecimento
- [[02_PROJETOS/]] - Para aplicar aprendizado
- [[04_RECURSOS/TEMPLATES/]] - Templates disponíveis

**Sistema 5C (Alan Nicolas):**
- [[01_CONHECIMENTO/Autores_Pensadores/Alan_Nicolas/Sistema_5C.md]]

---

**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

**APRENDER COM ESTRUTURA = CONHECIMENTO PERMANENTE! 🎓**
