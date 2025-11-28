# AULA 12 - FILTRANDO CURIOSOS COM NODES CONDICIONAIS

---
**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 12/11  
**DURAÇÃO**: 45min  
**PREREQUISITOS**: Aula 11 - Projeto Transcrevendo Áudio  
**CRIADO**: 22/07/2025 por Névoa
---

## ⚡ RESUMO EXECUTIVO
• **Domínio dos 3 tipos de nodes condicionais** (IF, FILTER, SWITCH) para criar automações inteligentes que filtram mensagens e direcionam fluxos
• **Implementação de sistema de atendimento automatizado** usando critérios específicos para separar leads qualificados de curiosos casuais
• **Integração avançada com IA** (OpenAI) para respostas dinâmicas baseadas em condições e extração de variáveis específicas

## 🎯 CONCEITOS-CHAVE

### Node IF - Condições Simples
**Definição**: Node básico para criar condições binárias simples (verdadeiro/falso)
**Aplicação**: Verificar palavras específicas como "Oi" para disparar respostas automáticas
**Estrutura**: Entrada → Condição → Saída True/False

### Node FILTER - Filtros Personalizados  
**Definição**: Node para condições mais específicas e complexas que o IF básico
**Aplicação**: Verificar se mensagem contém palavras-chave como "comprar", "preço", "disponível"
**Vantagem**: Maior flexibilidade para critérios de filtragem avançados

### Node SWITCH - Múltiplas Condições
**Definição**: Node para gerenciar várias condições diferentes em um único ponto
**Aplicação**: Direcionar diferentes tipos de produtos (carro, motosserra, celular) para vendedores específicos
**Estrutura**: Uma entrada → Múltiplas saídas baseadas em critérios distintos

### Automação de Atendimento Inteligente
**Conceito**: Sistema que filtra, prioriza e direciona mensagens automaticamente
**Componentes**: Filtros de relevância + Priorização de leads + Encaminhamento personalizado
**Objetivo**: Maximizar eficiência separando mensagens comerciais de conversas casuais

## 💻 IMPLEMENTAÇÃO PRÁTICA

### Configuração Node IF Básico
```
1. Webhook de entrada (WhatsApp)
2. Node IF com condição: message.text = "Oi"  
3. Node de resposta automática
4. Teste: enviar "Oi" → verificar resposta
```

### Sistema de Filtros com FILTER
```
Webhook → Node FILTER (contains "comprar") → True: Resposta comercial
                                          → False: Ignorar ou resposta padrão
```

### Implementação SWITCH para Múltiplos Produtos
```
Webhook → Node SWITCH:
    - Caso "carro": Direcionar para vendedor A
    - Caso "motosserra": Direcionar para vendedor B  
    - Caso "celular": Direcionar para vendedor C
    - Default: Resposta genérica
```

### Integração com OpenAI
```
1. Node OpenAI configurado com prompt inteligente
2. Extração de variáveis (ex: números de telefone)
3. Tratamento dinâmico de respostas baseado no contexto
4. Teste com diferentes tipos de mensagens
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### NÉVOA IA:
**Filtro de Consultas Técnicas**: Node SWITCH para direcionar dúvidas sobre IA, automação ou desenvolvimento para módulos específicos de resposta. Node FILTER para identificar consultas que precisam de análise humana vs automática.

### EVANGELISMO DIGITAL:
**Sistema de Acolhimento**: Node IF para detectar primeiras mensagens, Node FILTER para identificar pedidos de oração ou aconselhamento, Node SWITCH para direcionar entre conteúdo bíblico, eventos da igreja ou contato direto com liderança.

### GABRIELE CONFECÇÕES/KABAK:
**Qualificação de Leads**: Node FILTER para identificar interesse real de compra (palavras como "preço", "disponível", "comprar"), Node SWITCH para separar por categoria de produto (roupas femininas, masculinas, acessórios), integração OpenAI para extrair tamanho e preferências automaticamente.

## 🔗 CONEXÕES

### BUILDS SOBRE:
- Aula 11: Projeto de transcrição de áudio (base de webhook e processamento)
- Aula 10: Integração WhatsApp + Evolution API (entrada de mensagens)
- Aula 09: Fundamentos de nodes e fluxos de trabalho

### PREPARA PARA:
- Aula 13: Automações avançadas com múltiplas integrações
- Casos de uso comerciais escaláveis
- Sistemas de CRM automatizado com N8N

## ✅ CHECKLIST AULA 12

### CONCEITUAL:
- [ ] Compreendo a diferença entre IF, FILTER e SWITCH
- [ ] Entendo quando usar cada tipo de node condicional  
- [ ] Sei como estruturar fluxos de atendimento automatizado
- [ ] Compreendo integração de IA com nodes condicionais

### PRÁTICO:
- [ ] Configurei node IF funcionando com teste real
- [ ] Implementei node FILTER com palavra-chave específica
- [ ] Criei node SWITCH com múltiplas condições
- [ ] Testei integração OpenAI com extração de variáveis

### APLICAÇÃO:
- [ ] Identifiquei 3 casos de uso específicos para meus projetos
- [ ] Desenhei fluxo de atendimento para uma das minhas marcas
- [ ] Planejei integração com sistema existente de WhatsApp
- [ ] Documentei critérios de filtragem para leads qualificados

---
**STATUS**: ✅ Nodes condicionais dominados - Sistema de filtragem inteligente implementado
**PRÓXIMO**: Aula 13 - Automações avançadas e integração com CRM