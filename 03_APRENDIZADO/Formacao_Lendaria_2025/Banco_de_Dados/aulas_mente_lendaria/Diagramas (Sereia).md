---
criado: 2024-10-01T11:02:08-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir 

## O que é?

Diagramas são tipo a língua universal do seu cérebro. Eles transformam ideias complexas em algo tão simples que até o seu sobrinho de 5 anos entenderia. Com o Mermaid e o Obsidian, você vai criar diagramas consegue organizar seu caos mental diário, tudo num piscar de olhos. É como ter superpoderes, só que sem a necessidade de uma cueca por cima das calças.

## Por que usar?

Explicar qualquer coisa complicada — seja um algoritmo, uma estrutura de base de código ou um plano de projeto

## Mas por que precisamos de diagramas?

Cérebros humanos são mestres quando se trata de entender imagens e padrões, muito mais do que textos. Processamos uma estrutura complexa mais rápido se vemos sua representação visual, e acaba que também a lembramos melhor — isso é chamado de efeito de superioridade da imagem. É intuitivo, não é mesmo? Você pode sacar as conclusões de um gráfico de barras ou de pizza muito mais rápido do que lendo uma lista de números.

E imagens? Elas captam a atenção da galera. Se você dá uma explicação longa e complicada sem uma ajudinha visual, a maioria da sua audiência vai estar viajando depois de um minuto, ou já terá esquecido o início. Mas se você incluir um diagrama, eles podem voltar à sua explicação.

Elas também são úteis para você mesmo se quiser entender algo que requer mais informação do que sua memória de trabalho pode lidar. Desenhar a arquitetura de código de alto nível, o fluxo de informações em um componente ou os designs de classes OOP de nível inferior podem ajudar você a identificar erros de design de cara, quando é mais barato corrigir.

## Agora, o que faz do Mermaid uma parada muito fod@

Diferente de muitos outros softwares de desenho de gráficos baseados em GUI, o Mermaid é totalmente baseado em texto. Nada de arrastar caixas e setas, esqueça seu mouse, você apenas digita código baseado numa sintaxe inspirada no Markdown. Isso torna os diagramas super fáceis de manter. Você sempre terá o código que gerou o diagrama, então você não vai terminar com um arquivo de imagem bonito, mas desatualizado que você não pode mais modificar.

Isso também significa que você pode facilmente ver as mudanças em um diagrama, diferente de qualquer outro método baseado em imagem. E isso é perfeito aqui com Obsidian, você pode até mesmo linkar suas notas dentro do Diagrama.

## E o que o Mermaid pode fazer?

Vamos dar uma olhada em alguns exemplos que o Mermaid pode renderizar para nós, e como é o código que gera isso:

Você pode adicionar diagramas e gráficos às suas anotações, usando [Mermaid](https://mermaid.js.org/). O Mermaid suporta uma variedade de diagramas, como fluxogramas, diagramas de sequência e linhas do tempo.

Por exemplo, um diagrama de sequência pode ser usado para representar a interação entre objetos em um sistema. Já um diagrama de classes pode ser usado para representar as classes e seus relacionamentos em um sistema orientado a objetos. O Mermaid também suporta a criação de diagramas de fluxo, que podem ser usados para representar processos e fluxos de trabalho

**Tipos de diagrama que você pode fazer com ele:**

- Diagrama de fluxo
- Diagrama de sequência
- Diagrama de classes
- Diagrama de estados
- Diagrama de Gantt
- Diagrama de rede
- Diagrama de entidade-relacionamento (ERD)

## Vamos para alguns exemplos:

### Diagrama de entidade-relacionamento (ERD):

Código:

`   ```mermaiderDiagram CUSTOMER ||--o{ ORDER : places ORDER ||--|{ LINE-ITEM : contains CUSTOMER }|..|{ DELIVERY-ADDRESS : uses ```   `

Resultado:

![](https://api-club-file.cb.hotmart.com/public/v5/files/c5b4c292-0d30-4a3f-aee9-f7bde57126c3)

### Diagrama de Estados:

Código:

`   ```mermaid stateDiagram-v2 state if_state <<choice>> [*] --> IsPositive IsPositive --> if_state if_state --> False: if n < 0 if_state --> True : if n >= 0 ```   `

Resultado:

![](https://api-club-file.cb.hotmart.com/public/v5/files/33837ea2-6536-44b1-9718-740759f38671)

  

---

##   
Tutorial Completo em Inglês

[](https://youtu.be/Tsu02d6Qti0)https://youtu.be/Tsu02d6Qti0

---

## Próximos Passos:

1. ♾️ Se você chegou até aqui imagino que seja um heavy user, um lendário avançado no uso de tecnologia, então aconselho a ler a documentação do Mermaind [**» clicando aqui «**](https://mermaid.js.org/intro/)
2. 💬 Deixe seu comentário.
3. 👉 Avance para próxima aula.


# ia



O artigo discute sobre a importância de utilizar diagramas para comunicar ideias complexas de forma simples e eficaz. Ele apresenta o Mermaid, uma ferramenta de criação de diagramas baseada em texto, que permite criar diagramas de fluxo, sequência, classes, estados e outros tipos de diagramas.

O artigo destaca as vantagens do uso de diagramas, como:

* Eles são mais fáceis de entender do que textos longos e complicados
* Eles captam a atenção da audiência
* Eles são úteis para identificar erros de design e melhorar a compreensão de sistemas complexos

O Mermaid é apresentado como uma ferramenta poderosa para criar diagramas de forma fácil e rápida. Ele é baseado em texto e utiliza uma sintaxe inspirada no Markdown, o que torna os diagramas fáceis de manter e atualizar.

O artigo também inclui exemplos de código e diagramas criados com o Mermaid, como diagramas de entidade-relacionamento (ERD) e diagramas de estados.

Em resumo, o artigo apresenta o Mermaid como uma ferramenta útil para criar diagramas de forma eficaz e simples, e destaca a importância de utilizar diagramas para comunicar ideias complexas.

**Pontos principais:**

* O Mermaid é uma ferramenta de criação de diagramas baseada em texto
* Ele permite criar diagramas de fluxo, sequência, classes, estados e outros tipos de diagramas
* O Mermaid é fácil de usar e permite criar diagramas de forma rápida
* Ele é útil para identificar erros de design e melhorar a compreensão de sistemas complexos
* O Mermaid é baseado em texto e utiliza uma sintaxe inspirada no Markdown.