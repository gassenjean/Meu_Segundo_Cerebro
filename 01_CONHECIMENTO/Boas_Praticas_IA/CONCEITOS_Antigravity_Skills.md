---
created: 2026-01-25T12:27
updated: 2026-01-25T12:27
---
# CONCEITOS: Antigravity Skills (Jack Roberts)

**Fonte:** Jack Roberts - Antigravity_Skills_are_a_Cheat_Code__NEW_System_ (1).pdf
**Categoria:** Framework / Ferramenta
**Tags:** #antigravity #gemini #skills #automação #tokens

---

## 1. Skill vs MCP

### O Que É

Uma distinção fundamental na arquitetura do Gemini. Enquanto **MCP (Model Context Protocol)** é sobre **dados** (intercâmbio, gathering, conexão com bancos de dados, Slack, Sentry), as **Skills** são **paquetes reutilizáveis de conhecimento, código e instruções** para execução.

### Por Que Importa

Evita a confusão comum de tentar substituir um pelo outro. Eles são complementares, não substitutos. "Dizer 'não use MCP, use habilidades' é como dizer 'não coma comida, beba água'".

### Como Aplicar

1. Use **MCP** quando precisar buscar dados externos ou conectar com sistemas (o "ingrediente").
2. Use **Skills** quando precisar de um processo repetível de raciocínio e execução (a "receita").

### Aplicação no Bi-IA

No nosso sistema, o `MCP Server` (como o do Claude ou do sistema de arquivos) fornece a matéria-prima. As Skills (como as que você, Gemini, executa) são os agentes que processam essa matéria-prima.

---

## 2. Analogia do Chef (Conhecimento vs Automação)

### O Que É

Uma analogia para diferenciar Claude Code de Antigravity (Gemini).

- **Claude Code = Chef de Classe Mundial:** Tem uma biblioteca de livros de receitas (conhecimento). Ele lê a receita e executa as ações em si mesmo.
- **Antigravity = IDE de Automação:** É mais focado em automação repetível. Ele pode raciocinar e depois executar scripts gerados dinamicamente.

### Por Que Importa

Define o papel de cada agente. O Claude é excelente para tasks one-off complexas que exigem raciocínio criativo ("cozinhar um prato novo"). O Antigravity é superior para processos repetitivos e escaláveis ("linha de produção").

### Como Aplicar

1. Delegar ao Claude tarefas que exigem alto julgamento e contexto variável.
2. Delegar ao Gemini (Antigravity) tarefas que podem ser encapsuladas em skills repetíveis e scripts (ex: scrapers, formatação, extração massiva).

---

## 3. Skill Creator (A Meta-Habilidade)

### O Que É

A primeira e mais importante habilidade a ser criada: uma habilidade projetada especificamente para criar outras habilidades. É um "Skill Master" que garante consistência na arquitetura de novas skills.

### Por Que Importa

Garante padronização. Em vez de criar skills do zero com formatações diferentes, você usa o Skill Creator para gerar skills que já seguem as melhores práticas, documentação e estrutura de diretórios.

### Como Aplicar

1. Crie um prompt mestre (baseado no `skills.md` ou documentação oficial).
2. Sempre que identificar um processo repetitivo, invoque o Skill Creator: "Ei, crie uma habilidade para [PROCESSO] baseado no nosso padrão".

---

## 4. Gatilho de Criação (Repetição)

### O Que É

O sinal claro de que você precisa criar uma Skill.

> "Quando você se encontra repetindo um prompt, é provavelmente uma boa indicação que você quer construir uma habilidade."

### Por Que Importa

Transforma tarefas manuais em ativos reutilizáveis. Se você digita a mesma instrução 3 vezes, está desperdiçando tempo e tokens.

### Como Aplicar

1. Monitore seus prompts recorrentes.
2. Identificou repetição? PARE.
3. Crie uma Skill para aquilo.
4. Nunca mais digite o prompt, apenas invoque a skill.

---

## 5. Scripts Executáveis em Skills

### O Que É

A capacidade das skills do Antigravity de conterem e executarem scripts (Python, Bash, etc.) como parte de sua definição. Não é apenas texto/prompt, é código vivo.

### Exemplo Concreto

Jack menciona criar um "Reddit Scraper". A skill não apenas diz "analise o Reddit", ela contém (ou gera) o script Python específico para raspar os top 3 posts de um subreddit e executá-lo.

### Aplicação no Bi-IA

Podemos ter skills com scripts Python embutidos para tarefas de manutenção do Vault (ex: limpadores de tags, validadores de links) que rodamos via comando.

---

## 6. Economia de Tokens e Contexto

### O Que É

Skills funcionam como "pratos pré-feitos". Você não precisa passar todo o contexto e instruções de "como fazer" a cada interação. A skill já tem isso encapsulado.

### Por Que Importa

"Isso vai salvar o seu número de tokens e vai ser épico". Em codebases grandes ou sessões longas, economizar tokens de instruções repetitivas libera espaço para o contexto que realmente importa (o problema atual).

### Como Aplicar

Ao invés de um prompt de 500 linhas explicando como fazer um code review, invoque a Skill `CodeReviewMaster`. O Gemini carrega o contexto necessário sob demanda, mantendo a janela limpa.

---

## 7. Decisão de Uso (Natural Language Trigger)

### O Que É

O Gemini (ou o modelo subjacente) decide dinamicamente quando invocar uma skill baseada na linguagem natural do usuário. Você não precisa necessariamente saber o comando exato, apenas expressar a intenção.

### Como Aplicar

"Eu quero que você edite a informação e o contexto..."
O sistema entende a intenção e puxa a skill relevante de edição ou design. Isso torna a interface fluida.
