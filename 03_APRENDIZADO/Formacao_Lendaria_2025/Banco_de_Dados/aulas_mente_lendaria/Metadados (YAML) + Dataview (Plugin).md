---
criado: 2024-10-01T10:56:37-03:00
atualizado: 2025-07-09T20:27:08-03:00
---

#consumir 

## **Metadados**

Enquanto a maior parte do texto em uma nota deve ser lida por um ser humano, _metadados_ é um texto que deve ser facilmente lido por um programa, por exemplo um [plugin da comunidade](https://publish.obsidian.md/help-pt-br/Estendendo+o+Obsidian/Plugins+da+comunidade) ou o próprio Obsidian.

Você pode adicionar metadados às suas notas adicionando um bloco na primeira linha da sua nota. O bloco deve começar e terminar com três hífens (---).

Por exemplo, a nota a seguir contém dois metadados, tag e publish:

`   ---tag: diário publish: false --- # Nota diária Hoje eu aprendi sobre matéria de frente.   `

🚨 **Importante:**

Por padrão, os metadados só são visíveis na [editing view](https://publish.obsidian.md/help-pt-br/Edi%C3%A7%C3%A3o+e+formata%C3%A7%C3%A3o/Editando+e+visualizando+Markdown#Editor%20views).

Para exibir metadados na exibição de leitura:

1. Abra **Configurações**.
2. Em **Editor**, habilite **Mostrar frontmatter**.

### **Exempos de como eu uso Medata:**

Resumo de Livros:

![](https://api-club-file.cb.hotmart.com/public/v5/files/c655c200-d58a-42a7-9113-68aa6af9807b)

Com essas informações eu posso fazer consultas como se fosse um banco de dados, fazendo tabelas como essas aqui:

![](https://api-club-file.cb.hotmart.com/public/v5/files/2dab2377-cc01-4aba-8b45-cbc8327b93dc)

---

## Metadados predefinidos

Obsidian vem com um conjunto de chaves predefinidas que são importantes você já conhecer:

### Chave: Descrição

tag: Tags.  
tags: Alias para tag.  
alias: Veja Apelidos.  
aliases: Alias para alias.  
cssclass: Permite estilizar notas individuais usando Trechos de CSS.

Existem ainda os metadados predefinidos para o Obsidian Publish, que é a possibilidade paga de você publicar seu segundo cérebro na web para torná-lo acessível. Se for seu caso [» clique aqui «](https://publish.obsidian.md/help-pt-br/Obsidian+Publish/Introdu%C3%A7%C3%A3o+ao+Obsidian+Publish) para conferir.

---

## YAML

### Formato de ....

YAML é um aliado incrível para organizar suas ideias de maneira bem simples e fácil de entender. É uma linguagem feita para pessoas, não só para máquinas, então você não precisa ser um expert em tecnologia para usar.

YAML, que significa "YAML Ain't Markup Language" (em português, YAML não é uma linguagem de marcação), pode parecer um pouco confuso à primeira vista, mas não se preocupe, é só um trocadilho daqueles que deixam a gente com uma pulga atrás da orelha.

Basicamente é é um formato de configuração amplamente usado que pode ser lido por humanos e máquinas. Cada parte dos metadados consiste em uma _chave_ e um _valor_ correspondente.

As chaves são separadas de seus valores por dois pontos seguidos por um espaço:

`   --- chave: valor ---   `

Embora a ordem de cada par chave-valor não importe, cada chave deve ser única dentro de uma nota. Por exemplo, você não pode ter mais de uma chave tag.

Os valores podem ser texto, números, verdadeiro ou falso, ou até mesmo coleções de valores (arrays).

Veja este exemplo abaixo que se aplica para uma nota no Obsidian onde você vai escrever sobre um filme que assistiu:

`   --- titulo: Uma Nova Esperança ano: 1977 favorito: true elenco: - Mark Hamil - Harrison Ford - Carrie Fischer ---   `

E isso se aplica há muitas coisas, imagine que você está planejando uma viagem e não quer esquecer de nada. Você pode criar um arquivo YAML para listar todos os detalhes:

`   destinos: - Rio de Janeiro: - Praias: - Copacabana - Ipanema - Passeios: - Cristo Redentor - Pão de Açúcar - São Paulo: - Museus: - MASP - Pinacoteca - Parques: - Ibirapuera - Villa-Lobos   `

Outro exemplo bem prático é o que citei acima dos livros.

Eu também tenho usado ele para pessoas aqui no meu segundo cérebro:

Com essas informações consigo corelacionar entre notas usando inteligência artifical e criar MUITAS coisas interessantes que irei ensinar mais a frente.

---

## DATAVIEW

O Dataview é um plugin da comunidade Obsidian que transforma todas as suas notas no Obsidian em um banco de dados. Ele permite que você faça consultas complexas e personalizadas em suas notas, tornando-se uma ferramenta poderosa para gerenciar e organizar suas informações.

### **Por que utilizar o Dataview?**

O Dataview é útil para quem deseja ter um controle mais granular sobre suas notas no Obsidian. Ele permite que você faça consultas personalizadas em suas notas, o que pode ser útil para encontrar informações específicas, gerenciar tarefas, organizar reuniões, criar um glossário de termos, entre outros usos. Além disso, o Dataview é dinâmico, o que significa que as consultas são atualizadas automaticamente à medida que você adiciona ou altera suas notas.

### **Prós e contras**

**Prós:**

- Permite consultas complexas e personalizadas em suas notas.
- É dinâmico, atualizando as consultas automaticamente à medida que você adiciona ou altera suas notas.
- É altamente personalizável, permitindo que você defina seus próprios campos e critérios para suas consultas.

**Contras:**

- Pode ser um pouco complicado de aprender e usar, especialmente para usuários menos experientes.
- Requer que você anote suas notas com campos específicos para que elas possam ser incluídas nas consultas do Dataview.

### **Detalhes importantes ao utilizar a ferramenta**

Ao usar o Dataview, é importante lembrar que ele só pode consultar as notas que foram anotadas com campos específicos. Se uma nota não tem os campos que você está tentando consultar, ela não será incluída nos resultados da consulta.

Além disso, o Dataview é sensível aocaso, o que significa que "Projeto" e "projeto" seriam considerados campos diferentes. Portanto, é importante ser consistente ao anotar suas notas.

---

## Como utilizar o plugin

A sintaxe para usar o plugin Dataview no Obsidian envolve a criação de blocos de código que começam e terminam com três crases (```). Dentro desses blocos de código, você escreve suas consultas Dataview. Aqui está a estrutura básica de uma consulta Dataview:

`   ```dataview TIPO_DE_VISUALIZAÇÃO CAMPOS from LOCAL where CONDIÇÃO sort CAMPO DIREÇÃO limit NÚMERO ```   `

**Aqui está o que cada parte da consulta significa:**

- **TIPO_DE_VISUALIZAÇÃO**: Este é o tipo de visualização que você deseja para os resultados. Pode ser **table** (tabela), **list** (lista) ou **tasks** (tarefas).
- **CAMPOS:** Estes são os campos que você deseja incluir nos resultados. Por exemplo, se você está criando uma tabela de livros, você pode querer incluir os campos **title** (título), **author** (autor) e **rating** (classificação).
- **from LOCAL**: Este é o local de onde o Dataview deve buscar as notas. Pode ser uma tag (por exemplo, **#books**), uma pasta (por exemplo, **"My Books"**), ou uma nota específica (por exemplo, **"My Note"**).
- **onde CONDIÇÃO:** Esta é a condição que as notas devem atender para serem incluídas nos resultados. Por exemplo, você pode querer incluir apenas as notas que têm uma classificação de 5 (**rating = 5**).
- **sort CAMPO DIREÇÃO:** Este é o campo pelo qual você deseja ordenar os resultados, e a direção em que você deseja ordená-los. A direção pode ser **asc** (ascendente) ou **desc** (descendente).
- **limit NÚMERO:** Este é o número máximo de resultados que você deseja retornar.

Por exemplo, aqui está uma consulta Dataview que retorna uma tabela dos 5 livros com a classificação mais alta:

`   ```dataview table title, author, rating from #books where rating = 5 sort rating desc limit 5 ```   `

---

## **Formas de Visualização**

O plugin Dataview do Obsidian suporta três tipos principais de visualização: tabela, lista e tarefa. Cada tipo de visualização apresenta os resultados de maneira diferente.

### **1. Tabela**

A visualização de tabela apresenta os resultados em uma tabela. Isso é útil quando você deseja ver várias informações sobre cada nota de uma só vez.

Por exemplo, suponha que você tenha anotado suas notas de livro com campos para o título do livro, o autor e a classificação que você deu ao livro. Você poderia usar a visualização de tabela para criar uma tabela de todos os livros que você leu, com colunas para o título do livro, o autor e a classificação.

`   csharpCopy codedataview table title, author, rating from #books   `

Isso criaria uma tabela com o título, autor e classificação de cada livro que você leu.

### **2. Lista**

A visualização de lista apresenta os resultados em uma lista. Isso é útil quando você deseja ver uma lista simples de notas que atendem a certos critérios.

Por exemplo, você pode usar a visualização de lista para criar uma lista de todas as suas notas que não têm tags.

`   csharpCopy codedataview list from #notes where !contains(file.tags, "*")   `

Isso criaria uma lista de todas as suas notas que não têm tags.

### **3. Tarefa**

A visualização de tarefas apresenta os resultados como uma lista de tarefas. Isso é útil quando você deseja ver uma lista de tarefas que precisam ser concluídas.

Por exemplo, você pode usar a visualização de tarefas para criar uma lista de todas as suas tarefas pendentes.

`   bashCopy codedataview tasks from #tasks where done != true   `

Isso criaria uma lista de todas as suas tarefas que ainda não foram concluídas.

No contexto do plugin Dataview, o símbolo **#** é usado para indicar uma tag. Portanto, **from #book, #notes e #tasks** significa que a consulta deve buscar todas as notas que têm a tag **#book, #notas e #tasks**.

Tags são uma maneira de categorizar e organizar suas notas no Obsidian. Você pode adicionar quantas tags quiser a uma nota, e então usar essas tags para buscar e filtrar suas notas.

Então, se você tiver várias notas sobre diferentes livros e cada uma delas tiver a tag **#book**, você poderia usar a consulta **from #book** para buscar todas essas notas.

---

## **Parâmetros de Busca**

O plugin Dataview do Obsidian suporta vários parâmetros de busca que você pode usar para especificar de onde buscar suas notas e quais notas incluir nos resultados. Aqui estão os principais parâmetros de busca e como eles podem ser usados:

### **1. From**

O parâmetro "from" permite especificar de onde o Dataview deve buscar suas notas. Você pode buscar notas de uma tag específica, de uma pasta específica, ou notas que tenham links de entrada ou saída para uma nota específica.

Por exemplo, você pode usar o parâmetro "from" para buscar todas as notas que têm a tag "#books":

`   dataview table title, author from #books   `

Ou você pode usar o parâmetro "from" para buscar todas as notas em uma pasta específica:

`   dataview table title, author from "My Books"   `

### **2. Where**

O parâmetro "where" permite filtrar ainda mais os resultados da consulta. Você pode usar o parâmetro "where" para listar apenas as notas que atendem a uma condição específica.

Por exemplo, você pode usar o parâmetro "where" para buscar todas as notas que têm uma classificação de 5:

`   dataview table title, author from #books where rating = 5   `

Ou você pode usar o parâmetro "where" para buscar todas as notas que foram criadas após uma determinada data:

`   dataview table title, author from #books where date(created) > '2022-01-01'   `

### **3. Sort**

O parâmetro "sort" permite que você ordene os resultados da consulta com base em um campo específico. Você pode ordenar os resultados em ordem ascendente ou descendente.

Por exemplo, você pode usar o parâmetro "sort" para ordenar todos os livros que você leu por classificação, do mais alto ao mais baixo:

`   dataview table title, author, rating from #books sort rating desc   `

### **4. Limit**

O parâmetro "limit" permite que você limite o número de resultados retornados pela consulta. Isso pode ser útil se você tiver muitas notas e quiser ver apenas as primeiras ou últimas notas que atendem aos critérios da consulta.

Por exemplo, você pode usar o parâmetro "limit" para retornar apenas os 5 livros com a classificação mais alta:

`   dataview table title, author, rating from #books sort rating desc limit 5   `

### **5. Flatten**

O parâmetro "flatten" permite que você inclua subpastas na consulta. Por padrão, o Dataview busca apenas na pasta especificada e não em suas subpastas. Se você quiser incluir subpastas na consulta, pode usar o parâmetro "flatten".

Por exemplo, se você tiver uma estrutura de pastas onde cada autor tem sua própria subpasta dentro da pasta "books", você pode usar o parâmetro "flatten"e “Where“ para buscar todos os livros de todos os autores, com classificação 5:

`   dataview table title, author, rating from #books flatten where rating = 5   `

---

## **Operadores de Busca e Condições**

O plugin Dataview do Obsidian suporta uma variedade de operadores que você pode usar em suas consultas para buscar e filtrar notas. Aqui estão os principais operadores e como eles podem ser usados:

**1. Operadores de igualdade e desigualdade**

Os operadores de igualdade (**=**) e desigualdade (**!=**) podem ser usados para buscar notas que têm um campo específico que é igual ou diferente de um valor específico.

Por exemplo, você pode usar o operador de igualdade para buscar todas as notas que têm uma classificação de 5:

`   dataview table title, author from #books where rating = 5   `

Ou você pode usar o operador de desigualdade para buscar todas as notas que não têm uma classificação de 5:

`   dataview table title, author from #books where rating != 5   `

### **2. Operadores de maior e menor**

Os operadores de maior (**>**) e menor (**<**) podem ser usados para buscar notas que têm um campo específico que é maior ou menor que um valor específico. Você também pode usar os operadores de maior ou igual (**>=**) e menor ou igual (**<=**).

Por exemplo, você pode usar o operador de maior para buscar todas as notas que têm uma classificação maior que 3:

`   dataview table title, author from #books where rating > 3   `

### **3. Operador de contém**

O operador de contém (**contains**) pode ser usado para buscar notas que têm um campo específico que contém um valor específico.

Por exemplo, você pode usar o operador de contém para buscar todas as notas que têm uma tag de "ficção":

`   dataview table title, author from #books where contains(tags, "ficção")   `

### **4. Operador de negação**

O operador de negação (**!**) pode ser usado para inverter a condição de uma consulta.

Por exemplo, você pode usar o operador de negação para buscar todas as notas que não têm uma tag de "ficção":

`   dataview table title, author from #books where !contains(tags, "ficção")   `

---

## **Encadeamento de Laços Condicionais**

O encadeamento de laços condicionais é uma técnica poderosa que permite combinar várias condições em uma única consulta no Dataview. Isso permite que você crie consultas complexas que retornam notas que atendem a várias condições diferentes ao mesmo tempo.

Os operadores condicionais que você pode usar para encadear condições são "and" (e), "or" (ou) e "not" (não). Aqui estão alguns exemplos de como você pode encadear laços condicionais no Dataview:

### **1. Encadeamento com "e"**

O operador "and" permite que você combine várias condições em uma consulta. Uma nota deve atender a todas as condições para ser incluída nos resultados.

Por exemplo, você pode usar o operador "and" para buscar todas as notas que têm uma classificação de 5, uma tag de "ficção" e foram criadas após uma determinada data:

`   dataview table title, author from #books where rating = 5 and contains(tags, "ficção") and date(created) > '2022-01-01'   `

### **2. Encadeamento com "or"**

O operador "or" permite que você combine várias condições em uma consulta. Uma nota deve atender a pelo menos uma das condições para ser incluída nos resultados.

Por exemplo, você pode usar o operador "or" para buscar todas as notas que têm uma classificação de 5, uma tag de "ficção" ou foram criadas após uma determinada data:

`   dataview table title, author from #books where rating = 5 or contains(tags, "ficção") or date(created) > '2022-01-01'   `

### **3. Encadeamento com "not" e "and"**

O operador "not" permite que você inverta uma condição em uma consulta. Uma nota deve não atender à condição para ser incluída nos resultados. Você pode combinar isso com o operador "and" para buscar notas que atendem a uma condição e não atendem a outra.

Por exemplo, você pode usar os operadores "not" e "and" para buscar todas as notas que têm uma classificação de 5 e não têm uma tag de "ficção":

`   dataview table title, author from #books where rating = 5 and not contains(tags, "ficção")   `

### **4. Encadeamento com "not" e "or"**

Da mesma forma, você pode combinar o operador "not" com o operador "or" para buscar notas que não atendem a uma condição ou atendem a outra.

Por exemplo, você pode buscar todas as notas que não têm uma classificação de 5 ou têm uma tag de "ficção":

`   dataview table title, author from #books where not rating = 5 or contains(tags, "ficção")   `

### **5. Encadeamento complexo**

Você pode combinar vários operadores em uma única consulta para criar condições de busca mais complexas. Por exemplo, você pode buscar todas as notas que têm uma classificação de 5 e uma tag de "ficção", ou todas as notas que foram criadas após uma determinada data:

`   dataview table title, author from #books where (rating = 5 and contains(tags, "ficção")) or date(created) > '2022-01-01'   `

---

## Recursos Extras

### ♾️ Da comunidade:

Confira o post que Pedro Dias fez na Biblioteca Obsidian para mais informações sobre YAML [»clique aqui«](https://comunidade.vidalendaria.com.br/c/obsidian/yaml-no-obsidian-o-guia-completo-para-anotacoes-poderosas)

### ▶️ Do YouTube:

Se quiser mais exemplos de como utilizar Dateview, eu separei alguns vídeos que pode ser interessantes para você se aprofundar um pouco mais.

**Automate Your Vault With Dataview - How To Use Dataview in Obsidian**

**[](https://youtu.be/8yjNuiSBSAM "Compartilhar link")  
https://youtu.be/8yjNuiSBSAM**

**Como usar o plugin Obsidian Dataview por Nicole van der Hoeven**

**[](https://youtu.be/JTObSymEvWA)  
https://youtu.be/JTObSymEvWA**

**Como usar o Plugin Dataview no Obsidian por Jessika Rocha**

**[](https://youtu.be/YYfGXxJ0TQE)  
https://youtu.be/YYfGXxJ0TQE**

---

## Próximos Passos:

1. ♾️ Honre esse conhecimento com a prática.
2. 💬 Deixe seu comentário
3. 👉 Avance para próxima aula.


# ia



Você parece ter criado um guia detalhado sobre como consumir e usar metadados no Obsidian, um aplicativo de gerenciamento de notas. Aqui está um resumo do que você cobriu:

**Metadados**

* Metadados são informações adicionais que podem ser adicionadas às notas no Obsidian.
* Eles são úteis para organizar e gerenciar notas de forma eficiente.
* Os metadados podem ser adicionados usando um bloco de três hífens (---) no início da nota.

**Exemplos de uso de metadados**

* Você forneceu exemplos de como usar metadados para criar resumos de livros, listas de pessoas e outros tipos de informações.
* Você também mostrou como usar metadados para criar tabelas e gráficos.

**Dataview**

* O Dataview é um plugin do Obsidian que permite criar consultas personalizadas em notas.
* Ele pode ser usado para buscar notas que atendem a certos critérios, como tags, autor, título, etc.
* Você forneceu exemplos de como usar o Dataview para criar consultas simples e complexas.

**Parâmetros de busca**

* Você discutiu os parâmetros de busca que podem ser usados no Dataview, como "from", "where", "sort", "limit", etc.
* Você forneceu exemplos de como usar esses parâmetros para criar consultas personalizadas.

**Operadores de busca e condições**

* Você discutiu os operadores de busca que podem ser usados no Dataview, como "and", "or", "not", etc.
* Você forneceu exemplos de como usar esses operadores para criar condições complexas.

**Recursos extras**

* Você forneceu links para recursos adicionais, como vídeos e artigos, que podem ajudar a aprofundar o conhecimento sobre o Dataview.

**Próximos passos**

* Você incentivou os leitores a praticar o que aprenderam e a compartilhar seus comentários.
* Você também sugeriu avançar para a próxima aula.

Em resumo, você criou um guia detalhado e prático sobre como usar metadados e o Dataview no