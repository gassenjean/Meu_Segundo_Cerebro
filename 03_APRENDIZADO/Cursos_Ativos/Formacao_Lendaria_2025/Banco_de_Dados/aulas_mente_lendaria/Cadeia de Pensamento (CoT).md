---
criado: 2024-10-01T11:16:53-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir

# **Sugestão da cadeia de pensamento**

Quando mesmo o few-shot não é suficiente?

É aí que entra o Prompting da Cadeia de Pensamento (CoT)!

Nesta aula, vamos aprender:

- O que é CoT Prompting e como ele difere do prompting tradicional
- Como aplicar CoT Prompting para resolver problemas de raciocínio complexo
- Técnicas avançadas como Zero-Shot CoT e Auto-CoT
- Dicas práticas, exemplos de uso e aplicações no mundo dos negócios
- Uma prévia da próxima técnica que vamos estudar: Self-Consistency

Então vamos lá, é hora de levar seus prompts para o próximo nível! 🚀

## O que é Chain-of-Thought Prompting?

Chain-of-Thought (CoT) Prompting é uma técnica avançada que incentiva os Grandes Modelos de Linguagem (LLMs) a explicarem seu raciocínio passo a passo antes de chegar à resposta final.

A ideia central do CoT é que, ao mostrar exemplos (few-shot) onde o processo de raciocínio é explicado, o modelo aprende a mostrar seu próprio raciocínio ao responder novos prompts. E essa explicação geralmente leva a resultados mais precisos e interpretáveis.

## Aplicando CoT Prompting na Prática

![](https://api-club-file.cb.hotmart.com/public/v5/files/f7e95dd0-d7dc-44ba-a126-d31bf22cfb3e)

Saída:

![](https://api-club-file.cb.hotmart.com/public/v5/files/1fb98194-2e0a-4a3f-9707-d46e7b9dc836)

Explicando um PDF:

![](https://api-club-file.cb.hotmart.com/public/v5/files/db7d4709-52e0-4f76-93a2-9af6a4cff310)

Saída:

### ![](https://api-club-file.cb.hotmart.com/public/v5/files/2d5f3ced-00c8-428b-bf8f-c328af2a61d8)

### Aplicações Práticas de CoT Prompting

O CoT Prompting pode ser uma ferramenta poderosa em várias áreas de negócios:

- **Marketing**: Gere explicações passo a passo de como uma campanha de marketing levará aos resultados desejados, tornando a estratégia mais clara e convincente.
- **Gestão de Projetos**: Decomponha tarefas complexas em etapas menores e mais gerenciáveis, explicando a lógica por trás de cada passo. Isso ajuda a equipe a entender melhor seus papéis e responsabilidades.
- **Análise de Dados**: Interprete resultados de análises complexas, detalhando o raciocínio por trás de cada insight. Isso torna as descobertas mais acessíveis e acionáveis para tomadores de decisão.
- **Criação de Conteúdo**: Gere artigos, posts e ebooks com uma estrutura lógica clara, fornecendo exemplos passo a passo de conceitos chave. Isso torna o conteúdo mais envolvente e educativo.

CoT é especialmente valioso para problemas que requerem múltiplas etapas de raciocínio ou têm várias considerações a serem analisadas. Quanto mais complexa a tarefa, maior o benefício potencial do CoT.

## Técnicas Avançadas de CoT

### CoT de tiro zero

E se você não tiver bons exemplos para dar? Entra em cena o Zero-Shot CoT!

_Rápido:_

I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

_Output:_

11 apples

A resposta está incorreta! Agora vamos tentar com o prompt CoT.

_Prompt:_

I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?Let's think step by step.

_Output:_

First, you started with 10 apples.You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.Then you bought 5 more apples, so now you had 11 apples.Finally, you ate 1 apple, so you would remain with 10 apples.

A ideia é simplesmente adicionar a frase "Vamos pensar passo a passo" ao prompt original.

Rápido:

Fui ao mercado e comprei 10 maçãs. Dei 2 maçãs para o vizinho e 2 para o técnico. Depois comprei mais 5 maçãs e comi 1. Com quantas maçãs fiquei?

Vamos pensar passo a passo:

Resposta:

Primeiro, você começou com 10 maçãs.

Você deu 2 maçãs para o vizinho e 2 para o técnico, ficando com 6 maçãs.

Então você comprou mais 5 maçãs, ficando com 11 maçãs.

Por fim, você comeu 1 maçã, sobrando 10 maçãs.

Portanto, você ficou com 10 maçãs.

![](https://api-club-file.cb.hotmart.com/public/v5/files/a6454710-576d-4e49-9bda-ef92985bb567)

Incrível como esse prompt simples já faz o modelo explicar seu raciocínio! Isso é especialmente útil quando você não tem muitos exemplos para dar.

## Resumo

- A Solicitação da Cadeia de Pensamento permite que os LLMs expliquem seu raciocínio passo a passo
- CoT leva a respostas mais precisas e interpretáveis em tarefas complexas
- Zero-Shot CoT e Auto-CoT facilitam a aplicação de CoT sem muitos exemplos
- CoT tem aplicações práticas em marketing, gestão de projetos, análise de dados e criação de conteúdo
- CoT pode ser combinado com Self-Consistency (prévia da próxima aula) para melhorar ainda mais a precisão

Experimente aplicar CoT aos seus prompts e veja a mágica acontecer! Na próxima aula vamos elevar ainda mais com Self-Consistency.

Até lá, divirta-se explorando o poder do raciocínio passo-a-passo em seus projetos! E compartilhe seus prompts e resultados no fórum para inspirar os colegas.

## Referências

[https://arxiv.org/pdf/2201.11903](https://arxiv.org/pdf/2201.11903)

[https://arxiv.org/pdf/2309.15402](https://arxiv.org/pdf/2309.15402)

[https://arxiv.org/pdf/2203.11171](https://arxiv.org/pdf/2203.11171)

1. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E., Le, Q., & Zhou, D. (2022). A cadeia de estímulo da cadeia de pensamento provoca o raciocínio em grandes modelos de linguagem. pré-impressão arXiv arXiv:2201.11903.
2. Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Grandes modelos de linguagem são raciocinadores zero-shot. pré-impressão arXiv arXiv:2205.11916.
3. Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., & Zhou, D. (2022). A autoconsistência melhora o raciocínio da cadeia de pensamento em modelos de linguagem. pré-impressão arXiv arXiv:2203.11171.
4. Zhang, J., Yao, N., Xie, S., Chen, H., Yin, R., Jia, R., ... & Wang, X. (2023). Solicitação automática de cadeia de pensamento em grandes modelos de linguagem. pré-impressão arXiv arXiv:2210.03493.

## Recursos Adicionais

[https://www.mercity.ai/blog-post/guide-to-chain-of-thought-prompting](https://www.mercity.ai/blog-post/guide-to-chain-of-thought-prompting)

# ia

O texto apresenta uma explicação detalhada sobre o Chain-of-Thought (CoT) Prompting, uma técnica avançada para melhorar a precisão e interpretabilidade dos modelos de linguagem grandes (LLMs). Aqui está um resumo dos principais pontos:

**O que é CoT Prompting?**

CoT Prompting é uma técnica que incentiva os LLMs a explicar seu raciocínio passo a passo antes de chegar à resposta final. Isso é feito adicionando uma frase ao prompt original, como "Vamos pensar passo a passo".

**Benefícios do CoT Prompting**

- Leva a respostas mais precisas e interpretáveis em tarefas complexas
- Pode ser especialmente útil para problemas que requerem múltiplas etapas de raciocínio ou têm várias considerações a serem analisadas

**Técnicas Avançadas de CoT**

- Zero-Shot CoT: permite que os LLMs expliquem seu raciocínio sem exemplos prévios
- Auto-CoT: facilita a aplicação de CoT sem muitos exemplos

**Aplicações Práticas de CoT**

- Marketing: geração de explicações passo a passo de estratégias de marketing
- Gestão de Projetos: decomposição de tarefas complexas em etapas menores e mais gerenciáveis
- Análise de Dados: interpretação de resultados de análises complexas
- Criação de Conteúdo: geração de artigos, posts e ebooks com uma estrutura lógica clara

**Referências**

O texto inclui referências a artigos acadêmicos que discutem a técnica de CoT Prompting e suas aplicações.

**Recursos Adicionais**

O texto inclui um link para um guia adicional sobre CoT Prompting.

Em resumo, o CoT Prompting é uma técnica poderosa para melhorar a precisão e interpretabilidade dos LLMs, com aplicações práticas em várias áreas. A técnica pode ser especialmente útil para problemas complexos que requerem múltiplas etapas de raciocínio.
