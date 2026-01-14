---
criado: 2025-07-14T12:19:28-03:00
atualizado: 2025-07-14T12:19:32-03:00
---

# Guia Completo para Transcrição Automatizada de Áudio do WhatsApp

## Introdução

Em um mundo onde a comunicação instantânea é essencial, o WhatsApp se tornou uma ferramenta indispensável para empresas e indivíduos. No entanto, lidar com áudios pode ser desafiador, especialmente quando se trata de transcrição. Este ebook guiará você através do processo de automação da transcrição de áudios do WhatsApp, utilizando ferramentas como Evolution API e Groki, para tornar sua comunicação mais eficiente.

## 1. Configurando o Fluxo de Trabalho

### Criando o Fluxo de Trabalho

O primeiro passo é criar um novo fluxo de trabalho. Isso é feito clicando em "Create Workflow". Em seguida, importamos um template no formato JSON, que serve como base para nossa automação. Este template já contém a estrutura necessária para iniciar o processo.

### Importando o Template

Após baixar o template, clique nos três pontos e selecione "Import from file". Abra o template baixado para iniciar o projeto. Este arquivo JSON define o fluxo de dados e a lógica da automação.

#### Exemplo de Template JSON

```json
{
  "name": "Fluxo de Trabalho",
  "description": "Fluxo de trabalho para transcrição de áudios do WhatsApp",
  "steps": [
    {
      "type": "webhook",
      "trigger": { "event": "mensagem recebida" },
      "actions": [
        {
          "type": "formatar número",
          "config": { "remover caracteres indesejados": true }
        }
      ]
    },
    {
      "type": "corrigir bug",
      "config": {
        "bloco 1": { "configuração": "vermelho" },
        "bloco 2": { "configuração": "vermelho" }
      }
    }
  ]
}
```

## 2. Processando o Áudio

### Receiving the Webhook

O fluxo começa com um webhook, um gatilho que inicia a automação. O número recebido é formatado para remover caracteres indesejados, como o arroba, resultando em um número limpo (ex.: 8125346).

### Corrigindo o Bug do Evolution API

Dois blocos no fluxo são usados para corrigir um bug no Evolution API, garantindo que o áudio seja enviado corretamente. Esses blocos são pré-configurados, e você só precisará modificar as partes em vermelho.

## 3. Transcrição e Pós-Processamento

### Verificando o Tipo de Mensagem

O fluxo verifica se a mensagem é um áudio. Se for, prossegue; caso contrário, ignora. Isso é crucial para garantir que apenas áudios sejam processados.

### Convertendo e Transcrevendo

O áudio, recebido em Base64, é convertido para texto usando a API Groki. Em seguida, um nó de IA corrige a transcrição, melhorando a clareza e a pontuação.

### Enviando a Transcrição

A transcrição é enviada de volta ao WhatsApp. Para áudios longos, um resumo é criado se o texto exceder 1200 caracteres, oferecendo uma visão geral concisa.

## 4. Lidando com Casos Especiais

### Áudios Longos

Se o áudio ultrapassar um minuto, o fluxo cria um resumo, além da transcrição completa, ajudando a captar os pontos principais rapidamente.

## Conclusão

Automatizar a transcrição de áudios do WhatsApp não só economiza tempo mas também melhora a eficiência. Com este guia, você pode implementar um sistema robusto usando Evolution API e Groki, tornando sua comunicação mais eficiente e eficaz.

---

### Exemplo de Implementação

Aqui está um exemplo de como implementar o fluxo de trabalho:

1. Crie um novo fluxo de trabalho no Evolution API.
2. Importe o template JSON.
3. Configure os blocos de correção de bug.
4. Configure o webhook para receber a mensagem.
5. Configure a conversão e transcrição do áudio.
6. Configure a envio da transcrição.

### Dicas e Considerações

- Certifique-se de que o template JSON esteja correto e completo.
- Verifique se os blocos de correção de bug estão configurados corretamente.
- Certifique-se de que o webhook esteja configurado corretamente.
- Verifique se a conversão e transcrição do áudio estão funcionando corretamente.
- Certifique-se de que a envio da transcrição esteja funcionando corretamente.

---

Este ebook foi projetado para ser uma ferramenta prática, ajudando você a navegar pelo processo de transcrição automática com clareza e confiança.
