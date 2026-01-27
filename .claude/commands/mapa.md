---
description: Índice inteligente do vault (carregamento otimizado por categoria)
argument-hint: [opcional] sistema|conhecimento|projetos|aprendizado|recursos|completo|learn|work
---

# Mapa - Índice Inteligente do Vault (v3.0)

**Absorveu:** `/mode`

Carrega índice do vault com **carregamento inteligente por categoria**.

---

## 🎯 Novo Sistema (v2.0)

**Arquitetura otimizada:**
- ✅ Resumo (~3k tokens) - Padrão
- ✅ Índices por categoria (~4-10k tokens) - Sob demanda
- ✅ Índice completo (~41k tokens) - Raramente necessário

**Economia: 93% vs versão anterior!**

---

## 🚀 Uso

```bash
# Carregar resumo (padrão - 3k tokens)
/mapa

# Carregar categoria específica
/mapa sistema      # 00_SISTEMA (~5k tokens)
/mapa conhecimento # 01_CONHECIMENTO (~8k tokens)
/mapa projetos     # 02_PROJETOS (~6k tokens)
/mapa aprendizado  # 03_APRENDIZADO (~10k tokens)
/mapa recursos     # 04_RECURSOS (~4k tokens)

# Carregar tudo (raramente necessário - 41k tokens)
/mapa completo
```

---

## 📖 O Que Carrega

### `/mapa` (Padrão - Resumido)
**Arquivo:** `00_SISTEMA/INDICE_RESUMIDO.md` (~3k tokens)

**Inclui:**
- Overview de todas as 6 categorias
- Estatísticas do vault (2.243 arquivos)
- Quick access - localizações principais
- Guia de quando usar cada índice
- **Perfeito para:** Início de sessão, overview geral

---

### `/mapa sistema`
**Arquivo:** `00_SISTEMA/indices/INDICE_00_SISTEMA.md` (~5k tokens)

**Inclui:**
- Todos protocolos (29 docs)
- Todos MOCs (23 temas)
- Guias (4 principais)
- Checkpoints recentes
- Manuais técnicos
- **Perfeito para:** Consultar protocolos, encontrar MOCs

---

### `/mapa conhecimento`
**Arquivo:** `00_SISTEMA/indices/INDICE_01_CONHECIMENTO.md` (~8k tokens)

**Inclui:**
- Material TDAH completo (15 caps)
- Cultivo Medicinal (protocolos, sistema)
- DeFi & Finanças
- IA & Tecnologia (Alan Nicolas)
- Livros, autores, filosofia
- **Perfeito para:** Acessar material de estudo

---

### `/mapa projetos`
**Arquivo:** `00_SISTEMA/indices/INDICE_02_PROJETOS.md` (~6k tokens)

**Inclui:**
- KabaK (reuniões, docs, status)
- DeFi_Verso_2025
- Devocionais_RPSP (11 posts jan/2026)
- Gabriele Confecções
- Lio Liofilização
- **Perfeito para:** Work context, status projetos

---

### `/mapa aprendizado`
**Arquivo:** `00_SISTEMA/indices/INDICE_03_APRENDIZADO.md` (~10k tokens)

**Inclui:**
- Pedro Sobral - Tráfego (M02 9/13)
- Lucas Amoedo - DeFi (M4 5/10)
- Alan Nicolas - Formação IA (S7 7/10)
- Vida Lendária (24 episódios)
- Lives, checkpoints, lessons
- **Perfeito para:** Learning context, cursos

---

### `/mapa recursos`
**Arquivo:** `00_SISTEMA/indices/INDICE_04_RECURSOS.md` (~4k tokens)

**Inclui:**
- 9 Agentes completos (prompts)
- Templates, checklists
- Material TDAH (Mentes Inquietas)
- Prompts especializados (5C, DeFi, etc)
- **Perfeito para:** Acessar templates, agentes

---

### `/mapa completo`
**Arquivo:** `00_SISTEMA/INDICE_VAULT_COMPLETO.md` (~41k tokens)

**Inclui:** Tudo (2.243 arquivos catalogados)
**Perfeito para:** Raramente necessário (use índices específicos!)

---

## 💡 Quando Usar Qual Índice

| Se você precisa... | Use... | Tokens |
|:-------------------|:-------|:-------|
| Overview geral | `/mapa` | ~3k |
| Protocolos, MOCs | `/mapa sistema` | ~5k |
| Material TDAH, cultivo | `/mapa conhecimento` | ~8k |
| Status projetos | `/mapa projetos` | ~6k |
| Cursos ativos | `/mapa aprendizado` | ~10k |
| Templates, agentes | `/mapa recursos` | ~4k |
| Tudo (raro!) | `/mapa completo` | ~41k |

---

## 📊 Economia de Tokens

**Comparação vs v1.0:**

| Versão | Comportamento | Tokens | Economia |
|:-------|:--------------|:-------|:---------|
| v1.0 | Carrega completo sempre | ~41k | - |
| v2.0 (padrão) | Carrega resumido | ~3k | **93%** |
| v2.0 (categoria) | Carrega sob demanda | ~4-10k | 75-90% |

**Resultado:**
- Início de sessão: 41k → 3k tokens (**93% economia**)
- Janela disponível: 159k → 197k tokens (**+38k disponíveis**)

---

## 🔗 Integração com Skills

**Combinação poderosa:**

```bash
# Overview + Coach TDAH
/mapa
/coach

# Projetos + Work context
/mapa projetos
/work

# Cursos + Learning context
/mapa aprendizado
/learn

# Recursos + Agente específico
/mapa recursos
/pedro  # ou /lucas, /alan, etc
```

---

## 🎯 Quick Reference - Localizações

**TDAH:**
- `04_RECURSOS/Mentes_Inquietas/` (15 capítulos)
- `01_CONHECIMENTO/Desenvolvimento_Pessoal/017_Por_Que_Procrastinamos.md`

**Tráfego:**
- `03_APRENDIZADO/Cursos_Ativos/Subido_Trafego/`

**DeFi:**
- `03_APRENDIZADO/Cursos_Ativos/DeFi_Journey/`
- `02_PROJETOS/DeFi_Verso_2025/`

**IA/Automação:**
- `03_APRENDIZADO/Cursos_Ativos/Formacao_Lendaria_2025/`

**Projetos:**
- `02_PROJETOS/[KabaK|DeFi_Verso|Devocionais_RPSP]/`

**Agentes:**
- `04_RECURSOS/PROMPTS/Agentes_Sistema/`

---

## ⚡ Ação Imediata

**Primeiro uso?** Execute `/mapa` para carregar resumo!

**Resultado:**
- ✅ Overview completo do vault
- ✅ 93% economia de tokens vs v1.0
- ✅ Carregamento inteligente sob demanda
- ✅ Base perfeita para outras skills

---

## FUNCIONALIDADES ABSORVIDAS

### De /mode

Agora `/mapa` também ativa contextos:

```bash
/mapa learn    # Modo aprendizado (cursos)
/mapa work     # Modo projetos (trabalho)
```

**Modo Learn:** Carrega índice de aprendizado + contexto de estudo
**Modo Work:** Carrega índice de projetos + contexto de trabalho

---

**Versão:** 3.0 (Consolidado)
**Atualizado:** 26/Jan/2026
**Status:** ✅ Production Ready
**Economia:** 93% vs v1.0
