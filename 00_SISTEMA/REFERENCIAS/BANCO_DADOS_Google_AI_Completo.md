# BANCO DE DADOS - Documentação Google AI Completa

**Criado:** 30/12/2025
**Fonte:** Deep Research Gemini (ai.google.dev, notebooklm.google.com, cloud.google.com)
**Contexto:** Referência Técnica Definitiva para Ecossistema Google AI.

---

## 1. GEMINI MODELS (Família de Modelos)

### 1.1 Especificações Técnicas
| Modelo | Context Window (In/Out) | Modalidades | Casos de Uso |
| :--- | :--- | :--- | :--- |
| **Gemini 3 Pro** (Preview) | 1M / 65k Tokens | Texto, Imagem, Vídeo, Áudio, PDF | Raciocínio complexo, "Vibe Coding", Agentes Autônomos. |
| **Gemini 3 Flash** (Preview) | 1M / 65k Tokens | Multimodal Completo | Baixa latência, Alta frequência, Processamento em massa. |
| **Gemini 1.5 Pro/Flash** | Até 2M Tokens | Multimodal Completo | Análise de longa duração (livros, vídeos longos), RAG massivo. |

*Nota: A janela de 2M tokens está disponível em versões específicas do 1.5 Pro via Google AI Studio.*

### 1.2 Recursos de Diferenciação
- **Multimodalidade Nativa**: O modelo "vê" vídeo e "ouve" áudio nativamente, sem transcrição intermediária.
- **Raciocínio Longo (Long Context)**: Capacidade de manter coerência sobre milhões de tokens (ex: analisar codebase inteira).
- **Vibe Coding**: Capacidade do Gemini 3 de entender a intenção e "estilo" do código além da sintaxe.

---

## 2. GOOGLE AI STUDIO

Plataforma de desenvolvimento rápido e prototipagem.

### 2.1 Principais Funcionalidades
- **Prompt Management**: Interface para testar System Instructions e User Prompts com upload de arquivos multimodais.
- **Get API Key**: Central de gestão de chaves para acesso à API (Gratuito no tier básico, Pago no Pay-as-you-go).
- **Comparação de Modelos**: Toggle rápido para testar o mesmo prompt em Pro vs Flash vs Experimental.
- **App Templates**: Modelos prontos para "Conversational Agent", "Coding Assistant", etc.

### 2.2 Configurações de Modelo
- **Temperature**: Criatividade (0.0 a 2.0).
- **Top-K / Top-P**: Amostragem de tokens.
- **Safety Settings**: Configuração de filtros de segurança (Block Few, Block Some, Block All).

---

## 3. NOTEBOOKLM (Assistente de Pesquisa)

Ferramenta focada em síntese e aprendizado acelerado (RAG fixo nos seus documentos).

### 3.1 Limites e Capacidades
| Recurso | Limite / Especificação |
| :--- | :--- |
| **Fontes por Notebook** | Até 50 fontes. |
| **Tamanho por Fonte** | Até 500.000 palavras (aprox. 1000 páginas de PDF). |
| **Tipos de Fonte** | PDF, Google Docs, Slides, Texto Copiado, URL de Site, Vídeo YouTube (transcrição), Áudio. |
| **Notebooks por Conta** | 100 Notebooks. |
| **Interações Diárias** | Limite de approx. 50 queries (variável). |

### 3.2 Funcionalidades Exclusivas
- **Audio Overview**: Gera um podcast "Deep Dive" com dois hosts de IA discutindo seus documentos.
- **Citações (Citations)**: Toda resposta clica para o trecho exato do PDF/Doc original.
- **Suggested Actions**: Gera automaticamente Guias de Estudo, FAQs, Timelines e Briefings.

---

## 4. VERTEX AI (Enterprise)

Versão do Google Cloud para produção em larga escala e segurança corporativa.

### 4.1 Diferenciais Enterprise
- **Grounding with Google Search**: Conecta o modelo à pesquisa Google em tempo real para fatos atualizados (reduz alucinação).
- **Enterprise Data Privacy**: Seus dados NUNCA são usados para treinar os modelos base.
- **IAM & Governance**: Gestão de acesso granular e compliance (HIPAA, GDPR).
- **Model Garden**: Acesso a +130 modelos (incluindo Llama 3, Claude 3, Mistral) em uma API unificada.

### 4.2 Auto-SxS (Side by Side)
Ferramenta para avaliar automaticamente a qualidade de dois modelos (ex: Gemini vs Llama) usando um terceiro modelo como juiz.

---

## 5. GEMINI API & DESENVOLVIMENTO

### 5.1 Tool Use (Function Calling)
Estrutura JSON padrão para habilitar ações no modelo.

```json
{
  "name": "schedule_meeting",
  "description": "Schedule a meeting in the calendar",
  "parameters": {
    "type": "object",
    "properties": {
      "attendees": { "type": "array", "items": { "type": "string" } },
      "topic": { "type": "string" },
      "time": { "type": "string", "description": "ISO 8601 format" }
    },
    "required": ["topic", "time"]
  }
}
```

### 5.2 JSON Mode
Garante que o output seja um JSON válido, essencial para integração com sistemas.
*Ativado via configuração: `response_mime_type: "application/json"`.*

### 5.3 Context Caching
Para contextos muito longos que são reutilizados (ex: um livro inteiro ou documentação de API), o Cache reduz drasticamente o custo e a latência (paga-se apenas pelo armazenamento do cache e tokens novos).
