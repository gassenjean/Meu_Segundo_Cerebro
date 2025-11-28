---
criado: 2024-10-02T11:14:07-03:00
atualizado: 2025-07-09T20:27:08-03:00
---
## Tree of Thoughts (ToT) (74% + Qualidade nos Prompts)

Nesta aula, vamos aprender:

- O que é ToT e como difere de CoT
- Como ToT permite explorar múltiplos caminhos de raciocínio
- Aplicando ToT na prática com exemplos passo-a-passo
- Truques, melhores práticas e limitações de ToT
- Aplicações de ToT no mundo real dos negócios

## O que é Tree of Thoughts (ToT)?

Tree of Thoughts (ToT) é um framework que generaliza o CoT permitindo à IA explorar múltiplos caminhos de raciocínio em paralelo, em uma estrutura de árvore.

Vamos recapitular rapidamente:

- No **prompting padrão**, damos um prompt e o modelo gera uma resposta direta.
- Com **CoT**, o modelo gera uma cadeia linear de pensamentos intermediários antes da resposta.
- Agora com **ToT**, o modelo explora uma árvore de pensamentos, podendo considerar diferentes abordagens, fazer lookahead e backtracking.

A ideia central de ToT é tratar a solução de problemas como uma busca em um espaço de estados, onde cada nó é um estado parcial (prompt + pensamentos até agora) e cada aresta é uma operação que gera um novo pensamento.

Isso permite à IA:

1. Manter múltiplos caminhos promissores em paralelo
2. Avaliar o progresso de cada estado parcial
3. Podar ramos infrutíferos e voltar atrás quando necessário
4. Tomar decisões de forma mais global e deliberada

Em essência, ToT capacita as IAs com um "Sistema 2" de raciocínio lento e ponderado, guiado por algoritmos de busca em árvore conhecidos, como busca em largura (BFS) ou profundidade (DFS).

A estrutura ToT é ilustrada abaixo:

![](https://api-club-file.cb.hotmart.com/public/v5/files/23a4e52e-73fc-439b-9aaf-91d4b29be897)

Fonte da imagem: [Yao et el. (2023)](https://arxiv.org/abs/2305.10601)

Usando um algoritmo de busca em largura (BFS) com ToT, o GPT-4 passa a acertar impressionantes 74% dos problemas!

O segredo é permitir que a IA explore sistematicamente o espaço de soluções, podando caminhos impossíveis de antemão e iterando até convergir na resposta.

O processo é ilustrado abaixo:

![](https://api-club-file.cb.hotmart.com/public/v5/files/618942b8-fd94-4a38-b1e2-d42ba66ff4e5)

Fonte da imagem: [Yao et el. (2023)(opens in a new tab)](https://arxiv.org/abs/2305.10601)

Pelos resultados relatados na figura abaixo, a ToT supera substancialmente os outros métodos de estímulo:

![](https://api-club-file.cb.hotmart.com/public/v5/files/29bb8e77-5651-4a12-aaa5-796896e5b5ce)

Fonte da imagem: [Yao et el. (2023)](https://arxiv.org/abs/2305.10601)

Imagine que três especialistas diferentes estão respondendo a esta pergunta.

Todos os especialistas escreverão 1 passo do seu raciocínio, depois compartilharão com o grupo.

Então todos os especialistas passarão para o próximo passo, e assim por diante.

Se algum especialista perceber que está errado em qualquer ponto, ele sairá.

A pergunta é...

## ToT na Prática: Escrita Criativa

Ok, mas e se o problema for mais aberto e subjetivo, como escrever uma história coerente? Vamos ver!

Digamos que queremos gerar um texto de 4 parágrafos, cada um terminando com uma frase dada. Por exemplo: Frases de entrada:

1. Não é difícil fazer uma cambalhota se você apenas ficar de pé nas mãos.
2. Meu chapéu de guarda capturou o cheiro de bife selado.
3. Quando ela não gostou do cara que estava tentando pegá-la, ela começou a usar linguagem de sinais.
4. Cada pessoa que te conhece tem uma percepção diferente de quem você é.

Com ToT, podemos primeiro gerar diversos "planos de escrita" de alto nível, votar no melhor, e então gerar vários textos seguindo esse plano e escolher o mais coerente.

Um exemplo de plano gerado:

1. Introduzir um livro de autoajuda e mencionar fazer cambalhota como uma metáfora para abraçar desafios.
2. Falar das coisas inesperadas que aprendemos com os astronautas, incluindo o cheiro do espaço.
3. Descrever a tática esperta de uma mulher para evitar atenção indesejada em um bar.
4. Refletir em como diferentes percepções de si mesmo podem moldar sua identidade.

Seguindo esse plano, a IA consegue gerar textos muito mais coerentes, criativos e fiéis às frases dadas do que com prompting linear. A votação também serve como um mecanismo de autoconsistência "local".

## Dicas e Melhores Práticas de ToT

- Use ToT quando CoT "normal" não for suficiente e o problema puder ser decomposto em passos/decisões
- Projete cuidadosamente como dividir os pensamentos - nem muito grandes nem pequenos
- Dê exemplos de geração e avaliação de pensamentos para orientar a IA
- Ajuste os hiperparâmetros (largura/profundidade da busca, limites de tempo/espaço, etc.) conforme necessário
- Analise a árvore gerada para entender o raciocínio e identificar pontos de melhoria
- Combine com técnicas como Zero-Shot e Auto-CoT quando tiver poucos exemplos

## Aplicações no Mundo Real

ToT pode ser útil em vários problemas do mundo real que requerem raciocínio complexo e exploração de alternativas:

- **Planejamento e scheduling**: Gere planos/agendas com múltiplos recursos e restrições e encontre a solução ideal. Ex: Alocar salas e horários para um evento minimizando custos e conflitos.
- **Arquitetura e Design**: Explore diferentes layouts e designs considerando múltiplos critérios (estética, funcionalidade, orçamento, etc.)Ex: Projetar a planta de um escritório para maximizar colaboração e privacidade.
- **Estratégia e tomada de decisão**: Analise cenários e caminhos de ação futuros para tomar decisões robustas. Ex: Escolher em quais mercados e produtos investir baseado em tendências e riscos.
- **Resolução de problemas técnicos**: Solucione bugs e otimize código/sistemas explorando diferentes abordagens.Ex: Debugar um erro complexo em um app considerando diferentes causas-raízes.
- **Criação de conteúdo**: Gere roteiros, narrativas, anúncios, etc. explorando diferentes estruturas e estilos. Ex: Criar um post de blog comparando os prós e contras de diferentes formatos.

Em todos esses casos, ToT permite considerar múltiplas possibilidades, avaliar trade-offs e convergir para soluções de alta qualidade - exatamente como um especialista humano faria.

## Limitações e Riscos de ToT

Embora poderosa, ToT não é perfeita nem uma bala de prata. Principais limitações:

- Requer muito mais computação e chamadas de API que prompts normais (mas a flexibilidade permite equalizar custos)
- Depende da capacidade da IA de gerar e avaliar pensamentos. Falhas nisso podem levar a resultados ruins.
- Não substitui conhecimentos específicos do domínio. Combinar ToT com recuperação pode ser necessário.
- O espaço de busca pode explodir em problemas grandes. Heurísticas de poda são cruciais.
- Pode gerar pensamentos/ações incoerentes ou inseguros se não for bem instruída. Alinhamento ainda é chave.

Mas acreditamos que, com uso responsável, ToT pode sim elevar as IAs a novos patamares de raciocínio e resolução de problemas - possibilitando aplicações cada vez mais complexas e impactantes.

## Resumo

- Tree of Thoughts (ToT) permite às IAs explorar múltiplos caminhos de raciocínio em uma árvore de busca
- A cada passo, novos pensamentos são gerados, avaliados e priorizados/podados
- Algoritmos como BFS e DFS guiam a exploração do espaço de solução de forma mais global e deliberada
- ToT melhora muito a performance em problemas complexos como jogos, escrita criativa e palavras cruzadas
- Aplicações no mundo real incluem planejamento, design, estratégia, debugging e criação de conteúdo
- ToT tem limitações de custo e dificuldade, mas enorme potencial de elevar o raciocínio e impacto das IAs

Ficou curioso para testar ToT nos seus próprios problemas e projetos? Deixamos abaixo os notebooks e prompts para você se aprofundar.

Na próxima aula, vamos explorar como combinar ToT com técnicas ainda mais avançadas como aprendizado por reforço. O céu (ou a árvore) é o limite!

Obrigado por acompanhar essa jornada rumo ao raciocínio de alto nível das IAs. Juntos, estamos abrindo novas fronteiras do que é possível com linguagem natural.

## Referências

1. Yao, S., Yu, D., Zhao, J., Shafran, I., Narasimhan, K., Cao, Y. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. arXiv.
2. Gao, L., Madaan, A., Zhou, S., Liu, Y., Yang, J.G. (2023). PAL: Program-aided Language Models. arXiv.
3. Dohan, D. et al. (2022). Language Model Cascades. arXiv.

## Recursos Adicionais

Estudos

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903), Jan 2022.
- [Large Language Model Guided Tree-of-Thought](https://arxiv.org/abs/2305.08291), 15 May 2023. [Github](https://github.com/jieyilong/tree-of-thought-puzzle-solver).
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601), 17 May 2023. [Github](https://github.com/princeton-nlp/tree-of-thought-llm)
- [Tree of Thoughts](https://github.com/kyegomez/tree-of-thoughts) Github, 21st May 2023


# ia



A Árvore de Pensamentos (ToT) é um framework que permite às IAs explorar múltiplos caminhos de raciocínio de forma sistemática e deliberada, utilizando uma estrutura de árvore de busca. Isso permite às IAs considerar diferentes abordagens, avaliar trade-offs e convergir para soluções de alta qualidade.

## Principais Características da ToT:

1. **Exploração de múltiplos caminhos**: A ToT permite às IAs explorar diferentes caminhos de raciocínio em paralelo, em vez de se limitar a uma única abordagem.
2. **Estrutura de árvore**: A ToT utiliza uma estrutura de árvore para organizar os pensamentos e decisões, permitindo que as IAs avaliem e priorizem diferentes opções.
3. **Avaliação e priorização**: A ToT permite às IAs avaliar e priorizar diferentes opções, permitindo que elas sejam mais eficientes e eficazes em sua busca por soluções.
4. **Uso de algoritmos de busca**: A ToT utiliza algoritmos de busca, como a busca em largura (BFS) e a busca em profundidade (DFS), para guiar a exploração do espaço de solução.

## Aplicações da ToT:

1. **Planejamento e scheduling**: A ToT pode ser usada para gerar planos e agendas que minimizem custos e conflitos.
2. **Arquitetura e design**: A ToT pode ser usada para explorar diferentes layouts e designs que considerem múltiplos critérios.
3. **Estratégia e tomada de decisão**: A ToT pode ser usada para analisar cenários e caminhos de ação futuros para tomar decisões robustas.
4. **Resolução de problemas técnicos**: A ToT pode ser usada para solucionar bugs e otimizar código/sistemas explorando diferentes abordagens.
5. **Criação de conteúdo**: A ToT pode ser usada para gerar roteiros, narrativas, anúncios, etc. explorando diferentes estruturas e estilos.

## Limitações e Risc