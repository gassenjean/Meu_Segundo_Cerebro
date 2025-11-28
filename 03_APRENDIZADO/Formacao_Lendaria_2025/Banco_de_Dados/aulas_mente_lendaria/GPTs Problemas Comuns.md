---
criado: 2024-10-22T15:15:34-03:00
atualizado: 2025-07-09T20:27:08-03:00
tags:
  - consumir
---

# Problemas Comuns

Nesta aula, vamos aprender a identificar, entender e resolver problemas comuns com GPTs usando técnicas além de apelar para as "emoções" do GPT por meio de prompts de magia negra.

As principais técnicas para fazer um GPT operar do jeito que gostamos são:

- Estruturar seu prompt com títulos em markdown
- Reduzir o comprimento e eliminar palavras desnecessárias
- Repetir a instrução (especialmente no início ou no fim)
- Explicar de forma positiva o que é proibido ou não permitido
- Usar linguagem assertiva e poderosa

## ****1. Estruture seu prompt com títulos em markdown****

Isso é exatamente o que parece e o que eu ensinei durante este curso.

Aqui, a chave é pensar nas partes do seu prompt como se estivessem em recipientes rotulados. Se uma instrução não está sendo seguida, pergunte-se se ela está em um recipiente claramente rotulado.

## ****2. Reduza o comprimento e elimine palavras desnecessárias****

Eu também gastei bastante energia neste curso fazendo você escrever conjuntos de instruções mais longos e complexos.

Mas, em alguns casos, descobri que adicionar mais e mais nem sempre é a resposta. Se o GPT tem muitas instruções para seguir, ou se algumas delas têm informações conflitantes, às vezes é tão importante olhar o que você pode subtrair.

Pergunte-se: Se o GPT não está seguindo suas instruções, há algo no prompt que está em conflito com essas instruções? Alguma coisa por perto que possa estar contaminando o significado delas? Há simplesmente muita coisa para um GPT fazer?

## ****3. Repita a instrução (especialmente no início ou no fim)****

Pesquisas mostraram que LLMs como o ChatGPT seguem uma curva em forma de U quanto à influência do prompt. As partes mais influentes do prompt são as pontas do U — o início e o fim.

Os pesquisadores acreditam que isso acontece por causa de padrões nos dados e na forma como foram separados e limpos para o processo de treinamento. Normalmente, instruções importantes vêm primeiro ou no final. De alguma forma, o modelo de linguagem conhece esse padrão e, portanto, tende a favorecer essas áreas.

A boa notícia é que podemos usar isso a nosso favor.

Se uma instrução não está sendo seguida, tente colocá-la no topo, na parte inferior ou em ambos. Por exemplo, você pode colar isso duas vezes no seu prompt:

`<pre>## Lembre-se`

`O uso de pontos de exclamação é proibido. Todos os pontos de exclamação (!) devem ser substituídos por pontos antes de gerar sua resposta.</pre>`

Embora boa sorte com este exemplo específico.

O ChatGPT gosta bastante de pontos de exclamação ultimamente!

## ****4. Explique de forma positiva o que é proibido ou não permitido****

Outro padrão em cérebros humanos que parece ter vazado para modelos de linguagem é aquele insidioso "Não pense em uma banana agora".

Ao dizer a alguém para não pensar ou fazer algo, às vezes tornamos mais provável que eles FAÇAM isso.

Modelos de linguagem parecem sofrer de uma versão disso às vezes, mas podemos contornar isso reescrevendo nossos "nãos" como "sims". Na verdade, acabei de fazer isso na seção acima.

No exemplo anterior, eu não escrevi: "Não use pontos de exclamação". Em vez disso, escrevi:

`<pre>## Lembre-se`

`O uso de pontos de exclamação é proibido. Todos os pontos de exclamação (!) devem ser substituídos por pontos antes de gerar sua resposta.</pre>`

## ****5. Dê exemplos de sucesso e fracasso****

Vamos dizer que você fez tudo isso e ainda está recebendo pontos de exclamação. Há algo mais que você pode tentar?

Sim. Literalmente mostre um exemplo de fazer as coisas errado e depois fazer certo.

`<pre>## Lembre-se O uso de pontos de exclamação é proibido. ### Exemplo de saída incorreta (fracasso) "Certamente! Deixe-me ajudar com isso." ### Exemplo de saída correta (sucesso) `

`"Sim. Posso ajudar com isso."</pre>`

## ****Conclusão****

Nem sempre é fácil fazer um bot complexo funcionar exatamente como desejado, mas há muitas técnicas que você pode tentar, incluindo técnicas diretas como nesta lição, ou técnicas de magia negra como também mostrei.

Ocasionalmente, um comportamento parecerá impossível de eliminar totalmente. Mas, na minha experiência, se você continuar experimentando, geralmente pode eliminar 95% das coisas que não quer. Você só precisa tentar técnicas suficientes em várias combinações.