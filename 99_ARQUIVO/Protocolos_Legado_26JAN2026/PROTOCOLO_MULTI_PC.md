---
criado: 2025-12-02
atualizado: 2025-12-02
---
# 🖥️💻 Protocolo Multi-PC

**Sistema de Sincronização: Alienware ↔ Desktop Casa**

## 🎯 Objetivo

Garantir que o trabalho realizado no **Alienware** (notebook trabalho/externo) e no **Desktop Casa** permaneça sincronizado, evitando conflitos e divergências.

---

## 📋 Protocolo de Início de Sessão

### Ao abrir o vault em QUALQUER PC:

1. **LER `PC_SYNC_LOG.md` COMPLETAMENTE**
   - Ver o que foi feito no outro PC
   - Verificar mensagens deixadas
   - Confirmar última sincronização

2. **Executar comando `/sync-pc`** (opcional mas recomendado)
   - Mostra resumo das últimas mudanças
   - Alerta sobre potenciais conflitos

3. **Só então começar a trabalhar**

---

## 📝 Protocolo de Fim de Sessão

### Ao finalizar trabalho significativo em QUALQUER PC:

1. **Atualizar `PC_SYNC_LOG.md`**
   - Usar template fornecido no arquivo
   - Identificar claramente qual PC (🖥️ Desktop Casa ou 💻 Alienware)
   - Listar arquivos modificados
   - Deixar mensagens para o outro PC se necessário

2. **Aguardar sincronização OneDrive** (importante!)
   - Verificar ícone do OneDrive
   - Confirmar que arquivo foi enviado para nuvem

3. **Opcional: Executar `/sync-pc` para confirmar atualização**

---

## 🔍 Identificação de PC

### Como saber em qual PC você está:

**Desktop Casa:**
- Nome do computador: Geralmente "DESKTOP-..." ou nome personalizado
- Localização: Em casa
- Hardware: PC fixo

**Alienware:**
- Nome do computador: "aliengass" ou similar
- Localização: Trabalho ou externos
- Hardware: Notebook Alienware

### Via comando (PowerShell):
```powershell
$env:COMPUTERNAME
```

---

## ⚠️ Resolução de Conflitos

### Se encontrar arquivo com sufixo "-aliengass" ou "-desktop":

1. **PAUSAR trabalho**
2. **Verificar qual versão é mais recente:**
   - Abrir ambos arquivos
   - Comparar data de modificação
   - Verificar conteúdo

3. **Decidir:**
   - **Versão mais recente:** Renomear para nome original, deletar antiga
   - **Informações únicas em ambas:** Mesclar manualmente
   - **Dúvida:** Deixar mensagem no PC_SYNC_LOG e aguardar

4. **Registrar no PC_SYNC_LOG:**
   - Qual conflito foi resolvido
   - Como foi resolvido
   - Qual arquivo foi mantido

---

## 📊 Regras de Ouro

### ✅ SEMPRE:
1. Ler PC_SYNC_LOG ao iniciar sessão
2. Atualizar PC_SYNC_LOG ao finalizar trabalho significativo
3. Identificar claramente qual PC está usando
4. Aguardar sincronização OneDrive antes de fechar
5. Deixar mensagens claras para o outro PC

### ❌ NUNCA:
1. Trabalhar em ambos PCs simultaneamente no mesmo arquivo
2. Deletar arquivos sem verificar PC_SYNC_LOG
3. Renomear arquivos importantes sem comunicação
4. Ignorar conflitos de sincronização
5. Fechar vault sem atualizar PC_SYNC_LOG (se mudou algo)

---

## 🎯 Workflow Ideal

### Cenário 1: Iniciar trabalho no Desktop Casa

```
1. Abrir vault
2. Ler PC_SYNC_LOG.md
3. Ver que última sessão foi no Alienware
4. Confirmar que OneDrive sincronizou
5. Começar trabalho
6. Ao finalizar: Atualizar PC_SYNC_LOG
7. Aguardar sync OneDrive
```

### Cenário 2: Iniciar trabalho no Alienware

```
1. Abrir vault
2. Ler PC_SYNC_LOG.md
3. Ver que última sessão foi no Desktop Casa
4. Confirmar que OneDrive sincronizou
5. Começar trabalho
6. Ao finalizar: Atualizar PC_SYNC_LOG
7. Aguardar sync OneDrive
```

### Cenário 3: Trocar de PC no meio do dia

```
Desktop Casa (manhã):
1. Trabalhar e atualizar PC_SYNC_LOG
2. Aguardar sync OneDrive
3. Fechar vault

Alienware (tarde):
1. Abrir vault
2. Ler PC_SYNC_LOG (ver trabalho da manhã)
3. Continuar trabalho
4. Atualizar PC_SYNC_LOG
5. Aguardar sync OneDrive
```

---

## 🛠️ Ferramentas

### Comando `/sync-pc`

**Uso:**
```
/sync-pc
```

**Função:**
- Lê PC_SYNC_LOG.md
- Mostra últimas 3 mudanças
- Alerta sobre conflitos detectados
- Identifica qual PC você está usando

### Arquivo `PC_SYNC_LOG.md`

**Localização:** Raiz do vault
**Função:** Canal central de comunicação entre PCs
**Atualização:** Manual (usar template fornecido)

---

## 📈 Exemplo Prático

### Desktop Casa (Segunda 09:00):
```markdown
### 🖥️ Desktop Casa - 02/12/2025 (09:00)
**Ações realizadas:**
- ✅ Criado nota sobre curso Alan Nicolas
- ✅ Atualizado MOC_Aprendizado

**Arquivos modificados:**
- 03_APRENDIZADO/Alan_Nicolas/Aula_05_Agentes.md (nova)
- 03_APRENDIZADO/_MOC_Aprendizado.md (adicionado link)

**Mensagem para Alienware:**
> Criei nota da Aula 5. Quando trabalhar lá, continue da Aula 6!
```

### Alienware (Segunda 14:00):
```markdown
### 💻 Alienware - 02/12/2025 (14:00)
**Ações realizadas:**
- ✅ Li nota da Aula 5 (obrigado Desktop!)
- ✅ Criado nota Aula 6 
- ✅ Iniciado projeto prático

**Arquivos modificados:**
- 03_APRENDIZADO/Alan_Nicolas/Aula_06_Automacao.md (nova)
- 02_PROJETOS/Agente_Vendas/README.md (nova)

**Mensagem para Desktop Casa:**
> Aula 6 concluída! Iniciei projeto prático de agente de vendas.
> Pode revisar quando chegar em casa?
```

### Desktop Casa (Segunda 19:00):
```markdown
### 🖥️ Desktop Casa - 02/12/2025 (19:00)
**Ações realizadas:**
- ✅ Revisei projeto Agente_Vendas (ficou ótimo!)
- ✅ Adicionei sugestões no README

**Arquivos modificados:**
- 02_PROJETOS/Agente_Vendas/README.md (adicionado seção "Melhorias")

**Mensagem para Alienware:**
> Projeto revisado! Adicionei ideias de melhorias. Bom trabalho! 👏
```

---

## 📝 Template de Atualização

```markdown
### [🖥️ Desktop Casa | 💻 Alienware] - DD/MM/YYYY (HH:MM)
**Ações realizadas:**
- ✅ [Ação 1]
- ✅ [Ação 2]

**Arquivos modificados:**
- [caminho/arquivo.md] ([o que mudou])

**Próximos passos sugeridos:**
- [ ] [Tarefa pendente]

**Mensagem para [outro PC]:**
> [Mensagem clara e direta]
```

---

## 🚨 Troubleshooting

### Problema: OneDrive não está sincronizando

**Solução:**
1. Verificar conexão internet
2. Verificar ícone OneDrive (nuvem com X = problema)
3. Clicar com direito no ícone OneDrive → "Settings"
4. Verificar se pasta do vault está sendo sincronizada
5. Forçar sincronização: Clicar com direito → "Sync now"

### Problema: Arquivo de conflito criado

**Solução:**
Ver seção "Resolução de Conflitos" acima

### Problema: Esqueci de atualizar PC_SYNC_LOG

**Solução:**
1. Atualizar assim que lembrar
2. Ser o mais específico possível sobre o que foi feito
3. Deixar mensagem de alerta no outro PC

---

**LEMBRE-SE:** Sincronização é responsabilidade NOSSA, não da tecnologia. O sistema só funciona se usarmos! 🤝
