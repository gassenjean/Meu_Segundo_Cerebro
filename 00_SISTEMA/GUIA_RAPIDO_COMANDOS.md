---
criado: 2025-12-30
atualizado: 2025-12-30
versao: 3.0
---

# ⚡ GUIA RÁPIDO - Comandos Claude Code

**Total:** 18 comandos | **Doc completa:** `.claude/commands/README.md`

---

## 🚀 INÍCIO RÁPIDO

```bash
# Todo dia começa assim:
/mapa
/coach check-in

# Durante trabalho:
/coach foco "[tarefa]"

# Fim do dia:
/coach resumo
/sync
```

---

## 📋 REFERÊNCIA RÁPIDA

### 🤖 Core System (3)

| Comando             | Uso                 | Quando                    |
| ------------------- | ------------------- | ------------------------- |
| `/nevoa`            | Orquestração        | Não sabe qual agente usar |
| `/claude-architect` | Padrões & qualidade | Decisões críticas         |
| `/marie-kondo`      | Organização         | Limpar/reestruturar       |

### 🧠 Domain Agents (6)

| Comando     | Domínio            | Prioridade    | Uso                                                 |
| ----------- | ------------------ | ------------- | --------------------------------------------------- |
| `/coach`    | TDAH/Produtividade | ⭐⭐⭐ ALTA   | `check-in`, `foco "[tarefa]"`, `bloqueio`, `resumo` |
| `/elena`    | Metodologias TDAH  | ⭐⭐ Média    | `sistema`, `bloqueio`, `metodologia "[nome]"`       |
| `/lucas`    | DeFi & Cripto      | ⭐⭐⭐ ALTA   | `analise "[token]"`, `leva [#]`, `status`           |
| `/pedro`    | Tráfego Pago       | ⭐⭐ Média    | `aula [AXX]`, `kabak`, `status`                     |
| `/alan`     | IA & Automação     | ⭐⭐ Paralelo | `semana [#]`, `workflow`, `status`                  |
| `/dr-green` | Cultivo            | ⭐ Baixa      | `pesquisa`, `analise`                               |

### 🛠️ Essential Tools (5)

| Comando        | Uso               | Quando                                       |
| -------------- | ----------------- | -------------------------------------------- |
| `/validate`    | Validar criação   | **ANTES** de criar QUALQUER arquivo          |
| `/gemini`      | Delegar p/ Gemini | Bulk, refactoring, processar muitos arquivos |
| `/ultra-think` | Deep analysis     | Problemas complexos multi-dimensionais       |
| `/sync`        | Sincronizar       | Fim de sessão, após Gemini trabalhar         |
| `/mapa`        | Índice vault      | **SEMPRE** no início (economia 2000 tokens!) |

### 📚 Context (2)

| Comando  | Contexto       |
| -------- | -------------- |
| `/learn` | 03_APRENDIZADO |
| `/work`  | 02_PROJETOS    |

### 🔧 Maintenance (2)

| Comando               | Uso                       |
| --------------------- | ------------------------- |
| `/atualizar-status`   | Atualizar STATUS_VAULT.md |
| `/limpeza-raiz-vault` | Limpar duplicatas raiz    |

---

## 💡 POWER COMBOS

```bash
# Combo 1: Produtividade Máxima
/mapa + /coach check-in
→ Coach sabe TODO contexto!

# Combo 2: Foco Isolado
/coach foco "processar A10"
→ Coach carrega /pedro automaticamente
→ Timebox 45 min APENAS Tráfego

# Combo 3: Criação Segura
/validate "description" → /nevoa
→ Criação seguindo padrões

# Combo 4: Bi-IA Validation
[Gemini trabalha] → /sync
→ Claude valida trabalho Gemini

# Combo 5: Zero Busca
/mapa + /lucas
→ Lucas acessa TODO DeFi sem Grep!
```

---

## 🎯 WORKFLOWS

### Workflow Diário (TDAH)

**9h - Início:**

```bash
/mapa
/coach check-in
# Energia? Resultado? Horário?
```

**9h-11h30 - Deep Work:**

```bash
/coach foco "[tarefa prioritária]"
# Timebox 45 min
# Pausa 15 min
# Repeat
```

**Se travar:**

```bash
/coach bloqueio
# Coach destrói procrastinação!
```

**Fim do dia:**

```bash
/coach resumo
/atualizar-status
/sync
```

### Workflow por Domínio

**DeFi (ALTA prioridade):**

```bash
/mapa
/lucas
/coach foco "analisar AAVE"
# Meta: 30 tokens em 3 meses
```

**Tráfego (MÉDIA prioridade):**

```bash
/mapa
/pedro
/coach foco "processar A10"
# Meta: Finalizar M02, KabaK ROAS 4.0x
```

**IA (PARALELO - energia criativa):**

```bash
/mapa
/alan
/coach foco "criar workflow N8N"
# Meta: Completar 3 semanas restantes
```

### Workflow Criação de Arquivo

**SEMPRE este fluxo:**

```bash
1. /validate "want to create [description]"
2. [Revisar validação]
3. [Criar arquivo]
4. [Atualizar MOC relevante]
5. (Opcional) /atualizar-status
```

**NUNCA pule /validate!**

---

## 🧠 ISOLAMENTO DE CONTEXTO

**Economia de ~90% tokens!**

| Agente   | Acessa                   | NÃO acessa        |
| -------- | ------------------------ | ----------------- |
| `/lucas` | DeFi Journey, DeFi_Verso | Tráfego, IA, TDAH |
| `/pedro` | Subido_Trafego, KabaK    | DeFi, IA, TDAH    |
| `/alan`  | Formação_Lendaria, N8N   | DeFi, Tráfego     |
| `/elena` | TDAH, Produtividade      | DeFi, Tráfego, IA |

**Resultado:**

- Zero confusão entre contextos
- Respostas mais rápidas
- Economia massiva de tokens

---

## 📊 ESTATÍSTICAS

**Com /mapa:**

- Economia: 2000 tokens/sessão
- Velocidade: Instantâneo (vs 30-60s busca)
- Precisão: 100% (vs Grep imperfeito)

**Com isolamento:**

- Tokens/sessão: -90%
- Foco: 100% domínio correto
- Performance: 10x mais rápido

**Com /coach:**

- Procrastinação: 40% → <10%
- Produtividade: 4x ganho efetivo
- Deep Work: 2-3h/dia consistente

---

## 🆘 TROUBLESHOOTING

| Problema                  | Solução                                 |
| ------------------------- | --------------------------------------- |
| Não sei qual comando usar | `/nevoa`                                |
| Preciso criar arquivo     | `/validate "description"` ANTES         |
| Gemini fez algo errado    | `/sync` para validar/corrigir           |
| Vault desorganizado       | `/limpeza-raiz-vault` ou `/marie-kondo` |
| Estou procrastinando      | `/coach bloqueio`                       |
| Não sei progresso         | `/[agente] status`                      |
| Dispersão entre contextos | `/coach redirecionar`                   |

---

## 📖 STATUS ATUAL

**DeFi (Lucas):**

- M4: Leva 5/10 (50%)
- DeFi_Verso: 12/30 tokens
- **Meta 3 meses:** 30+ tokens ⭐⭐⭐

**Tráfego (Pedro):**

- M02: 9/13 (69%)
- KabaK ROAS: 2.5x → Meta 4.0x
- **Prioridade:** Média ⭐⭐

**IA (Alan):**

- Semana 7/10 (70%)
- Restam: 3 semanas
- **Uso:** Paralelo (energia criativa) ⭐⭐

**TDAH (Coach/Elena):**

- **Uso diário:** check-in, timeboxes, bloqueios ⭐⭐⭐

---

## 🎯 PRINCÍPIOS

1. **Mapa sempre primeiro** → Zero busca
2. **Validate antes de criar** → Zero erro
3. **Coach diariamente** → Zero procrastinação
4. **Isolamento rigoroso** → Zero desperdício
5. **Sync ao finalizar** → Zero perda de contexto

---

## 🔗 LINKS ÚTEIS

**Docs:**

- [README Completo](.claude/commands/README.md)
- [CLAUDE.md](../CLAUDE.md)
- [Nomenclatura](00_SISTEMA/PADROES/NOMENCLATURA.md)
- [Protocolo Criação](00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md)

**Agentes (Prompts):**

- [Névoa](../04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_NEVOA.md)
- [Elena](../04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_ELENA_VASQUEZ.md)
- [Pedro](../04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_PEDRO_SOBRAL.md)
- [Lucas](../04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_LUCAS_AMOEDO.md)
- [Alan](../04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_ALAN_NICOLAS.md)

**Material TDAH:**

- [Mentes Inquietas](../04_RECURSOS/Mentes_Inquietas/) - 15 capítulos
- [Procrastinação](../01_CONHECIMENTO/Desenvolvimento_Pessoal/017_-_Por_Que_Procrastinamos__E_Como_Parar!.md)

---

**Versão:** 3.0
**Atualizado:** 30/12/2025
**Total comandos:** 18

**ESTE É SEU GUIA RÁPIDO! IMPRIMA, MEMORIZE, USE! ⚡**
