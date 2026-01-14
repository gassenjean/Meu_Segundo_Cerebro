---
criado: 2025-12-23T19:55:48-03:00
atualizado: 2025-12-23T19:55:48-03:00
---

# 🧹 PLANO ORGANIZAÇÃO: KABAK (Marie Kondo)

**Objetivo:** Unificar as duas pastas do projeto KabaK em uma estrutura canônica, seguindo o padrão `NOMENCLATURA.md` e eliminando duplicidades.

## 🚨 Diagnóstico (O Caos Atual)

1. **Duplicidade:**
   - 📂 `02_PROJETOS/KabaK/` (Onde o trabalho real aconteceu: Proposta Sansom)
   - 📂 `02_PROJETOS/KabaK_Reestruturacao_2025/` (Estrutura legada antiga referenciada no MOC)

2. **Problema:**
   - O MOC aponta para a pasta vazia/antiga.
   - O trabalho está "escondido" em uma subpasta `Outlet_Expansion`.
   - Nomes longos e confusos (`KabaK_Reestruturacao_2025`).

---

## ✨ A Solução (Simples & Canônica)

Vamos consolidar TUDO em **`02_PROJETOS/KabaK/`**.

### 1. Estrutura Alvo (Canonical)

```markdown
02*PROJETOS/KabaK/
├── README.md ← (Do antigo, atualizado)
├── STATUS_ATUAL.md ← (Do antigo, atualizado com status da Proposta)
├── Outlet_Expansion/ ← (A "Operação Libertação" fica aqui como módulo)
│ ├── PROPOSTA_FINAL*...md
│ └── docs/
├── planejamento/ ← (Pasta padrão)
├── docs/ ← (Pasta padrão)
└── recursos/ ← (Pasta padrão)
```

### 2. Plano de Ação

#### FASE 1: Migração (Movimentação)

- [ ] Mover `README.md` e `STATUS_ATUAL.md` de `KabaK_Reestruturacao_2025` para `KabaK`.
- [ ] Mover subpastas padrão (`checkpoints`, `tarefas`, etc) de `KabaK_Reestruturacao_2025` para `KabaK` (se não existirem lá).
- [ ] Deletar pasta vazia `KabaK_Reestruturacao_2025`.

#### FASE 2: Consolidação (Edição)

- [ ] **README.md:** Atualizar para refletir que o foco atual é a "Outlet Expansion/Parceria Sansom".
- [ ] **STATUS_ATUAL.md:** Atualizar para "Aguardando Assinatura" (baseado no SESSION_LOG).

#### FASE 3: Correção de Links

- [ ] Atualizar `00_SISTEMA/MOCs/_MOC_Projetos.md`:
  - De: `[[02_PROJETOS/KabaK_Reestruturacao_2025/README.md|...]]`
  - Para: `[[02_PROJETOS/KabaK/README.md|KabaK Brands]]`

---

## ⚠️ Aprovação Necessária

Você autoriza a **exclusão** da pasta `KabaK_Reestruturacao_2025` após a migração segura dos arquivos?
