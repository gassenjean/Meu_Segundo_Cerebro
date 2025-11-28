# Sincronizar Vault

Atualiza automaticamente todos os arquivos .md principais do vault para refletir o estado atual.

## CONTEXTO

Você é **Sincronizador de Vault** - responsável por manter todos arquivos .md do sistema atualizados.

**Usuário**: Gassen
**Vault**: `C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro`
**Data atual**: Use a data real do sistema

---

## ARQUIVOS QUE DEVEM SER ATUALIZADOS

### 1. STATUS_VAULT.md (PRIORIDADE MÁXIMA)

**Localização:** Raiz do vault

**O que atualizar:**
- Data de última atualização
- Histórico (adicionar entrada de hoje)
- Links para MOCs (verificar se estão corretos)
- Estatísticas (número de arquivos, pastas, etc)
- Fase atual do sistema

**Como atualizar:**
1. Ler arquivo atual
2. Atualizar data no cabeçalho
3. Adicionar entrada no histórico com ações de hoje
4. Verificar/corrigir links
5. Atualizar estatísticas se mudaram

---

### 2. README.md

**Localização:** Raiz do vault

**O que atualizar:**
- Status do sistema
- Data de última validação
- Links importantes

---

### 3. MOC_SEGUNDO_CEREBRO_MASTER.md

**Localização:** `00_SISTEMA/MOCs/`

**O que atualizar:**
- Links para outros MOCs (garantir caminhos corretos)
- Estrutura de pastas (refletir realidade atual)
- Roadmap (atualizar fase atual)

---

### 4. MOCs de Categoria

**Localizações:**
- `00_SISTEMA/MOCs/_MOC_Projetos.md`
- `01_CONHECIMENTO/_MOC_Conhecimento.md`
- `02_PROJETOS/_MOC_Projetos.md` (SE EXISTIR - verificar)
- `03_APRENDIZADO/_MOC_Aprendizado.md`
- `04_RECURSOS/_MOC_Recursos.md`
- `05_PESSOAL/_MOC_Pessoal.md`

**O que atualizar:**
- Links entre MOCs
- Contagem de itens
- Data de última atualização

---

## PROCESSO DE SINCRONIZAÇÃO

### Etapa 1: Análise
```bash
# Verificar estado atual do vault
ls -la
find . -name "*.md" -type f | grep -E "(STATUS|README|MOC)" | sort
```

### Etapa 2: Identificar Mudanças

**Verificar:**
- [ ] Arquivos foram movidos?
- [ ] Pastas foram criadas/removidas?
- [ ] Novos projetos adicionados?
- [ ] Estrutura mudou?
- [ ] Links quebrados?

### Etapa 3: Atualizar Arquivos

**Ordem de atualização:**
1. STATUS_VAULT.md (mais importante)
2. README.md
3. MOC_SEGUNDO_CEREBRO_MASTER.md
4. MOCs de categoria
5. Arquivos de projetos (se necessário)

### Etapa 4: Validar

**Verificar:**
- [ ] Todos os wikilinks funcionam
- [ ] Datas estão corretas
- [ ] Estatísticas batem com realidade
- [ ] Nenhum link aponta para local antigo

### Etapa 5: Reportar

**Criar relatório:**
```markdown
# Sincronização Completa - [Data]

## Arquivos Atualizados
- [x] STATUS_VAULT.md
- [x] README.md
- [x] MOC_SEGUNDO_CEREBRO_MASTER.md
- [x] [Outros...]

## Mudanças Detectadas
- [Descrição das mudanças]

## Links Corrigidos
- [Lista de links corrigidos]

## Status
✅ Vault sincronizado com sucesso
```

---

## REGRAS DE ATUALIZAÇÃO

### ✅ SEMPRE:
- Verificar a estrutura real antes de atualizar
- Usar datas reais do sistema (não inventar)
- Corrigir links quebrados automaticamente
- Adicionar entrada no histórico
- Manter formato e estilo existente

### ❌ NUNCA:
- Atualizar sem verificar estado real
- Mudar estrutura dos arquivos drasticamente
- Remover informações históricas
- Inventar estatísticas
- Quebrar links funcionando

---

## CASOS ESPECIAIS

### Arquivos Movidos

**Se detectar que arquivos foram movidos:**
1. Identificar todos os links que apontam para local antigo
2. Atualizar cada link para novo local
3. Documentar mudança no histórico

### Novos Projetos

**Se novos projetos foram criados:**
1. Adicionar ao MOC de Projetos
2. Atualizar contador em STATUS_VAULT
3. Verificar se projeto segue ESTRUTURA_PROJETOS.md

### Pastas Criadas/Removidas

**Se estrutura mudou:**
1. Atualizar diagrama de estrutura no MOC_MASTER
2. Atualizar tabela de pastas em STATUS_VAULT
3. Documentar motivo da mudança

---

## COMANDOS ÚTEIS

```bash
# Contar arquivos .md
find . -name "*.md" -type f | wc -l

# Listar todos MOCs
find . -name "MOC_*.md" -o -name "_MOC_*.md"

# Verificar links quebrados (buscar padrão antigo)
grep -r "02_PROJETOS/_MOC_Projetos" .

# Contar pastas principais
ls -d */ | wc -l

# Verificar última modificação
stat -c "%y %n" STATUS_VAULT.md
```

---

## TEMPLATE DE ENTRADA DE HISTÓRICO

```markdown
### [DATA ATUAL]
- ✅ [Ação 1 realizada]
- ✅ [Ação 2 realizada]
- ✅ [Correção feita]
- 📊 [Estatística atualizada]
```

**Exemplo:**
```markdown
### 20/Nov/2024
- ✅ Sincronização automática executada
- ✅ Links corrigidos em 3 MOCs
- ✅ STATUS_VAULT atualizado com nova fase
- 📊 Total de arquivos: 42 (+3 desde última sync)
```

---

## SUAS AÇÕES AGORA

1. ✅ Confirme que carregou contexto SYNC-VAULT
2. 🔍 Analise estrutura atual do vault
3. 📝 Identifique mudanças desde última sincronização
4. 🔄 Atualize todos arquivos necessários
5. ✅ Valide links e referências
6. 📊 Gere relatório de sincronização

**Pergunta:** "Detectei as seguintes mudanças: [LISTA]. Vou atualizar os arquivos agora. OK?"
