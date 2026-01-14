---
description: Ativar Gemini Guardian (Processamento em Massa)
---

# Gemini Guardian - Processamento em Massa

Ativa o modo **Gemini Guardian** para catalogação e processamento de grande volume de conteúdo.

## Contexto carregado

- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_GEMINI_LIMITES_TOKENS.md` ⚠️ **CRÍTICO**
- `00_SISTEMA/PROTOCOLOS/GUIA_RECUPERACAO_ERRO_GEMINI.md`
- `04_RECURSOS/TEMPLATES/TEMPLATE_CHECKPOINT.md`
- `00_SISTEMA/planejamento/Planos/PLANO_CATALOGACAO_TOTAL_LEGADO.md`
- `SESSION_LOG.md` (comunicação com Claude)

## Protocolos obrigatórios

1. **NUNCA processar arquivo > 30KB sem dividir**
2. **MÁXIMO 10 arquivos por lote**
3. **CHECKPOINT obrigatório a cada 10 arquivos**
4. **PAUSAR antes de arquivo gigante (>50KB)**
5. **Atualizar SESSION_LOG frequentemente**

## Limites de tamanho

| Tamanho   | Ação                               |
| --------- | ---------------------------------- |
| < 10 KB   | ✅ Processar normal                |
| 10-30 KB  | ⚠️ Processar com checkpoint depois |
| 30-50 KB  | 🔴 Dividir em 2 partes             |
| 50-100 KB | 🔴 Dividir em 3-4 partes           |
| > 100 KB  | 🔴 Dividir em 5+ partes            |

## Quando usar

- Catalogação de grande volume (300+ KB)
- Processar múltiplos arquivos (15+ arquivos)
- Varredura completa de pastas
- Inventário de conhecimento histórico
- Migração em massa

## Workflow padrão

```
1. Processar LOTE de 10 arquivos (só < 30KB)
2. CHECKPOINT obrigatório
3. Atualizar SESSION_LOG
4. Se arquivo > 30KB: PAUSAR e pedir estratégia
5. NUNCA pular checkpoint
```

## Compromisso

**"Devagar e sempre, com checkpoints no caminho."** 🐢✅

Qualidade > Velocidade. Zero exceções aos limites.
