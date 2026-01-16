---
criado: 2025-12-02T11:14:00-03:00
tipo: guia-rapido
status: deprecado
atualizado: 2026-01-16T13:22:50-03:00
---

# [DEPRECADO] ⚡ GUIA RÁPIDO: Erro "Model Provider Overload"

⚠️ **DEPRECADO** - Ver [[TROUBLESHOOTING_GUIA_RAPIDO.md]] (Categoria 1: Overload Contexto)

**Razão:** Consolidado em guia único de troubleshooting com 6 categorias
**Data deprecação:** 16/Jan/2026
**Substituído por:** [[TROUBLESHOOTING_GUIA_RAPIDO.md#categoria-1-overload-contexto-claude]]

**Por que deprecado:**
- Conteúdo fragmentado em 2 guias diferentes (este + GUIA_RECUPERACAO_ERRO_GEMINI)
- Dificulta navegação e manutenção
- TROUBLESHOOTING_GUIA_RAPIDO.md consolida 6 categorias de problemas em um único local

**Use o novo arquivo:**
→ [[TROUBLESHOOTING_GUIA_RAPIDO.md]]

---

**[CONTEÚDO ORIGINAL PRESERVADO ABAIXO PARA REFERÊNCIA HISTÓRICA]**

---

# ⚡ GUIA RÁPIDO: Erro "Model Provider Overload"

**Problema:** "Agent execution terminated due to model provider overload"

---

## 🚨 O QUE FAZER AGORA

### Opção 1: Aguardar e Tentar Novamente (Recomendado)

```
1. ⏸️ Aguardar 5 minutos
2. 🔄 Trocar para Gemini 3 Pro novamente
3. ✅ Se funcionar: Continuar trabalho
4. ❌ Se falhar: Ir para Opção 2
```

### Opção 2: Usar Claude Temporariamente

```
1. 🔵 Continuar com Claude (você está usando agora)
2. 📝 Fazer a tarefa atual
3. 💾 Documentar no SESSION_LOG
4. ⏰ Tentar Gemini novamente em 15-30 min
```

### Opção 3: Agendar para Depois

```
1. 📅 Anotar tarefa pendente
2. ⏰ Processar em horário alternativo:
   - Madrugada (0h-6h)
   - Fim de semana
   - Horários fora de pico
3. ✅ Maior taxa de sucesso
```

---

## 📊 QUANDO OCORRE MAIS

**Horários de PICO (mais erros):**
- 🔴 Segunda a Sexta: 9h-18h
- 🔴 Início da manhã: 8h-10h
- 🔴 Após almoço: 13h-15h

**Horários MELHORES (menos erros):**
- 🟢 Madrugada: 0h-6h
- 🟢 Fim de semana
- 🟢 Noite: 22h-0h

---

## 💡 ESTRATÉGIA HÍBRIDA (Recomendada)

```
┌─────────────────────────────────────┐
│ 1. Tentar Gemini 3 Pro              │
└──────────┬──────────────────────────┘
           │
           ▼
    ┌──────────────┐
    │ Funcionou?   │
    └──┬───────┬───┘
       │       │
      SIM     NÃO
       │       │
       ▼       ▼
   ┌─────┐  ┌──────────────────────┐
   │ Usar│  │ Aguardar 5 min       │
   │Gemini│ │ Tentar novamente     │
   └─────┘  └──────┬───────────────┘
                   │
                   ▼
            ┌──────────────┐
            │ Funcionou?   │
            └──┬───────┬───┘
               │       │
              SIM     NÃO
               │       │
               ▼       ▼
           ┌─────┐  ┌─────────────────┐
           │ Usar│  │ Usar Claude     │
           │Gemini│ │ Documentar      │
           └─────┘  │ Tentar depois   │
                    └─────────────────┘
```

---

## 📝 TEMPLATE DE DOCUMENTAÇÃO

**Quando usar Claude por causa de overload, adicionar ao SESSION_LOG:**

```markdown
### 🔵 Claude Code - [DATA] ([HORA])

**FALLBACK: Gemini Overload**

**Ações realizadas:**
- ⚠️ Gemini 3 Pro indisponível (model provider overload)
- ✅ Tarefa executada com Claude: [Descrição]
- 📝 Arquivos: [Lista]

**Próximos passos:**
- [ ] Tentar Gemini novamente em [Horário]
- [ ] Retomar processamento em massa quando disponível

**Mensagem para Gemini:**
> Executei [tarefa] por você pois estava indisponível.
> Quando voltar, pode retomar a partir de [ponto].
```

---

## ✅ CHECKLIST RÁPIDO

**Quando ver erro de overload:**

- [ ] Aguardei 5 minutos?
- [ ] Tentei novamente?
- [ ] Se persistiu: Usei Claude?
- [ ] Documentei no SESSION_LOG?
- [ ] Agendei retry para depois?

---

## 🎯 REGRA DE OURO

**NÃO ficar tentando repetidamente!**

```
❌ ERRADO:
Tentar → Erro → Tentar → Erro → Tentar → Erro...

✅ CORRETO:
Tentar → Erro → Aguardar 5min → Tentar → Erro → Usar Claude → Tentar depois
```

---

## 💰 ECONOMIA

**Por que não usar só Claude:**
- Gemini: R$ 0,00 (gratuito)
- Claude: ~R$ 0,10 por 1000 tokens
- Tarefa de 1M tokens: R$ 0 (Gemini) vs R$ 100 (Claude)

**Estratégia:**
- Gemini: 80% do trabalho (processamento em massa)
- Claude: 20% do trabalho (decisões críticas + fallback)
- **Economia: ~R$ 400-500 por projeto grande**

---

**Versão:** 1.0
**Criado:** 02/Dez/2025
**Atualizado:** 02/Dez/2025

**"Paciência e estratégia > Insistência sem planejamento"** ⏰✅
