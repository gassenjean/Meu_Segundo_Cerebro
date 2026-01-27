---
created: 2026-01-24T22:25
updated: 2026-01-26T14:12
---
# PLANO: Organização Total do Segundo Cérebro 2026 (A Grande Triagem)

**Status:** PLANEJAMENTO
**Data:** 24/JAN/2026
**Responsável:** Névoa (Orquestração) + Guardian (Execução)

---

## 1. Objetivo

Executar a organização "pasta a pasta, arquivo a arquivo" solicitada, migrando o legado e estabelecendo a ordem absoluta no novo vault, utilizando a hierarquia de agentes (Névoa > Gerentes > Guardian).

## 2. Estrutura de Comando (Hierarquia em Ação)

- **Névoa (Eu):** Decido O QUE vai para onde.
- **Gerentes (Especialistas):** Ajudam a classificar.
  - `Gerente Conhecimento`: Classifica notas de estudo e referências.
  - `Gerente Projetos`: Classifica documentos de projetos (KabaK, etc).
  - `Gerente Finanças`: Identifica planilhas e comprovantes.
- **Guardian (O Zelador):** EXECUTA as movimentações (mv, rename) seguindo a lei (`NOMENCLATURA.md`).

## 3. Fases da Execução

### FASE 1: Preparação e Segurança (Ground Zero)

- [ ] **Snapshot do Vault:** Backup do estado atual.
- [ ] **Definir "Zonas Seguras":** Pastas que NÃO devem ser tocadas sem permissão expressa (ex: `00_SISTEMA`).
- [ ] **Mapear a Fonte (Legado):** Listar conteúdo de `Segunda_Mente_Legendaria_Sync` (ou pasta indicada).

### FASE 2: A Grande Triagem (Batch Processing)

Faremos isso pasta por pasta, em ciclos:

#### Ciclo 1: Inbox Zero (Limpeza Imediata)

- Processar tudo que está na raiz e em `_inbox`.
- Destinos: `02_PROJETOS`, `01_CONHECIMENTO`, `99_ARQUIVO`, ou Lixo.

#### Ciclo 2: Migração de Projetos (Gerente Projetos)

- Identificar pastas de projetos no legado.
- Migrar para `02_PROJETOS` aplicando estrutura padrão (7 pastas).
- **Foco:** KabaK, DeFi, Lançamentos.

#### Ciclo 3: Consolidação de Conhecimento (Gerente Conhecimento)

- Identificar cursos, notas e referências.
- Migrar para `01_CONHECIMENTO` ou `03_APRENDIZADO`.
- Aplicar tags e links nos MOCs.

#### Ciclo 4: Arquivamento

- Tudo que é antigo (> 2 anos) e inativo vai para `99_ARQUIVO` (Cold Storage).

### FASE 3: Refinamento Técnico (Guardian)

- [ ] **Auditoria de Nomenclatura:** Renomear arquivos fora do padrão.
- [ ] **Correção de Links:** Verificar links quebrados após migração.
- [ ] **Sanitização:** Remover caracteres especiais, espaços, arquivos temporários.

## 4. Protocolo de Execução (Loop Ralph)

Para cada lote de arquivos:

1. **Névoa:** Lista arquivos e sugere destino.
2. **Usuário:** Aprova/Ajusta plano.
3. **Guardian:** Executa (`/guardian fix` ou `/guardian auto`).
4. **Ralph:** Verifica se arquivos chegaram íntegros.

---

## 5. Próximos Passos Imediatos

1. Aprovar este plano.
2. Confirmar local da pasta "Antiga" (`Segunda_Mente_Legendaria_Sync`?).
3. Iniciar Ciclo 1 (Inbox Zero).
