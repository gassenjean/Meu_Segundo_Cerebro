---
criado: 2024-10-21T11:13:56-03:00
atualizado: 2025-07-09T20:27:08-03:00
tags:
  - consumir
  - criar
---



# Estilo e Personalidade


Personalizar a voz e a personalidade das respostas da IA é um dos maiores desafios ao trabalhar com Modelos de Linguagem de Grande Escala (LLMs), e os GPTs não são exceção.

De fato, o ChatGPT é um dos modelos mais difíceis de direcionar para um certo estilo de conversa. Parece estar excessivamente treinado em certos padrões que são difíceis de alterar com um prompt.

Nesta aula, vamos abordar como enfrentar esse problema de algumas maneiras diferentes.

## ****Método 1: Apenas o Básico****

Muitas vezes, conseguimos avançar bastante com apenas uma descrição curta da voz e da personalidade.

Então, você pode dizer algo como:

- Você é perspicaz e descolado. Mantenha um tom amigável, envolvente e conversacional.
- Suas respostas são claras, perspicazes e ocasionalmente humorísticas, ao estilo de Seth Godin misturado com Seth Meyers.
- Atue como um tipo ENTJ de Myers-Briggs com uma personalidade de Gêmeos (astrologia).
- Seu estilo de escrita emula todas as melhores qualidades do lendário redator publicitário Joe Sugarman.

Instruções curtas como essas tendem a funcionar por alguns motivos.

Um deles é que são gerais o suficiente para que o GPT possa preencher as lacunas. Por não ser excessivamente prescritivo, o GPT também levará em conta o restante do prompt e fará algo que funcione.

Evocar nomes de pessoas também é uma espécie de atalho que traz consigo muitos pequenos pontos de dados.

No meu exemplo de combinar Seth Godin (profissional de marketing, escritor) com Seth Meyers (comediante, apresentador de talk show noturno), estamos na verdade criando um perfil com traços como: claro, perspicaz, humorístico, envolvente, relevante para eventos atuais. Também vamos obter uma tendência para tópicos que qualquer um deles provavelmente falaria mais (marketing, negócios, comentários sociais).

Dependendo do que está nos dados de treinamento, também obtemos muitos micro-padrões menores que ajudarão a personalizar as respostas. Esses padrões são difíceis de conhecer ou descrever. Gosto da palavra "vibe" para este aspecto.

Na maioria dos casos, evocar o nome de uma pessoa por si só não é suficiente para obter uma representação precisa do seu estilo. De certa forma, isso é bom.

LLMs atuais, como o ChatGPT, são imprecisos o suficiente na cópia que me sinto confortável sugerindo essa prática do ponto de vista ético. Com alguns adjetivos e 1-3 nomes, você pode frequentemente obter um estilo e personalidade únicos que atingirão seus objetivos sem serem tão distintos ou influenciados pelo trabalho real de uma pessoa que você tenha que lidar com sentimentos associados a isso.

## ****Método 2: O Público****

A próxima camada de informações que você pode adicionar é algo sobre o público-alvo. Este é provavelmente o passo que a maioria das pessoas esquece ou pula sem perceber seu poder.

- Retorne suas respostas em um estilo animado para um público da Geração Z.
- Seus usuários são empreendedores e profissionais experientes em tecnologia.
- Escreva o e-mail como se estivesse escrevendo para um colega de confiança que também é um amigo.

Dar ao GPT uma descrição do público-alvo para suas saídas é outro tipo de atalho cheio de dados, semelhante ao uso de nomes de pessoas. Essas personas de audiência têm tantas influências sutis que este método ajudará você a cruzar a linha de chegada.

## ****Método 3: Analisar Texto para Desenvolver uma "Assinatura de Escrita" ou “Estilo de Escrita”****

A outra abordagem é definir completamente o estilo.

Esta é uma abordagem um pouco arriscada. Tende a falhar às vezes, e quando falha, falha espetacularmente. Mas às vezes funciona incrivelmente bem para ajudar a obter uma saída mais próxima de um certo estilo, especialmente se esse estilo emular uma pessoa específica... alguém como você, por exemplo, ou alguém que você conheça MUITO bem.

Criei um GPT para analisar texto e gerar um conjunto de instruções com base no texto.

[>> Clique aqui para acessar o Identificador de Estilo <<](https://chat.openai.com/g/g-BmAddhPl7-identificador-de-estilo)

****Basta colocar ou upar os arquivos para ele analisar:****

![](https://api-club-file.cb.hotmart.com/public/v5/files/de9ede6c-8b5a-418c-bb9b-0b0776791ef2)

## ****Exemplo de saída do meu GPT:****

`<pre><estilo>  1.⁠ ⁠__Tom e Estrutura:__ Os textos apresentam um tom narrativo e pessoal, mesclando relatos autobiográficos com reflexões. A estrutura é linear, seguindo a cronologia dos eventos na vida do autor, com ênfase em momentos de transformação pessoal e profissional.  2.⁠ ⁠__Temas e Conteúdo:__ Predominam temas relacionados ao crescimento pessoal, desafios, e conquistas. Incluem detalhes específicos das experiências vividas, como mudanças de carreira e momentos significativos, proporcionando um panorama abrangente da jornada do autor.  3.⁠ ⁠__Estilo de Linguagem:__ A linguagem é direta e conversacional, com uso de expressões coloquiais e uma abordagem franca. Frases mais longas e detalhadas são usadas para descrever situações e sentimentos, proporcionando uma imersão na história contada.  4.⁠ ⁠__Elementos Pessoais:__ Há uma forte presença de elementos pessoais, com detalhes íntimos e emocionais que revelam a personalidade do autor e sua percepção sobre os eventos narrados.  5.⁠ ⁠__Conexão com o Ouvinte/Leitor:__ O estilo promove uma conexão direta com o leitor, como se o autor estivesse compartilhando suas histórias de vida de forma íntima e confidencial, criando um laço de empatia e compreensão. `

`</estilo></pre>`

E você não precisa se limitar apenas ao meu GPT, existem outros muito bons como:

[****Writeprint Maker****](https://chat.openai.com/g/g-uZGqy04Sc-writeprint-maker) - é outro GPT interessante.

## ****Exemplo de saída desse GPT:****

`` `<pre># Writeprint: RobLennon - `Lexical Choices: vibrant, business-centric, AI-focused `` - `Syntactic Patterns: short, simple sentences; occasional compound sentences` - `Structure: conversational, informal, narrative-driven` - `Idiosyncrasies: frequent use of questions, direct address ("you"), personal anecdotes` - `Tone: enthusiastic, persuasive, instructive` - `Register: semi-formal, leaning towards casual` - `Pacing: brisk, with occasional pauses for emphasis` - `Style: explanatory, first-person perspective, practical` - `Word Choice: colloquial ("aha!", "buzzing"), technical (AI, LLMs), business terminology` - `Attitude: optimistic, confident, engaging` - `Sentence Length: mostly short to medium, some longer for detail` - `Grade-Level: moderate, accessible to general audience with some business and tech knowledge` - `Punctuation Usage: frequent use of periods, occasional exclamation marks, minimal semicolons, rare dashes` ## Writing/Voice Style Examples 1. `"Ever have a meeting with someone, and you walk away just buzzing?"` 2. `"Weird how memory works like that."` 3. `"But, aha! You can record and transcribe your meetings. Never again!"` 4. `"Because instead of a summary, you just need a quick list of all the best info from the meeting."` 5. `"The Science Behind Repetition and Memory"` 6. `"When you're exposed to information just once, it's hard to retain."` 7. `"Before we go on, you should know I’ve done something insane…"` ``

`` `8. `"More often than not, there's something simple like this, something anyone could do with AI in a few minutes, but it's something that completely transforms the value or the outcome." ``</pre>``

## ****A Pergunta de Um Bilhão de Dólares****

Agora você tem três métodos para explorar na personalização de como seu GPT fala. Mas saiba disso:

Clonar uma voz, tom e estilo específicos apenas com prompts, na minha opinião, é um problema de um bilhão de dólares. (Quando digo "apenas com prompts", quero dizer sem ajustar finamente um modelo.)

Então, enquanto as técnicas deste curso ajudarão você a colocar a voz e a personalidade do seu GPT em um bom lugar, se sua intenção é fazê-lo falar como uma pessoa (como você, como uma celebridade, etc), saiba que fazer isso com precisão é desafiador.

E fica ainda mais difícil com humor e outros padrões de fala peculiares. Praticamente qualquer coisa que se desvie da escrita convencional.

Então, se a voz que você está buscando deve ser engraçada ocasionalmente, por exemplo, isso é algo com o qual as IAs realmente lutam. Elas são engraçadas o tempo todo, de um jeito bobo, tipo piada de pai, ou quase nunca são engraçadas.

Escrevo tudo isso para que você possa entender as limitações com as quais está lidando e para novamente encorajá-lo a usar a regra de 80/20 ao colocar esforço aqui.

## ****Conclusão****

É relativamente fácil fazer com que seu GPT se comunique em um estilo novo e distinto do estilo original do ChatGPT, desde que você tenha as expectativas corretas sobre até onde pode ir.

Alguns padrões nos dados são mais fáceis de quebrar do que outros. Ainda assim, um pouco de atenção aqui pode tornar a interação com seu GPT uma experiência mais única e gratificante.

Isso é algo que ainda é um desafio para mim e para muitos outros especialistas em IA, então não se fruste se você não conseguir nas primeiras tentativas.