# Workflow: Criar Briefing

**Versao:** 2.0
**Trigger:** Usuario precisa briefing, documento para stakeholder, proposta

---

## 1. IDENTIFICAR DESTINATARIO

**Perguntar:**
- Para quem e o briefing?
- Qual o objetivo/proposito?
- Qual o prazo de entrega?

**Stakeholders comuns:**
| Stakeholder | Foco do Briefing |
|-------------|------------------|
| Dr. Alexandre | Juridico, contratos, governanca |
| Sansom | Financeiro, operacional, estrategia |
| Titanium | Marketing, lancamento, branding |
| Fornecedores | Produto, volumes, prazos |

---

## 2. CARREGAR CONTEXTO

**Consultar referencias:**

| Referencia | Quando Carregar |
|------------|-----------------|
| `estrutura_societaria.md` | Sempre |
| `produto_tecnico.md` | Produto, custos, producao |
| `metricas_kpis.md` | Numeros, projecoes |
| `stakeholders.md` | Perfis detalhados |

**Fonte unica de numeros:** `VALORES_OFICIAIS.md`

**Valores oficiais:**
- Investimento total: R$ 2.096.300
- Sansom: 51% decisao, 50% lucro
- Jean/Gassen/Kris: 49% decisao, 50% lucro
- Kit: R$ 129 (custo ~R$ 48)

---

## 3. CUSTOMIZAR POR AUDIENCIA

### Para Advogado (Dr. Alexandre)
**Foco:**
- Estrutura societaria
- Governanca e decisoes
- Contratos necessarios
- Riscos juridicos
- Protecao de patrimonio

**Secoes obrigatorias:**
- Perfil dos socios
- Questoes juridicas (com opcoes)
- Documentos necessarios
- Perguntas para responder

### Para Investidor (Sansom)
**Foco:**
- ROI e retorno
- Timeline de investimento
- Riscos e mitigacoes
- Responsabilidades claras

**Secoes obrigatorias:**
- Sumario executivo
- Numeros detalhados
- Cronograma
- Proximos passos

### Para Marketing (Titanium)
**Foco:**
- Produto e posicionamento
- Publico-alvo
- Orcamento disponivel
- KPIs esperados

**Secoes obrigatorias:**
- Briefing de produto
- Estrategia de lancamento
- Metricas de sucesso
- Budget e timeline

### Para Fornecedor
**Foco:**
- Especificacoes tecnicas
- Volumes e prazos
- Qualidade esperada
- Condicoes comerciais

---

## 4. VALIDAR ARQUIVO

**Antes de criar, executar:**
```bash
python scripts/validate_before_create.py "BRIEFING_[STAKEHOLDER]_[DDMMMYYYY].md" "docs"
```

**Regras de nome:**
- Prefixo: `BRIEFING_`
- Stakeholder: CamelCase (Dr_Alexandre)
- Data: DDMMMYYYY (opcional, usar se versao datada)
- Local: `docs/`

**Exemplos corretos:**
```
BRIEFING_DR_ALEXANDRE_19JAN2026.md
BRIEFING_SANSOM_PROPOSTA_PARCERIA.md
BRIEFING_TITANIUM_LANCAMENTO.md
```

---

## 5. CRIAR DOCUMENTO

**Usar template:** `assets/templates/TEMPLATE_BRIEFING.md`

**Frontmatter obrigatorio:**
```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: briefing
destinatario: [Nome]
prioridade: [critica|alta|media|baixa]
confidencial: sim
---
```

**Secoes minimas:**
1. Sumario executivo
2. Contexto do negocio
3. Perfil dos stakeholders
4. Questoes especificas (customizar por audiencia)
5. Prazos e entregas
6. Proximos passos
7. Perguntas para o stakeholder
8. Anexos

**Tamanho esperado:** 500-1000+ linhas (briefings sao detalhados)

---

## 6. SALVAR

**Localizacao:** `02_PROJETOS/KabaK/docs/`

**Versoes:**
- Se existir versao anterior: manter como historico
- Nova versao: adicionar data no nome
- Exemplo: `BRIEFING_DR_ALEXANDRE_19JAN2026.md` (v1)
-          `BRIEFING_DR_ALEXANDRE_26JAN2026.md` (v2)

---

## 7. ATUALIZAR MOC

**Adicionar em secao `/docs`:**
```markdown
| [[docs/BRIEFING_XXX.md]] | Briefing [stakeholder] | [status] |
```

---

## 8. CHECKLIST ENVIO

**Criar/atualizar:** `CHECKLIST_ENVIO_[STAKEHOLDER].md`

**Incluir:**
- [ ] Briefing anexado
- [ ] Documentos de apoio
- [ ] Mensagem de envio
- [ ] Confirmar recebimento

---

## CHECKLIST FINAL

- [ ] Destinatario identificado
- [ ] Referencias carregadas
- [ ] Conteudo customizado por audiencia
- [ ] Nome arquivo validado
- [ ] Template utilizado
- [ ] Frontmatter PT-BR
- [ ] Salvo em docs/
- [ ] MOC atualizado
- [ ] Checklist envio criado

---

**Versao:** 2.0
**Criado:** 22/Jan/2026
