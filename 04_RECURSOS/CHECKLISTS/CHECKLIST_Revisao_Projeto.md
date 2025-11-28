# ✅ CHECKLIST: Revisão de Projeto com IA

**Instruções:**
Use este checklist para revisar o trabalho entregue pela IA antes de aprovar como concluído.

---

## 📋 REVISÃO GERAL

### Briefing e Requisitos

- [ ] Todos os requisitos do briefing foram atendidos
- [ ] Nenhum requisito foi esquecido
- [ ] Escopo não foi extrapolado (sem funcionalidades não pedidas)
- [ ] Prioridades foram respeitadas (must have implementados primeiro)

### Documentação

- [ ] README existe e está completo
- [ ] Instruções de setup são claras
- [ ] Dependências estão listadas
- [ ] Exemplos de uso estão presentes (se aplicável)
- [ ] Comentários no código onde necessário (não em excesso)

---

## 💻 CÓDIGO

### Qualidade

- [ ] Código está limpo e legível
- [ ] Nomes de variáveis/funções são descritivos
- [ ] Sem código duplicado desnecessariamente
- [ ] Sem código comentado (dead code)
- [ ] Sem console.logs ou debuggers esquecidos
- [ ] Padrões de projeto estão sendo seguidos
- [ ] DRY (Don't Repeat Yourself) aplicado
- [ ] SOLID principles respeitados (se aplicável)

### Estrutura

- [ ] Organização de pastas faz sentido
- [ ] Separação de responsabilidades está clara
- [ ] Componentes/módulos são reutilizáveis
- [ ] Imports estão organizados
- [ ] Arquivos não estão muito grandes (> 300 linhas é suspeito)

### Performance

- [ ] Sem loops desnecessários ou ineficientes
- [ ] Queries de banco estão otimizadas
- [ ] Não há N+1 queries
- [ ] Imagens estão otimizadas
- [ ] Lazy loading aplicado onde faz sentido
- [ ] Code splitting implementado (se necessário)
- [ ] Bundle size é razoável

### Segurança

- [ ] Input validation em todos os pontos de entrada
- [ ] Output encoding/sanitization
- [ ] SQL injection prevenido (parameterized queries)
- [ ] XSS prevenido
- [ ] CSRF protection implementado
- [ ] Secrets não estão no código
- [ ] Variáveis de ambiente usadas corretamente
- [ ] Permissões e autorizações verificadas
- [ ] Rate limiting implementado (se necessário)

---

## 🎨 FRONTEND (Se aplicável)

### UI/UX

- [ ] Design matches o briefing/mockup
- [ ] Cores estão corretas
- [ ] Tipografia está correta
- [ ] Espaçamentos consistentes
- [ ] Alinhamentos corretos
- [ ] Hierarquia visual clara
- [ ] Call-to-actions (botões) são evidentes

### Responsividade

- [ ] Mobile (320px - 480px) funciona
- [ ] Tablet (481px - 768px) funciona
- [ ] Desktop (769px+) funciona
- [ ] Breakpoints fazem sentido
- [ ] Imagens são responsivas
- [ ] Texto é legível em todos os tamanhos
- [ ] Navegação funciona em touch e mouse

### Acessibilidade

- [ ] Alt text em imagens
- [ ] Labels em form inputs
- [ ] Contraste de cores adequado (WCAG AA)
- [ ] Navegação por teclado funciona
- [ ] Focus states visíveis
- [ ] Estrutura semântica HTML
- [ ] ARIA attributes onde necessário
- [ ] Screen reader friendly

### Interatividade

- [ ] Todos os botões funcionam
- [ ] Links direcionam corretamente
- [ ] Formulários validam corretamente
- [ ] Mensagens de erro são claras
- [ ] Loading states existem
- [ ] Feedback visual ao interagir
- [ ] Animations são suaves (não causam enjoo)
- [ ] Hover/active states presentes

---

## ⚙️ BACKEND (Se aplicável)

### API

- [ ] Endpoints retornam status codes corretos
- [ ] Response bodies têm estrutura consistente
- [ ] Erros são tratados adequadamente
- [ ] Error messages são úteis (mas não expõem detalhes sensíveis)
- [ ] Paginação implementada (se necessário)
- [ ] Sorting/filtering funcionam (se necessário)
- [ ] Rate limiting configurado
- [ ] CORS configurado corretamente

### Banco de Dados

- [ ] Schema faz sentido
- [ ] Relacionamentos estão corretos
- [ ] Indexes criados em campos relevantes
- [ ] Migrations existem
- [ ] Seeds de desenvolvimento (se necessário)
- [ ] Constraints de integridade
- [ ] Sem dados sensíveis em plain text

### Autenticação/Autorização

- [ ] Login funciona
- [ ] Logout funciona
- [ ] Tokens expiram corretamente
- [ ] Refresh tokens implementados (se necessário)
- [ ] Permissões são verificadas
- [ ] Usuários não acessam dados de outros
- [ ] Password hashing usa algoritmo seguro (bcrypt, argon2)

---

## 🧪 TESTES

### Cobertura

- [ ] Testes unitários existem
- [ ] Testes de integração existem (se necessário)
- [ ] Coverage está acima do mínimo (>80% idealmente)
- [ ] Casos de sucesso testados
- [ ] Casos de erro testados
- [ ] Edge cases considerados

### Qualidade dos Testes

- [ ] Testes são independentes (não dependem de ordem)
- [ ] Testes são determinísticos (sempre mesmo resultado)
- [ ] Nomes dos testes são descritivos
- [ ] Setup/teardown corretos
- [ ] Mocks/stubs usados apropriadamente
- [ ] Não há testes desabilitados (.skip) sem justificativa

### Execução

- [ ] Todos os testes passam
- [ ] Testes rodam em tempo razoável (< 5min ideal)
- [ ] CI/CD roda os testes automaticamente
- [ ] Coverage report é gerado

---

## 🚀 DEPLOY E INFRAESTRUTURA

### Configuração

- [ ] Variáveis de ambiente estão documentadas
- [ ] .env.example existe
- [ ] Secrets não estão commitados
- [ ] Build funciona sem erros
- [ ] Deploy script funciona

### Ambientes

- [ ] Development funciona
- [ ] Staging funciona
- [ ] Production está pronto
- [ ] Configurações diferem apropriadamente entre ambientes

### CI/CD

- [ ] Pipeline está configurado
- [ ] Testes rodam no CI
- [ ] Build roda no CI
- [ ] Deploy automático funciona (ou manual está documentado)

---

## 📊 FUNCIONALIDADES ESPECÍFICAS

### Formulários

- [ ] Validação client-side funciona
- [ ] Validação server-side funciona
- [ ] Mensagens de erro são claras
- [ ] Campo required marcados
- [ ] Placeholders são úteis
- [ ] Submit funciona
- [ ] Loading state durante submit
- [ ] Success/error messages aparecem

### Autenticação

- [ ] Signup funciona
- [ ] Login funciona
- [ ] Logout funciona
- [ ] Password reset funciona (se implementado)
- [ ] Email verification funciona (se implementado)
- [ ] Sessions expiram corretamente
- [ ] Redirecionamento pós-login funciona

### CRUD Básico

- [ ] Create funciona
- [ ] Read funciona
- [ ] Update funciona
- [ ] Delete funciona
- [ ] Confirmação antes de delete
- [ ] Feedback visual após ações

### Upload de Arquivos

- [ ] Upload funciona
- [ ] Validação de tipo de arquivo
- [ ] Validação de tamanho
- [ ] Preview (se aplicável)
- [ ] Progress indicator
- [ ] Error handling

### Busca

- [ ] Busca retorna resultados relevantes
- [ ] Busca vazia não quebra
- [ ] Caracteres especiais são tratados
- [ ] Performance é aceitável
- [ ] Paginação funciona
- [ ] Filtros funcionam (se existem)

### Paginação

- [ ] Navegação entre páginas funciona
- [ ] Número correto de itens por página
- [ ] Total de páginas está correto
- [ ] URLs refletem a página atual (se aplicável)
- [ ] Não quebra em edge cases (página 0, página > max)

---

## 🔍 TESTES FUNCIONAIS

### Fluxo do Usuário Principal

**Teste o caminho feliz:**
- [ ] Usuário consegue completar tarefa principal
- [ ] Sem erros ou bugs no fluxo
- [ ] Performance é aceitável
- [ ] UX é fluida

### Casos de Erro

- [ ] Formulário com dados inválidos mostra erros
- [ ] API offline mostra mensagem apropriada
- [ ] 404 page existe
- [ ] 500 error é tratado gracefully
- [ ] Validações funcionam

### Edge Cases

- [ ] Testado com usuário sem permissões
- [ ] Testado com dados vazios
- [ ] Testado com dados muito grandes
- [ ] Testado com caracteres especiais
- [ ] Testado em diferentes navegadores
- [ ] Testado em diferentes dispositivos

---

## 🌐 CROSS-BROWSER E CROSS-DEVICE

### Navegadores

- [ ] Chrome (última versão)
- [ ] Firefox (última versão)
- [ ] Safari (última versão)
- [ ] Edge (última versão)
- [ ] Mobile browsers (Chrome Mobile, Safari Mobile)

### Dispositivos

- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] Tablet (iPad, Android)
- [ ] Desktop (Windows, Mac, Linux)

### Orientações

- [ ] Portrait funciona
- [ ] Landscape funciona
- [ ] Transição entre orientações não quebra

---

## ⚡ PERFORMANCE

### Métricas

- [ ] Page Load < 3s (mobile 3G)
- [ ] Time to Interactive < 5s
- [ ] First Contentful Paint < 1.5s
- [ ] Lighthouse score > 90 (performance)
- [ ] No layout shifts (CLS < 0.1)

### Otimizações

- [ ] Imagens otimizadas/comprimidas
- [ ] CSS/JS minificados
- [ ] Gzip/Brotli compression habilitado
- [ ] Caching headers configurados
- [ ] Lazy loading implementado
- [ ] Prefetching/preloading usado (se necessário)

---

## 🐛 BUGS E ISSUES

### Verificação

- [ ] Sem erros no console (browser)
- [ ] Sem warnings importantes
- [ ] Sem erros nos logs (backend)
- [ ] Nenhum comportamento inesperado
- [ ] Loading states não travam
- [ ] Sem memory leaks

### Testes de Stress

- [ ] Testado com muitos dados
- [ ] Testado com requests simultâneas
- [ ] Não quebra com inputs extremos
- [ ] Recupera de erros gracefully

---

## 📱 ESPECÍFICO MOBILE (Se app mobile)

### Funcionalidades

- [ ] Touch gestures funcionam
- [ ] Swipe funcionam (se aplicável)
- [ ] Zoom funciona (se permitido)
- [ ] Teclado virtual não cobre inputs
- [ ] Status bar considerada no layout

### Performance

- [ ] Scrolling é fluido
- [ ] Animações rodam a 60fps
- [ ] App size é razoável
- [ ] Offline mode funciona (se aplicável)

---

## 🔐 COMPLIANCE E LEGAL

### LGPD/GDPR (Se aplicável)

- [ ] Cookie consent (se usa cookies)
- [ ] Termos de uso acessíveis
- [ ] Política de privacidade acessível
- [ ] Usuário pode deletar dados
- [ ] Usuário pode exportar dados
- [ ] Logs de acesso a dados sensíveis

---

## 📝 DOCUMENTAÇÃO FINAL

### Para Desenvolvedores

- [ ] README completo
- [ ] Setup instructions claras
- [ ] Troubleshooting section
- [ ] Contributing guidelines (se open source)
- [ ] Changelog
- [ ] API documentation (se aplicável)

### Para Usuários

- [ ] Manual do usuário (se necessário)
- [ ] FAQ
- [ ] Tutoriais/onboarding
- [ ] Help/support contact

---

## ✨ POLISH E DETALHES

### Pequenos Detalhes que Fazem Diferença

- [ ] Favicon presente
- [ ] Meta tags (title, description, og:image)
- [ ] Loading spinners são bonitos
- [ ] Empty states bem desenhados
- [ ] Success confirmations são satisfatórias
- [ ] Error messages são amigáveis, não técnicas
- [ ] 404 page é útil e tem navegação
- [ ] Footer tem informações úteis

---

## 🎯 REVISÃO POR TIPO DE PROJETO

### Landing Page

- [ ] Hero section impactante
- [ ] CTA claro e visível
- [ ] Seções contam história coerente
- [ ] Social proof (se aplicável)
- [ ] Footer com links importantes
- [ ] Forms funcionam

### Dashboard/Admin

- [ ] Navegação intuitiva
- [ ] Filtros funcionam
- [ ] Tabelas são responsivas
- [ ] Gráficos carregam corretamente
- [ ] Export/import funciona (se aplicável)
- [ ] Bulk actions funcionam

### E-commerce

- [ ] Carrinho funciona
- [ ] Checkout completo
- [ ] Payment integration funciona
- [ ] Order confirmation
- [ ] Email notifications
- [ ] Inventory management

### Blog/CMS

- [ ] Posts são criados corretamente
- [ ] Editor funciona bem
- [ ] Preview funciona
- [ ] Publicação/draft funciona
- [ ] SEO fields presentes
- [ ] Categorias/tags funcionam

---

## 🚦 DECISÃO FINAL

### Status do Projeto

- [ ] ✅ **APROVADO** - Está pronto para produção
- [ ] ⚠️ **APROVADO COM RESSALVAS** - Pequenos ajustes necessários (listar abaixo)
- [ ] ❌ **REPROVADO** - Precisa de trabalho significativo (listar abaixo)

### Ajustes Necessários (se aplicável)

**Críticos (MUST FIX):**
1. [Item específico]
2. [Item específico]

**Importantes (SHOULD FIX):**
1. [Item específico]
2. [Item específico]

**Nice to Have (COULD FIX):**
1. [Item específico]
2. [Item específico]

---

## 📊 SCORECARD (Opcional)

Rate cada categoria de 1-5:

- [ ] **Funcionalidade:** ___ / 5
- [ ] **Código Quality:** ___ / 5
- [ ] **Performance:** ___ / 5
- [ ] **Segurança:** ___ / 5
- [ ] **UX/UI:** ___ / 5
- [ ] **Documentação:** ___ / 5
- [ ] **Testes:** ___ / 5

**Score Total:** ___ / 35

**Mínimo para aprovação:** 28/35 (80%)

---

## 💬 FEEDBACK PARA IA

**O que funcionou bem:**
- [Ponto positivo]
- [Ponto positivo]

**O que precisa melhorar:**
- [Ajuste necessário]
- [Ajuste necessário]

**Aprendizados para próximo projeto:**
- [Learning]
- [Learning]

---

## 📅 PRÓXIMOS PASSOS

Após aprovação:

- [ ] Merge para main/master
- [ ] Deploy para staging
- [ ] QA final em staging
- [ ] Deploy para produção
- [ ] Monitorar métricas primeiras 24h
- [ ] Coletar feedback inicial de usuários
- [ ] Agendar retrospectiva do projeto

---

**Revisado por:** [Seu Nome]
**Data:** [Data]
**Tempo de revisão:** [tempo]
**Aprovação:** [ ] Sim [ ] Não [ ] Com ajustes

---

**Criado em:** 24/Nov/2025
**Baseado em:** Metodologia Profissional IA - Alan Nicolas
**Versão:** 1.0
