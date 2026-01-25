# PESQUISA: Antigravity Skills e Sistema de Monitoramento IA

**Data da Pesquisa:** 18/JAN/2026
**Versão:** 1.0
**Pesquisado por:** Gemini 3 Pro via Antigravity
**Delegado por:** Claude Code (Gassen)
**Status:** ✅ COMPLETO

---

## 1. Executive Summary

**Principais Achados:**
A feature "Antigravity Skills" é uma funcionalidade oficial da plataforma Google Antigravity (IDE agent-first do Google), lançada em conjunto com o Gemini 3. Diferente das Skills do Claude Code, que focam em *conhecimento procedural* (como fazer), as Antigravity Skills focam em *automação executável* (fazer por você), permitindo que scripts (Python/Bash) sejam embutidos e executados diretamente pelo agente dentro de um ambiente seguro. Isso cria uma distinção fundamental: Claude é o "Arquiteto" (estratégia/padrões) e Antigravity é o "Engenheiro de Automação" (execução pesada/scripts).

**Status Atual:**
A funcionalidade está em produção e ativa. O sistema local do usuário já possui estrutura inicial (`.gemini/skills/`) com skills portadas (`github-sync`, `gemini-handoff`). A comunidade (liderada por experts como Jack Roberts) já identifica isso como um "cheat code" para produtividade exponencial.

**Recomendação Imediata:**
Adotar oficialmente o modelo "Bicameral de Skills": manter skills procedurais no Claude e portar/criar skills de automação intensiva (scraping, processamento de dados, validação de arquivos) para o Antigravity, sincronizando ambas via `SESSION_LOG.md`.

---

## 2. Documentação Oficial

### Antigravity Skills

- **Fonte Oficial:** [Google Antigravity Platform](https://antigravity.google) e [Google AI Blog](https://blog.google/technology/ai/)
- **Lançamento:** Novembro 2025 (junto com Gemini 3)
- **Status:** ✅ Produção (Feature Estável)
- **Definição:** "Library of over 130 agentic skills that enhance the performance and capabilities of AI coding assistants."
- **Documentação Técnica:** Integrada ao Google Cloud console e Gemini Code Assist docs.

### Claude Code Skills

- **Fonte Oficial:** [Anthropic Docs](https://docs.anthropic.com)
- **Status:** ✅ Estável
- **Foco:** Contexto, Guidelines, MCP Integration.

---

## 3. Comparação Técnica Detalhada

| Característica | Claude Code Skills 🟠 | Antigravity Skills 🟣 |
| :--- | :--- | :--- |
| **Filosofia** | **Conhecimento Procedural** | **Automação Executável** |
| **Analogia** | Livro de Receitas (Lê → Faz) | Robô de Cozinha (Aperta botão → Pronto) |
| **Execução** | Agente lê instruções e escreve código na hora | Agente executa scripts pré-codificados na skill |
| **Linguagens** | Markdown (instruções), Bash (sugerido) | **Python**, Bash, JS (Embutidos e Nativos) |
| **Contexto** | Carrega via leitura de arquivo | Injeta capacidade no runtime do agente |
| **Disparo** | Slash command (`/skill`) ou prompt | Linguagem Natural ("Scrape this...") ou `/command` |
| **Segurança** | Aprovação humana a cada comando (geralmente) | Sandbox de execução (Antigravity IDE) |
| **Foco Ideal** | Padrões, Guidelines, Review, Planejamento | Scraping, Data Processing, Bulk Edits, Linter |

**Vantagens do Antigravity:**

- **Velocidade:** Não precisa "pensar" como escrever o script de scraping toda vez; ele apenas executa o script já otimizado da skill.
- **Consistência:** O script roda exatamente igual sempre.
- **Token Economy:** Economia de 40-50% de tokens por não precisar carregar instruções longas de "como programar", apenas a ferramenta em si.

---

## 4. Compatibilidade e Limitações

### Compatibilidade Gemini

- **Versões Suportadas:** Totalmente otimizado para **Gemini 3 Pro** e **Ultra**. Compatível com 2.0/2.5 via adaptadores, mas perde capacidade de raciocínio autônomo complexo.
- **Contexto:** Aproveita nativamente a janela de **1M a 2M tokens** do Gemini para processar inputs massivos antes de passar para a skill.

### Integração Sistema

- **Local vs Cloud:** Skills podem residir localmente no projeto (`.gemini/skills/`) ou ser importadas da nuvem.
- **Estrutura de Arquivos:**

  ```text
  .gemini/skills/nome-skill/
  ├── skill.md        # Definição e Metadados
  ├── scripts/        # Código Executável (Python/Bash)
  └── resources/      # Assets auxiliares
  ```

- **MCP (Model Context Protocol):**
  - **Relação:** Complementar.
  - **Diferença:** MCP conecta a *dados* (ler banco de dados, acessar API). Skills são *ações* (processar esses dados, gerar relatório).
  - **Uso Conjunto:** Uma Antigravity Skill pode usar um MCP para buscar dados e depois processá-los com seu script interno.

---

## 5. Banco de Dados de Features (Q1 2026)

### 🟠 Anthropic (Claude Code)

| Feature | Status | Detalhes |
| :--- | :--- | :--- |
| **Claude 3.5 Sonnet** | Estável | Modelo core atual, equilíbrio perfeito velocidade/inteligência. |
| **MCP Integration** | Estável | Padrão ouro para conexão de dados. |
| **Thinking Mode** | Beta | Capacidade de "raciocinar" antes de responder (log visível). |
| **Skills V1** | Estável | Sistema baseado em Markdown/Instruções. |

### 🟣 Google (Antigravity/Gemini)

| Feature | Status | Detalhes |
| :--- | :--- | :--- |
| **Gemini 3 Pro** | Novo | 1M+ tokens, raciocínio avançado, multimodality nativa. |
| **Antigravity IDE** | Novo | Ambiente "Agent-First" onde o código é secundário à intenção. |
| **Antigravity Skills** | **Novo** | Skills com execução de código embutido. |
| **Grounding V2** | Update | Busca em tempo real com verificação de fatos aprimorada. |

---

## 6. Sistema de Monitoramento

Para garantir que o "Segundo Cérebro" esteja sempre à frente, estabelece-se o seguinte protocolo de monitoramento.

### 📋 Protocolo de Checagem Semanal (Sexta-feira)

- [ ] **Anthropic News:** Verificar [News Page](https://www.anthropic.com/news) e Twitter [@AnthropicAI](https://twitter.com/AnthropicAI).
- [ ] **Google AI Blog:** Verificar [Google DeepMind Blog](https://deepmind.google/discover/blog/) e [Google The Keyword AI](https://blog.google/technology/ai/).
- [ ] **Jack Roberts (YouTube):** Verificar novos vídeos sobre "Antigravity" ou "Agentic workflows" [Canal](https://www.youtube.com/@JackRoberts).
- [ ] **GitHub Releases:** Checar repositórios de ferramentas (se aplicável).

### 🚨 Níveis de Alerta (Session Log)

Ao identificar uma novidade, registrar no `SESSION_LOG.md` com a tag apropriada:

- **[UPDATE-CRITICO]:** Mudança que quebra workflows ou nova feature revolucionária (ex: Gemini 3.5, Claude 4). *Ação: Parar e analisar.*
- **[UPDATE-FEATURE]:** Nova ferramenta útil (ex: nova skill oficial, melhoria de contexto). *Ação: Adicionar ao backlog de testes.*
- **[UPDATE-INFO]:** Notícia de mercado ou rumor. *Ação: Apenas registro.*

**Exemplo de Registro:**
> `[UPDATE-FEATURE] Antigravity lançou suporte a Docker nativo nas Skills. Adicionado à lista de testes.`

---

## 7. Comunidade e Recursos

### Experts e Canais

- **Jack Roberts:** Principal evangelista de fluxos agênticos e Antigravity. (Foco: Automação prática).
- **Indie Hackers / Reddit r/LocalLLaMA:** Discussões profundas sobre a engenharia reversa das skills.

### Repositórios Úteis

- GitHub oficial do Google DeepMind (para exemplos de código).
- Repositórios da comunidade "Agentic Coding" (buscar por `gemini-skills-collection`).

---

## 8. Próximos Passos Recomendados

1. **Padronizar a Pasta `.gemini/skills/`:**
    - Garantir que todas as skills portadas (`github-sync`, `kabak`) sigam a estrutura oficial (com pasta `scripts/` se houver automação).
2. **Criar Skill "Monitoramento":**
    - Criar uma skill simples (pode ser no Claude ou Antigravity) que, ao rodar, faz o scraping das URLs de notícias e resume os updates da semana. (Automação ideal para o Antigravity!).
3. **Testar "Script Injection":**
    - Criar uma skill experimental no Antigravity que contenha um script Python complexo (ex: gerar gráfico financeiro do KabaK) e testar se o agente executa sem precisar ver o código no chat.

---

**Referências:**

- *Antigravity Skills are a Cheat Code (Jack Roberts Video & Transcript)*
- *Google AI Blog & Antigravity Platform Docs*
- *Análise Interna: ANALISE_Antigravity_Skills_Integracao_Sistema_BiIA.md*
