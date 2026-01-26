# GUIDELINES: CONHECIMENTO

**Diretrizes Específicas - Base de Conhecimento Pessoal**

**Categoria:** 01_CONHECIMENTO
**Versão:** 1.1
**Criado:** 16/Jan/2026
**Movido:** 26/Jan/2026 (de 01_CONHECIMENTO/ para 00_SISTEMA/PADROES/)

---

## O QUE PERTENCE AQUI

### Sim, Vai em CONHECIMENTO

- ✅ Conceitos aprendidos e consolidados
- ✅ Resumos de livros/artigos/papers
- ✅ Frameworks e metodologias
- ✅ Conhecimento técnico permanente
- ✅ Insights pessoais importantes
- ✅ Referências de autores/pensadores
- ✅ Notas de podcasts/vídeos (processadas)
- ✅ Anotações de lives (após consolidação)

### Não, Vai em Outro Lugar

- ❌ Notas de curso (ainda estudando) → `03_APRENDIZADO/`
- ❌ Templates reutilizáveis → `04_RECURSOS/TEMPLATES/`
- ❌ Documentação de projeto → `02_PROJETOS/[Projeto]/docs/`
- ❌ Ideias não desenvolvidas → `05_PESSOAL/Ideas/`
- ❌ Journal/reflexões → `05_PESSOAL/Journal/`
- ❌ Conteúdo temporário → `_inbox/`

**Princípio:** Conhecimento = Informação **processada** e **consolidada** que você quer manter para sempre.

---

## NOMENCLATURA ESPECÍFICA

### Padrão Hierárquico

```text
[Categoria]_[Subcategoria]_[Topico].md

Exemplos corretos:
✅ IA_LLMs_Prompt_Engineering.md
✅ DevPessoal_TDAH_Estrategias_Foco.md
✅ Negocios_Marketing_Funil_Vendas.md
✅ Filosofia_Estoicismo_Marco_Aurelio.md
```

### Regras Específicas

1. **Máximo 3 níveis de hierarquia**
   - Se precisar de mais → use pastas
   - Exemplo: `IA_Tecnologia/LLMs/Prompt_Engineering_Avancado.md`

2. **CamelCase obrigatório**
   - ✅ `Marketing_Digital_SEO.md`
   - ❌ `marketing_digital_seo.md`

3. **Sem prefixos especiais**
   - ❌ `CONHECIMENTO_IA_Prompts.md` (redundante)
   - ✅ `IA_Prompts_Engenharia.md`

4. **Para autores/pensadores:**

   ```text
   Autores_Pensadores/[Nome_Autor]/[Topico].md

   Exemplo:
   Autores_Pensadores/Alan_Nicolas/Sistema_5C.md
   Autores_Pensadores/Tiago_Forte/PARA_Method.md
   ```

5. **Para livros específicos:**

   ```text
   Livros/[Nome_Livro]_[Autor].md

   Exemplo:
   Livros/Atomic_Habits_James_Clear.md
   Livros/Building_Second_Brain_Tiago_Forte.md
   ```

---

## ESTRUTURA DE MOCs

### 3 Níveis de MOCs

```text
01_CONHECIMENTO/
├── _MOC_Conhecimento.md           ← Nível 1: MOC Master da categoria
├── IA_Tecnologia/
│   ├── _MOC_IA_Tecnologia.md      ← Nível 2: MOC de subcategoria
│   ├── LLMs/
│   │   └── _MOC_LLMs.md          ← Nível 3: MOC de tópico específico
│   │   ├── LLMs_Claude_Sonnet.md
│   │   └── LLMs_Gemini_Pro.md
```

### Quando Criar MOC

**Crie MOC de subcategoria quando:**

- Tiver 5+ arquivos na subcategoria
- Subcategoria tiver subpastas
- Precisar organizar visualmente o conteúdo

**Crie MOC de tópico quando:**

- Tópico tiver 10+ arquivos
- Houver múltiplas perspectivas sobre o mesmo tema
- Precisar mapear conexões complexas

**Não crie MOC quando:**

- Menos de 5 arquivos (desnecessário)
- Estrutura é linear e simples

---

## ESTRATÉGIAS DE CONEXÃO

### 1. Wikilinks (Conexões Diretas)

**Use wikilinks para:**

- Conceitos relacionados
- Sequência de aprendizado
- Contraste de ideias
- Aplicação prática

**Exemplo de seção "Conexões":**

```markdown
## Conexões

### Conceitos Relacionados
- [[IA_LLMs_Fine_Tuning]] - Complementar
- [[IA_Prompts_Chain_of_Thought]] - Técnica específica
- [[DevPessoal_Criatividade]] - Aplicação prática

### Contraste/Comparação
- vs [[IA_RAG_Retrieval]] - Abordagem alternativa

### Aplicação em Projetos
- [[02_PROJETOS/KabaK/docs/Estrategia_IA.md]]
```

### 2. Tags (Conexões Temáticas)

**Frontmatter padrão:**

```yaml
---
criado: 2026-01-16
atualizado: 2026-01-16
tags: [IA, Prompts, Produtividade]
categorias: [Tecnologia, DevPessoal]
fonte: [Livro/Curso/Experiência]
status: [Consolidado/Em_Revisão/Incompleto]
---
```

### 3. MOCs (Conexões Estruturais)

**Sempre linkar:**

- De volta para o MOC da categoria
- Para MOCs relacionados de outras categorias
- Para projetos que usam este conhecimento

---

## TEMPLATE DE NOTA PADRÃO

```markdown
# [Título do Conhecimento]

**Fonte:** [Livro/Artigo/Curso/Experiência/Autor]
**Data aprendizado:** [DD/MMM/YYYY]
**Contexto:** [Por que aprendi isso]
**Status:** [Consolidado/Em_Revisão/Incompleto]

---

## Conceito Principal

[Resumo do conceito em 2-4 parágrafos]
[O QUE é, POR QUE importa, QUANDO usar]

---

## Pontos Chave

- **Ponto 1:** [Descrição]
- **Ponto 2:** [Descrição]
- **Ponto 3:** [Descrição]

---

## Aplicação Prática

### Contexto Gassen (Personalizado)

**Como uso isso:**
[Aplicação específica ao seu contexto]

**Onde já apliquei:**
- Projeto X: [Como foi usado]
- Situação Y: [Resultado]

**Próximas aplicações:**
- [ ] Aplicar em [Projeto/Situação]

---

## Insights Pessoais

[Suas reflexões, adaptações, descobertas únicas]
[O que você pensa diferente da fonte original]

---

## Conexões

### Conceitos Relacionados
- [[Conceito_A]] - [Como se relacionam]
- [[Conceito_B]] - [Complementar/Contraste]

### Aplicação em Projetos
- [[02_PROJETOS/Nome/]] - [Onde é usado]

### Fonte de Aprendizado
- [[03_APRENDIZADO/Curso/nota.md]] - [Origem]

---

## Referências

- [Link 1] - Título
- [Link 2] - Título
- [[Livros/Nome_Livro.md]] - Capítulo X

---

**Última revisão:** [DD/MMM/YYYY]
```

---

## WORKFLOW DE CRIAÇÃO

### Da Captura à Consolidação

```text
1. CAPTURAR (Sistema 5C)
   ↓
   _inbox/nota_rapida.md

2. PROCESSAR
   ↓
   Identificar categoria: IA? DevPessoal? Negócios?

3. NOMEAR
   ↓
   Aplicar padrão: Categoria_Sub_Topico.md

4. ESTRUTURAR
   ↓
   Usar template de nota padrão

5. CONECTAR
   ↓
   Adicionar wikilinks para conceitos relacionados

6. INDEXAR
   ↓
   Atualizar MOC relevante

7. CONSOLIDAR
   ↓
   Marcar status: Consolidado
```

### Checklist de Validação

Antes de marcar como "Consolidado":

- [ ] Nome segue padrão `Categoria_Sub_Topico.md`
- [ ] Frontmatter completo
- [ ] Template preenchido (mínimo: Conceito + Pontos Chave + Conexões)
- [ ] Pelo menos 2 wikilinks para outros conceitos
- [ ] Adicionado ao MOC relevante
- [ ] Fonte original documentada
- [ ] Aplicação prática descrita

---

## ANTI-PADRÕES (EVITAR)

### Erro 1: Duplicação de Conteúdo

```text
❌ Errado:
01_CONHECIMENTO/IA/Prompts.md
03_APRENDIZADO/Curso_IA/notas/Prompts.md

✅ Correto:
03_APRENDIZADO/Curso_IA/notas/Aula_Prompts.md (contexto curso)
    ↓ (após consolidar)
01_CONHECIMENTO/IA_Prompts_Engineering.md (conhecimento permanente)
```

### Erro 2: Nota Sem Conexões

```text
❌ Errado:
Nota isolada, sem wikilinks, sem estar em MOC

✅ Correto:
Mínimo 2 wikilinks + listado em MOC relevante
```

### Erro 3: Conteúdo Não Processado

```text
❌ Errado:
Transcrição bruta de vídeo em 01_CONHECIMENTO/

✅ Correto:
Transcrição em 03_APRENDIZADO/ ou _inbox/
Depois processar e extrair conceitos para 01_CONHECIMENTO/
```

### Erro 4: Nome Genérico

```text
❌ Errado:
Notas.md
Ideias.md
Importante.md

✅ Correto:
IA_Claude_Prompt_Templates.md
DevPessoal_TDAH_Pomodoro_Adaptado.md
```

---

## CHECKLIST DE MANUTENÇÃO

### Semanal

- [ ] Processar notas de `_inbox/` para categorias corretas
- [ ] Revisar notas criadas na semana (conexões feitas?)
- [ ] Atualizar MOCs com novos links

### Mensal

- [ ] Consolidar notas relacionadas (fusão se necessário)
- [ ] Revisar notas "Em_Revisão" → marcar "Consolidado"
- [ ] Atualizar estatísticas nos MOCs
- [ ] Verificar nomenclatura (tudo correto?)

### Trimestral

- [ ] Avaliar criação de novos MOCs (se subcategoria cresceu muito)
- [ ] Revisar e atualizar conhecimento desatualizado
- [ ] Arquivar conhecimento obsoleto (mover para `00_SISTEMA/ARQUIVO/`)

---

## LINKS RELACIONADOS

- [[00_SISTEMA/PADROES/NOMENCLATURA.md|NOMENCLATURA]] - Padrões gerais de nomenclatura
- [[01_CONHECIMENTO/_MOC_Conhecimento.md|_MOC_Conhecimento]] - MOC master desta categoria
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md|PROTOCOLO_CRIACAO_ARQUIVOS]] - Protocolo geral
- [[04_RECURSOS/TEMPLATES/]] - Templates disponíveis

---

**Versão:** 1.1
**Criado:** 16/Jan/2026
**Movido:** 26/Jan/2026 (para 00_SISTEMA/PADROES/)
