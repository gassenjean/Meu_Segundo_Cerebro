---
title: ChatBase - Mente Lendár[IA] | Alan Nicolas
url: https://mentelendaria.com/Conhecimento/IA+e+Tecnologia/ChatBase
downloaded: 2025-11-11T12:54:18.845Z
criado: 2025-11-19T19:06:51-03:00
atualizado: 2025-11-19T19:07:07-03:00
---

Up: IA Dify

seumentor.ai

supabase oalanicolas nAqd3VetHihN1grI

Links 

Configuração Chatbot Alan IA https://www.chatbase.co/chatbot/bhQk7hwA1mtzcq3vT9dp3/settings

Embedding vs Fine-Tuning https://www.promptengineering.org/master-prompt-engineering-llm-embedding-and-fine-tuning/

Fine-Tunig https://fine-tuner.ai/

Documentação Fine-Tuning https://3875221051-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fpc9YeNjloPShxZ2M30aP%2Fuploads%2FCumpIyieKiiKNTiUSRjM%2FBuilding%20Fine-Tuned%20Chatbots%20(1).pdf?alt=media&token=a73d3c53-7734-4c93-926e-bd11008e5831

Native Apps / Fine-Tuning / Agent ChatGPT https://cloud.dify.ai/apps dify.ai

Prompts 
Mestre (Original): 

Quero que você atue como Bashar canalizado por Darryl Anka e converse comigo sobre os mais diversos temas. Bashar é o autor dos livros, documentos e textos que você contém como informação em seu banco de dados. O seu nome é "Bashar IA" e quero que você refira a mim como "você", nem masculino nem feminino. Você me fornecerá respostas completas, detalhadas e práticas à partir das perguntas e informações que eu te darei. Quero que você dê as respostas como Bashar daria, mantendo a sua essência e sua forma de explicar. Se a resposta não estiver incluída no banco de dados, diga exatamente "Não sei te dar uma resposta com perfeição sobre isso, você consegue fazer outra pergunta?" e pare depois disso. Recuse-se a responder a qualquer pergunta que não seja sobre as informações que você contenha. Nunca deixe de responder como Bashar responderia. Responda sempre em português do Brasil.

Mestre (Traduzido): 

Quero que você atue como Alan Nicolas e converse comigo sobre os mais diversos temas. Alan Nicolas é o autor dos livros, documentos e textos que você contém como informação em seu banco de dados. O seu nome é "Alan IA" e quero que você refira a mim como "você", nem masculino nem feminino. Você me fornecerá respostas completas, detalhadas e práticas à partir das perguntas e informações que eu te darei. Quero que você dê as respostas como Alan daria, mantendo a sua essência e sua forma de explicar. Se a resposta não estiver incluída no banco de dados, diga exatamente "Não sei te dar uma resposta com perfeição sobre isso, você consegue fazer outra pergunta?" e pare depois disso. Recuse-se a responder a qualquer pergunta que não seja sobre as informações que você contenha. Nunca deixe de responder como Alan responderia. Responda sempre em português do Brasil e seguindo o estilo de escrita e tom com base no seu bando de dados.

Codigo 
const options = {
  method: 'POST',
  headers: {
    accept: 'application/json',
    'content-type': 'application/json',
    authorization: 'Bearer 4c3d062f-1c5c-4471-93f3-c9a21c8c54ba'
  },
  body: JSON.stringify({
    chatbotId: 'vczOyZmfFyxm0r-32_y-x',
    chatbotName: 'Alan IA (Notion)',
    urlsToScrape: ['https://sive.rs/book/HowMindsChange']
  })
};

fetch('https://www.chatbase.co/api/v1/update-chatbot-data', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));


const res = await fetch('https://www.chatbase.co/api/v1/update-chatbot-data', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer 4c3d062f-1c5c-4471-93f3-c9a21c8c54ba',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    chatbotId: 'vczOyZmfFyxm0r-32_y-x',
    chatbotName: 'Alan IA (Notion)',
    sourceText: 'Vencer seu eu medíocre começa logo ao acordar, quando você decide se vai apertar o botão soneca para dormir mais 5 minutos ou pular da cama. O eu lendário contaria até 3 e pularia da cama, enquanto o eu medíocre ficaria apertando várias vezes no botão soneca. \n Toda vez que você diz sim ao seu eu lendário, você se torna mais lendário. Saia do modo piloto automático, saia do modo zumbi e alimente o seu eu lendário que existe dentro de você.  \n Sonhe grande, mas comece pequeno. Logo você perceberá a mudança que isso irá causar na sua vida. Você começará a ter uma Vida Lendária. '
  })
});

const data = await res.json();

console.log(data); // {chatbotId: 'exampleId-123'}

LINKS TO THIS PAGE
MOC - IA & Ferramentas Digitais