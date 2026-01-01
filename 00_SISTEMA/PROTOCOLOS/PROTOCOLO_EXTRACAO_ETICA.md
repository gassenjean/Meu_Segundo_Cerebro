---
criado: 2025-12-30
tipo: Protocolo de Extração Ética
versao: 1.0
responsavel: Claude Code + Gemini/Antigravity
---

# PROTOCOLO DE EXTRAÇÃO ÉTICA - Anti-Plágio

**Objetivo:** Integrar conhecimento externo (mentelendaria.com) ao vault de forma ÉTICA: aprender e adaptar, NÃO copiar.

**Responsáveis:**
- Gemini/Antigravity: Pesquisa e extração
- Claude Code: Validação e integração

**Fonte:** https://mentelendaria.com (Segundo Cérebro Alan Nicolas)

---

## 🎯 PRINCÍPIO FUNDAMENTAL

**"Aprender, Não Copiar"**

- ✅ **Aprender:** Entender conceitos, princípios, lógica
- ✅ **Adaptar:** Aplicar ao contexto específico (DeFi, TDAH, KabaK)
- ✅ **Sintetizar:** Expressar em suas próprias palavras
- ✅ **Atribuir:** Citar fonte original sempre
- ❌ **Copiar:** Reproduzir textos, estruturas, exemplos

---

## 📋 WORKFLOW COMPLETO

### FASE 1: Planejamento (Claude Code)

**Responsável:** Claude Code

**Ação:**
1. Definir QUAIS conceitos extrair (priorização)
2. Criar lista de tópicos específicos
3. Definir objetivo de cada extração
4. Preparar contexto Gassen para adaptação

**Template:**
```markdown
## Requisição de Pesquisa - mentelendaria.com

**Data:** [data]
**Tópicos prioritários:**
1. [Conceito 1] - Aplicação: [DeFi/TDAH/Tráfego]
2. [Conceito 2] - Aplicação: [DeFi/TDAH/Tráfego]
3. [Conceito 3] - Aplicação: [DeFi/TDAH/Tráfego]

**Contexto para adaptação:**
- DeFi: [objetivo específico - ex: metodologia análise tokens]
- TDAH: [objetivo específico - ex: sistema anti-procrastinação]
- Tráfego: [objetivo específico - ex: frameworks copy KabaK]

**Critério sucesso:**
- Conceito aplicável imediatamente
- Adaptado ao contexto Gassen
- Conexões com vault existente identificadas
```

**Entrega:** Lista de tópicos → Gemini (via SESSION_LOG.md)

---

### FASE 2: Deep Research (Gemini/Antigravity)

**Responsável:** Gemini/Antigravity

**Ferramenta:** Deep Research (pesquisa autônoma iterativa)

**Processo:**

**2.1. Pesquisa Inicial**
```bash
gemini deep-research "Pesquise mentelendaria.com sobre: [tópicos]

Extraia:
1. Conceitos-chave (nomes + definições síntese)
2. Princípios fundamentais
3. Frameworks/metodologias
4. Casos práticos mencionados
5. Agentes/ferramentas relacionados

CRÍTICO:
- Sintetize em suas palavras (NÃO copie textos)
- Foco: ENTENDER lógica, não reproduzir conteúdo
- Máx 200 palavras por conceito"
```

**Gemini vai:**
- Navegar mentelendaria.com autonomamente
- Ler múltiplas páginas iterativamente
- Formular perguntas e investigar
- Gerar relatório síntese

**2.2. Auto-Validação (Gemini)**

Antes de continuar, Gemini DEVE verificar:

```markdown
Checklist Auto-Validação Fase 2:
□ Usei minhas próprias palavras (não cópia literal)
□ Compreendi a lógica/princípio (não só decorei)
□ Identifiquei URLs específicas (atribuição fonte)
□ Máx 200 palavras por conceito (síntese, não transcrição)

Se TODOS ✅ → Fase 3
Se QUALQUER ❌ → Refazer pesquisa
```

**Entrega:** Relatório síntese → Arquivo temporário

---

### FASE 3: Síntese e Adaptação (Gemini/Antigravity)

**Responsável:** Gemini/Antigravity

**Ação:** Transformar relatório bruto em arquivos estruturados

**Para cada conceito extraído:**

**3.1. Criar Arquivo Individual**

**Nomenclatura obrigatória:**
```
Alan_Nicolas_[Nome_Conceito].md

Exemplos:
✅ Alan_Nicolas_Sistema_5C.md
✅ Alan_Nicolas_Agente_Salesperson.md
✅ Alan_Nicolas_Framework_Copy_AIDA.md

❌ Sistema_5C.md (falta prefixo)
❌ Alan Nicolas Sistema 5C.md (espaços)
❌ sistema-5c-alan.md (formato errado)
```

**3.2. Seguir Template Obrigatório**

```markdown
# Alan_Nicolas_[Nome_Conceito]

## Fonte Original
- URL: https://mentelendaria.com/[página-específica]
- Autor: Alan Nicolas
- Data acesso: [DD/MM/YYYY]
- Seção: [qual parte do site - ex: "Academia/Frameworks"]

## Conceito Aprendido

[Síntese em suas próprias palavras - máx 200 palavras]

**Princípio central:** [1 frase resumo]

**Como funciona:** [explicação lógica - 2-3 parágrafos]

**Por que é importante:** [valor/benefício]

## Aplicação ao Contexto Gassen

### 🪙 DeFi (Lucas)
**Problema resolvido:** [qual problema específico]
**Como aplicar:** [passo a passo adaptado]
**Exemplo prático:** [cenário DeFi_Verso ou análise token]

### 🧠 TDAH (Coach/Elena)
**Problema resolvido:** [procrastinação, foco, etc]
**Como aplicar:** [passo a passo adaptado]
**Exemplo prático:** [cenário sessão Deep Work]

### 📈 Tráfego (Pedro)
**Problema resolvido:** [qual problema KabaK]
**Como aplicar:** [passo a passo adaptado]
**Exemplo prático:** [cenário campanha/criativo]

## Conexões Vault Existente

### Conceitos Relacionados
- [[Conceito_Vault_1]] - [como se conecta]
- [[Conceito_Vault_2]] - [como se conecta]
- [[Conceito_Vault_3]] - [como se conecta]

### Aplicações Cruzadas
- Usar com [[Skill_X]] para [resultado]
- Combinar com [[Framework_Y]] quando [situação]

## Diferenças da Fonte Original

**O que adaptei:**
- [Mudança 1: Original → Adaptado]
- [Mudança 2: Original → Adaptado]
- [Mudança 3: Original → Adaptado]

**Por que adaptei:**
- [Justificativa contextual]

## Implementação Prática

### Próximos Passos
- [ ] [Tarefa concreta 1 - prazo]
- [ ] [Tarefa concreta 2 - prazo]
- [ ] [Tarefa concreta 3 - prazo]

### Métricas de Sucesso
- [ ] [Como medir se funcionou]
- [ ] [Indicador de resultado]

### Recursos Necessários
- [Ferramenta/skill/arquivo necessário]

---

**Tags:** #alan-nicolas #mentelendaria #[categoria]

**Status:** 📥 Aguardando Validação Claude

---
*Inspirado em metodologia Alan Nicolas (mentelendaria.com)*
*Adaptado para contexto: DeFi + TDAH + Tráfego Pago*
*Este conteúdo é uma SÍNTESE ORIGINAL, não cópia do material fonte*
```

**3.3. Auto-Validação Fase 3 (Gemini)**

```markdown
Checklist Auto-Validação Fase 3:
□ Template completo preenchido
□ Nomenclatura correta (Alan_Nicolas_[Conceito].md)
□ Fonte específica citada (URL exata)
□ Texto é síntese original (não cópia)
□ 3 aplicações práticas criadas (DeFi/TDAH/Tráfego)
□ Conexões vault identificadas (mínimo 3)
□ Diferenças explicitadas (o que mudou)
□ Tarefas concretas definidas
□ < 60 caracteres nome arquivo
□ Sem espaços no nome

Se TODOS ✅ → Fase 4
Se QUALQUER ❌ → Corrigir antes de prosseguir
```

**Entrega:** Arquivos individuais → Pasta temporária (para revisão Claude)

---

### FASE 4: Validação Anti-Plágio (Claude Code)

**Responsável:** Claude Code

**Trigger:** Gemini atualiza SESSION_LOG.md com lista de arquivos criados

**Ação:** Validação rigorosa de cada arquivo

**4.1. Checklist Automático**

```markdown
Validação Claude Code:

NOMENCLATURA:
□ Prefixo "Alan_Nicolas_" presente
□ CamelCase após underscore
□ Sem espaços no nome
□ < 60 caracteres
□ Extensão .md

LOCALIZAÇÃO:
□ Arquivos em pasta correta (01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/)
□ Estrutura de pastas criada se necessário

ANTI-PLÁGIO:
□ Texto é síntese (comparar com amostra fonte se necessário)
□ Estrutura difere do original
□ Exemplos são adaptados (não copiados)
□ Tem voz própria (não parece transcrição)

ADAPTAÇÃO:
□ 3 aplicações ao contexto Gassen (DeFi/TDAH/Tráfego)
□ Aplicações são específicas (não genéricas)
□ Exemplos práticos concretos
□ Métricas de sucesso definidas

ATRIBUIÇÃO:
□ Fonte citada (URL específica)
□ Autor mencionado (Alan Nicolas)
□ Data acesso registrada
□ Rodapé de inspiração presente

INTEGRAÇÃO:
□ Mínimo 3 conexões vault existente
□ Wikilinks válidos [[arquivo_existente]]
□ Tarefas práticas definidas
□ Tags apropriadas

TEMPLATE:
□ Todas as seções obrigatórias presentes
□ Formatação markdown correta
□ Seção "Diferenças da Fonte Original" preenchida
```

**4.2. Decisão**

```markdown
Se TODOS ✅:
→ APROVADO
→ Mover para 01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/
→ Atualizar MOCs
→ Integrar ao vault
→ Informar Gemini: "Aprovado"

Se QUALQUER ❌:
→ REPROVADO
→ Gerar relatório específico de problemas
→ Retornar para Gemini via SESSION_LOG.md
→ Gemini corrige e reenvia
```

**4.3. Relatório de Validação**

Se reprovado, Claude gera:

```markdown
## Relatório Validação - [Nome_Arquivo]

**Status:** ❌ REPROVADO

**Problemas identificados:**

NOMENCLATURA:
- [Problema específico]

ANTI-PLÁGIO:
- [Trecho que parece cópia - linha X]
- [Estrutura muito similar - seção Y]

ADAPTAÇÃO:
- [Aplicação genérica - reescrever com exemplo concreto]
- [Falta contexto Gassen - adicionar]

INTEGRAÇÃO:
- [Wikilink inválido: [[arquivo_nao_existe]]]
- [Faltam conexões - mínimo 3]

**Ações corretivas:**
1. [Ação específica 1]
2. [Ação específica 2]
3. [Ação específica 3]

**Prazo:** Imediato (antes de próxima extração)
```

**Entrega:** Relatório → Gemini (SESSION_LOG.md) OU Aprovação → Integração

---

### FASE 5: Integração Vault (Claude Code)

**Responsável:** Claude Code (apenas se aprovado)

**Ação:** Adicionar ao vault seguindo padrões

**5.1. Criar Estrutura**

```bash
# Se não existir, criar:
mkdir -p 01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/
```

**5.2. Mover Arquivos Aprovados**

```bash
# Mover da pasta temporária para localização final
mv temp/Alan_Nicolas_*.md 01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/
```

**5.3. Criar/Atualizar MOC Específico**

```markdown
# Criar: 01_CONHECIMENTO/IA_Tecnologia/_MOC_Alan_Nicolas.md

# MOC - Alan Nicolas (Mente Lendária)

**Fonte:** https://mentelendaria.com
**Objetivo:** Integração ética de metodologias (aprender, não copiar)
**Última atualização:** [data]

---

## 📚 Conceitos Integrados

### Frameworks/Metodologias
- [[Alan_Nicolas_Sistema_5C]] - PKM workflow
- [[Alan_Nicolas_Framework_X]] - [descrição]

### Agentes Especializados
- [[Alan_Nicolas_Agente_Salesperson]] - Vendas/Copy
- [[Alan_Nicolas_Agente_Y]] - [descrição]

### Produtividade TDAH
- [[Alan_Nicolas_Conceito_Z]] - [descrição]

---

## 🔗 Aplicações

### DeFi (Lucas)
- [Conceito → Como usado em DeFi]

### TDAH (Coach/Elena)
- [Conceito → Como usado em produtividade]

### Tráfego (Pedro)
- [Conceito → Como usado em KabaK]

---

**Total conceitos:** [número]
**Status:** 🟢 Ativo
```

**5.4. Atualizar MOC Categoria**

```markdown
# Adicionar em: 01_CONHECIMENTO/_MOC_Conhecimento.md

## IA & Tecnologia
- [[_MOC_Alan_Nicolas]] - Metodologias Mente Lendária (integração ética)
```

**5.5. Atualizar STATUS_VAULT.md**

```markdown
# Adicionar seção:

## Integrações Externas

### Mente Lendária (Alan Nicolas)
- Fonte: https://mentelendaria.com
- Conceitos integrados: [número]
- Última atualização: [data]
- Status: 🟢 Ativo
- Protocolo: PROTOCOLO_EXTRACAO_ETICA.md
```

**5.6. Criar Wikilinks**

Para cada conceito integrado, adicionar wikilink em arquivos relacionados existentes.

Exemplo:
```markdown
# Em: 01_CONHECIMENTO/Desenvolvimento_Pessoal/Procrastinacao.md

Adicionar:
**Ver também:** [[Alan_Nicolas_Sistema_Anti_Procrastinacao]]
```

---

## 🚫 PROIBIÇÕES ABSOLUTAS

### O Que NUNCA Fazer

1. **❌ Copiar parágrafos inteiros**
   - Mesmo que pareça "útil"
   - Mesmo que seja "só um trecho pequeno"
   - SEMPRE sintetizar

2. **❌ Reproduzir estrutura exata de artigos**
   - Títulos devem ser diferentes
   - Ordem de seções deve ser adaptada
   - Exemplos devem ser novos

3. **❌ Usar mesmos exemplos sem adaptar**
   - Trocar nomes, números, contextos
   - Criar exemplos originais baseados no princípio

4. **❌ Omitir atribuição de fonte**
   - SEMPRE citar mentelendaria.com
   - SEMPRE incluir URL específica
   - SEMPRE mencionar Alan Nicolas

5. **❌ Integrar sem validação Claude**
   - Gemini NÃO integra diretamente ao vault
   - Claude SEMPRE valida primeiro
   - Sem exceções

---

## ✅ OBRIGAÇÕES ABSOLUTAS

### O Que SEMPRE Fazer

1. **✅ Sintetizar com suas próprias palavras**
   - Ler → Entender → Expressar de forma original
   - Máx 200 palavras por conceito
   - Voz própria (não transcrição)

2. **✅ Adaptar exemplos ao contexto Gassen**
   - DeFi: Tokens reais, DeFi_Verso
   - TDAH: Timeboxing 45min, Coach
   - Tráfego: KabaK, campanhas reais

3. **✅ Criar aplicações práticas originais**
   - Tarefas concretas
   - Métricas de sucesso
   - Exemplos específicos

4. **✅ Atribuir fonte claramente**
   - URL completa
   - Data de acesso
   - Rodapé de inspiração
   - Seção "Fonte Original"

5. **✅ Conectar com conhecimento existente vault**
   - Mínimo 3 wikilinks
   - Explicar conexões
   - Criar aplicações cruzadas

6. **✅ Explicitar diferenças do original**
   - Seção "Diferenças da Fonte Original"
   - O que mudou e por quê
   - Transparência total

---

## 📊 MÉTRICAS DE SUCESSO

### Como Medir Qualidade da Integração

**Originalidade:**
- [ ] Texto passa em detector de plágio (< 10% similaridade)
- [ ] Estrutura difere do original
- [ ] Exemplos são novos

**Utilidade:**
- [ ] Aplicável imediatamente (DeFi/TDAH/Tráfego)
- [ ] Tarefas concretas definidas
- [ ] Métricas de sucesso claras

**Integração:**
- [ ] Conectado a ≥3 arquivos existentes
- [ ] MOC atualizado
- [ ] Wikilinks válidos

**Ética:**
- [ ] Fonte atribuída
- [ ] Transparência sobre adaptações
- [ ] Síntese (não cópia)

---

## 🔄 CICLO ITERATIVO

```
Claude planeja
    ↓
Gemini pesquisa (Deep Research)
    ↓
Gemini sintetiza (Template)
    ↓
Gemini auto-valida (Checklist)
    ↓
Claude valida (Anti-plágio)
    ↓
    ├─→ APROVADO → Claude integra → FIM
    └─→ REPROVADO → Relatório → Gemini corrige → Volta validação
```

**Iterações esperadas:** 1-2 (Gemini aprende com feedback)

---

## 📝 TEMPLATE SESSION_LOG.MD

**Quando Gemini terminar extração:**

```markdown
## 🟢 Antigravity/Gemini - [DATA] ([HORA])

### Integração Mentelendaria.com - Fase Pesquisa

**Tópicos pesquisados:**
- [Tópico 1]
- [Tópico 2]
- [Tópico 3]

**Conceitos extraídos:**
- Sistema 5C (arquivo: Alan_Nicolas_Sistema_5C.md)
- Agente Salesperson (arquivo: Alan_Nicolas_Agente_Salesperson.md)
- Framework Copy AIDA (arquivo: Alan_Nicolas_Framework_Copy_AIDA.md)

**Arquivos criados:** 3
**Localização temporária:** temp/alan_nicolas/
**Status:** ⏳ Aguardando validação Claude

**Auto-Validação:**
✅ Sintetizado (não copiado)
✅ Adaptado ao contexto Gassen
✅ Fontes atribuídas
✅ Template seguido
✅ Nomenclatura correta

**Mensagem para Claude:**
> Claude, concluí a extração dos 3 conceitos prioritários de mentelendaria.com.
> Arquivos estão em `temp/alan_nicolas/` aguardando sua validação anti-plágio.
> Todos os checklists passaram. Pronto para integração se aprovado.
```

---

**Versão:** 1.0
**Criado:** 30/12/2025
**Atualizado:** 30/12/2025
**Status:** ✅ ATIVO

**Este protocolo é OBRIGATÓRIO para qualquer integração de conhecimento externo ao vault.**
