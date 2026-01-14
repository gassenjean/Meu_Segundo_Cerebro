---
criado: 2025-07-22T10:40:53-03:00
atualizado: 2025-07-22T10:40:53-03:00
---

# AULA 02 - INSTALAÇÃO VPS + EASYPANEL

---

**MÓDULO**: N8N Mastery  
**SEQUÊNCIA**: 02/11  
**DURAÇÃO**: 60min  
**PREREQUISITOS**: Fundamentos e Arquitetura (Aula 01)  
**CRIADO**: 09/07/2025 por Névoa

---

## ⚡ RESUMO EXECUTIVO

Esta é a aula da **INFRAESTRUTURA SÓLIDA**! Você vai sair do conceitual para o prático, criando a base tecnológica que sustentará todos os seus workflows. VPS configurado + EasyPanel instalado = fundação pronta para o N8N.

**O QUE VOCÊ VAI DOMINAR:**

- Contratação e configuração de VPS adequado
- Instalação e configuração do EasyPanel
- Preparação do ambiente para receber N8N + Evolution + Chatwoot

## 🎯 CONCEITOS-CHAVE

### **VPS - Virtual Private Server:**

- **Definição**: Máquina virtual dedicada rodando 24/7 na nuvem
- **Vantagem**: Controle total vs hospedagem compartilhada
- **Necessidade**: Base estável para automações críticas

### **EasyPanel - Interface de Gerenciamento:**

- **Função**: Painel visual para gerenciar aplicações no VPS
- **Benefício**: Instalar N8N, Evolution, Chatwoot sem linha de comando
- **Alternativas**: Portainer, Docker direto (mais complexo)

### **Requisitos Mínimos vs Recomendados:**

```
MÍNIMO (teste):
- RAM: 2GB
- CPU: 1 core
- Storage: 10GB

RECOMENDADO (produção):
- RAM: 4GB
- CPU: 2 cores
- Storage: 20GB SSD
```

## 💻 IMPLEMENTAÇÃO PRÁTICA

### **PASSO 1: Contratação VPS**

```bash
# Fornecedores recomendados:
- DigitalOcean (internacional, confiável)
- Vultr (boa performance)
- Contabo (custo/benefício)
- HostGator (suporte português)

# SO recomendado:
Ubuntu 22.04 LTS (estabilidade + compatibilidade)
```

### **PASSO 2: Acesso SSH Inicial**

```bash
# Via terminal/putty:
ssh root@SEU_IP_VPS
# Primeira configuração:
- Atualizar sistema: apt update && apt upgrade
- Configurar firewall básico
- Criar usuário não-root (opcional)
```

### **PASSO 3: Instalação EasyPanel**

```bash
# Comando oficial (uma linha):
curl -sSL https://get.easypanel.io | sh

# Aguardar instalação completa (5-10 minutos)
# Acessar via navegador: http://SEU_IP:3000
```

### **PASSO 4: Configuração Inicial EasyPanel**

```javascript
// Interface web EasyPanel:
1. Criar conta admin
2. Configurar domínio (opcional)
3. Ativar SSL (Let's Encrypt)
4. Testar criação de app básico
```

## 🛠️ CASOS DE USO - MEUS PROJETOS

### **NÉVOA IA:**

- **Ambiente isolado** para processamento de IA
- **Recursos dedicados** para respostas rápidas
- **Logs centralizados** para debugging
- **Escalabilidade** baseada em demanda

### **EVANGELISMO DIGITAL:**

- **Disponibilidade 24/7** para leads espirituais
- **Backup automático** de conversas importantes
- **Monitoramento** de performance em tempo real
- **Segurança** de dados sensíveis

### **GABRIELE CONFECÇÕES/KABAK:**

- **Integração e-commerce** sem interrupções
- **Processamento de pedidos** contínuo
- **Relatórios automáticos** de vendas
- **Suporte multicanal** unificado

## 🔗 CONEXÕES

### **BUILDS SOBRE:**

- Aula 01: Arquitetura agora vira realidade física

### **PREPARA PARA:**

- Aula 03: N8N será instalado nesta base
- Aula 04: Evolution API usará este ambiente
- Aula 05: Chatwoot integrará ao stack completo

### **DEPENDÊNCIAS CRÍTICAS:**

- VPS estável = todos os workflows funcionando
- EasyPanel configurado = instalações futuras simplificadas

## ✅ CHECKLIST AULA 02

### **INFRAESTRUTURA:**

- [ ] VPS contratado com especificações adequadas
- [ ] Acesso SSH funcionando perfeitamente
- [ ] Sistema operacional atualizado
- [ ] EasyPanel instalado e acessível

### **CONFIGURAÇÃO:**

- [ ] Interface EasyPanel acessível via navegador
- [ ] Conta admin criada e configurada
- [ ] SSL configurado (se domínio disponível)
- [ ] Teste de criação de app realizado

### **VALIDAÇÃO:**

- [ ] VPS respondendo consistentemente
- [ ] EasyPanel estável sem travamentos
- [ ] Recursos de sistema adequados (RAM, CPU)
- [ ] Pronto para receber aplicações complexas

### **DOCUMENTAÇÃO:**

- [ ] IPs e credenciais anotados em local seguro
- [ ] URLs de acesso documentadas
- [ ] Procedimentos de backup planejados
- [ ] Contatos de suporte do fornecedor salvos

---

**STATUS**: ✅ Infraestrutura sólida estabelecida  
**RESULTADO**: VPS + EasyPanel prontos para receber N8N stack  
**PRÓXIMO**: Aula 03 - Instalação do N8N no ambiente preparado

_"Base sólida, automações estáveis"_
