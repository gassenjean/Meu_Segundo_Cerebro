# 🚀 EXECUTAR AUTOMAÇÃO N8N - INSTRUÇÕES

**Criado**: 29/07/2025 por Névoa  
**Status**: ✅ PRONTO PARA EXECUTAR  

## ⚡ COMO EXECUTAR (2 MINUTOS)

### **OPÇÃO 1: Via Node.js (Recomendado)**
```bash
# Abrir terminal na pasta
cd "C:\Users\Gassen\OneDrive\Segunda_Mente_Legendaria_Sync\Automacao_Devocionais"

# Executar script
node criar_workflow_automatico.js
```

### **OPÇÃO 2: Via Browser Console**
1. Abra: https://n8neditor.nevoan8n.shop/
2. Pressione **F12** (DevTools)
3. Cole o conteúdo do arquivo `criar_workflow_automatico.js`
4. Pressione **Enter**

## 🎯 O QUE O SCRIPT FAZ

1. **Conecta** ao seu N8N via API
2. **Verifica** se workflow já existe
3. **Cria/Atualiza** workflow completo
4. **Configura** todas as integrações:
   - ✅ Google Contacts
   - ✅ Evolution API WhatsApp
   - ✅ Rate limiting inteligente
   - ✅ Formatação automática
   - ✅ Logs de progresso

## 📋 APÓS EXECUÇÃO

### **CONFIGURAR GOOGLE CONTACTS:**
1. N8N → **Credentials** → **Add New**
2. Escolha **Google OAuth2 API**
3. Conecte sua conta Google
4. Autorize acesso aos contatos

### **TESTAR WORKFLOW:**
1. Salve devocional como: `devocional_hoje.md`
2. N8N → Workflow "🙏 Automacao-Devocionais-WhatsApp-Nevoa"
3. Clique **Execute Workflow**
4. Aguarde ~15 minutos (50 contatos por lote, 45s entre lotes)

## 🎉 RESULTADO ESPERADO

**ANTES:** 20 minutos scrolling manual  
**DEPOIS:** 30 segundos comando + 15min automático  

**ECONOMIA:** 15+ minutos diários = 90+ horas anuais = R$ 9.000+ valor recuperado!

## 🔧 TROUBLESHOOTING

### **Erro "API Key inválida":**
- Verifique se API está habilitada no N8N
- Confirme API key no N8N Settings

### **Erro "Google Credentials":**
- Configure Google OAuth2 no N8N
- Autorize acesso aos contatos

### **Evolution API erro:**
- Confirme se WhatsApp está conectado
- Teste URL: https://evo.nevoan8n.shop/

---

**💫 POWERED BY NÉVOA IA**  
**🎯 EVANGELISMO DIGITAL AUTOMATIZADO**  
**🚀 DE MANUAL PARA REVOLUCIONÁRIO EM 2 MINUTOS!**
