// 🚀 SCRIPT DE CRIAÇÃO AUTOMÁTICA DO WORKFLOW N8N
// Execute este script para criar o workflow diretamente no seu N8N
// Criado por Névoa em 29/07/2025

const API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjOTdkMTRiZS03MmEzLTQzZmQtYmY0Yi0yMWRmMjY4NzJkMjEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzUzODczNDY0fQ.CLfLlIEbsAqw7RbeajtQyvRpra_fpv_DYvqwAUTXpdc";
const N8N_URL = "https://n8neditor.nevoan8n.shop";
const EVOLUTION_URL = "https://evo.nevoan8n.shop";
const EVOLUTION_KEY = "6EF081570B08-4C4C-9ADD-54D9B3101262";

// Workflow completo para automação de devocionais
const workflowData = {
  "name": "🙏 Automacao-Devocionais-WhatsApp-Nevoa",
  "active": false,
  "nodes": [
    {
      "id": "manual-trigger",
      "name": "🚀 Trigger Devocional",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [240, 300],
      "parameters": {}
    },
    {
      "id": "set-config",
      "name": "⚙️ Configurações",
      "type": "n8n-nodes-base.set",
      "position": [440, 300],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "devocional_path",
              "value": "C:\\\\Users\\\\Gassen\\\\OneDrive\\\\Segunda_Mente_Legendaria_Sync\\\\Devocionais\\\\devocional_hoje.md"
            },
            {
              "name": "evolution_url",
              "value": EVOLUTION_URL
            },
            {
              "name": "evolution_key",
              "value": EVOLUTION_KEY
            }
          ]
        }
      }
    },
    {
      "id": "read-devocional",
      "name": "📖 Ler Devocional",
      "type": "n8n-nodes-base.readFile",
      "position": [640, 300],
      "parameters": {
        "filePath": "={{ $json.devocional_path }}",
        "dataPropertyName": "devocional_content"
      }
    },
    {
      "id": "format-whatsapp",
      "name": "✨ Formatar WhatsApp",
      "type": "n8n-nodes-base.code",
      "position": [840, 300],
      "parameters": {
        "code": `// Formatar devocional para WhatsApp por Névoa
const content = items[0].json.devocional_content;

// Converter markdown para WhatsApp
let formatted = content
  .replace(/#+\\s/g, '*') // Headers para bold
  .replace(/\\*\\*(.*?)\\*\\*/g, '*$1*') // Bold
  .replace(/_{2}(.*?)_{2}/g, '_$1_') // Italic
  .replace(/\`\`\`[\\s\\S]*?\`\`\`/g, '') // Remove code blocks
  .replace(/\\[([^\\]]+)\\]\\([^\\)]+\\)/g, '$1') // Remove links
  .replace(/\\n{3,}/g, '\\n\\n') // Max 2 quebras
  .trim();

// Header e footer personalizados
const header = "☀️ *BOM DIA!* ☀️\\n\\n";
const footer = "\\n\\n🙏 _Que Deus abençoe seu dia!_\\n\\n_Enviado com ❤️ por Névoa IA_";

const finalMessage = header + formatted + footer;

console.log('📝 Devocional formatado:', finalMessage.length, 'caracteres');

return [{
  json: {
    message: finalMessage,
    char_count: finalMessage.length,
    ready_to_send: true,
    timestamp: new Date().toISOString()
  }
}];`
      }
    },
    {
      "id": "google-contacts",
      "name": "📞 Buscar Contatos",
      "type": "n8n-nodes-base.googleContacts",
      "position": [1040, 300],
      "parameters": {
        "operation": "getAll",
        "returnAll": true,
        "additionalFields": {
          "fields": "phoneNumbers,names"
        }
      }
    },
    {
      "id": "filter-phones",
      "name": "📱 Filtrar WhatsApp",
      "type": "n8n-nodes-base.code",
      "position": [1240, 300],
      "parameters": {
        "code": `// Filtrar contatos válidos por Névoa
const validContacts = [];
let processed = 0;

for (const item of items) {
  const contact = item.json;
  processed++;
  
  if (contact.phoneNumbers && contact.phoneNumbers.length > 0) {
    for (const phone of contact.phoneNumbers) {
      let phoneNumber = phone.value.replace(/\\D/g, '');
      
      // Validar número brasileiro (10-13 dígitos)
      if (phoneNumber.length >= 10 && phoneNumber.length <= 13) {
        // Adicionar código do país se necessário
        if (phoneNumber.length === 10 || phoneNumber.length === 11) {
          phoneNumber = '55' + phoneNumber;
        }
        
        validContacts.push({
          json: {
            name: contact.names?.[0]?.displayName || 'Contato',
            whatsapp: phoneNumber,
            phone_raw: phone.value,
            contact_id: contact.id || processed
          }
        });
        break; // Apenas um número por contato
      }
    }
  }
}

console.log(\`📊 Processados: \${processed} contatos\`);
console.log(\`📱 Válidos para WhatsApp: \${validContacts.length}\`);

return validContacts;`
      }
    },
    {
      "id": "split-batches",
      "name": "✂️ Dividir em Lotes",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [1440, 300],
      "parameters": {
        "batchSize": 50,
        "options": {}
      }
    },
    {
      "id": "send-whatsapp",
      "name": "📲 Enviar WhatsApp",
      "type": "n8n-nodes-base.httpRequest",
      "position": [1640, 300],
      "parameters": {
        "method": "POST",
        "url": `${EVOLUTION_URL}/message/sendText/Gassen-Instance`,
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "apikey",
              "value": EVOLUTION_KEY
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "bodyContentType": "json",
        "jsonBody": `{
  "number": "{{ $json.whatsapp }}",
  "text": "{{ $node['✨ Formatar WhatsApp'].json.message }}"
}`,
        "options": {
          "timeout": 45000,
          "retry": {
            "enabled": true,
            "maxTries": 3
          }
        }
      }
    },
    {
      "id": "wait-rate-limit",
      "name": "⏰ Aguardar 45s",
      "type": "n8n-nodes-base.wait",
      "position": [1840, 300],
      "parameters": {
        "time": 45,
        "unit": "seconds"
      }
    },
    {
      "id": "log-progress",
      "name": "📊 Log Progresso",
      "type": "n8n-nodes-base.code",
      "position": [2040, 300],
      "parameters": {
        "code": `// Log de progresso por Névoa
const batch = items[0].json;
const splitInfo = items[0].json['SplitInBatches'];

if (splitInfo && splitInfo.context) {
  const current = splitInfo.context.currentRunIndex + 1;
  const total = splitInfo.context.totalRuns;
  const percent = Math.round((current / total) * 100);
  
  console.log(\`🚀 Progresso: \${current}/\${total} lotes (\${percent}%)\`);
  console.log(\`📨 Lote atual: \${items.length} mensagens enviadas\`);
  
  if (current === total) {
    console.log('🎉 AUTOMAÇÃO CONCLUÍDA COM SUCESSO!');
    console.log(\`📱 Total aproximado: \${total * 50} contatos alcançados\`);
    console.log('✨ Powered by Névoa IA - Evangelismo Digital Automatizado');
  }
} else {
  console.log(\`✅ Processado: \${items.length} itens\`);
}

return items;`
      }
    }
  ],
  "connections": {
    "🚀 Trigger Devocional": {
      "main": [
        [
          {
            "node": "⚙️ Configurações",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "⚙️ Configurações": {
      "main": [
        [
          {
            "node": "📖 Ler Devocional",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "📖 Ler Devocional": {
      "main": [
        [
          {
            "node": "✨ Formatar WhatsApp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "✨ Formatar WhatsApp": {
      "main": [
        [
          {
            "node": "📞 Buscar Contatos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "📞 Buscar Contatos": {
      "main": [
        [
          {
            "node": "📱 Filtrar WhatsApp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "📱 Filtrar WhatsApp": {
      "main": [
        [
          {
            "node": "✂️ Dividir em Lotes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "✂️ Dividir em Lotes": {
      "main": [
        [
          {
            "node": "📲 Enviar WhatsApp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "📲 Enviar WhatsApp": {
      "main": [
        [
          {
            "node": "⏰ Aguardar 45s",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "⏰ Aguardar 45s": {
      "main": [
        [
          {
            "node": "📊 Log Progresso",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": ["devocional", "whatsapp", "evangelismo", "automacao", "nevoa", "gassen"],
  "triggerCount": 0,
  "updatedAt": new Date().toISOString(),
  "versionId": "1"
};

// Função para criar o workflow
async function createWorkflow() {
  console.log('🚀 Iniciando criação do workflow...');
  console.log('🔗 URL N8N:', N8N_URL);
  
  try {
    // Primeiro, testar conexão
    console.log('🔍 Testando conexão com N8N...');
    const testResponse = await fetch(`${N8N_URL}/api/v1/workflows`, {
      method: 'GET',
      headers: {
        'X-N8N-API-KEY': API_KEY,
        'Content-Type': 'application/json'
      }
    });

    if (!testResponse.ok) {
      throw new Error(`Erro na conexão: ${testResponse.status} - ${testResponse.statusText}`);
    }

    const existingWorkflows = await testResponse.json();
    console.log(`✅ Conexão OK! Workflows existentes: ${existingWorkflows.data?.length || 0}`);

    // Verificar se workflow já existe
    const existingWorkflow = existingWorkflows.data?.find(w => w.name === workflowData.name);
    if (existingWorkflow) {
      console.log('⚠️ Workflow já existe! ID:', existingWorkflow.id);
      console.log('🔄 Atualizando workflow existente...');
      
      // Atualizar workflow existente
      const updateResponse = await fetch(`${N8N_URL}/api/v1/workflows/${existingWorkflow.id}`, {
        method: 'PUT',
        headers: {
          'X-N8N-API-KEY': API_KEY,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(workflowData)
      });
      
      if (updateResponse.ok) {
        const updated = await updateResponse.json();
        console.log('✅ Workflow atualizado com sucesso!');
        console.log('🌐 Acesse:', `${N8N_URL}/workflow/${updated.data.id}`);
        return updated;
      } else {
        throw new Error(`Erro ao atualizar: ${updateResponse.status}`);
      }
    } else {
      // Criar novo workflow
      console.log('🎯 Criando novo workflow...');
      const createResponse = await fetch(`${N8N_URL}/api/v1/workflows`, {
        method: 'POST',
        headers: {
          'X-N8N-API-KEY': API_KEY,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(workflowData)
      });

      if (createResponse.ok) {
        const created = await createResponse.json();
        console.log('🎉 WORKFLOW CRIADO COM SUCESSO!');
        console.log('📋 Nome:', created.data.name);
        console.log('🆔 ID:', created.data.id);
        console.log('🌐 Acesse:', `${N8N_URL}/workflow/${created.data.id}`);
        console.log('');
        console.log('📝 PRÓXIMOS PASSOS:');
        console.log('1. Configure Google Contacts credentials no N8N');
        console.log('2. Salve um devocional em: devocional_hoje.md');
        console.log('3. Execute o workflow manualmente');
        console.log('4. Aguarde ~15 minutos para envio completo');
        console.log('');
        console.log('✨ Automação criada por Névoa IA - Evangelismo Digital Revolucionário!');
        
        return created;
      } else {
        const errorText = await createResponse.text();
        throw new Error(`Erro ao criar workflow: ${createResponse.status} - ${errorText}`);
      }
    }
    
  } catch (error) {
    console.error('💥 ERRO:', error.message);
    console.log('');
    console.log('🔧 POSSÍVEIS SOLUÇÕES:');
    console.log('1. Verifique se N8N está rodando:', N8N_URL);
    console.log('2. Confirme se API está habilitada no N8N');
    console.log('3. Verifique se API key está correta');
    console.log('4. Teste acesso manual ao N8N interface');
    
    return null;
  }
}

// Executar criação
console.log('🤖 NÉVOA IA - CRIADOR AUTOMÁTICO DE WORKFLOWS N8N');
console.log('================================================');
console.log('');

createWorkflow().then((result) => {
  if (result) {
    console.log('');
    console.log('🚀 WORKFLOW IMPLANTADO COM SUCESSO!');
    console.log('De 20 minutos manuais para 30 segundos automáticos!');
  } else {
    console.log('');
    console.log('❌ Falha na implantação. Verifique os logs acima.');
  }
});
