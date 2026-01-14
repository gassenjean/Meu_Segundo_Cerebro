# AULA 13 - LIDANDO COM VARIÁVEIS DE UM JEITO SIMPLES

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 13/11  
**DURAÇÃO**: 45min  
**PREREQUISITOS**: Aula 12 - Nodes Condicionais  
**CRIADO**: 23/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

• **Dominar 4 tipos de variáveis** N8N (String, Number, Object, Boolean) com seus símbolos e aplicações práticas
• **Diferenciar dados estáticos vs dinâmicos** para criar automações flexíveis que se adaptam a diferentes situações
• **Implementar configuração de dados** usando nodes Set/Edit Field + correção com IA para formatação automática

## 🎯 CONCEITOS-CHAVE

### **Dados Estáticos vs Variáveis**

- **Estático**: Valores fixos que nunca mudam (ex: número específico "5592...")
- **Dinâmico**: Valores que se adaptam a cada execução (ex: número de quem enviou mensagem)
- **Regra de Ouro**: Sempre prefira variáveis para automações flexíveis

### **Pin Data (Pinar Dados)**

- **Função**: Fixar dados de teste para desenvolvimento sem reenviar mensagens
- **Identificação**: Azulzinho ao lado do node indica dados pinados
- **Vantagem**: Testa workflows sem precisar disparar triggers repetidamente
- **Limitação**: Dados ficam estáticos até você despinar

### **4 Tipos de Variáveis N8N**

#### **1. String (Texto) - Símbolo: "A" azul**

- **Uso**: Nomes, mensagens, textos em geral
- **Exemplo**: pushName = "José Carlos Amorim"
- **Condições**: Existe, vazio, contém, igual, start with

#### **2. Number (Número) - Símbolo: "#" verde**

- **Uso**: Timestamps, códigos, valores numéricos
- **Exemplo**: messageTimestamp = 1642532847
- **Condições**: Existe, maior que, menor que, igual

#### **3. Object (Objeto) - Símbolo: Cubo 3D**

- **Uso**: Conjuntos de dados relacionados (como caixinhas com vários itens)
- **Exemplo**: conversation = {evento, instância, remoteGid, pushName}
- **Característica**: Passa múltiplas informações simultaneamente

#### **4. Boolean (Lógico) - Símbolo: Setinha preta**

- **Uso**: Valores verdadeiro/falso, sim/não, true/false
- **Exemplo**: fromMe = true
- **Condições**: Apenas true ou false

### **Configuração de Dados**

- **Node Set**: Criar dados do zero
- **Node Edit Field**: Modificar dados existentes
- **Método**: Data Transformation → Set ou Edit Field
- **Resultado**: Transforma "sopa de letrinhas" em dados específicos organizados

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **Setup Básico da Aula**

```
1. Create Workflow → Renomear: "aula n8n tipos de variáveis"
2. Importar JSON template fornecido
3. Configurar Webhook: "aula variáveis" (sem acentos/caracteres especiais)
4. Conectar Evolution API com URL do webhook
5. Enviar mensagem teste do próprio número para si mesmo
6. Pinar dados (Pin Data) para desenvolvimento
```

### **Identificando Tipos de Variáveis**

```
STRING: pushName = "José Carlos Amorim" (símbolo "A" azul)
NUMBER: messageTimestamp = 1642532847 (símbolo "#" verde)
OBJECT: body = {conversation, headers, instance} (símbolo cubo 3D)
BOOLEAN: fromMe = true (símbolo setinha preta)
```

### **Configurando Dados com Set**

```
1. Node Switch → Escolher tipo correto da variável
2. Configurar condição (ex: "string existe")
3. Renomear output para identificação clara
4. Data Transformation → Set
5. Puxar variável do node anterior
6. Test Step para validar
```

### **Correção com IA (OpenAI)**

```
Problema: remoteGid vem como "5592...@s.whatsapp.net"
Solução: Node OpenAI
- Model: GPT-4O-MINI
- Prompt: "Corrija esse número tirando o @s.whatsapp.net"
- Refinamento: "Gere somente o número e nada mais"
- Resultado: Número limpo para uso direto
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**

- **String**: Nome do usuário para personalização de respostas
- **Number**: Timestamp para controle de sessão e timeout
- **Object**: Dados completos da conversa para contexto IA
- **Boolean**: Status de usuário ativo/premium para funcionalidades

### **EVANGELISMO DIGITAL:**

- **String**: Nome do contato para mensagens personalizadas
- **Number**: Código de confirmação para estudos bíblicos
- **Object**: Perfil completo do discipulado (progresso, preferências)
- **Boolean**: Status batismo/interesse para segmentação

### **GABRIELE CONFECÇÕES/KABAK:**

- **String**: Nome cliente para atendimento humanizado
- **Number**: CEP para cálculo de frete automático
- **Object**: Dados pedido completo (itens, valores, endereço)
- **Boolean**: Cliente recorrente para ofertas especiais

## 🔗 CONEXÕES

### **BUILDS SOBRE:**

- Aula 12: Nodes Condicionais (Switch/IF/Filter)
- Aula 11: Lógica e Algoritmos
- Aula 10: IA Generativa básica

### **PREPARA PARA:**

- Aula 14: Requisições HTTP avançadas
- Aula 15: Integração APIs externas
- Automações robustas com dados estruturados

## ✅ CHECKLIST AULA 13

### **CONCEITUAL:**

- [ ] Diferenço dados estáticos de variáveis dinâmicas
- [ ] Identifico os 4 tipos de variáveis pelos símbolos
- [ ] Entendo quando usar cada tipo em condições
- [ ] Compreendo função do Pin Data para desenvolvimento

### **PRÁTICO:**

- [ ] Configuro webhook e pino dados corretamente
- [ ] Uso Node Switch com tipo correto de variável
- [ ] Configuro Set/Edit Field para organizar dados
- [ ] Implemento correção IA para formatação automática

### **APLICAÇÃO:**

- [ ] Identifico onde usar variáveis nos meus projetos
- [ ] Planejo estrutura de dados para Névoa/Evangelismo/KabaK
- [ ] Domino fluxo completo: receber → processar → setar → usar
- [ ] Pronto para requisições HTTP e APIs externas

---

**STATUS**: ✅ Fundamentos de Variáveis Dominados - Base Sólida para IA Avançada
**PRÓXIMO**: Aula 14 - Requisições HTTP e Integração APIs
