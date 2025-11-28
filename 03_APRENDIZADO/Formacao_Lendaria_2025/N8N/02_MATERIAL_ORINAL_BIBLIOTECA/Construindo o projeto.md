---
criado: 2025-07-14T12:26:26-03:00
atualizado: 2025-07-14T12:26:30-03:00
---
# Guia Completo para Transcrição de Áudios do WhatsApp usando Evolução API e n8n

## Introdução

Bem-vindos a este guia completo sobre como transcrever áudios do WhatsApp usando a Evolução API e o n8n. Neste ebook, vamos explorar passo a passo como configurar um fluxo de trabalho automático para transcrever áudios recebidos ou enviados via WhatsApp, utilizando ferramentas poderosas como a Evolução API, n8n, Grok e OpenAI. Este guia é ideal para quem deseja automatizar processos, entender melhor como integrar diferentes APIs e melhorar a eficiência na gestão de mensagens.

## Configuração do Evolução API e Conexão do WhatsApp

### Preparando o Evolução API

Para começar, precisamos preparar o nosso ambiente de trabalho com a Evolução API. Acesse o link do Evolução API através do endereço `https://seu-dominio.evolucao/manager`. Caso você não lembre da senha, pode recuperá-la através do painel de controle do seu hosting.

1. **Acessando o Painel de Controle:**
    
    - Acesse o seu painel de controle do hosting.
    - Navegue até a seção da Evolução API.
    - Localize a API key em uso. Se você ainda não a copiou ou perdeu, este é o local para recuperá-la.
2. **Criando uma Nova Instância:**
    
    - No ambiente da Evolução API, clique no ícone de engrenagem e selecione "Criar Nova Instância".
    - Dê um nome à sua instância, evitando caracteres especiais, acentos e espaços. Por exemplo, "TranscriacaoWhatsApp".
    - Clique em "Salvar" para criar a instância.

### Conectando o WhatsApp

Agora que a instância está criada, vamos conectar o WhatsApp à nossa instância.

1. **Conectando o WhatsApp:**
    
    - Clique no ícone de engrenagem na instância recém-criada e selecione "Conectar Dispositivo".
    - Siga as instruções para conectar seu WhatsApp. Isso pode incluir a leitura de um QR Code com outro dispositivo.
2. **Configurações Iniciais:**
    
    - Após a conexão, acesse as configurações da instância.
    - Certifique-se de que as opções "Ignorar Grupos" e "Rejeitar Chamadas" estejam habilitadas para evitar o consumo desnecessário de créditos.

## Integração com n8n e Configuração do Fluxo de Trabalho

### Configurando o Webhook

Com a Evolução API configurada, vamos integrar o n8n para criar um fluxo de trabalho automático.

1. **Criando o Webhook no n8n:**
    
    - Acesse o seu ambiente n8n e crie um novo workflow.
    - Adicione um node de "Webhook" e configure-o com o método POST.
    - Copie a URL gerada pelo webhook para usar na Evolução API.
2. **Conectando Evolução API e n8n:**
    
    - Retorne à Evolução API e acesse a seção de Eventos.
    - Cole a URL do webhook no campo adequado e ative o "Webhook Base64" e "Messages Upsearch".
    - Clique em "Salvar" para confirmar as configurações.

### Configurando o Fluxo de Trabalho

Agora que o webhook está configurado, vamos definir o fluxo de trabalho no n8n.

1. **Adicionando Nodes:**
    
    - Após o node de webhook, adicione um node para a transcrição usando o Grok.
    - Configure o node do Grok com sua API key para transcrição de áudio.
2. **Integração com OpenAI:**
    
    - Adicione um node para o OpenAI para resumir a transcrição.
    - Configure o node com sua API key do OpenAI e defina os parâmetros para o resumo.

## Implementação da Transcrição e Resumo

### Transcrição de Áudio com Grok

O Grok é uma ferramenta poderosa para transcrição de áudio. Vamos configurá-lo para processar os áudios recebidos.

1. **Configurando a API Key do Grok:**
    
    - Acesse o Grok e faça login com sua conta.
    - Gere uma nova API key e copie-a.
    - Retorne ao n8n e adicione a chave na configuração do node do Grok.
2. **Processando o Áudio:**
    
    - Certifique-se de que o node do Grok está configurado para receber o áudio e retornar a transcrição em texto.

### Resumo com OpenAI

Após a transcrição, vamos usar a OpenAI para resumir o texto.

1. **Configurando a API Key do OpenAI:**
    
    - Acesse o ChatGPT e gere uma nova API key.
    - Adicione-a no node do OpenAI no n8n.
2. **Definindo Parâmetros para o Resumo:**
    
    - Configure o node do OpenAI para receber o texto transcrito e retornar um resumo conciso.

## Testes e Ativação para Produção

### Testando o Fluxo de Trabalho

Antes de colocar tudo em produção, vamos testar o fluxo para garantir que tudo funcione corretamente.

1. **Enviando um Áudio para Teste:**
    
    - Envie um áudio de teste para o número conectado ao WhatsApp.
    - Verifique no n8n se o workflow foi acionado e se a transcrição e o resumo foram gerados corretamente.
2. **Verificando os Logs:**
    
    - Analise os logs do n8n para identificar possíveis erros ou problemas.

### Ativando o Workflow para Produção

Com o fluxo testado e funcionando, está na hora de ativá-lo para produção.

1. **Alterando para Modo Produção:**
    
    - No webhook da Evolução API, altere o endpoint para o modo produção, removendo o sufixo "test".
    - Ative o workflow no n8n para que ele fique em execução contínua.
2. **Monitorando o Fluxo:**
    
    - Mantenha um monitoramento constante do fluxo para garantir que ele continue funcionando sem interrupções.

## Conclusão

Parabéns! Você agora tem um fluxo de trabalho completo para transcrever áudios do WhatsApp usando a Evolução API e o n8n. Este guia o levou passo a passo desde a configuração inicial até a ativação em produção. Com esta automação, você pode economizar tempo e melhorar a eficiência na gestão de mensagens. Sinta-se à vontade para explorar e personalizar ainda mais o fluxo, integrando novas funcionalidades conforme necessário.