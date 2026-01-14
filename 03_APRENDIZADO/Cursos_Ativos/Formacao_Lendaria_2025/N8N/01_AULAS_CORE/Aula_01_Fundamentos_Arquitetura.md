---
criado: 2025-07-22T10:40:24-03:00
atualizado: 2025-07-22T10:40:24-03:00
---

# AULA 01 - FUNDAMENTOS E ARQUITETURA N8N

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 01/11  
**DURAÇÃO**: 90min  
**PREREQUISITOS**: Conhecimento básico de automação  
**CRIADO**: 09/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

Esta aula estabelece a **arquitetura completa do sistema N8N**, comparações de custo com concorrentes, e apresenta o modelo self-hosted que permite controle total e economia a longo prazo. É a **aula de fundação** que justifica todo o investimento de tempo e esforço no projeto.

**O QUE VOCÊ VAI DOMINAR:**

- Comparação financeira N8N vs Make (economia 80%+)
- Arquitetura completa: Domínio → VPS → EasyPanel → N8N + Evolution + Chatbot
- Casos de uso conectados com seus projetos reais

## 🎯 CONCEITOS-CHAVE

### **N8N vs Make - Análise Estratégica:**

**N8N Cloud**: $125/mês (2.500 workflows + 5 ativos) = R$750/mês
**Make**: $9/mês (10.000 operações) = R$54/mês
**DIFERENÇA**: 1300% mais caro!

**N8N Self-hosted**: $20-50/mês VPS = economia 80%+ a longo prazo

### **Arquitetura Completa do Sistema:**

```
🌐 DOMÍNIO (seu endereço web)
    ↓
💻 VPS (máquina virtual 24/7)
    ↓
🖥️ EasyPanel (interface visual/monitor)
    ↓
🔧 N8N (automação/integração)
🤖 Evolution (API WhatsApp)
💬 Chatwoot (centralizador comunicação)
```

### **Self-hosted vs SaaS:**

- **Controle total** sobre dados e configurações
- **Escalabilidade ilimitada** sem custo por operação
- **Customização avançada** para necessidades específicas
- **Independência** de mudanças de política das plataformas

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **Especificações VPS Recomendadas:**

```bash
RAM: 4GB (mínimo 2GB)
CPU: 2 cores
Storage: 20GB SSD
Bandwidth: Ilimitado
Uptime: 99.9% garantido
```

### **Stack de Software:**

```javascript
// Ordem de instalação obrigatória:
1. VPS + Sistema Operacional
2. EasyPanel (interface de gerenciamento)
3. N8N (plataforma de automação)
4. Evolution API (WhatsApp Business)
5. Chatwoot (centralizador de atendimento)
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**

- Integração via N8N para processamento de dados
- Evolution para conversas WhatsApp
- Chatwoot para centralizar atendimento multicanal
- **Benefício**: IA rodando em infraestrutura própria

### **EVANGELISMO DIGITAL:**

- Workflows automáticos para nurturing espiritual
- Sequências baseadas em comportamento/engajamento
- Integração com CRM de leads espirituais
- **Benefício**: Automação 24/7 sem dependência externa

### **GABRIELE CONFECÇÕES/KABAK:**

- Automação pedidos → produção → entrega
- Lead scoring e qualificação automática
- Relatórios de performance em tempo real
- **Benefício**: Operação escalável sem aumentar equipe

## 🔗 CONEXÕES

### **SE CONECTA COM:**

- Aula 02: Implementação prática da arquitetura
- Aula 03: Instalação do N8N no stack definido

### **PREPARA PARA:**

- Todo o projeto N8N Mastery
- Compreensão do investimento vs retorno
- Decisão consciente sobre self-hosted

## ✅ CHECKLIST AULA 01

### **CONCEITUAL:**

- [ ] Entendi a diferença de custo N8N vs Make
- [ ] Compreendi a arquitetura completa do sistema
- [ ] Vejo as vantagens do modelo self-hosted
- [ ] Identifiquei aplicações nos meus projetos

### **DECISÓRIO:**

- [ ] Decidi investir no modelo self-hosted
- [ ] Tenho clareza do tempo de setup necessário
- [ ] Estou preparado para a complexidade inicial
- [ ] Vejo o ROI a longo prazo

### **PREPARATÓRIO:**

- [ ] Pesquisei fornecedores de VPS
- [ ] Defini orçamento para infraestrutura
- [ ] Planejei cronograma de implementação
- [ ] Estou pronto para Aula 02

---

**STATUS**: ✅ Fundação arquitetural estabelecida  
**RESULTADO**: Justificativa técnica e financeira para o projeto  
**PRÓXIMO**: Aula 02 - Implementação prática da infraestrutura

_"Quem entende a arquitetura, domina a implementação"_
