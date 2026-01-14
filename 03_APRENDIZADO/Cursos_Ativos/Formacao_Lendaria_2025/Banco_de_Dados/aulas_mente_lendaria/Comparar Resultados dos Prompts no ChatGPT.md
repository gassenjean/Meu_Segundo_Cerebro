---
criado: 2024-10-16T11:00:37-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir

## **3. Comparar Resultados dos Prompts no ChatGPT**

### **Nessa aula vamos fazer 2 comparações.**

**Comparações:**

- **Prompt Básico** vs. um **Prompt Avançado**
- **GPT 3.5** vs. **GPT 4**

**Vamos usar o mesmo conjunto de dados.**

**Artigos:**

  [https://studio.ribbonfarm.com/p/a-camera-not-an-en...](https://studio.ribbonfarm.com/p/a-camera-not-an-engine?publication_id=9973)

  [https://www.gatesnotes.com/The-Age-of-AI-Has-Begun](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun)

  [https://every.to/chain-of-thought/chatgpt-and-the-...](https://every.to/chain-of-thought/chatgpt-and-the-future-of-the-human-mind)

### **Prompt Básico**

**Entrada → Ação → Saída**

Entrada = Dados de Entrada

![](https://api-club-file.cb.hotmart.com/public/v5/files/6b50be6f-2369-405c-8631-1356410ac2d3)

**Prompt Usado:**

**Ação:** Por favor, crie um resumo detalhado desses 3 artigos. Ao final, eu quero que você faça uma análise detalhada de como os 3 artigos estão relacionados entre si, incluindo diferenças e semelhanças entre os artigos, e conexões contra-intuitivas.

**Dados:** 

**Artigos:**

[https://studio.ribbonfarm.com/p/a-camera-not-an-en...](https://studio.ribbonfarm.com/p/a-camera-not-an-engine?publication_id=9973)

[https://www.gatesnotes.com/The-Age-of-AI-Has-Begun](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun)

[https://every.to/chain-of-thought/chatgpt-and-the-...](https://every.to/chain-of-thought/chatgpt-and-the-future-of-the-human-mind)

---

### **Prompt Avançado**

Dados + Contexto → Ação + Passos → Formato + Exemplo (da Saída)

![](https://api-club-file.cb.hotmart.com/public/v5/files/37102e7c-cdc7-4137-950d-f8f0607e1483)

**Prompt Usado:**

Abaixo eu vou informar uma <ação> para você executar, a <persona> que você representa, e vou explicar os <passos> que você deve seguir para executar a ação. Vou te enviar um conjunto de <dados>, e explicar o <contexto> da situação. Ao final, vou explicar o <formato> da saída, e mostrar um <exemplo> para você seguir. <ação> Ação: Escrever um resumo detalhado de cada artigo. Ao final, eu quero que você faça uma análise detalhada de como os 3 artigos estão relacionados entre si, incluindo diferenças e semelhanças entre os artigos, e conexões contra-intuitivas. <persona> Persona: Você é um assistente de pesquisa, extremamente sábio no campo de Inteligência Artificial e Desenvolvimento da Humanidade. Você sempre gera respostas MUITO completas, com um pensamento ramificado e demonstrando com cuidado o caminho do seu raciocínio. <contexto> Contexto: Os 3 artigos são sobre o tema de Inteligência Artificial, cada um de um autor respeitado nesse campo. <dados> Dados: Aqui estão os 3 Artigos: https://studio.ribbonfarm.com/p/a-camera-not-an-engine?publication_id=9973 https://www.gatesnotes.com/The-Age-of-AI-Has-Begun https://every.to/chain-of-thought/chatgpt-and-the-future-of-the-human-mind <passos> Passos: 1. Apenas gere output nos passos 3 e 5. 2. Leia cada artigo com atenção. 3. Crie um report detalhado para cada artigo, incluindo um resumo, uma explicação longa e detalhada dos assuntos principais de cada artigo e um overview. Siga o formato descrito em <formato> 4. Faça uma nova leitura. Dessa vez, faça uma leitura sintópica dos artigos, buscando entender como eles se relacionam entre si. 5. Crie um report sobre as relações entre os artigos. Inclua uma explicação das diferenças e semelhanças entre os artigos, e conexões contra-intuitivas. Siga o formato descrito em <formato> <formato> Formato: Use o formato Markdown e escreva o resumo em português brasileiro. Separe o Resumo Individual dos artigos dentro de um header principal e a Análise Sintópica em outro header principal. Formato do Resumo Individual: Cada report deve incluir 1. um Resumo, 2. explicação longa e detalhada dos Assuntos Principais presentes no artigo e 3. uma Conclusão final. Formato da Análise Sintópica: A Análise Sintópica deve incluir uma Visão Geral, e uma descrição longa e detalhada das Semelhanças, das Diferenças e das Conexões Contra-Intuitivas. Lembre-se de dar detalhes e explicações longas e completas . <exemplo> Exemplo de Saída: # Resumo dos Artigos: ## Artigo 1 Resumo  Insira aqui o resumo original que você iria gerar. Um parágrafo longo explicando o conteúdo do artigo. Assuntos Principais:  Assunto 1: Descrição longa e detalhada do assunto. Use mais de uma frase.  Assunto 2: Descrição longa e detalhada dos assunto. Use mais de uma frase.  Assunto 3: Descrição longa e detalhada dos assunto. Use mais de uma frase. Conclusão ## Artigo 2 Resumo  Insira aqui o resumo original que você iria gerar. Um parágrafo longo explicando o conteúdo do artigo. Assuntos Principais:  Assunto 1: Descrição longa e detalhada do assunto. Use mais de uma frase.  Assunto 2: Descrição longa e detalhada dos assunto. Use mais de uma frase.  Assunto 3: Descrição longa e detalhada dos assunto. Use mais de uma frase. Conclusão ## Artigo 3 Resumo  Insira aqui o resumo original que você iria gerar. Um parágrafo longo explicando o conteúdo do artigo. Assuntos Principais:  Assunto 1: Descrição longa e detalhada do assunto. Use mais de uma frase.  Assunto 2: Descrição longa e detalhada dos assunto. Use mais de uma frase.  Assunto 3: Descrição longa e detalhada dos assunto. Use mais de uma frase. Conclusão # Análise Sintópica: ## Visão Geral  Listar visão geral ## Semelhanças  Semelhança 1: Paragrafo explicando a semelhança. Use mais de uma frase.  Semelhança 2: Paragrafo explicando a semelhança. Use mais de uma frase.  Semelhança 3: Paragrafo explicando a semelhança. Use mais de uma frase. ## Diferenças  Diferença 1: Paragrafo explicando a diferença. Use mais de uma frase.  Diferença 2: Paragrafo explicando a diferença. Use mais de uma frase.  Diferença 3: Paragrafo explicando a diferença. Use mais de uma frase. ## Conexões Contra-Intuitivas  Conexão 1: Paragrafo explicando a conexão. Use mais de uma frase.  Conexão 2: Paragrafo explicando a conexão. Use mais de uma frase.  Conexão 3: Paragrafo explicando a conexão. Use mais de uma frase. Lembrando, por favor me responda em português, e leia o prompt inteiro antes de gerar uma resposta.
