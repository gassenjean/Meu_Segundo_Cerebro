---
criado: 2025-08-20T09:59:09-03:00
atualizado: 2025-08-20T09:59:24-03:00
---
# E-Book

---

# Guia Completo do Nó EditFields no N8N: Manipulando Dados com Eficiência

## Introdução

Bem-vindos a este guia completo sobre o nó EditFields no N8N, anteriormente conhecido como nó 7. Este recurso é fundamental para qualquer um que deseje manipular dados de forma eficiente dentro de seus fluxos de trabalho. Neste ebook, vamos explorar em profundidade como utilizar o EditFields para transformar, formatar e aprimorar seus dados, tornando-os mais úteis para suas necessidades específicas.

O nó EditFields é uma ferramenta poderosa no N8N que permite a manipulação de dados de entrada. Ele funciona como um processador de variáveis, permitindo que você altere, formate e transforme dados de variados tipos, incluindo strings, números, booleans, arrays e objetos. Com o EditFields, você pode criar fluxos de trabalho mais eficientes e automatizar tarefas que antes eram feitas manualmente.

## Entendendo o Nó EditFields

### O que é o Nó EditFields?

O nó EditFields é uma ferramenta essencial para qualquer usuário do N8N que deseje manipular dados de forma eficiente. Ele permite que você altere, formate e transforme dados de variados tipos, tornando-os mais úteis para suas necessidades específicas.

### Interface Básica do Nó

Ao adicionar um nó EditFields ao seu fluxo, você será apresentado a uma interface intuitiva. O principal campo de atuação é o "Fields", onde você pode adicionar, remover ou modificar variáveis. Cada campo pode ser configurado para um tipo específico de dado, como string, número, booleano, array ou objeto.

### Configuração Inicial

Vamos configurar um exemplo básico para ilustrar como o EditFields funciona. Suponha que temos as seguintes variáveis:

- **Nome**: "Adável"
- **Sobrenome**: "Titone"
- **E-mail**: "adavel.titone@test.com"
- **Aluno**: true

Ao executar o fluxo, o EditFields retornará exatamente o que foi configurado, permitindo que você veja como as variáveis são processadas.

## Configurações Básicas e Manipulações

### Tipos de Dados no EditFields

Antes de mergulharmos nas manipulações, é essencial entender os tipos de dados que o EditFields suporta:

- **String**: Qualquer texto, como nomes, endereços ou descrições.
- **Número**: Valores numéricos que podem ser usados em cálculos.
- **Booleano**: Valores verdadeiro ou falso, úteis para condições lógicas.
- **Array**: Listas de itens, úteis para coletar múltiplos valores.
- **Objeto**: Estruturas de dados complexas, geralmente usadas para dados JSON.

### Configuração Inicial

Vamos configurar um exemplo básico para ilustrar como o EditFields funciona. Suponha que temos as seguintes variáveis:

- **Nome**: "Adável"
- **Sobrenome**: "Titone"
- **E-mail**: "adavel.titone@test.com"
- **Aluno**: true

Ao executar o fluxo, o EditFields retornará exatamente o que foi configurado, permitindo que você veja como as variáveis são processadas.

## Manipulações Avançadas com Expressões

### Introdução às Expressões

As expressões no EditFields permitem que você vá além das configurações fixas, tornando suas manipulações mais dinâmicas e adaptáveis. Existem várias expressões úteis que você pode usar para transformar seus dados.

### Expressão Replace

A expressão Replace é usada para substituir partes de um texto. Por exemplo, se você tiver um e-mail "adavel.titone@test.com" e deseja alterar o domínio para "suaempresa.com", pode usar a seguintão configuração:

- **Pattern**: "test.com"
- **Replacement**: "suaempresa.com"

Isso resultará no e-mail "adavel.titone@suaempresa.com".

### Expressão LENTE

A expressão LENTE é usada para contar o número de caracteres em uma string. Isso é particularmente útil para validar dados como CPFs, que devem ter exatamente 11 dígitos.

### Expressão Split

A expressão Split divide uma string em uma lista (array) com base em um caractere delimitador. Por exemplo, dividindo "adavel.titone@test.com" pelo caractere "@" resultaria na lista ["adavel.titone", "test.com"].

### Expressão Slice

A expressão Slice permite extrair uma parte específica de uma string. Por exemplo, para remover o "W" de "WAdável Titone", você pode iniciar do caractere 1, resultando em "Adável Titone".

## Aplicações Práticas

### Preparação de Dados para CRM

Imagine que você está importando leads de um formulário e deseja formatar os nomes completos antes de enviá-los para seu CRM. Usando o EditFields, você pode combinar os campos "Nome" e "Sobrenome" em um único campo "Nome Completo".

### Formatação de E-mails

Se você receber e-mails em um formato que deseja alterar, como mudar o domínio, o EditFields pode ajudar a automatizar essa tarefa, economizando tempo e reduzindo erros manuais.

## Conclusão

O nó EditFields é uma ferramenta indispensável para qualquer usuário do N8N que deseje manipular dados de forma eficiente. Com suas capacidades de transformação, formatação e validação, ele torna possíveis uma infinidade de tarefas que seriam complicadas ou demoradas de outra forma. Esperamos que este guia tenha fornecido uma compreensão clara de como aproveitar ao máximo o EditFields em seus fluxos de trabalho. Continue explorando e descobrindo novas maneiras de otimizar seus processos com o N8N!