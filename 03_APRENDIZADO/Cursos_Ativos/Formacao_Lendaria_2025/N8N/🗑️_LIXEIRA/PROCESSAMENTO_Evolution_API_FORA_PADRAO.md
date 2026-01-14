---
criado: 2025-07-10T14:10:00-03:00
atualizado: 2025-07-10T14:10:00-03:00
tipo: material-source
tags: [#evolution, #api, #whatsapp, #instalacao, #tutorial]
status: processado
prioridade: alta
---

# 📱 MATERIAL ORIGINAL - EVOLUTION API INSTALLATION

## 📄 DOCUMENTO BASE

**Arquivo Original**: `4. Instalando o Evolution API.md`
**PDF Transcrito**: `4. Instalando o Evolution API [LENDARIA][N8N].pdf`
**Data Processamento**: 10/07/2025
**Status**: ✅ Processado e implementado com sucesso

## 🎯 RESUMO DO MATERIAL

### **CONTEÚDO PRINCIPAL**

Guia completo para instalação e configuração do Evolution API, incluindo:

- Preparação do ambiente N8N
- Criação do projeto Evolution no EasyPanel
- Configuração de esquemas e portas internas
- Setup de PostgreSQL e Redis
- Configuração de DNS e domínios
- Acesso ao manager e autenticação

### **LINKS ESSENCIAIS FORNECIDOS**

- **Helper Evolution**: https://evolutiolendario.netlify.app
- **Gerador de senhas**: https://acte.ltd/utils/randomkeygen
- **Verificação DNS**: dnschecker.org (mencionado no contexto)

## 🔧 PROCESSO DOCUMENTADO

### **FASE 1: Preparação**

1. Acessar N8N funcionando via EasyPanel
2. Voltar à área inicial do EasyPanel
3. Criar novo projeto "Evolution API"

### **FASE 2: Configuração Esquemas**

1. Copiar esquema fornecido no material
2. Criar esquema no EasyPanel
3. Aguardar instalação dos componentes:
   - evo-postgres (banco de dados)
   - evo-redis (cache/filas)
   - evolution-api (core)

### **FASE 3: Configuração Portas**

1. **evo-postgres**: Credentials → Internal Port → Expose Port
2. **evo-redis**: Credentials → Internal Port → Expose Port
3. Salvar configurações e aguardar reinicialização

### **FASE 4: Configuração Ambiente Evolution**

1. **Linha 10**: Substituir por PostgreSQL Internal Connection URL
2. **Linha 13**: Substituir por Redis Internal Connection URL
3. **Linha 106**: Substituir API Key por nova gerada
4. Salvar todas as configurações

### **FASE 5: Deploy e DNS**

1. Force Rebuild → Deploy
2. Aguardar aplicativo implantado (verde)
3. Configurar DNS: evo.dominio.com → IP_VPS
4. Configurar DNS: www.evo.dominio.com → IP_VPS

### **FASE 6: Configuração Domínio Evolution**

1. EasyPanel → Evolution → Domains
2. Porta: 8080
3. Domínio: evo.seudominio.com
4. Criar domínio

### **FASE 7: Acesso Final**

1. URL: evo.seudominio.com/manager
2. Login: API Global Key (linha 106)
3. Interface Evolution carregando

## 💡 INSIGHTS DO MATERIAL ORIGINAL

### **Dicas Técnicas Importantes**

- **Caracteres especiais**: Evitar em nomes de projetos
- **URL Manager**: Sempre usar /manager no final
- **API Global**: Linha 106 é crítica para acesso
- **DNS Propagation**: Aguardar até 24h se necessário

### **Troubleshooting Mencionado**

- Problemas com caracteres especiais em nomes
- Necessidade de /manager na URL
- API Global key deve ser salva com cuidado
- DNS pode demorar para propagar

### **Sequência Lógica Identificada**

1. Infraestrutura (VPS + EasyPanel) ✅
2. N8N funcionando ✅
3. Evolution API (este material) ✅
4. Chatbot (próximo na sequência)

## 🎯 APLICAÇÃO PRÁTICA REALIZADA

### **IMPLEMENTAÇÃO REAL (10/07/2025)**

- [x] Material estudado e estruturado
- [x] Processo seguido passo-a-passo
- [x] Evolution API instalado com sucesso
- [x] Manager acessível e funcional
- [x] API Global configurada
- [x] Sistema pronto para workflows

### **ADAPTAÇÕES NECESSÁRIAS**

- Domínio específico do Gassen utilizado
- API Global key específica gerada e salva
- DNS configurado conforme provider específico
- Integração validada com N8N existente

## 📚 TRANSFORMAÇÃO EM AULA ESTRUTURADA

### **PROCESSO DE CRIAÇÃO**

1. **Análise do material**: Identificação de conceitos-chave
2. **Estruturação didática**: Organização em fases lógicas
3. **Conexão com projetos**: Aplicação específica do Gassen
4. **Troubleshooting**: Antecipação de problemas comuns
5. **Checkpoint**: Validação passo-a-passo

### **ARQUIVO GERADO**

- **Nome**: `Aula_04_Instalacao_Evolution_API.md`
- **Localização**: `01_AULAS_CORE/`
- **Estrutura**: Seguindo template "Aula-Lego"
- **Foco**: Aplicação prática nos projetos do Gassen

## 🔄 STATUS PROCESSAMENTO

### **✅ CONCLUÍDO**

- [x] Material original analisado
- [x] Aula estruturada criada
- [x] Implementação prática realizada
- [x] Checkpoint de sucesso documentado
- [x] Integração com sistema existente
- [x] Próximos passos identificados

### **📁 ARQUIVOS RELACIONADOS**

- `Aula_04_Instalacao_Evolution_API.md` (aula estruturada)
- `CHECKPOINT_AULA_04_EVOLUTION_SUCESSO.md` (validação)
- `INDICE_COMPLETO_N8N_MASTERY.md` (atualizado)
- `PROGRESSO_SEMANAL_10_07_2025.md` (marcos)

## 🚀 IMPACTO NO PROJETO

### **CAPACIDADES DESBLOQUEADAS**

- WhatsApp como interface de automação
- Gateway para comunicação N8N → WhatsApp
- Base para workflows comerciais
- Integração com projetos Névoa, evangelismo, negócios

### **CONHECIMENTO CONSOLIDADO**

- Processo completo de instalação Evolution
- Troubleshooting específico da ferramenta
- Integração com infraestrutura N8N
- Configuração DNS e domínios

### **PRÓXIMOS PASSOS IDENTIFICADOS**

- Aula 05: Chatbot integration
- Primeiro workflow N8N → Evolution → WhatsApp
- Casos de uso específicos por projeto
- Templates reutilizáveis

---

**Status**: ✅ Material processado com sucesso e aplicado na prática
**Resultado**: Evolution API operacional e integrado ao sistema
**Próximo**: Chatbot para completar a tríade N8N + Evolution + Chat

_"Do material bruto ao conhecimento estruturado e aplicado"_
