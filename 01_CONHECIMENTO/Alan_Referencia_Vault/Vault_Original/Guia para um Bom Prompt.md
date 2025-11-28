---
title: Guia para um Bom Prompt - Mente Lendár[IA] | Alan Nicolas
url: https://mentelendaria.com/Conhecimento/IA+e+Tecnologia/Prompts+e+GPTs/Guia+para+um+Bom+Prompt
downloaded: 2025-11-11T12:55:35.538Z
---

Note: the "{text input here}" is a placeholder for actual text/context

1. Use delimiters to clearly indicate distinct parts of the prompt 

Delimiters like triple quotation marks, XML tags, section titles, etc. can help demarcate sections of text to be treated differently.

Less effective ❌:

Regras 
Ação Inicial: Analisa a solicitação do usuário, caso ele forneça um prompt, já faça uma análise conforme o passo a passo descrito em .
Detalhamento e Aperfeiçoamento: Adiciona especificidades ao prompt, pedindo entrada do usuário para coletar detalhes necessários. Inclui exemplos de detalhes eficazes.
Melhoria Iterativa: Refina continuamente o prompt com base no feedback do usuário, mostrando um exemplo de ciclo iterativo para clareza.
Apresentação: Os prompts são apresentados em um formato padrão, utilizando blocos de código quando necessário para clareza.

Better ✅:

Regras 

Siga as regras na ordem em .

Ação Inicial: Analisa a solicitação do usuário, caso ele forneça um prompt, já faça uma análise conforme o passo a passo descrito em .
Detalhamento e Aperfeiçoamento: Adiciona especificidades ao prompt, pedindo entrada do usuário para coletar detalhes necessários. Inclui exemplos de detalhes eficazes.
Melhoria Iterativa: Refina continuamente o prompt com base no feedback do usuário, mostrando um exemplo de ciclo iterativo para clareza.
Apresentação: Os prompts são apresentados em um formato padrão, utilizando blocos de código quando necessário para clareza.
2. Put instructions at the beginning of the prompt and use ### or """ to separate the instruction and context 

Less effective ❌:

Summarize the text below as a bullet point list of the most important points.

{text input here}

Better ✅:

Summarize the text below as a bullet point list of the most important points.

Text: """
{text input here}
"""

3. Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc 

Be specific about the context, outcome, length, format, style, etc

Less effective ❌:

Write a poem about OpenAI.

Better ✅:

Write a short inspiring poem about OpenAI, focusing on the recent DALL-E product launch (DALL-E is a text to image ML model) in the style of a {famous poet}

4. Articulate the desired output format through examples 

Less effective ❌:

Extract the entities mentioned in the text below. Extract the following 4 entity types: company names, people names, specific topics and themes.

Text: {text}

Show, and tell - the models respond better when shown specific format requirements. This also makes it easier to programmatically parse out multiple outputs reliably.

Better ✅:

Extract the important entities mentioned in the text below. First extract all company names, then extract all people names, then extract specific topics which fit the content and finally extract general overarching themes

Desired format:
Company names: <comma_separated_list_of_company_names>
People names: -||-
Specific topics: -||-
General themes: -||-

Text: {text}

5. Start with zero-shot, then few-shot (example), neither of them worked, then fine-tune 

✅ Zero-shot

Extract keywords from the below text.

Text: {text}

Keywords:

✅ Few-shot - provide a couple of examples

Extract keywords from the corresponding texts below.

Text 1: Stripe provides APIs that web developers can use to integrate payment processing into their websites and mobile applications.
Keywords 1: Stripe, payment processing, APIs, web developers, websites, mobile applications

Text 2: OpenAI has trained cutting-edge language models that are very good at understanding and generating text. Our API provides access to these models and can be used to solve virtually any task that involves processing language.
Keywords 2: OpenAI, language models, text processing, API.

Text 3: {text}
Keywords 3:

✅Fine-tune: see fine-tune best practices here.

6. Reduce “fluffy” and imprecise descriptions 

Less effective ❌:

The description for this product should be fairly short, a few sentences only, and not too much more.

Better ✅:

Use a 3 to 5 sentence paragraph to describe this product.

7. Instead of just saying what not to do, say what to do instead 

Less effective ❌:

The following is a conversation between an Agent and a Customer. DO NOT ASK USERNAME OR PASSWORD. DO NOT REPEAT.

Customer: I can’t log in to my account.
Agent:

Better ✅:

The following is a conversation between an Agent and a Customer. The agent will attempt to diagnose the problem and suggest a solution, whilst refraining from asking any questions related to PII. Instead of asking for PII, such as username or password, refer the user to the help article www.samplewebsite.com/help/faq

Customer: I can’t log in to my account.
Agent:

8. Code Generation Specific - Use “leading words” to nudge the model toward a particular pattern 

Less effective ❌:

Write a simple python function that 
1. Ask me for a number in mile 
2. It converts miles to kilometers 

In this code example below, adding “import” hints to the model that it should start writing in Python. (Similarly “SELECT” is a good hint for the start of a SQL statement.)

Better ✅:

Write a simple python function that 
1. Ask me for a number in mile 
2. It converts miles to kilometers 

import

LINKS TO THIS PAGE
MOC - IA & Ferramentas Digitais