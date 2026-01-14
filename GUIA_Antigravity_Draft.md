# Guia Avançado: Dominando o Antigravity (Draft)

> [!NOTE]
> Este documento foi gerado pelo Gemini 3 Pro a partir da transcrição do vídeo "How to Use Antigravity Better than 99% of People".
> **Status:** Rascunho para refinamento pelo Claude Code.

## 1. Introdução: O Que é o Antigravity?

O Antigravity do Google não é apenas um chatbot; é uma ferramenta de **"AI encoder"** (codificador de IA) que muda o jogo. Enquanto a maioria das pessoas o usa apenas para conversar, seu verdadeiro poder está em construir aplicações de software completas e de alta qualidade — até 10x mais rápido que o desenvolvimento tradicional.

Pense na seguinte analogia:

- **Microsoft Word:** Para documentos.
- **Microsoft Excel:** Para planilhas.
- **Antigravity:** Para construir **software**.

Ele oferece acesso a modelos de ponta (como Gemini 3 Pro, Claude Sonnet 4.5), um editor de código central, um gerenciador de agentes ("Agent Manager") e integração nativa com o MCP (Model Context Protocol).

---

## 2. O Framework F.L.O.W

Para construir apps que funcionam de verdade, utilizamos um processo de 4 passos chamado **FLOW**:

### **F - FRAME (Enquadrar)**

- **Conceito:** Seja específico sobre o problema que você está resolvendo.
- **Princípio Einstein:** "Se eu tivesse uma hora para resolver um problema, passaria 55 minutos pensando no problema e 5 minutos pensando na solução."
- **Ação:** Converse com a IA (ex: Claude) para refinar sua ideia. Peça para ela desafiar seu pensamento e gerar um SOP (Procedimento Operacional Padrão) ou um resumo de uma página antes de começar a codificar.
- **Objetivo:** Ter um "prompt inicial" robusto e bem definido.

### **L - LAYOUT (Design)**

- **Conceito:** Defina a aparência e as regras visuais antes de codificar.
- **Ação:**
  - Busque inspirações (ex: Dribbble).
  - **Regras de Marca (Brand Rules):** Crie um arquivo (ex: `gemini.md` ou `brand_rules.md`) na barra lateral esquerda.
  - Especifique fontes, tipografia, cores e estilo nestes arquivos.
  - Faça upload de logos e imagens de referência.
  - **Dica:** Você pode desativar/ativar esses arquivos de contexto conforme necessário para não confundir a IA.

### **O - ORCHESTRATION (Orquestração)**

- **Conceito:** A construção propriamente dita, gerenciada por IA.
- **Ferramentas:**
  - **Artefatos:** O Antigravity gera planos de implementação, listas de tarefas e descrições.
  - **Comentários:** Você pode clicar em qualquer linha do plano ou código e adicionar comentários específicos (ex: "Use as regras de marca do arquivo X", "Faça essa animação mais interativa").
  - **Agent Manager:** Execute múltiplos agentes em paralelo (ver seção abaixo).
  - **Editor:** Acompanhe o código sendo gerado no centro e a estrutura de arquivos à esquerda.

### **W - WORLD (Mundo/Publicação)**

- **Conceito:** Levar sua aplicação para o mundo real.
- **Fluxo de Deploy:**
  1. Conectar ao **GitHub** (cria o repositório).
  2. Conectar ao **Vercel** (hospeda a aplicação).
  3. **Ciclo Contínuo:** Antigravity atualiza GitHub -> GitHub aciona Vercel -> App atualizado em segundos.
- Isso permite que você saia do "localhost" para um link público que pode ser compartilhado e monetizado.

---

## 3. O "Agent Manager" (Gerenciador de Agentes)

O **Open Agent Manager** é uma das "features escondidas" mais poderosas do Antigravity.

- **Conceito:** Pense nisso como uma "equipe de funcionários" ou uma "caixa universal de agência". Você pode ter 10, 20 ou 30 agentes trabalhando simultaneamente em diferentes aspectos do projeto.
- **Funcionalidade:**
  - **Paralelismo:** Enquanto um agente codifica a UI, outro pode estar fazendo pesquisa de mercado (ex: criando um `Competitors.md`) e outro pesquisando melhores práticas fiscais.
  - **Modo de Visualização:** Você pode alternar entre a visão de código (Editor) e a visão de gestão (Agent Dashboard) para aprovar mudanças e supervisionar o progresso.
  - **Auto-fixação:** O sistema consegue abrir um navegador (Google Chrome), testar a UI, clicar em botões e se "autocorrigir" com base nos erros encontrados.

---

## 4. MCP (Model Context Protocol)

O **MCP** é a linguagem universal que permite ao Antigravity se conectar com o mundo externo sem configurações complexas de API individuais para cada ferramenta.

- **O que é:** Um protocolo unificado para apps e IA conversarem.
- **Servidores MCP:** O Antigravity tem uma "loja" de servidores MCP onde você pode conectar ferramentas como:
  - **GitHub:** Para gestão de repositórios.
  - **PostgreSQL / Superbase:** Para banco de dados.
  - **Google Drive / Slack / Sentry:** Para produtividade e monitoramento.
  - **N8N:** Para automação de workflows.
- **Configuração:** Geralmente envolve apenas pegar um token da ferramenta original e colá-lo na configuração do MCP dentro do Antigravity.
- **Dica (Context 7):** Recomenda-se instalar o servidor "Context 7" para ter acesso à documentação mais recente de como conectar qualquer coisa.

---

## 5. Integração GitHub & Vercel

A integração é projetada para ser perfeita e contínua ("Seamless").

1. **Conexão:** No menu de administração/projetos, você conecta sua conta GitHub.
2. **Repo:** O Antigravity cria o repositório para você.
3. **Deploy:** Ao conectar com a Vercel, qualquer "push" feito pelo Antigravity no GitHub dispara automaticamente uma nova build na Vercel.
4. **Resultado:** Você tem um ambiente de produção (site ao vivo) e um ambiente de desenvolvimento (localhost) sincronizados.

---

## 6. Dicas Avançadas (Hacks do Especialista)

### **A. "Lemon Debugging" (Instruções de Sistema)**

Crie um arquivo de "Workflow" para debugging (ex: `debugging.md` ou nas instruções do sistema) com um prompt claro sobre como resolver erros.

- **O Hack:** Ao invés de explicar o erro toda vez, você apenas digita "Lemon Debugging" (ou sua palavra-chave) no chat.
- **O que acontece:** A IA consulta o arquivo de regras que explica exatamente como analisar logs, identificar problemas comuns e propor soluções no formato que você gosta.

### **B. Seleção de Modelos por Tarefa (Model Router)**

Não use o mesmo modelo para tudo. Otimize custos e qualidade:

- **Gemini 3 Pro:** O melhor para **Design**, UI e Visão (multimodal). Use quando estiver mexendo no layout.
- **Claude 3.5 Sonnet / Cloud Sonic:** Melhor para **Copywriting**, linguagem natural e "pensamento" complexo de codificação.
- **GPT-4o / GPT-4:** Bom para tarefas básicas que não exigem o raciocínio longo dos outros, ou como backup.
- A interface permite trocar o modelo ativo dinamicamente no canto direito.

### **C. Arquivos de Contexto Dinâmicos**

Use a barra lateral esquerda para gerenciar o contexto da IA.

- Crie arquivos `.md` com instruções específicas (Regras de Marca, Regras de Negócio).
- **Ative/Desative** (o ícone de "olho" ou check) esses arquivos conforme a fase do projeto. Não sobrecarregue a janela de contexto com regras de design quando estiver debugando banco de dados.

### **D. Browser Testing**

A janela de "Preview" do Antigravity não é apenas um visualizador estático; ela é um navegador Chrome real embutido. A IA pode interagir com ela, preencher formulários e testar a aplicação como um usuário real faria.

---

**Próximos Passos:**
[ ] Claude Code deve revisar e refinar este conteúdo.
[ ] Validar os nomes técnicos (ex: confirmar se "Context 7" é o nome exato da ferramenta de docs MCP mencionada).
[ ] Testar o framework FLOW em um projeto piloto.
