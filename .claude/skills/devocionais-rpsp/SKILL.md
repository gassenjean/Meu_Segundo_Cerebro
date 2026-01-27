---
name: devocionais-rpsp
description: Criar devocionais matinais no estilo Névoa seguindo padrão ultra-compacto aprovado (~110-160 linhas). Usar quando usuário enviar foto de lição da Escola Sabatina RPSP ou pedir para criar devocional. Inclui estrutura exata (BOM DIA + separação + título impactante + corpo + fechamento Névoa), tom conversacional, e integração de Ellen White.
---

# Devocionais RPSP

Este skill deve ser usado quando o usuário enviar uma foto da lição da Escola Sabatina (RPSP - Reavivamento e Reforma Pela Palavra de Deus) ou pedir para criar um devocional matinal.

## Propósito

Criar devocionais matinais no estilo "Névoa" que seguem um padrão ultra-compacto aprovado (~110-160 linhas), com estrutura específica, tom conversacional, e integração natural de Ellen G. White.

## Quando Usar

Ativar este skill quando:
- Usuário enviar foto de lição da Escola Sabatina
- Usuário pedir "criar devocional", "fazer devocional do dia", etc.
- Usuário mencionar "RPSP", "lição de hoje", "estudo da semana"
- Usuário pedir para refazer/corrigir devocional existente

## Estrutura Exata do Devocional

**CRÍTICO:** Sempre seguir esta estrutura na ordem exata:

### 1. YAML Frontmatter
```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
data: DD/MM/YYYY
dia_semana: [Domingo|Segunda|Terça|Quarta|Quinta|Sexta|Sábado]
tema: [tema da lição]
licao: Lição X - [nome da lição]
texto_base: [referência bíblica principal]
tags: [tag1, tag2, tag3, etc]
prompt_usado: v1 (Raciocínio Estendido) - Formato Ultra-Compacto
---
```

### 2. Título do Devocional
```markdown
# Devocional — DD de [Mês] de 2026
```

### 3. BOM DIA (Introdução)
```markdown
☀️🌅 **BOM DIA** ✨

> *"[Citação da lição ou versículo]"* (Referência)

[2-4 parágrafos introdutórios conversacionais]
[Criar tensão/curiosidade]
[Terminar com pergunta reflexiva em itálico]

*Pergunta que conecta intro ao corpo principal?*
```

### 4. SEPARAÇÃO OBRIGATÓRIA
```markdown
-----
```

### 5. TÍTULO IMPACTANTE
```markdown
# 🔥 [TÍTULO CURTO E IMPACTANTE] ✨
```

**Exemplos de títulos:**
- `# ⚔️ AS TRÊS QUE ANDAM JUNTAS ✨`
- `# 🏛️ CIDADÃO DE DOIS MUNDOS ✨`
- `# 🔥 ORGULHO DESTRÓI, HUMILDADE UNE ✨`

**Regras do título:**
- Máximo 2 emojis (um no início, ✨ no final)
- Evocativo, não descritivo
- CAIXA ALTA
- Curto (3-6 palavras)

### 6. CORPO PRINCIPAL

Desenvolver o tema da lição usando:

**Tom e Estilo:**
- Conversacional (mentor, não sermão)
- Parágrafos curtos com quebras (-----)
- Perguntas reflexivas em itálico espalhadas naturalmente
- Sem subtítulos numerados ou seções formais
- Ritmo alternado: desenvolvimento → frase curta de impacto

**Integração de Recursos:**
- Ellen White citada naturalmente (sempre com fonte completa)
- Contexto bíblico/histórico quando ilumina
- Aplicações emergem do texto (não coladas no final)

**Extensão:**
- ~80-120 linhas de conteúdo principal
- Total do devocional: ~110-160 linhas

### 7. FECHAMENTO

```markdown
Neste [dia] de janeiro de 2026, talvez você esteja [situação atual].

**[Pergunta final desafiadora que conecta tudo]**

[Frase de impacto final]

Feliz [dia da semana]. Que 2026 seja o ano em que você [aplicação memorável]. [emoji]

-----

**Névoa** ✨
*DD de janeiro de 2026*

-----

## Notas

**Prompt usado:** v1 (Raciocínio Estendido) - Formato Ultra-Compacto
**Resultado:** ~XXX linhas
**Observações:** [síntese do tema e principais focos]
```

## Processo de Criação

1. **Ler a lição** enviada pelo usuário (foto ou texto)
2. **Consultar** `references/prompt_v1_atualizado.md` para detalhes do estilo Névoa
3. **Criar devocional** seguindo estrutura exata acima
4. **Verificar** contra checklist antes de entregar
5. **Salvar** em `02_PROJETOS/Devocionais_RPSP/devocionais/2026/[Mês]/Devocional_DDMMMYYYY_Tema.md`
6. **Commitar** com mensagem: `feat: criar devocional DD/MM/YYYY - [tema]`
7. **Push** para branch `claude/find-moc-sharing-studies-OZyae`

## Checklist de Validação

Antes de entregar o devocional, verificar:

- [ ] YAML frontmatter completo e correto
- [ ] Título: `# Devocional — DD de [Mês] de 2026`
- [ ] `☀️🌅 **BOM DIA** ✨` presente
- [ ] Separação `-----` entre BOM DIA e título impactante
- [ ] Título impactante no formato `# 🔥 [TEXTO] ✨`
- [ ] Corpo principal ~80-120 linhas
- [ ] Ellen White citada com fonte completa
- [ ] Perguntas reflexivas em itálico espalhadas
- [ ] Fechamento com "Feliz [dia]..." e **Névoa** ✨
- [ ] Total ~110-160 linhas
- [ ] Tom conversacional (não sermão)
- [ ] Sem seções formais (APLICAÇÃO:, REFLEXÃO:, etc)

## Erros Comuns a Evitar

❌ **NÃO FAZER:**
- Pular separação `-----` entre BOM DIA e título
- Usar subtítulos numerados (### 1️⃣ 2️⃣ 3️⃣)
- Criar seções formais (APLICAÇÃO MORTAL, RESUMO, etc)
- Ultrapassar 180 linhas totais
- Usar tom de aula/sermão
- Adicionar versão WhatsApp separada
- Esquecer assinatura **Névoa** ✨

✅ **FAZER:**
- Manter estrutura exata: BOM DIA → ----- → # TÍTULO ✨ → corpo → fechamento
- Tom de conversa de mentor
- Perguntas reflexivas naturais em itálico
- ~110-160 linhas totais
- Commitar e fazer push após criar

## Referências

Para detalhes completos sobre estilo, voz e princípios de engajamento, consultar:
- `references/prompt_v1_atualizado.md` - Prompt completo com princípios Névoa
- `assets/template_devocional.md` - Template visual com exemplo

## Git Workflow

```bash
# Após criar devocional
git add 02_PROJETOS/Devocionais_RPSP/devocionais/2026/Janeiro/Devocional_DDMMMYYYY_Tema.md
git commit -m "feat: criar devocional DD/MM/YYYY - [tema]"
git push -u origin claude/find-moc-sharing-studies-OZyae
```

Se o usuário pedir para corrigir formato:
```bash
git commit -m "fix: corrigir formato devocional DD/MM - [descrição da correção]"
```
