---
criado: 2024-09-23T17:26:45-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir

## Quer saber por que você deveria aprender isso?

- Por que o LLM não consegue soletrar palavras? Tokenização.
- Por que o LLM não consegue realizar tarefas super simples de processamento de strings, como reverter uma string? Tokenização.
- Por que o LLM é pior em idiomas que não são em inglês (por exemplo, japonês)? Tokenização.
- Por que o LLM é ruim em aritmética simples? Tokenização.
- Por que eu deveria preferir usar YAML ao invés de JSON com LLMs? Tokenização.
- Qual é a verdadeira raiz do sofrimento? Tokenização. 😂

Dominar a Tokenização é essencial para se comunicar de forma eficaz com IAs e extrair delas todo o potencial

Então bora aprender!

## Por que é Importante?

Para entender por que a tokenização é importante, precisamos pensar em dois aspectos dos modelos implantados: limites de tokens e precificação de tokens.

Limites de Tokens. Cada modelo tem uma janela de contexto definida como o número máximo de tokens que pode processar por solicitação única. Por exemplo, modelos antigos de gpt-3.5-turbo têm um limite de 4K tokens (contexto) para cada solicitação. O limite de tokens é compartilhado entre o prompt e a conclusão. Como a conclusão é adicionada ao prompt para gerar o próximo token, torna-se necessário ajustar ambos dentro da janela de contexto total para uma única solicitação.

Precificação de Tokens. Como em qualquer API, o uso da implantação do modelo incorre em custos baseados no tipo e versão do modelo. Atualmente, a precificação do modelo está vinculada ao número de tokens usados, com diferentes pontos de preço possíveis para cada tipo ou versão de modelo.

## Introdução à Tokenização:

No mundo dos LLMs, a tokenização é o processo de dividir textos em pedaços menores, conhecidos como tokens.

- Um token pode ser um único caractere, uma fração de palavra ou uma palavra inteira.
- Muitas palavras comuns são representadas por um único token.
- Palavras menos comuns são representadas por múltiplos tokens.

Imagine que cada palavra, ou até mesmo partes de palavras, é um quebra-cabeça. A tokenização é o que nos permite separar cada peça desse quebra-cabeça para que a máquina possa entender e, posteriormente, juntar essas peças novamente para formar uma imagem completa.

Por exemplo, o texto acima tem 99 tokens, pode [testar aqui](https://tiktokenizer.vercel.app/?model=gpt-4-1106-preview).

![[Pasted image 20240923172921.png]]

A Importância da Tokenização:

Por que isso é crucial?

Bem, sem a tokenização, os LLMs seriam como um turista perdido em uma cidade estrangeira sem um mapa.

Os tokens são como coordenadas no mapa, guiando o modelo através da complexidade da linguagem humana, permitindo que ele faça previsões precisas sobre o que vem a seguir no texto ou como responder a uma pergunta.

Se liga agora no "mapa da IA" no texto da imagem que te mostrei no parágrafo anterior: 2822, 29452, 8924, 445, 11237, 82, 11, 264, 4037, 48476, 4046, 297, 59996, 409, 29932, 404, 1495, 437, 991, 10696, 64, 49019, 3026, 4692, 11, 71583, 13652, 8112, 11460, 13, 38891, 1744, 19394, 95747, 11, 6033, 39583, 41349, 81282, 409, 11091, 89223, 11, 4046, 4543, 1744, 14720, 1824, 8393, 17930, 13, 362, 4037, 48476, 4046, 297, 1744, 12155, 52603, 4941, 277, 19394, 1069, 17930, 951, 325, 1744, 14720, 1824, 8393, 17930, 3429, 1744, 264, 29830, 54506, 2278, 64, 96537, 384, 11, 46000, 12826, 11, 503, 3935, 277, 4043, 300, 1069, 46378, 88019, 3429, 1376, 277, 10832, 63997, 71301, 13

Isso ai são os Tokens.

Por exemplo, "No" é 2882, " mundo" é 29452, e assim por diante.

![[Pasted image 20240923173026.png]]

Tá difícil de entender? Vamos continuar que vai ficar mais fácil.

Imagine que você está jogando um videogame onde cada objeto, personagem ou ação é representado por um número único. Em nosso jogo, o mundo da inteligência artificial, esses números são chamados de tokens, e o mapa que estamos seguindo é composto exatamente por eles.

A sequência numérica que mencionei antes, essa longa lista de números, é como se fosse um código secreto. Cada número representa uma peça específica do nosso grande quebra-cabeça de linguagem. Por exemplo, o número 2822 pode representar a palavra "No", e 29452 pode representar " mundo". Esses números não são aleatórios; eles são cuidadosamente selecionados e organizados por um processo chamado tokenização.

Então, quando vemos ==2822, 29452, 8924, 445...==, não estamos apenas olhando para números; estamos vendo uma história sendo contada em uma linguagem que os modelos de IA, como os LLMs, podem entender. É como se estivéssemos traduzindo português para o idioma da inteligência artificial.

Confesso que meu lado nerd gosta de entender sobre isso.

Mas se você não entender isso, você vai perder muitas noites de sono, grana e talvez até cabelo. hehe

Então vamos continuar.

## A Essência da Tokenização:

Após treinados, os tokenizadores têm duas funções primordiais: ==encode()==, que traduz de strings para tokens, e ==decode()==, que faz o caminho inverso.

Para tornar isso mais palpável, imagine que você está enviando uma mensagem codificada a um amigo, onde cada palavra é substituída por um número baseado em um livro de códigos que ambos têm. Somente quem tem o livro de códigos (ou, neste caso, o algoritmo de tokenização) pode traduzir essa mensagem de volta para o português.

Isso é exatamente o que acontece na tokenização em LLMs. Transformamos texto em uma sequência de números (tokens) que o modelo pode "ler" e processar. E assim como em nosso jogo imaginário, esses tokens são a chave para desbloquear significados, responder perguntas, ou até mesmo criar textos novos e interessantes.

## Métodos de Tokenização:

- Tokenização Baseada em Palavras: O método mais direto, dividindo o texto em palavras individuais. É como desmontar um Lego, peça por peça, onde cada peça é uma palavra.
- Tokenização Baseada em Subpalavras: Essa técnica vai um passo além, dividindo palavras em fragmentos menores. Isso é especialmente útil para lidar com palavras novas ou raras. Imagine cortar cada peça de Lego em partes ainda menores para entender melhor cada detalhe.
- Tokenização Baseada em Caracteres: Aqui, cada caractere é um token. É como se disséssemos que cada átomo de cada peça de Lego importa. Essa abordagem é útil para idiomas com muitos caracteres, como o chinês.

## Desafios da Tokenização:

- Eficiência vs. Precisão: Encontrar o equilíbrio certo entre cortar o texto em pedaços pequenos o suficiente para ser gerenciável, mas não tão pequenos que percam o significado, é uma arte.
- Variações Linguísticas: Diferentes línguas e dialetos podem exigir abordagens de tokenização distintas. É como se as peças de Lego mudassem de forma dependendo da cidade que você está tentando construir.

## Técnicas Avançadas de Prompt

Engenharia Reversa de Prompt Use ferramentas como o TikTokenizer para ver exatamente como seu prompt é tokenizado. Compare diferentes formatos e veja qual é mais eficiente.

Exemplo: JSON: {"produto": "camiseta", "descrição": "100% algodão, várias cores", "preço": 29.99} Fichas: 27

YAML: produto: camiseta Descrição: 100% algodão, várias cores Preço: 29.99 Fichas: 21

## Atividades Práticas:

Experimento de Tokenização: Escolha um parágrafo de texto e tente aplicar diferentes métodos de tokenização manualmente. Observe como o significado é afetado.

# Recursos Adicionais

## Ferramentas:

https://tiktokenizer.vercel.app/

Esse é melhor vídeo sobre o assunto:

https://hundredblocks.github.io/transcription_demo/

https://www.youtube.com/watch?v=zduSFxRajkE&t=6711s

Fontes:

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Atenção é tudo que você precisa. Sistemas de processamento de informações neurais.
2. Sennrich, R., Haddow, B., & Birch, A. (2016). Tradução automática neural de palavras raras com unidades de subpalavras. Associação de Linguística Computacional.

# ia

Este texto é uma introdução ao conceito de tokenização em modelos de linguagem, como os LLMs (Large Language Models). A tokenização é o processo de dividir textos em pedaços menores, conhecidos como tokens, que podem ser processados por modelos de linguagem.

**Por que a tokenização é importante?**

A tokenização é importante porque:

1. **Limites de tokens**: Cada modelo tem um limite de tokens que pode processar por solicitação. A tokenização ajuda a otimizar o uso desses tokens.
2. **Precificação de tokens**: A precificação de modelos está vinculada ao número de tokens usados. A tokenização ajuda a reduzir os custos.

**Introdução à tokenização**

A tokenização é o processo de dividir textos em pedaços menores, conhecidos como tokens. Um token pode ser um caractere, uma fração de palavra ou uma palavra inteira.

**Métodos de tokenização**

Existem diferentes métodos de tokenização, incluindo:

1. **Tokenização baseada em palavras**: divide o texto em palavras individuais.
2. **Tokenização baseada em subpalavras**: divide palavras em fragmentos menores.
3. **Tokenização baseada em caracteres**: divide o texto em caracteres individuais.

**Desafios da tokenização**

A tokenização apresenta desafios, incluindo:

1. **Eficiência vs. precisão**: encontrar o equilíbrio entre cortar o texto em pedaços pequenos o suficiente para ser gerenciável, mas não tão pequenos que percam o significado.
2. **Variações linguísticas**: diferentes línguas e dialetos podem exigir abordagens de tokenização distintas.

**Técnicas avançadas de prompt**

A engenharia reversa de prompt é uma técnica que envolve analisar como um prompt é tokenizado e ajustar o prompt para otimizar o uso de tokens.

**Recursos adicionais**

O texto fornece recursos adicionais, incluindo:

1. **Ferramentas**: como o TikTokenizer, que pode ser usado para analisar como um prompt é tokenizado.
2. **Vídeos**: um vídeo sobre o assunto de tokenização.
3. \*\*
