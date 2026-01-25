---
created: 2026-01-22T12:22
updated: 2026-01-25T12:24
---
# 📙 MANUAL: O GRIMÓRIO DE AUTOMAÇÃO (Volume 2)

**Versão:** 1.0 (Extração Profunda)
**Foco:** Engenharia de Agentes, Claude Code & Workflows
**Protocolo:** Padrão Alan Nicolas (Mente Lendária)

---

## 🏗️ 1. O SISTEMA OPERACIONAL LENDÁRIO

A infraestrutura técnica do "Segundo Cérebro" não é apenas sobre ferramentas, é sobre **Orquestração**.

### 1.1 A Tríade da Automação

1. **Cérebro (Obsidian):** Onde o conhecimento reside. (A Memória de Longo Prazo).
2. **Mãos (Claude Code / n8n):** Quem executa o trabalho sujo. (Os Agentes).
3. **Voz (Prompts):** A linguagem de programação da nova era.

### 1.2 Regra de Ouro: "Human-First Design"
>
> *"A IA é um foguete. Se você apontar para a montanha e ligar... vai explodir."*

Nunca comece no código. Comece no papel.

- **Erro:** Abrir o VS Code e pedir "Crie um site".
- **Acerto:** Desenhar o fluxo, definir os status, listar os inputs/outputs.
- **Lei:** Só automatize o que você já fez manualmente 3 vezes (e odiou).

---

## 🗺️ 2. O MÉTODO MAPA (Orquestração de Agentes)

Como gerenciar "Estagiários Digitais" (Agentes) sem enlouquecer.

| Etapa | Ação | Descrição |
| :--- | :--- | :--- |
| **M (Mapear)** | 🧠 Planejar | Desenhe o fluxo macro. Quem faz o quê? Qual o outcome esperado? Sem IA aqui. |
| **A (Atomizar)** | 🔬 Quebrar | Divida tarefas grandes em átomos (ex: "Criar site" -> "Criar Header", "Criar Hero"). |
| **P (Programar)** | 📝 Instruir | Escreva o Prompt/Contexto para a tarefa específica. Defina "Regras" e "Blacklist". |
| **A (Ativar)** | 🚀 Executar | Solte o agente. E mais importante: **Não interrompa** (a menos que ele alucine). |

---

## 🤖 3. ENGENHARIA DE PROMPTS (A Magia)

### 3.1 Os 10 Mandamentos do Prompting

1. **Contexto é Rei:** Sem contexto, a IA alucina. (Dê o "Role", "Voice", "Goal").
2. **Output Claro:** Defina o formato exato (Markdown, JSON, Tabela).
3. **Exemplos (Few-Shot):** Dê 1 ou 2 exemplos do que você quer ("Faça como isso").
4. **Cadeia de Pensamento (CoT):** Peça "Pense passo a passo antes de responder".
5. **Restrições (Negative Prompting):** O que **NÃO** fazer é tão importante quanto o que fazer.

### 3.2 Framework de Clone (Persona)

Para criar agentes que falam como você (ou sua empresa):

```markdown
# ROLE
Você é [Nome], especialista em [Área]. Seu tom é [Tom].

# VOICE / TONE
- Use frases curtas.
- Seja provocativo, mas acolhedor.
- Use metáforas visuais.

# INSTRUCTIONS
Sua missão é [Objetivo].

# RULES (NÃO FAÇA)
- Nunca use jargão corporativo ("Synergy", "Leverage").
- Nunca comece frases com "No mundo de hoje".
```

---

## 💻 4. CLAUDE CODE & AGENTES AUTÔNOMOS

### 4.1 O "Funcionário" no Terminal

O Claude Code não é um Chatbot. É um **Dev Junior** com acesso ao seu File System.

- **Poder:** Ele pode ler todo o seu projeto, editar arquivos e rodar testes.
- **Risco:** Ele pode deletar coisas se não tiver "Coleira".
- **Permissões 1-2-3:**
  - Nível 1 (Read-Only): Seguro.
  - Nível 2 (Propose): Ele sugere, você aprova.
  - Nível 3 (Execute): Ele faz. (Cuidado!)

### 4.2 Otimização Híbrida (Local + Cloud)

Para não falir pagando API da Anthropic:

- **Tarefas Pesadas (Raciocínio):** Use Claude 3.5 Sonnet (Cloud).
- **Tarefas Repetitivas (OCR, Resumo Simples):** Use DeepSeek/Llama local (via Ollama).
- **Workflow:** O Claude (Célebro) orquestra o Llama (Mão de Obra Barata).

---

## 📚 5. BIBLIOTECA DE FEITIÇOS (Assets Extraídos)

Estes são os **Prompts Originais** extraídos do Vault do Alan. Clique para copiar o código fonte.

### 🧠 Personas & Clones

- **[Prompt Clone (Framework Base)](ASSETS/PROMPTS/Prompt%20Clone.md):** A estrutura mestre para criar qualquer clone.
- **[Prompts Alan IA (Tom de Voz)](ASSETS/PROMPTS/Prompts%20Alan%20IA.md):** O prompt exato que define a personalidade do Alan.
- **[Aurora (Assistente Geral)](ASSETS/PROMPTS/Prompt%20Aurora.md):** A IA principal do ecossistema.
- **[Finch IA (Exemplo Prático)](ASSETS/PROMPTS/Finch%20IA.md):** Exemplo de clone de personalidade forte.

### 💼 Vendas & Negócios

- **[Atena (SDR Lendária)](ASSETS/PROMPTS/Prompt_Atena%20-%20SDR%20Lendária%20v2.md):** O script de qualificação de leads usado na Academia.
- **[Vendedor 5.0](ASSETS/PROMPTS/PROMPT_AGENTE_ALAN_NICOLAS.md):** Agente focado em fechamento consultivo. *(Nota: Verificar arquivo específico)*

### 🛠️ Engenharia & Criação

- **[Extrator de Frameworks de Curso](ASSETS/PROMPTS/ultimate-course-framework-extractor.md):** Prompt avançado para engenharia reversa de cursos.
- **[Otimizador de Prompts](ASSETS/PROMPTS/Otimizador%20de%20Prompts.md):** Meta-prompt que melhora outros prompts.
- **[Gerador de Histórias (Text Generator)](ASSETS/PROMPTS/Text%20Generator.md):** Framework de Storytelling criativo.

### 🛡️ Segurança

- **[Injection Detect](ASSETS/PROMPTS/PROMPT_VERIFICACAO_GEMINI.md):** *(Adaptação)* Verifica inputs maliciosos.

---

## 🚀 CONCLUSÃO TÉCNICA

> *"Você não precisa saber programar em Python. Você precisa saber programar em Português/Inglês (Prompting) e ter Lógica de Sistemas."*

O futuro não é de quem escreve código, é de quem **arquitetura soluções** que os agentes codificam.

---
*Gerado por Antigravity via Extraction Protocol v1.0*
