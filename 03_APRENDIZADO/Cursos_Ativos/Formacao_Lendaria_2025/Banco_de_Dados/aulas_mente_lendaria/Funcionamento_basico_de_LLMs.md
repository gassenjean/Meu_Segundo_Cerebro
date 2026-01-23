---
criado: 2024-10-01T11:57:23-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir

### **Por dentro do motor dos LLMs**

Vamos agora desvendar os segredos por trás desses modelos. Como eles conseguem processar e gerar linguagem tão bem?

Tudo começa quando o LLM "lê" um texto. Ele quebra o texto em pequenos pedaços chamados tokens. Cada token pode ser uma palavra, parte de palavra ou símbolo. O LLM transforma esses tokens em números que seus "neurônios" conseguem entender.

Depois, ele faz previsões estatísticas para determinar qual será o próximo token, levando em conta todos os tokens anteriores. É assim que ele gera novo texto ou completa nosso prompt, token por token!

Agora que sabemos o básico de como os LLMs funcionam, é hora de aprender a controlar essas poderosas máquinas de linguagem para obter os resultados que queremos.

Podemos usar certas configurações do LLM para controlar vários aspectos do modelo, como o quão 'aleatório' ele é. Essas configurações podem ser ajustadas para produzir resultados mais criativos, diversificados e interessantes. As configurações de temperatura, P superior e comprimento máximo são mais importantes, mas descrevemos todas as configurações que o OpenAI Playground permite modificar.

---

## Temperatura

![](https://api-club-file.cb.hotmart.com/public/v5/files/90af88d7-6d7d-434d-9fcb-f21f2724c07c)

A temperatura regula a imprevisibilidade da saída de um modelo de linguagem. Com configurações de temperatura mais altas, os resultados tornam-se mais criativos e menos previsíveis, pois amplificam a probabilidade de tokens menos prováveis e, ao mesmo tempo, reduzem a probabilidade de tokens mais prováveis. Por outro lado, temperaturas mais baixas produzem resultados mais conservadores e previsíveis. O exemplo a seguir ilustra essas diferenças na saída:

![](https://api-club-file.cb.hotmart.com/public/v5/files/6d20758c-891a-4f33-bf77-9dbe63d80274)

![](https://api-club-file.cb.hotmart.com/public/v5/files/bbdb3d30-f535-44c9-b742-4441a883cbf1)

![](https://api-club-file.cb.hotmart.com/public/v5/files/e3c052dd-7f31-47d7-ab32-98e9a27f5be5)

---

​

![](https://api-club-file.cb.hotmart.com/public/v5/files/0685243d-ec73-464b-a7d4-b3fae5a447c9)

![](https://api-club-file.cb.hotmart.com/public/v5/files/158adc95-339a-494b-90ef-976dffb26b26)

![](https://api-club-file.cb.hotmart.com/public/v5/files/d1497193-669a-435d-9058-b57f49f39aa3)

---

## Topo P

![](https://api-club-file.cb.hotmart.com/public/v5/files/aea0d467-2f1a-4d7e-8823-f4e5001f9967)

​

Top P é uma configuração em modelos de linguagem que ajuda a gerenciar a aleatoriedade de sua saída. Funciona estabelecendo um limite de probabilidade e, em seguida, selecionando tokens cuja probabilidade combinada ultrapasse esse limite.

Por exemplo, vamos considerar um exemplo em que o modelo prevê a próxima palavra em 'The cat climbed up the \_\_\_'. As cinco principais palavras que podem ser consideradas poderiam ser 'tree'(probabilidade 0,5), 'roof'(probabilidade 0,25), 'wall'(probabilidade 0,15), 'window'(probabilidade 0,07) e 'carpet', com probabilidade de 0,03.

Se definirmos Top P como '.90', a IA considerará apenas os tokens que somam cumulativamente pelo menos ~90%. No nosso caso:

- Adicionando 'tree'-> total até agora é '50%'.

- Em seguida, adicionando 'roof'-> total torna-se '75%'.

- Em seguida vem 'wall', e agora nossa soma chega a '90%'.

Portanto, para gerar resultados, a IA escolherá aleatoriamente uma entre essas três opções ( 'tree',, 'roof'e 'wall'), pois elas representam cerca de 90 por cento de todas as probabilidades. Este método pode produzir resultados mais diversos do que os métodos tradicionais que amostram todo o vocabulário indiscriminadamente porque restringe as escolhas com base em probabilidades cumulativas, em vez de tokens individuais.

---

## Comprimento Máximo

![](https://api-club-file.cb.hotmart.com/public/v5/files/1bcd699c-e940-4f31-9ff8-caabb36e3e23)

​

O comprimento máximo é o número total de tokens que a IA pode gerar. Esta configuração é útil porque permite aos usuários gerenciar a duração da resposta do modelo, evitando respostas excessivamente longas ou irrelevantes. Também ajuda a controlar os custos, pois o comprimento é compartilhado entre a entrada na caixa Playground e a resposta gerada.

---

## Penalidade de Frequência

![](https://api-club-file.cb.hotmart.com/public/v5/files/833a993d-a1e9-41d5-9cba-6d904377bedf)

​

A penalidade de frequência é uma configuração que desencoraja a repetição no texto gerado, penalizando os tokens proporcionalmente à frequência com que aparecem. Quanto mais frequentemente um token for usado no texto, menor será a probabilidade de a IA usá-lo novamente.

---

## Penalidade de Presença

![](https://api-club-file.cb.hotmart.com/public/v5/files/6861b326-84c2-4262-b5d1-24d37d805ec2)

​

A penalidade de presença é semelhante à penalidade de frequência, mas penaliza categoricamente os tokens com base na ocorrência ou não, em vez de proporcionalmente.

---

Concluindo, dominar configurações como temperatura, top p, comprimento máximo e outras são essenciais ao trabalhar com modelos de linguagem. Esses parâmetros permitem o controle preciso da saída do modelo para atender a tarefas ou aplicações específicas. Eles gerenciam aspectos como aleatoriedade nas respostas, duração da resposta e frequência de repetição, entre outras coisas – tudo contribuindo para melhorar sua interação com a IA.

# ia

O artigo descreve como os modelos de linguagem geram texto e como as configurações podem ser ajustadas para controlar a saída do modelo. Aqui está um resumo das principais configurações mencionadas:

1. **Temperatura**: Regula a imprevisibilidade da saída do modelo. Quanto mais alta a temperatura, mais criativos e imprevisíveis são os resultados.
2. **Top P**: Ajuda a gerenciar a aleatoriedade da saída do modelo. Funciona estabelecendo um limite de probabilidade e selecionando tokens cuja probabilidade combinada ultrapasse esse limite.
3. **Comprimento Máximo**: É o número total de tokens que a IA pode gerar. É útil para controlar a duração da resposta do modelo e evitar respostas excessivamente longas ou irrelevantes.
4. **Penalidade de Frequência**: Desencoraja a repetição no texto gerado, penalizando os tokens proporcionalmente à frequência com que aparecem.
5. **Penalidade de Presença**: Penaliza categoricamente os tokens com base na ocorrência ou não, em vez de proporcionalmente.

Essas configurações são importantes para controlar a saída do modelo e atender a tarefas ou aplicações específicas. Ao ajustar esses parâmetros, é possível melhorar a interação com a IA e obter resultados mais precisos e relevantes.

Além disso, o artigo destaca a importância de entender como os modelos de linguagem funcionam e como as configurações podem ser ajustadas para controlar a saída do modelo. Isso pode ser útil para quem trabalha com IA e deseja melhorar sua interação com os modelos de linguagem.

Em resumo, o artigo fornece uma visão geral das principais configurações dos modelos de linguagem e como elas podem ser ajustadas para controlar a saída do modelo.
