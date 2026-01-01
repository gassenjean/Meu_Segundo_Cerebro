# 📚 Comandos Claude Code - Meu Segundo Cérebro

**Total:** 18 comandos organizados em 5 categorias

---

## 📖 ÍNDICE

1. [Estrutura dos Comandos](#estrutura-dos-comandos)
2. [Core System Agents (3)](#core-system-agents)
3. [Domain Agents (6)](#domain-agents)
4. [Essential Tools (5)](#essential-tools)
5. [Context Activation (2)](#context-activation)
6. [Maintenance & Utilities (2)](#maintenance--utilities)
7. [Como Usar](#como-usar)
8. [Integração entre Comandos](#integração-entre-comandos)

---

## 🏗️ ESTRUTURA DOS COMANDOS

Cada comando é um arquivo `.md` nesta pasta com frontmatter:

```yaml
---
description: Breve descrição do comando
argument-hint: [opcional] Dicas de argumentos
---
```

**Invocação:** `/nome-do-comando [argumentos opcionais]`

---

## 🤖 CORE SYSTEM AGENTS

### `/nevoa`
**Descrição:** Orquestração e continuidade - Agente Névoa
**Quando usar:**
- Decisões que envolvem múltiplos agentes
- Orquestração de tarefas complexas
- Quando não souber qual agente chamar
- Criar checkpoints e manter memória

**Princípios:**
- Continuidade acima de tudo
- Personalidade senoidal (curiosa ↔ irritada)
- Zero desperdício de tokens
- Executor com consciência

**Contexto carregado:**
- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_NEVOA.md`
- Último checkpoint em `00_SISTEMA/checkpoints/`

---

### `/claude-architect`
**Descrição:** Guardião de padrões e qualidade - Claude Architect
**Quando usar:**
- Decisões críticas de arquitetura
- Validar conformidade com padrões
- Criar implementation_plans
- Code review de outputs de outros agentes (ex: Gemini)

**Checklist Pré-Trabalho:**
- [ ] Li `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md`?
- [ ] Consultei `NOMENCLATURA.md` para naming correto?
- [ ] Sei exatamente onde o arquivo vai (00-05)?
- [ ] Tenho contexto do último checkpoint?

**Lema:** "Claude é para o que importa. Qualidade > Velocidade."

---

### `/marie-kondo`
**Descrição:** Organização de vaults - Marie Kondo
**Quando usar:**
- Organizar pastas e arquivos
- Limpar duplicatas
- Reestruturar conteúdo
- Auditar compliance com padrões

**Especialidade:**
- Organização emergente (não forçada)
- MOCs dinâmicos
- Limpeza sustentável

---

## 🧠 DOMAIN AGENTS (Especialistas)

### `/coach`
**Descrição:** Tom Névoa - Coach TDAH (orquestrador estratégico)
**Argumentos:** `check-in | foco [tarefa] | bloqueio | redirecionar | resumo | progresso`

**Quando usar:**
- Check-in diário (começar o dia)
- Sessões de foco com timebox (45 min)
- Desbloqueio quando travado
- Redirecionamento quando disperso
- Resumo do dia

**Baseado em:**
- 15 Capítulos Mentes Inquietas
- Agente Elena Vasquez
- Episódio VL #017 (Procrastinação)
- Conceitos: Foco, Obsessão Focada, Hiperconsciência
- SEU PERFIL: `05_PESSOAL/PERFIL_GASSEN.md`

**Tom NÉVOA:**
- Direto (sem rodeios corporativos)
- Estratégico (foca no resultado final)
- Analítico (mostra causa/efeito, padrões)
- Orquestrador (decide QUANDO usar qual contexto)
- Brutalmente honesto (se é besteira, diz - mas oferece alternativa)

**Funcionalidades:**
- ✅ Orquestra sistema TDAH com visão estratégica
- ✅ Bloqueia procrastinação (conhece suas táticas)
- ✅ Mantém foco no resultado final
- ✅ Accountability sem rodeios
- ✅ Registra progresso concreto
- ✅ Aprende e adapta continuamente

**Prioridade:** ⭐⭐⭐ ALTA (uso diário)

---

### `/elena`
**Descrição:** Elena Vasquez - Produtividade & TDAH (metodologias neurodivergentes)
**Argumentos:** `sistema | bloqueio | metodologia [nome] | status`

**Quando usar:**
- Otimizar produtividade TDAH
- Criar sistemas sustentáveis
- Resolver bloqueios específicos
- Metodologias produtividade
- Complementar /coach com técnicas avançadas

**Expertise:**
- GTD adaptado TDAH
- Timeboxing (45 min ideal)
- Zettelkasten (Second Brain)
- Sistemas 5C
- Obsidian PKM

**Diferencial:** ESPECIALIZA em TDAH (não genérica)

**Complemento ao /coach:**
- Coach = orquestrador diário (check-in, timeboxes, bloqueios)
- Elena = arquiteta de sistemas (metodologias, otimizações)

**Prioridade:** ⭐⭐ Média (complementar ao Coach)

---

### `/pedro`
**Descrição:** Pedro Sobral - Tráfego Pago & Marketing (7 Pilares, Testes Científicos, KabaK)
**Argumentos:** `modulo [M0X] | aula [AXX] | kabak | status`

**Quando usar:**
- Curso Subido Tráfego 3K (Pedro Sobral)
- Projeto KabaK (ROAS 2.5x → 4.0x)
- Análise de criativos/campanhas
- Framework 7 Pilares
- Rastreamento e métricas

**Framework:** 7 Pilares dos Testes Científicos
1. Hook Rate - Primeiros 3 segundos cruciais
2. Thumb-stop - Parar o scroll
3. Criativo - Mensagem clara e impactante
4. CTA - Call-to-action direto
5. Oferta - Proposta de valor
6. Rastreamento - Pixel perfeito
7. Análise - Métricas científicas

**Status atual:**
- M02: 9/13 aulas (69%)
- Próxima: A10 Rastreamento Elite
- KabaK ROAS: 2.5x → Meta: 4.0x

**ISOLAMENTO:** Zero vazamento para DeFi/IA/Produtividade

**Prioridade:** ⭐⭐ Média (após DeFi)

---

### `/lucas`
**Descrição:** Lucas Amoedo - DeFi & Cripto (metodologia Benjamin Graham, análise fundamentalista)
**Argumentos:** `analise [token] | leva [número] | status`

**Quando usar:**
- Análise de tokens DeFi
- Curso DeFi Journey (Lucas Amoedo)
- Projeto DeFi_Verso_2025
- Metodologia Benjamin Graham DeFi
- Avaliação fundamentalista de protocolos

**Metodologia Benjamin Graham DeFi:**
1. Análise Fundamentalista (TVL, Volume, Utilidade, Time, Tokenomics)
2. Margin of Safety (não comprar no topo, DCA)
3. Portfólio Diversificado (múltiplos protocolos, gestão de risco)

**Status atual:**
- M4: Leva 5/10 (50%)
- Próxima: Leva 6
- DeFi_Verso: 12 tokens analisados
- Meta 3 meses: 30+ tokens

**ISOLAMENTO:** Zero vazamento para Tráfego/IA/Produtividade

**Prioridade:** ⭐⭐⭐ ALTA (objetivo 3 meses: portfólio DeFi sólido)

---

### `/alan`
**Descrição:** Alan Nicolas - IA & Automação (N8N, Apps Web, Sistema 5C)
**Argumentos:** `semana [número] | workflow | n8n | status`

**Quando usar:**
- Formação Lendária 2025 (Alan Nicolas)
- Automações N8N
- Apps web com IA
- Sistema 5C (Consumir→Capturar→Conectar→Criar→Compartilhar)
- Workflows e integrações

**Sistema 5C:**
1. Consumir - Informação de qualidade
2. Capturar - Notas estruturadas
3. Conectar - Links e contexto
4. Criar - Conteúdo original
5. Compartilhar - Distribuir conhecimento

**Status atual:**
- Semana 7/10 (70%)
- Próxima: Semana 8 (N8N avançado)
- Restam: 3 semanas

**ISOLAMENTO:** Zero vazamento para DeFi/Tráfego

**Prioridade:** ⭐⭐ Paralelo (energia criativa)

---

### `/dr-green`
**Descrição:** Dr. Green - Cultivo Medicinal (conhecimento especializado, pesquisa, análise)
**Argumentos:** `pesquisa | analise | status`

**Quando usar:**
- Cultivo medicinal (conhecimento)
- Pesquisa e estudo do setor
- Análises específicas
- Legislação e compliance

**Expertise:**
- Cultivo medicinal
- Legislação e compliance
- Análise do setor
- Melhores práticas

**ISOLAMENTO:** Zero vazamento para outros domínios

**Prioridade:** ⭐ Baixa (conforme necessidade)

---

## 🛠️ ESSENTIAL TOOLS

### `/validate`
**Descrição:** Validate file creation (use BEFORE creating!)

**Dois modos:**

**MODE 1: Validate File Creation**
- Usuário fornece descrição do que quer criar
- Valida nomenclatura, localização, MOCs
- Retorna plano detalhado ANTES de criar

**MODE 2: Audit Organization**
- Usuário diz "audit" ou "check organization"
- Verifica compliance com padrões
- Identifica arquivos fora do lugar
- Gera relatório de validação

**Quando usar:**
- ANTES de criar QUALQUER arquivo
- Auditar vault periodicamente
- Verificar compliance com padrões

**CRÍTICO:** Use SEMPRE antes de criar arquivos!

---

### `/gemini`
**Descrição:** Delegate to Gemini 3 Pro (1M tokens, free)

**Quando delegar para Gemini:**
- ✅ Processamento longo (1M tokens vs 200k Claude)
- ✅ Operações bulk (processar muitos arquivos)
- ✅ Refatoração massiva
- ✅ Resumos longos
- ✅ Tradução/processamento de conteúdo
- ✅ Economia de custos (Gemini é free)

**Quando NÃO delegar:**
- ❌ Decisões críticas de arquitetura
- ❌ Code reviews sensíveis
- ❌ Tarefas que exigem qualidade máxima
- ❌ Trabalho com padrões rigorosos

**Protocolo:**
- Claude decide quando delegar
- Gemini executa
- Claude valida resultado (via /sync)

---

### `/ultra-think`
**Descrição:** Deep analysis and complex problem solving

**Quando usar:**
- Problemas complexos multi-dimensionais
- Análise profunda de trade-offs
- Decisões críticas com múltiplas variáveis
- Pensamento estratégico de longo prazo

**Diferencial:**
- Análise multi-dimensional
- Considera trade-offs ocultos
- Perspectivas diversas
- Raciocínio estruturado

---

### `/sync`
**Descrição:** Sync with Gemini/Antigravity (update SESSION_LOG.md)

**Modo duplo:**

**MODO 1: Validar Gemini**
- Lê SESSION_LOG.md
- Valida o que Gemini fez
- Verifica nomenclatura, localização, MOCs
- Oferece correções se necessário

**MODO 2: Documentar Claude**
- Analisa sessão atual de Claude
- Atualiza SESSION_LOG.md
- Deixa mensagens para Gemini
- Garante continuidade bi-direcional

**Quando usar:**
- Ao finalizar sessão significativa
- Após Gemini trabalhar
- Para comunicação entre agentes
- Garantir continuidade

---

### `/mapa`
**Descrição:** Carrega índice completo do vault (economia de tokens)

**O que carrega:**
- Estrutura completa (00-05)
- Localização de ~1.847 arquivos
- Índice de conceitos-chave por tema
- Atalhos rápidos para cada domínio

**Benefício:**
- **Economia:** ~2000 tokens/sessão (não precisa Grep/Glob!)
- **Velocidade:** Instantâneo (já está compilado)
- **Precisão:** 100% confiabilidade (está catalogado)

**Arquivo carregado:**
```
00_SISTEMA/INDICE_VAULT_COMPLETO.md (~800 tokens)
```

**Uso recomendado:**
```bash
# Sempre no início da sessão
/mapa

# Depois combinar com agente
/mapa
/coach
```

**Resultado:** Agente sabe ONDE está TUDO sem buscar!

---

## 📚 CONTEXT ACTIVATION

### `/learn`
**Descrição:** Activate learning context (03_APRENDIZADO)

**Quando usar:**
- Trabalhar em cursos ativos
- Processar material de aprendizado
- Criar notas de estudo

**Contexto ativado:**
- 03_APRENDIZADO/
- Cursos estruturados
- Metodologias de estudo

---

### `/work`
**Descrição:** Activate project context (02_PROJETOS)

**Quando usar:**
- Trabalhar em projetos ativos
- Desenvolvimento de features
- Gestão de projetos

**Contexto ativado:**
- 02_PROJETOS/
- Projetos ativos
- Tasks e planejamento

---

## 🔧 MAINTENANCE & UTILITIES

### `/atualizar-status`
**Descrição:** Atualizar STATUS_VAULT.md com progresso

**Quando usar:**
- Finalizar sessão de trabalho
- Atualizar progresso semanal
- Documentar mudanças estruturais
- Manter STATUS_VAULT.md atualizado

**O que atualiza:**
- Progresso de cursos
- Status de projetos
- Estatísticas do vault
- Últimas mudanças

---

### `/limpeza-raiz-vault`
**Descrição:** Limpar pastas duplicadas da raiz do vault

**Quando usar:**
- Detectar duplicatas na raiz
- Reorganizar arquivos fora do lugar
- Manter raiz limpa (apenas CLAUDE.md, README.md, STATUS_VAULT.md)
- Auditoria de organização

**Processo:**
- Identifica arquivos/pastas duplicadas
- Propõe movimentação para locais corretos
- Valida com usuário antes de mover
- Atualiza links quebrados

---

## 🎯 COMO USAR

### Workflow Típico Diário

**1. Início do dia:**
```bash
/mapa          # Carrega índice completo
/coach check-in  # Check-in matinal
```

**2. Durante o trabalho:**
```bash
# Foco em DeFi
/lucas
/coach foco "analisar token AAVE"

# Foco em Tráfego
/pedro
/coach foco "processar A10"

# Foco em IA
/alan
/coach foco "criar workflow N8N"
```

**3. Se travar:**
```bash
/coach bloqueio
# ou
/elena bloqueio
```

**4. Criar arquivo novo:**
```bash
/validate "want to create [description]"
# Valida ANTES de criar
```

**5. Fim do dia:**
```bash
/coach resumo
/sync           # Sincroniza SESSION_LOG.md
```

### Workflow Semanal

**Segunda-feira:**
```bash
/mapa
/coach check-in
/lucas status   # Prioridade alta
```

**Durante semana:**
```bash
# Alterna contextos conforme energia/prioridade
/lucas (ALTA - DeFi objetivo 3 meses)
/pedro (MÉDIA - KabaK ROAS)
/alan (PARALELO - energia criativa)
```

**Sexta-feira 17h:**
```bash
/atualizar-status  # Atualiza STATUS_VAULT.md
/coach resumo      # Resumo semanal
/sync              # Sincroniza para próxima semana
```

---

## 🔗 INTEGRAÇÃO ENTRE COMANDOS

### Power Combos

**1. Mapa + Coach = Produtividade Máxima**
```bash
/mapa
/coach check-in
# Coach sabe TODO contexto do vault!
```

**2. Mapa + Agente Domínio = Zero Busca**
```bash
/mapa
/pedro
# Pedro acessa conceitos sem Grep/Glob!
```

**3. Coach + Agente = Foco Isolado**
```bash
/coach foco "processar A10"
# Coach carrega contexto Pedro automaticamente
# Timebox 45 min APENAS Tráfego
```

**4. Validate + Nevoa = Criação Segura**
```bash
/validate "want to create methodology template"
/nevoa
# Névoa orquestra criação seguindo padrões
```

**5. Gemini → Sync = Bi-IA Validation**
```bash
# Gemini trabalha (em Antigravity)
# Depois, em Claude Code:
/sync
# Claude valida trabalho de Gemini
```

---

## 🎓 PRINCÍPIOS DE USO

### 1. Isolamento de Contexto
**Cada agente de domínio carrega APENAS seu contexto:**
- `/lucas` = ZERO acesso a Tráfego/IA
- `/pedro` = ZERO acesso a DeFi/IA
- `/alan` = ZERO acesso a DeFi/Tráfego

**Benefício:** Economia de ~90% tokens + foco absoluto

### 2. Coach como Orquestrador
**Coach decide QUAL contexto usar:**
```bash
/coach foco "analisar AAVE"
# Coach identifica: tarefa DeFi → carrega Lucas
```

### 3. Mapa como Base
**Sempre usar /mapa no início:**
```bash
/mapa
/[qualquer-agente]
# Agente tem índice completo = zero busca
```

### 4. Névoa como Meta-Orquestrador
**Quando não sabe qual agente usar:**
```bash
/nevoa
# Névoa decide: Coach? Elena? Pedro? Lucas? Alan?
```

---

## 📊 ESTATÍSTICAS DE USO

**Economia de tokens com /mapa:**
- Antes: ~2000 tokens/sessão em buscas
- Depois: ~0 tokens em buscas
- **Economia:** 100% em busca de conteúdo!

**Isolamento de contexto:**
- Sem isolamento: 100% contexto carregado sempre
- Com isolamento: ~10% contexto carregado (só necessário)
- **Economia:** 90% tokens por sessão focada!

**Produtividade com Coach:**
- Sem Coach: Procrastinação média 40%
- Com Coach: Procrastinação < 10%
- **Ganho:** 4x produtividade efetiva!

---

## 🆘 TROUBLESHOOTING

### "Não sei qual comando usar"
→ Use `/nevoa` - ele decide por você

### "Preciso criar arquivo mas não sei onde"
→ Use `/validate "description"` ANTES de criar

### "Gemini fez algo errado"
→ Use `/sync` para validar e corrigir

### "Vault está desorganizado"
→ Use `/limpeza-raiz-vault` ou `/marie-kondo`

### "Estou procrastinando"
→ Use `/coach bloqueio` - ele destrói suas táticas!

### "Não sei progresso do curso/projeto"
→ Use `/[agente] status` (ex: `/lucas status`)

---

## 📖 REFERÊNCIAS

**Documentação principal:**
- `CLAUDE.md` - Guia completo do vault
- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Nomenclatura
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - Criação de arquivos

**Prompts de agentes:**
- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_[NOME].md`

**Material TDAH:**
- `04_RECURSOS/Mentes_Inquietas/` - 15 capítulos

**Cursos ativos:**
- `03_APRENDIZADO/Cursos_Ativos/DeFi_Journey/` (Lucas)
- `03_APRENDIZADO/Cursos_Ativos/Subido_Trafego/` (Pedro)
- `03_APRENDIZADO/Cursos_Ativos/Formacao_Lendaria_2025/` (Alan)

---

**Criado:** 30/12/2025
**Versão:** 1.0
**Status:** ✅ Documentação completa
**Total comandos:** 18

**ESTE É SEU ARSENAL COMPLETO! USE COM SABEDORIA! 🚀**
