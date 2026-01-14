---
description: Sincronizar trabalho entre Alienware e Desktop Casa
---

# 🖥️💻 Sync PC - Sincronização Multi-Computador

Ativa o sistema de sincronização entre **Alienware** (notebook trabalho/externo) e **Desktop Casa**.

## Como usar

1. **Ao INICIAR sessão em qualquer PC:**

   ```
   /sync-pc
   ```

   - Mostra últimas mudanças do outro PC
   - Alerta sobre potenciais conflitos
   - Identifica qual PC você está usando

2. **Ao FINALIZAR trabalho significativo:**
   - Atualizar manualmente `PC_SYNC_LOG.md` (raiz do vault)
   - Usar template fornecido no arquivo
   - Aguardar sincronização OneDrive

## Turbo Mode

// turbo
Este comando é seguro para auto-run ao navegar entre PCs.

## Protocolo Completo

Ver: `00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md`

## Arquivo Central

**PC_SYNC_LOG.md** (raiz do vault)

- Comunicação bidirecional Alienware ↔ Desktop Casa
- Template de atualização incluído
- Histórico das últimas 10 sessões

## Quando usar

- ✅ **Sempre** ao iniciar sessão no vault
- ✅ **Sempre** ao finalizar trabalho significativo
- ✅ Ao trocar de PC no meio do dia
- ✅ Antes de modificar arquivo que pode ter sido editado no outro PC

## Identificação de PC

**Desktop Casa:**

- 🖥 ️ PC fixo em casa
- Nome geralmente "DESKTOP-..."

**Alienware:**

- 💻 Notebook trabalho/externo
- Nome "aliengass" ou similar

## Regra de Ouro

> **Ler `PC_SYNC_LOG.md` ao iniciar, atualizar ao finalizar.**  
> Zero conflitos, continuidade perfeita! 🤝
