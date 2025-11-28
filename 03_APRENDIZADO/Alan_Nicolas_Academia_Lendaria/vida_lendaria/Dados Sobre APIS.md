---
title: Dados Sobre APIS - Mente Lendár[IA] | Alan Nicolas
url: https://mentelendaria.com/Conhecimento/IA+e+Tecnologia/Dados+Sobre+APIS
downloaded: 2025-11-11T12:52:35.199Z
criado: 2025-11-19T19:06:52-03:00
atualizado: 2025-11-19T19:07:03-03:00
---

API META 
Configuração dos webhooks 

Blog do WhatsApp Business

Como usar o Node.js para implementar webhooks

Assine o Webhooks para obter notificações sobre mensagens recebidas pela sua empresa e atualizações nos perfis de clientes.

Como criar um ponto de extremidade 

Antes de começar, será necessário criar um ponto de extremidade no seu servidor para receber notificações.

Seu ponto de extremidade deve processar dois tipos de solicitação HTTPS: solicitações de verificação e notificações de evento. Como as duas solicitações usam o HTTPS, seu servidor deve ter um certificado de TLS ou SSL válido configurado e instalado corretamente. Certificados autoassinados não são aceitos.

Saiba mais sobre as solicitações de verificação e notificações de eventos .

A configuração do Webhooks não afeta o número de telefone do seu app WhatsApp Business. Somente após a migração do telefone para a Plataforma do WhatsApp Business não será mais possível usar esse número no app WhatsApp Business.

Assinar Webhooks 

Para assinar o Webhooks, será necessário obter um ID e permissões da Meta. Para isso, acesse o Painel de Apps da Meta. Depois, siga estas etapas:

Crie um app do tipo Empresa no Painel de Apps da Meta .

Adicione o produto Webhooks ao seu app da Meta no Painel de Apps .

Um aplicativo da Meta não pode ter mais de um ponto de extremidade configurado ao mesmo tempo. Use diversos aplicativos da Meta para enviar as atualizações de webhook a múltiplos pontos de extremidade.

Se você for um parceiro de solução, será necessário fazer o seguinte:

Adicione a permissão whatsapp_business_messaging no Painel de Apps.
Conclua a análise do app da Meta . Essa etapa pode demorar, mas é possível continuar fazendo testes durante todo o processo de análise.

Como funcionam os Webhooks 

Sempre que ocorre um evento de disparo, a Plataforma do WhatsApp Business identifica o evento e envia uma notificação à URL do Webhook especificada por você. Você pode receber dois tipos de notificação:

Mensagens recebidas: alerta sobre o recebimento de uma mensagem. Também podem ser chamadas de "notificações de entrada" na documentação.
Notificações de preço e status da mensagem: alerta quando há uma alteração no status de uma mensagem. Por exemplo, a mensagem foi lida ou entregue. Também podem ser chamadas de "notificações de saída" na documentação.

Todos os Webhooks têm o seguinte formato genérico:

{ "object": "whatsapp_business_account", "entry": [{ "id": "WHATSAPP_BUSINESS_ACCOUNT_ID", "changes": [{ "value": { "messaging_product": "whatsapp", "metadata": { "display_phone_number": "PHONE_NUMBER", "phone_number_id": "PHONE_NUMBER_ID" }, # specific Webhooks payload }, "field": "messages" }] }] }

Consulte Webhooks Notification Payload Reference para ver informações sobre cada campo.

Ao receber uma mensagem que não é compatível com a API de Nuvem, você obterá um webhook de mensagem desconhecida.

Tamanho de carga 

As cargas de webhooks podem ter até 3 MB.

Exemplos de pontos de extremidade do app 

Crie um ponto de extremidade de exemplo de app para testar os webhooks.

Pontos de extremidade de exemplo de app (Glitch)  
Exemplos de aplicativos (Heroku)  

Falha na entrega do webhook 

Se enviarmos uma solicitação de webhook para seu ponto de extremidade e o servidor responder com um código de status HTTP que não seja 200, ou se não pudermos enviar o webhook por outro motivo, continuaremos fazendo tentativas diminuindo a frequência durante 7 dias.

Essas tentativas serão enviadas a todos os apps que assinaram os webhooks (e os campos relacionados) na conta do WhatsApp Business. Isso pode fazer com que as notificações de webhook sejam duplicadas.

Endereços IP 

É possível obter endereços IP dos nossos servidores de webhook ao executar este comando no seu terminal:

whois -h whois.radb.net — '-i origin AS32934' | grep ^route | awk '{print $2}' | sort

De tempo em tempo, alteramos os endereços IP. Por isso, se você estiver fazendo uma lista de permissão de servidores, será preciso gerar a lista de novo periodicamente para atualizar a lista de permissão.

Próximas etapas 

Saiba mais sobre as informações que você pode receber via notificação do Webhooks.

LINKS TO THIS PAGE
MOC - IA & Ferramentas Digitais