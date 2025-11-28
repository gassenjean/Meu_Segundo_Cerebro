// 🚀 TESTE CONEXÃO N8N API - Automação Devocionais
// Criado: 29/07/2025 por Névoa

const API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjOTdkMTRiZS03MmEzLTQzZmQtYmY0Yi0yMWRmMjY4NzJkMjEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzUzODczNDY0fQ.CLfLlIEbsAqw7RbeajtQyvRpra_fpv_DYvqwAUTXpdc";
const N8N_URL = "https://n8neditor.nevoan8n.shop";

// Função para testar conexão
async function testN8NConnection() {
    try {
        const response = await fetch(`${N8N_URL}/api/v1/workflows`, {
            method: 'GET',
            headers: {
                'X-N8N-API-KEY': API_KEY,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const workflows = await response.json();
            console.log('✅ CONEXÃO SUCESSO!');
            console.log(`📊 Total workflows: ${workflows.data?.length || 0}`);
            return workflows;
        } else {
            console.log('❌ Erro na conexão:', response.status);
            const error = await response.text();
            console.log('Erro detalhado:', error);
        }
    } catch (error) {
        console.log('💥 Erro de rede:', error.message);
    }
}

// Função para criar workflow de devocionais
async function createDevotionalWorkflow() {
    const workflowData = {
        name: "Automacao-Devocionais-WhatsApp-Nevoa",
        active: false,
        nodes: [
            {
                id: "webhook-trigger",
                name: "Manual Trigger",
                type: "n8n-nodes-base.manualTrigger",
                position: [250, 300],
                parameters: {}
            },
            {
                id: "read-devocional",
                name: "Read Devocional File",
                type: "n8n-nodes-base.readFile",
                position: [450, 300],
                parameters: {
                    filePath: "/path/to/devocional.md",
                    dataPropertyName: "data"
                }
            },
            {
                id: "format-message",
                name: "Format WhatsApp Message",
                type: "n8n-nodes-base.code",
                position: [650, 300],
                parameters: {
                    code: `
                        // Formatar devocional para WhatsApp
                        const content = items[0].json.data;
                        const formattedMessage = content.replace(/#+\\s/g, '*').replace(/\\*\\*(.*?)\\*\\*/g, '*$1*');
                        
                        return [{
                            json: {
                                message: formattedMessage,
                                ready_to_send: true
                            }
                        }];
                    `
                }
            }
        ],
        connections: {
            "Manual Trigger": {
                "main": [
                    [
                        {
                            "node": "Read Devocional File",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "Read Devocional File": {
                "main": [
                    [
                        {
                            "node": "Format WhatsApp Message",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        }
    };

    try {
        const response = await fetch(`${N8N_URL}/api/v1/workflows`, {
            method: 'POST',
            headers: {
                'X-N8N-API-KEY': API_KEY,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(workflowData)
        });

        if (response.ok) {
            const result = await response.json();
            console.log('🎉 WORKFLOW CRIADO!');
            console.log('ID:', result.data.id);
            return result;
        } else {
            console.log('❌ Erro criando workflow:', response.status);
            const error = await response.text();
            console.log('Erro:', error);
        }
    } catch (error) {
        console.log('💥 Erro:', error.message);
    }
}

// Executar testes
testN8NConnection().then(() => {
    console.log('\n🚀 Próximo: Criar workflow automação...');
    // createDevotionalWorkflow();
});

module.exports = {
    testN8NConnection,
    createDevotionalWorkflow,
    API_KEY,
    N8N_URL
};
