# HANDOFF: Catalogar 99_ARQUIVO

**ID:** T028
**De:** Claude (Névoa)
**Para:** Gemini (Guardian/IO)
**Data:** 26/Jan/2026
**Prioridade:** Alta

---

## 1. Contexto

A pasta `99_ARQUIVO/` contém 87 arquivos legacy que nunca foram integrados ao vault atual. Alguns são tesouros históricos, outros são lixo.

**Tesouros identificados (verificar se existem):**
- PROMPT_NEVOA_3.0.md (histórico)
- ultimate-course-framework-extractor.md (metodologia)
- Biblioteca_36_Prompts.md (coleção)

---

## 2. Tarefa

**Ação:** Catalogar e classificar

**Objeto:** Todos os 87 arquivos em `99_ARQUIVO/`

**Condição:** Para cada arquivo, definir:
- Tipo (prompt/template/nota/config/outro)
- Valor (1-5, onde 5 = tesouro)
- Destino sugerido (mover para X / deletar / manter em arquivo)
- Se há duplicata em outro lugar do vault

---

## 3. Ferramenta Google Necessária

| Ferramenta | Squad | Motivo |
| ---------- | ----- | ------ |
| Antigravity (IO) | Research | Leitura e classificação massiva |

---

## 4. Inputs (O que Gemini precisa)

**Arquivos:**
- [ ] `99_ARQUIVO/` (87 arquivos)
- [ ] Referência cruzada com `04_RECURSOS/PROMPTS/`, `04_RECURSOS/TEMPLATES/`

**Contexto adicional:**
- 99_ARQUIVO = "cold storage" do vault
- Arquivos podem ter nomenclatura antiga (pré-padrões)
- Objetivo: integrar tesouros, deletar lixo

---

## 5. Output Esperado

**Formato:** Markdown

**Local de entrega:** `.bi-ia/handoffs/CATALOGO_99_ARQUIVO.md`

**Estrutura:**

```markdown
# CATÁLOGO 99_ARQUIVO

## Resumo
- Total arquivos: 87
- Por tipo: {prompts: X, templates: Y, ...}
- Tesouros (valor 5): Z
- Recomendação deletar: W

## Tesouros Identificados (Valor 4-5)
| Arquivo | Tipo | Valor | Destino Sugerido | Notas |
| ------- | ---- | ----- | ---------------- | ----- |

## Catalogação Completa
| Arquivo | Tipo | Valor | Duplicata? | Ação Sugerida |
| ------- | ---- | ----- | ---------- | ------------- |

## Recomendações
### Mover para 04_RECURSOS/PROMPTS/
- arquivo1.md
- arquivo2.md

### Mover para 04_RECURSOS/TEMPLATES/
- ...

### Deletar (sem valor)
- arquivo_x.md (motivo)
- ...

### Manter em 99_ARQUIVO (histórico)
- ...
```

---

## 6. Quality Gate

Antes de marcar como completo, verificar:

- [ ] Completo? (87 arquivos catalogados)
- [ ] Correto? (Classificação de valor faz sentido)
- [ ] Útil? (Permite Gassen decidir o que fazer)
- [ ] Limpo? (Formatação correta)

---

## 7. Comunicação

**Ao concluir:**
1. Atualizar `state.json` (status: completed)
2. Adicionar nota em SESSION_LOG.md
3. Marcar T028 como completed

---

**Status:** Pendente
**Criado por:** Névoa 6.0
