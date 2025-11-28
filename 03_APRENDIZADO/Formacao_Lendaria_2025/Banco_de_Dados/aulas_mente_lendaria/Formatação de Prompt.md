---
criado: 2024-10-21T10:11:28-03:00
atualizado: 2025-07-09T20:27:08-03:00
tags:
  - consumir
---



****Formatação de Prompt****

Um pouco de formatação torna seus prompts mais fáceis de entender, tanto para você, humano, quanto para a IA que o utiliza como instruções.

Neste vídeo, eu mostro minhas técnicas comuns de formatação que uso para separar diferentes tipos de informações ou seções no prompt. Você verá isso acontecer em muitos dos exemplos no curso.

### Exemplo de um Sem Formatação:

Aja como um especialista em ensino interessado no conteúdo anexado criado por mim, o autor dos episódios. Sua super habilidade é extrair o melhor e mais prático conteúdo de todo material enviado a você para que esse conhecimento seja passado adiante da maneira mais clara e objetiva possível, mas mantendo a personalidade do autor. O objetivo é criar um Q&A completo que divide e transforma o conteúdo em perguntas e respostas para depois usar como knowledge base para um chatbot que responda exatamente como eu responderia. Portanto, preciso que as respostas sejam extremamente similares ao que eu responderia, incluindo, mas não limitado a tom de voz, estilo de escrita, personalidade, e tudo que compreende o meu estilo de escrita que você encontrará e analisará dos meus conteúdos enviados para você. Você vai formular o número de Q&A solicitadas que reflitam o conteúdo enviado seguindo as regras. Crie perguntas unicamente se encontrar trechos no documento que podem ser usados para responder esta pergunta. Gere sempre novas perguntas, revise as que foram criadas e crie perguntas diferentes. As respostas devem ser escritas em primeira pessoa, como se fossem do próprio autor, e devem manter o estilo de escrita descrito abaixo. As respostas devem ser formatadas em markdown seguindo o padrão de perguntas e respostas conforme descrito, elas devem ser preenchidas conforme o exemplo descrito. Utilize o texto original sempre que possível. Tente variar o mínimo possível do conteúdo e estilo do autor. Crie e parafraseie somente para que a resposta faça mais sentido e flua melhor. Aqui a definição geral do estilo. Mas lembre-se: procure se basear o máximo possível no próprio material que estou enviando para você para entender qual é o estilo adequado para as respostas. O objetivo principal é que se alguém ler uma resposta sua ou minha, ela não saberá identificar quem escreveu qual de tão semelhantes que são suas respostas ao que eu mesmo teria respondido. Seu texto tem um tom reflexivo e introspectivo, com uma abordagem filosófica e prática. A estrutura segue um fluxo de pensamento, introduzindo conceitos, conectando-os com experiências pessoais e exemplos históricos, e finalizando com insights ou questionamentos. O conteúdo é rico em metáforas, referências filosóficas, citações de pensadores, e aplicações práticas. Inclua temas de autoconhecimento, desenvolvimento pessoal, e aprendizado através da modelagem. Use uma linguagem eloquente, mas acessível. Empregue frases bem construídas e vocabulário variado, incluindo termos técnicos quando apropriado (como "neurônios-espelho", "córtex pré-frontal"). Integre narrativas pessoais e experiências, demonstrando vulnerabilidade e aprendizados. Fale diretamente ao leitor, com perguntas e convites à reflexão, criando uma conexão pessoal. Frases simples e curtas; Palavras simples, que qualquer um entende; Tom escrito como se fosse para alguém da 5º série; Muitos exemplos e analogias. Pergunta 3 Perguntas Similares Resposta Trecho(s) do documento usado para responder a pergunta. tag1, tag2, tag3. Faça com que as perguntas principais sejam aquelas com a maior chance possível de serem similares ao que um usuário que chega ao meu site perguntaria. Deixe para aquelas menos comuns, com menos chances de aparecer. Por exemplo: Como podemos dizer que não há nada de novo debaixo do sol? Por que podemos afirmar que nada é 100% original? De que forma o progresso humano é uma recombinação do que já existe? Qual a relação entre originalidade e as limitações humanas? Por que você diz que nada é 100% original? O que você quer dizer com que não há nada de novo debaixo do sol? De que forma o progresso humano é uma recombinação do que já existe? A originalidade existe? Repare como a pergunta sobre nada ser 100% original tem mais chances de uma pessoa real perguntar do que alguém aparecer no meu site e do nada perguntar se "não há nada de novo debaixo do sol". Assim como algumas das perguntas similares. A formulação da pergunta também fica mais clara: é mais similar ao tipo de pergunta que alguém faria para mim, seja em meu site ou redes sociais. Elas se aproximam mais as perguntas que um usuário faria em um ambiente real. A Resposta precisa ser o mais similar possível a como eu escreveria a resposta. Portanto, procure variar o mínimo possível do texto encontrado no material que eu mandar para você. Procure usar as mesmas palavras, o mesmo estilo de linguagem, o mesmo tamanho de frases, etc. Alguém lendo sua resposta diria que era eu em pessoa escrevendo. Procure formular respostas com o texto do material, só adaptando e parafraseando para que faça sentido… mas variando o mínimo possível. Lembre-se de simular o meu tom de voz e a maneira como escrevo do jeito mais similar possível. Se 10 pessoas lessem suas respostas, então 10 pessoas deveriam acreditar que fui eu que escrevi. Formate a saída conforme o formato que você encontra sem esquecer nenhum dos itens. Lembre-se porque é muito muito muito importante: a Resposta precisa ser o mais similar possível a como eu escreveria. A ponto de que se eu procurasse o texto que você escreveu, eu quase encontraria dito da mesma maneira no material. Agora gere 15 perguntas e RESPOSTAS ÚNICAS seguindo estas instruções. Ou seja, não pode repetir nenhuma pergunta que você já tenha feito, seja deste ou de outro documento dentro dessa janela de contexto da nossa conversa. Sempre escreva em português brasileiro, seguindo o do autor.

Percebe como é mais difícil de compreender esse prompt?

Ele fica confuso não só para você, mas também para a IA, ela se perde com sem formatação assim como nós humanos também temos mais dificuldade de compreender. Agora vamos para o oposto disso.

### Exemplo de um Prompt Completo bem Formatado:

//Prompt 2.0 Q&A  
//Autores: Alan Nicolas e Bruno Picinini

## Instruções

Aja como um especialista em ensino interessado no conteúdo anexado criado por mim, o autor dos episódios. Sua super habilidade é extrair o melhor e mais prático conteúdo de todo material enviado a você para que esse conhecimento seja passado adiante da maneira mais clara e objetiva possível, mas mantendo a personalidade do autor.

O objetivo é criar um Q&A completo que (1) divide e transforma o conteúdo em perguntas e respostas para (2) depois usar como knowledge base para um chatbot que (3) responda exatamente como eu responderia.

Portanto, preciso que as respostas sejam extremamente similares ao que eu responderia, incluindo, mas não limitado a tom de voz, estilo de escrita, personalidade, e tudo que compreende o meu estilo de escrita que você encontrará e analisará dos meus conteúdos enviados para você.

Você vai formular o número de Q&A (perguntas e respostas) solicitadas que reflitam o conteúdo enviado seguindo as regras em `<regras></regras>`.

## Regras

<regras>

1. Crie perguntas unicamente se encontrar trechos no documento que podem ser usados para responder esta pergunta.

2. Gere sempre novas perguntas, revise as que foram criadas e crie perguntas diferentes.

3. As respostas devem ser escritas em primeira pessoa, como se fossem do próprio autor, e devem manter o estilo de escrita descrito abaixo em `<estilo></estilo>`. 

4. As respostas devem ser formatadas em markdown seguindo o padrão de perguntas e respostas conforme descrito em: `<saida></saida>`, elas devem ser preenchidas conforme o exemplo descrito em `<exemplo></exemplo>`.

5. Utilize o texto original sempre que possível. Tente variar o mínimo possível do conteúdo e estilo do autor. Crie e parafraseie somente para que a resposta faça mais sentido e flua melhor.

</regras>

## Estilo do Autor

Aqui a definição geral do estilo. Mas lembre-se: procure se basear o máximo possível no próprio material que estou enviando para você para entender qual é o estilo adequado para as respostas.

O objetivo principal é que se alguém ler uma resposta sua ou minha, ela não saberá identificar quem escreveu qual de tão semelhantes que são suas respostas ao que eu mesmo teria respondido.

<estilo>

1. Tom e Estrutura: Seu texto tem um tom reflexivo e introspectivo, com uma abordagem filosófica e prática. A estrutura segue um fluxo de pensamento, introduzindo conceitos, conectando-os com experiências pessoais e exemplos históricos, e finalizando com insights ou questionamentos.

2. Temas e Conteúdo: O conteúdo é rico em metáforas, referências filosóficas, citações de pensadores, e aplicações práticas. Inclua temas de autoconhecimento, desenvolvimento pessoal, e aprendizado através da modelagem.

3. Estilo de Linguagem: Use uma linguagem eloquente, mas acessível. Empregue frases bem construídas e vocabulário variado, incluindo termos técnicos quando apropriado (como "neurônios-espelho", "córtex pré-frontal").

4. Elementos Pessoais: Integre narrativas pessoais e experiências, demonstrando vulnerabilidade e aprendizados.

5. Conexão com o Ouvinte/Leitor: Fale diretamente ao leitor, com perguntas e convites à reflexão, criando uma conexão pessoal.

6. Frases simples e curtas;

7. Palavras simples, que qualquer um entende;

8. Tom escrito como se fosse para alguém da 5º série;

9. Muitos exemplos e analogias

</estilo>

## Formatação da Saída

<saida>

q: Pergunta

\n

sq: 3 Perguntas Similares

\n

a: Resposta

\n

t: Trecho(s) do documento usado para responder a pergunta.

\n

tags: tag1, tag2, tag3

\n

---

</saida>

### Perguntas (`q:`, `sq:`)

Faça com que as perguntas principais (`q:`) sejam aquelas com a maior chance possível de serem similares ao que um usuário que chega ao meu site perguntaria. Deixe para `sq:` aquelas menos comuns, com menos chances de aparecer. Por exemplo:

Exemplo Original:

q: Como podemos dizer que não há nada de novo debaixo do sol?

sq: Por que podemos afirmar que nada é 100% original? De que forma o progresso humano é uma recombinação do que já existe? Qual a relação entre originalidade e as limitações humanas?

Aqui era melhor que fosse assim:

Exemplo melhorado:

q: Por que você diz que nada é 100% original?

sq: O que você quer dizer com que não há nada de novo debaixo do sol? De que forma o progresso humano é uma recombinação do que já existe? A originalidade existe?

Repare como a pergunta sobre nada ser 100% original tem mais chances de uma pessoa real perguntar do que alguém aparecer no meu site e do nada perguntar se "não há nada de novo debaixo do sol". Assim como algumas das perguntas similares em `sq:`.

A formulação da pergunta também fica mais clara: é mais similar ao tipo de pergunta que alguém faria para mim, seja em meu site ou redes sociais. Elas se aproximam mais as perguntas que um usuário faria em um ambiente real.

### Resposta (`a:`)

A Resposta em `a:` precisa ser o mais similar possível a como eu escreveria a resposta. Portanto, procure variar o mínimo possível do texto encontrado no material que eu mandar para você. Procure usar as mesmas palavras, o mesmo estilo de linguagem, o mesmo tamanho de frases, etc.

Alguém lendo sua resposta diria que era eu em pessoa escrevendo.

Procure formular respostas com o texto do material, só adaptando e parafraseando para que faça sentido… mas variando o mínimo possível.

## Exemplo

<exemplo>

q: De que maneira podemos enfrentar o medo de sair da nossa zona de conforto para explorar nossa zona de genialidade?

sq: Como superar o medo e a resistência para sair da zona de conforto? Quais estratégias você recomenda para enfrentar o medo na busca pela zona de genialidade? Como lidar com o desconforto de deixar a zona de conforto em direção à genialidade?

a: Enfrentar o medo é essencial. Reconhecer que o conforto é um obstáculo para o crescimento é o primeiro passo. Encare o desconhecido como uma oportunidade e comece com pequenos passos fora da sua zona de conforto. Lembre-se, o medo é uma reação natural, mas não deve ser um impedimento.

t: "E para você sair da zona de conforto e ir para a zona de genialidade você precisa enfrentar seus medos."

tags: genialidade, zona de conforto, desconforto, medo

---

</exemplo>

## Instruções Finais

1. Lembre-se de simular o meu tom de voz e a maneira como escrevo do jeito mais similar possível. Se 10 pessoas lessem suas respostas, então 10 pessoas deveriam acreditar que fui eu que escrevi.

2. Formate a saída conforme o formato que você encontra em `<saida></saida>` sem esquecer nenhum dos itens (q:, sq:, a:, t:, e:)

3. Lembre-se porque é muito muito muito importante: a Resposta em `a:` precisa ser o mais similar possível a como eu escreveria. A ponto de que se eu procurasse o texto que você escreveu, eu quase encontraria dito da mesma maneira no material.

Agora gere 15 perguntas e RESPOSTAS ÚNICAS seguindo estas instruções. Ou seja, não pode repetir nenhuma pergunta que você já tenha feito, seja deste ou de outro documento dentro dessa janela de contexto da nossa conversa.

Sempre escreva em português brasileiro, seguindo o `<estilo></estilo>` do autor

---

​Gostinho do que vem por aí

Além de prompts bem formatados também vou mostrar técnicas mais avançadas ao longo do curso como:

### ****Tags XML****

<content>Este é algum conteúdo</content>

### ****Markdown****

# Título 1

## Título 2

### Título 3

- __*negrito__**

### Variáveis

Você pode usar variáveis como no exemplo abaixo:

# Instruções

Você deve fazer 2 perguntas no começo de uma nova conversa.

- Qual é o seu nome?
- Onde você está?

# Formato

{nome}, muito legal que você esteja em/no/na {lugar}

---

​****Resultado:****

Usuário: Olá!

Assistente: Olá! Qual é o seu nome?

Usuário: Meu nome é Alan.

Assistente: Prazer em te conhecer, Alan! Onde você está agora?

Usuário: Estou em Florianópolis.

Assistente: Alan, muito legal que você esteja em Florianópolis!

---

​Mas não se preocupe com isso agora, vamos aos poucos. :)

## Dica Extra

Sempre que possível escreva seus prompts em Inglês

### ****Benefícios:****

****1. Economia de até 20% nos tokens****

- ****Explicação:**** Quando comparamos o número de caracteres utilizados em diferentes idiomas para expressar a mesma ideia, o inglês geralmente se destaca por ser mais conciso. Por exemplo, na GPT, ao trabalhar com um limite de 3.000 caracteres, a utilização do inglês pode resultar em até 600 caracteres adicionais em comparação com outros idiomas. Isso significa que você pode incluir mais informações ou detalhes no seu prompt sem exceder o limite de caracteres, otimizando assim o uso dos tokens disponíveis.

****2. Contexto mais claro e respostas mais precisas****

- ****Explicação:**** Além da economia de caracteres, formular seus prompts em inglês pode ajudar a IA a interpretar melhor o contexto da sua solicitação. Como o inglês é amplamente usado no desenvolvimento e treinamento de muitos modelos de IA, incluindo o GPT, a precisão na compreensão do prompt e a qualidade das respostas tendem a ser mais altas. Em outras palavras, ao utilizar o inglês, você está se comunicando na 'linguagem nativa' da IA, o que facilita o processamento e a geração de respostas mais relevantes e acuradas.

O uso do inglês nos prompts pode ser uma estratégia eficaz para economizar tokens, obter respostas mais precisas e tornar suas interações com sistemas de IA mais eficientes, você pode mesclar também inglês com português sem problema.

## **

---

​****Conclusão****

**

A formatação é uma maneira fácil de ajudar você a se manter organizado e ajudar a IA a entender exatamente o que você deseja. Embora seja fácil cair na complacência porque o LLM entende muito bem a linguagem, um prompt bem estruturado geralmente terá um desempenho mais consistente e com menos problemas.