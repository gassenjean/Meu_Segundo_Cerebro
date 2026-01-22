# Workflow: Processar Reuniao

**Versao:** 2.0
**Trigger:** Usuario menciona reuniao, transcricao, meeting, call, ligacao

---

## 1. CAPTURAR

**Perguntar ao usuario:**
- Tem transcricao ou vai narrar os pontos?
- Quem participou da reuniao?
- Qual foi o objetivo principal?

**Se transcricao:**
- Ler transcricao completa
- Identificar participantes automaticamente

**Se narracao:**
- Guiar com perguntas estruturadas:
  1. Decisao principal?
  2. Action items?
  3. Prazos definidos?
  4. Proximos passos?

---

## 2. IDENTIFICAR STAKEHOLDERS

**Consultar:** `references/stakeholders.md`

**Mapear participantes:**
| Nome Mencionado | Stakeholder | Papel |
|-----------------|-------------|-------|
| Sansom | Sansom | Socio-investidor |
| Jean | Jean | CEO/Fabrica |
| Gassen | Gassen | Gestor projeto |
| Kris | Kris | Producao |
| Dr. Alexandre | Dr. Alexandre | Advogado |
| Titanium | Titanium | Marketing |
| Danilo | Danilo | Consultor marketing |

---

## 3. EXTRAIR INFORMACOES

**Decisoes:**
- O que foi decidido?
- Quem decidiu?
- Tem consenso ou divergencia?

**Action Items:**
- Quais tarefas surgiram?
- Quem e responsavel?
- Qual o prazo?

**Numeros:**
- Valores mencionados?
- Validar contra VALORES_OFICIAIS.md
- Se divergir, perguntar ao usuario

**Riscos:**
- Problemas identificados?
- Mitigacoes discutidas?

---

## 4. VALIDAR ARQUIVO

**Antes de criar, executar:**
```bash
python scripts/validate_before_create.py "RESUMO_REUNIAO_[STAKEHOLDER]_[DDMMMYYYY].md" "docs/reunioes"
```

**Regras de nome:**
- Prefixo: `RESUMO_REUNIAO_`
- Stakeholder: CamelCase (Dr_Alexandre)
- Data: DDMMMYYYY (21JAN2026)
- Local: `docs/reunioes/`

**Exemplos corretos:**
```
RESUMO_REUNIAO_DR_ALEXANDRE_21JAN2026.md
RESUMO_REUNIAO_SANSOM_14JAN2026.md
RESUMO_REUNIAO_TITANIUM_16JAN2026.md
```

---

## 5. CRIAR DOCUMENTO

**Usar template:** `assets/templates/TEMPLATE_RESUMO_REUNIAO.md`

**Frontmatter obrigatorio:**
```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: resumo_reuniao
participantes: [Lista]
status: consolidado
prioridade: [alta|media|baixa]
---
```

**Secoes obrigatorias:**
1. Decisao principal (com bullets)
2. Participantes e contexto
3. Detalhes por tema
4. Proximos passos acordados (com prazos e responsaveis)
5. Riscos identificados (se houver)
6. Checklist de continuidade

---

## 6. SALVAR

**Localizacao:** `02_PROJETOS/KabaK/docs/reunioes/`

**Nao criar em:**
- Raiz do projeto
- docs/ (sem subpasta)
- Qualquer outro lugar

---

## 7. ATUALIZAR MOC

**Executar:**
```bash
python scripts/update_moc.py "02_PROJETOS/KabaK/docs/reunioes/RESUMO_REUNIAO_XXX.md"
```

**Ou manualmente:**
1. Abrir `_MOC_KabaK.md`
2. Localizar secao `/docs/reunioes`
3. Adicionar link: `[[docs/reunioes/NOME_ARQUIVO.md]]`
4. Atualizar timestamp do MOC

---

## 8. CASCATA (SE APLICAVEL)

**Se action items novos:**
- Atualizar `tarefas/TODO_Sprint_Atual.md`
- Adicionar novas tarefas com responsavel e prazo

**Se metricas novas:**
- Atualizar `metricas/DASHBOARD.md`
- Validar numeros contra VALORES_OFICIAIS.md

**Se decisoes importantes:**
- Considerar atualizar STATUS_ATUAL.md
- Comunicar ao usuario

---

## CHECKLIST FINAL

- [ ] Stakeholders identificados
- [ ] Nome arquivo validado
- [ ] Template utilizado
- [ ] Frontmatter PT-BR
- [ ] Salvo em docs/reunioes/
- [ ] MOC atualizado
- [ ] TODO atualizado (se action items)
- [ ] Dashboard atualizado (se metricas)

---

**Versao:** 2.0
**Criado:** 22/Jan/2026
