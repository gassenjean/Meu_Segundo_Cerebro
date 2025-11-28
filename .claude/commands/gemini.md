# Delegar para Gemini 3 Pro

Você vai coordenar uma tarefa para o **Gemini 3 Pro** - economizando tokens e aproveitando alto contexto.

## QUANDO USAR GEMINI 3 PRO

**Gemini 3 é MELHOR para** (gratuito, 1M tokens, 3x mais rápido):
- ✅ **Documentos longos** (livros, transcrições, bases de código COMPLETAS)
- ✅ **Processamento de conteúdo** (lives, cursos, podcasts → notas estruturadas)
- ✅ **Análise profunda com contexto total** (1M tokens vs 200k Claude)
- ✅ **Tarefas longas e repetitivas** (3x melhor que Claude segundo testes)
- ✅ **Multimodal avançado** (texto, imagem, vídeo, áudio)
- ✅ **Summarização de TUDO** (não trunca como outros modelos)
- ✅ **Tradução com contexto completo**
- ✅ **Extração de dados** (entende INTENÇÃO do usuário)
- ✅ **Geração de conteúdo em escala**
- ✅ **Refatoração de código** (uma única chamada)

**Claude Code é MELHOR para** (pago, vault-aware):
- ✅ **Planejamento estratégico** do vault
- ✅ **Código do vault** (conhece CLAUDE.md, protocolos, MOCs)
- ✅ **Decisões críticas** (estrutura, nomenclatura, localização)
- ✅ **Validação de padrões** (NOMENCLATURA.md, PROTOCOLO_CRIACAO_ARQUIVOS.md)
- ✅ **Integração com vault** (atualizar MOCs, STATUS_VAULT.md)

## COMO FUNCIONA

1. Você descreve a tarefa
2. Claude gera o comando Gemini CLI
3. Você executa no terminal
4. Claude valida/processa o resultado

## COMANDOS GEMINI CLI

```bash
# Básico
gemini "sua pergunta ou prompt aqui"

# Com arquivo
gemini "summarize this" < arquivo.txt

# Output para arquivo
gemini "translate to english" < input.md > output.md
```

## EXEMPLOS PRÁTICOS

### 1. Processar Live/Podcast Completa (NOVO - Alan Nicolas)
```bash
# Transcrição inteira → Nota estruturada (aproveitando 1M tokens)
gemini "Processar esta transcrição completa e criar nota estruturada com:
1. Resumo executivo
2. Conceitos principais (com explicações)
3. Aplicações práticas
4. Citações memoráveis
5. Links relacionados
6. Ações sugeridas

Formato: Markdown profissional" < live_completa.txt > Live_Processada.md
```

### 2. Análise de Livro Completo (NOVO)
```bash
# Livro inteiro → Insights acionáveis
gemini "Analisar este livro completo (não resumir, ANALISAR) e gerar:
1. Top 20 conceitos mais importantes
2. 10 aplicações práticas imediatas
3. 5 projetos para implementar
4. Roadmap de implementação em 90 dias
5. Connections com [seu nicho]" < livro_completo.txt > Analise_Livro.md
```

### 3. Geração de Conteúdo em Escala (NOVO - Comercial)
```bash
# Briefing → 30 dias de conteúdo
gemini "Com base neste briefing, gerar calendário mensal de conteúdo:
- 20 posts Instagram (caption + ideias visuais)
- 10 posts LinkedIn (profissionais)
- 4 newsletters (estrutura completa)
- 2 blog posts (outlines detalhados)

Tema: [seu tema]
Tom: [seu tom]
Público: [seu público]" < briefing.md > Calendario_Conteudo_30_Dias.md
```

### 4. Summarização (Alto Contexto)
```bash
# Documento longo → Resumo mantendo TODAS as nuances
gemini "Summarize entire document (don't truncate) in Portuguese with:
- Executive summary
- Key concepts (with context)
- Actionable insights" < artigo_longo.md > resumo.md
```

### 5. Tradução (Contexto Completo)
```bash
# Traduzir documento técnico mantendo contexto
gemini "Translate to Brazilian Portuguese:
- Maintain all technical terms
- Preserve formatting
- Keep markdown structure
- Adapt examples to BR context" < doc_en.md > doc_pt.md
```

### 6. Extração de Dados (Inteligente)
```bash
# Extrair e estruturar (entende intenção)
gemini "From this content, extract and structure:
- All concepts and definitions (as table)
- Action items (as checklist)
- References (as links)
- Timeline (if applicable)" < texto.md > dados_estruturados.md
```

### 7. Criação de Sistema 5C (NOVO - Alan Nicolas)
```bash
# Conteúdo → Sistema 5C completo
gemini "Processar este conteúdo aplicando Sistema 5C:
1. CAPTURAR: Extrair pontos-chave
2. CONECTAR: Identificar links com conceitos existentes
3. CRIAR: Gerar insights originais
4. COMPARTILHAR: Preparar formato para publicação

Include MOC suggestions and wikilink recommendations" < conteudo.md > Sistema_5C_Processado.md
```

### 8. Workflow Profissional (NOVO - 5 Etapas)
```bash
# Briefing completo → Plano de execução
gemini "Analisar este briefing e criar plano profissional:
1. Análise de requisitos
2. Arquitetura proposta
3. Task list detalhada
4. Ordem de implementação
5. Estimativa de complexidade
6. Desafios e soluções

Use metodologia profissional de 5 etapas" < briefing_projeto.md > plano_execucao.md
```

### 9. Refatoração de Código (Uma Chamada)
```bash
# Código complexo → Versão otimizada
gemini "Refactor this entire codebase:
- Improve performance
- Enhance readability
- Add comments (Portuguese)
- Suggest architectural improvements
- Identify potential bugs" < codigo_complexo.js > codigo_refatorado.js
```

### 10. Processamento de Base de Conhecimento
```bash
# Múltiplos arquivos → Mapa de conhecimento
cat arquivo1.md arquivo2.md arquivo3.md | gemini "Create comprehensive knowledge map:
- Main concepts and relationships
- MOC structure suggestion
- Wikilink network
- Missing connections
- Next learning steps"
```

## PROTOCOLO

✅ **SEMPRE**:
- Usar Gemini 3 para tarefas longas (aproveitar 1M tokens)
- Usar Gemini para processamento de conteúdo (lives, cursos, livros)
- Usar Gemini para geração de conteúdo em escala
- Validar output crítico com Claude Code
- Manter prompts claros e estruturados
- **NOVO:** Aproveitar contexto completo (não dividir documentos)

❌ **NUNCA**:
- Usar Gemini para mudanças estruturais no vault (use Claude)
- Confiar sem validação em decisões críticas
- Usar Gemini para atualizar MOCs/STATUS (Claude tem contexto)
- Dividir documentos que cabem em 1M tokens

---

## FERRAMENTAS GOOGLE INTEGRADAS (Alan Nicolas)

### Notebook LM (Aprendizado Acelerado)
**Acesso:** notebooklm.google

**Uso:**
1. Upload conteúdo (PDF, docs, transcrições)
2. Gerar podcast automaticamente
3. Criar flashcards para revisão
4. Gerar guias de estudo
5. Exportar para vault

**Ideal para:** Processar episódios Vida Lendária, cursos, livros

### Banana Nano Pro (Imagens com Texto)
**Acesso:** Via interface Gemini

**Uso:**
1. Prompt específico para imagem com texto
2. Gemini gera com Banana Pro automaticamente
3. Texto fica PERFEITO (diferencial crítico)

**Casos de uso:**
- Banners para redes sociais
- Mockups de produtos
- Certificados
- Flyers e convites
- Infográficos técnicos

### Google Skills (Certificações)
**Acesso:** skills.google

**Uso:**
- 35 créditos gratuitos
- Cursos gamificados
- Certificação oficial Google
- Focus em IA e ferramentas Google

### Antigravity IDE (Desenvolvimento)
**Acesso:** antigravity.google

**Diferencial:**
- Modo de planejamento (Shift+Tab)
- Task Inbox (múltiplos agentes paralelos)
- Browser sub-agent (controla navegador)
- Yolo Mode (execução sem interrupções)
- **GRATUITO** (por enquanto)

**Workflow profissional:**
1. Planejamento (Shift+Tab)
2. Revisão do plano
3. Aprovação
4. Execução automática (Yolo Mode)

---

## WORKFLOW BI-IA OTIMIZADO

### Fluxo 1: Processamento de Conteúdo Longo
```
1. Usuário: "Processar live do Alan sobre Gemini 3"
2. Claude: Gera comando Gemini otimizado
3. Gemini: Processa 100% da transcrição (1M tokens)
4. Output: Nota estruturada
5. Claude: Valida padrões, atualiza MOC, integra vault
```

### Fluxo 2: Criação de Conteúdo Comercial
```
1. Claude: Cria briefing detalhado
2. Gemini: Gera 30 dias de conteúdo
3. Claude: Valida qualidade e padrões
4. Usuário: Aprova e usa
```

### Fluxo 3: Sistema 5C Automatizado
```
1. CONSUMIR: Usuário fornece fonte
2. CAPTURAR: Gemini processa e estrutura
3. CONECTAR: Gemini identifica conexões + Claude valida MOCs
4. CRIAR: Gemini gera insights
5. COMPARTILHAR: Claude formata para publicação
```

---

## ECONOMIA DE CUSTOS (Importante!)

| Tarefa | Claude Code | Gemini 3 Pro | Economia |
|--------|-------------|--------------|----------|
| Resumir live 2h | $2.50 | $0.00 | 100% |
| Traduzir livro | $5.00 | $0.00 | 100% |
| Gerar 30 posts | $3.00 | $0.00 | 100% |
| Processar curso | $10.00 | $0.00 | 100% |
| Refatorar código | $1.50 | $0.00 | 100% |

**Total mensal estimado:** $200-500 → $0 (Gemini 3)

**Use Claude apenas para:** Planejamento, decisões críticas, código vault

---

## SUAS AÇÕES AGORA

1. Descreva a tarefa que quer delegar
2. Claude vai gerar o comando Gemini 3 otimizado
3. Execute o comando no terminal
4. Retorne o resultado para Claude validar (se necessário)

**Exemplos de solicitação:**
- "Processar live completa do Alan sobre [tema]"
- "Gerar 30 dias de conteúdo sobre [tema]"
- "Analisar livro completo [nome] e extrair insights"
- "Criar plano profissional baseado neste briefing"
- "Refatorar esta base de código"

**Qual tarefa você quer delegar para o Gemini 3 Pro?**
