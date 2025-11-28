---
criado: 2024-10-01T10:06:17-03:00
atualizado: 2025-07-09T20:27:08-03:00
---
#consumir 

## O que é Zero-Shot Prompting?

Imagine que você está conversando com um especialista muito inteligente, como um médico ou um advogado. Você faz uma pergunta sobre um assunto que ele domina, e ele responde na hora, sem precisar de nenhum exemplo ou contexto adicional. Isso é zero-shot: a capacidade de realizar uma tarefa sem nenhum exemplo prévio.

IAs gigantes como o GPT-4 e o Claude conseguem fazer zero-shot em várias tarefas, graças ao enorme volume de dados que elas "estudaram" e aos métodos especiais de treinamento, como instruct tuning (ajuste por instrução) e RLHF (aprendizado por reforço com feedback humano). Legal né?

### Exemplo de Zero-Shot

Digamos que você queira classificar um texto como positivo, negativo ou neutro (análise de sentimento). Com zero-shot, basta escrever assim:  

Prompt:

Classifique o texto a seguir como positivo, negativo ou neutro.

Texto: Eu achei o atendimento razoável, mas o produto deixou a desejar.

Sentimento:

Output:

Neutro

Viu? Não precisou dar nenhum exemplo. A IA já sabe o que é "sentimento" e consegue analisar o texto sozinha.

  

### Quando usar Zero-Shot?

- Quando a tarefa é simples e direta, como classificação binária, extração de entidades, etc.
- Quando você não tem bons exemplos para fornecer.
- Quando quer economizar tokens e deixar espaço para mais instrução ou contexto.

## O que é Few-Shot Prompting?

Voltando à analogia do especialista, imagine que agora você está falando de um assunto que ele não conhece tão bem. Para te ajudar, você dá alguns exemplos de perguntas e respostas sobre o tema, e aí sim ele consegue responder coisas parecidas. Isso é few-shot: fornecer alguns exemplos (geralmente de 1 a 10) para a IA "estudar" e se adaptar à tarefa.

Few-shot é muito útil quando o zero-shot não funciona bem. Os exemplos ajudam a IA a entender exatamente o que você quer e seguir o mesmo formato nas respostas.

### Exemplo de Few-Shot

Vamos tentar uma tarefa mais desafiadora: interpretar código Python e explicar o que ele faz.

Prompt:

def soma(a, b):

    return a + b

Explique o código acima:

O código define uma função chamada "soma" que recebe dois parâmetros (a e b) e retorna a soma desses parâmetros.

def fatorial(n):

    if n == 0:

        return 1

    else:

        return n * fatorial(n-1)

Explique o código acima:

Output:

O código define uma função chamada "fatorial" que calcula o fatorial de um número n usando recursão.

A função verifica primeiro se n é igual a zero. Se for, retorna 1, pois o fatorial de 0 é 1.

Se n não for zero, a função retorna n multiplicado pelo fatorial de n-1. Isso é recursão: a função chama a si mesma com um valor menor de n, até que n chegue a zero.

Por exemplo, para calcular fatorial(5), a função faz:

5 * fatorial(4)

5 * 4 * fatorial(3)

5 * 4 * 3 * fatorial(2)

5 * 4 * 3 * 2 * fatorial(1)

5 * 4 * 3 * 2 * 1 * fatorial(0)

5 * 4 * 3 * 2 * 1 * 1 = 120

Funcionou! Com apenas 1 exemplo (1-shot), a IA entendeu que deveria:  

1. Explicar o que a função faz em geral
2. Detalhar a lógica passo a passo
3. Dar um exemplo de execução

  

### Quando usar Few-Shot?

- Quando o zero-shot não funciona bem para a tarefa.
- Quando você tem bons exemplos para fornecer, de preferência com variações.
- Quando é importante que a resposta siga um formato específico.
- Para tarefas mais complexas que exigem raciocínio passo a passo.

### Dicas para Formular Exemplos

1. Destaque o que é entrada e o que é saída. Ajuda a IA a distinguir instrução dos exemplos.
2. Varie os exemplos para cobrir diferentes casos. Ex: sentimentos positivos, negativos e neutros.
3. Mantenha o mesmo formato nos exemplos e na entrada final.
4. Mais exemplos (5-shot, 10-shot) podem ajudar em tarefas difíceis, mas ocupam mais tokens.

## Limitações e Alternativas

Nem zero-shot nem few-shot são perfeitos. Para tarefas muito complexas que exigem raciocínio avançado, planejamento de etapas e uso de conhecimento externo, pode ser necessário usar técnicas mais avançadas, como encadeamento de pensamentos (_chain of thought_) ou até retreinar modelos com dados específicos (fine-tuning). Mas isso fica para outra aula!

## Resumo

- Zero-shot: fazer tarefas sem exemplos. Ideal para instruções simples e diretas.
- Few-shot: dar exemplos para ajudar na tarefa. Melhor para formatos específicos e lógicas passo a passo.
- Escolha entre os dois de acordo com a complexidade da tarefa e a qualidade dos exemplos que você tem.
- Se ambos falharem, considere técnicas mais avançadas.

![](https://api-club-file.cb.hotmart.com/public/v5/files/77fa1231-f8d7-4599-bf64-5a87b0db8dd5)

## Recursos Adicionais

**Artigos:**

- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Um guia completo sobre engenharia de prompts.
- [Prompt Engineering 101](https://humanloop.com/blog/prompt-engineering-101) - Artigo introdutório sobre engenharia de prompts.

**Vídeos:**

- [Prompt Engineering - Como Fazer a IA Trabalhar Para Você](https://www.youtube.com/watch?v=y7tFHfzVzC4) - Palestra sobre técnicas de engenharia de prompts (em inglês).
- [Prompt Engineering para GPT-3](https://www.youtube.com/watch?v=bp12xtRmHGE) - Tutorial hands-on de prompt engineering com GPT-3 (em inglês).

**Cursos:**

- [ChatGPT Prompt Engineering para Desenvolvedores](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) - Curso gratuito de prompt engineering voltado para desenvolvedores, por Andrew Ng e Isa Fulford (OpenAI).
- [Prompt Engineering Básico](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/prompt-engineering) - Tutorial interativo de prompt engineering da Microsoft.

## Referências

1. Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... & Amodei, D. (2020). Os modelos de linguagem são aprendizes de poucos tiros. _Avanços nos sistemas de processamento de informações neurais_, 33, 1877-1901.
2. Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., ... & Le, Q. V. (2021). Modelos de linguagem ajustados são aprendizes zero-shot. _pré-impressão arXiv arXiv:2109.01652_.
3. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Modelos de linguagem de treinamento para seguir instruções com feedback humano. _Avanços em Sistemas de Processamento de Informações Neurais_, 35, 27730-27744.
   

# ia


O artigo discute sobre as técnicas de "Zero-Shot Prompting" e "Few-Shot Prompting" em inteligência artificial (IA), especificamente em modelos de linguagem como o GPT-4 e o Claude. Aqui está um resumo do artigo:

**Zero-Shot Prompting**

* É a capacidade de realizar uma tarefa sem nenhum exemplo prévio.
* É útil para tarefas simples e diretas, como classificação binária e extração de entidades.
* Exemplo: classificar um texto como positivo, negativo ou neutro.

**Few-Shot Prompting**

* É fornecer alguns exemplos (geralmente de 1 a 10) para a IA "estudar" e se adaptar à tarefa.
* É útil para tarefas mais complexas que exigem raciocínio passo a passo e formatos específicos.
* Exemplo: interpretar código Python e explicar o que ele faz.

**Quando usar cada técnica**

* Zero-Shot: quando a tarefa é simples e direta, e não há exemplos disponíveis.
* Few-Shot: quando a tarefa é mais complexa, e há exemplos disponíveis para fornecer.

**Dicas para formular exemplos**

* Destaque o que é entrada e o que é saída.
* Varie os exemplos para cobrir diferentes casos.
* Mantenha o mesmo formato nos exemplos e na entrada final.

**Limitações e alternativas**

* Nem zero-shot nem few-shot são perfeitos.
* Para tarefas muito complexas, pode ser necessário usar técnicas mais avançadas, como encadeamento de pensamentos ou retreinar modelos com dados específicos.

**Recursos adicionais**

* Artigos, vídeos e cursos sobre engenharia de prompts e modelos de linguagem.

Em resumo, o artigo discute sobre as técnicas de zero-shot e few-shot prompting em IA, suas limitações e como escolher a técnica certa para a tarefa. Além disso, fornece dicas para formular exemplos e apresenta recursos adicionais para aprender mais sobre o assunto.