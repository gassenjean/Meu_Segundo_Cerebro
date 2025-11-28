---
criado: 2025-11-28T07:32:43-03:00
atualizado: 2025-11-24T21:26:48-03:00
---
# 📐 TEMPLATE: PRD Técnico (Product Requirements Document)

**Instruções:**
Este documento é mais técnico que o Briefing. Use quando o projeto for complexo ou quando trabalhar com equipe técnica (ou IA em modo avançado).

---

## 📊 VISÃO GERAL

### Informações do Documento
- **Projeto:** [Nome do Projeto]
- **Versão do PRD:** 1.0
- **Data:** [Data]
- **Autor:** [Seu Nome]
- **Status:** [Draft / Em Revisão / Aprovado]
- **Última Atualização:** [Data]

### Resumo Executivo
[2-3 parágrafos resumindo o projeto, seu valor e principais características]

---

## 1. PROBLEMA E OPORTUNIDADE

### 1.1 Declaração do Problema
**O problema:**
[Descrição clara do problema que estamos resolvendo]

**Afeta:**
[Quem é impactado pelo problema]

**Impacto:**
[Consequências do problema não resolvido]

**Solução proposta:**
[Como vamos resolver em alto nível]

### 1.2 Oportunidade de Mercado
- **Tamanho do mercado:**
- **Concorrentes atuais:**
- **Diferencial competitivo:**
- **Momento/timing:**

### 1.3 Objetivos de Negócio
- Objetivo 1: [Mensurável]
- Objetivo 2: [Mensurável]
- Objetivo 3: [Mensurável]

---

## 2. USUÁRIOS E PERSONAS

### 2.1 Personas Principais

#### Persona 1: [Nome]
- **Quem é:** [Descrição demográfica e profissional]
- **Objetivos:** [O que quer alcançar]
- **Dores:** [Problemas que enfrenta]
- **Comportamento:** [Como age/decide]
- **Tech-savviness:** [Nível técnico]

#### Persona 2: [Nome]
[Mesmo formato]

### 2.2 User Stories

**Como [persona], eu quero [ação], para [benefício].**

1. Como administrador, eu quero gerenciar usuários, para controlar acessos
2. Como usuário final, eu quero login rápido, para acessar sem fricção
3. [Adicionar mais conforme necessário]

---

## 3. REQUISITOS FUNCIONAIS DETALHADOS

### 3.1 Funcionalidade Principal 1: [Nome]

**Descrição:**
[Explicação detalhada do que faz]

**Comportamento Esperado:**
- Quando [condição], então [resultado]
- Quando [condição], então [resultado]

**Regras de Negócio:**
1. Regra 1
2. Regra 2
3. Regra 3

**Campos/Dados Envolvidos:**
| Campo | Tipo | Obrigatório | Validação | Default |
|-------|------|-------------|-----------|---------|
| Nome | String | Sim | Min 2 chars | - |
| Email | String | Sim | Email válido | - |
| Idade | Number | Não | 18-120 | null |

**Mensagens de Erro:**
- Erro 1: [mensagem] → Quando: [condição]
- Erro 2: [mensagem] → Quando: [condição]

**Mensagens de Sucesso:**
- Sucesso 1: [mensagem] → Quando: [condição]

**Permissões:**
- Quem pode acessar:
- Quem pode editar:
- Quem pode deletar:

**Prioridade:** [Alta / Média / Baixa]
**Complexidade:** [Baixa / Média / Alta / Muito Alta]
**Dependências:** [Lista de funcionalidades que dependem desta ou que esta depende]

---

### 3.2 Funcionalidade 2: [Nome]
[Repetir estrutura acima para cada funcionalidade principal]

---

## 4. REQUISITOS NÃO-FUNCIONAIS DETALHADOS

### 4.1 Performance

**Métricas Obrigatórias:**
- **Page Load Time:** < 2s (3G) / < 1s (4G/WiFi)
- **Time to Interactive:** < 3s
- **First Contentful Paint:** < 1s
- **API Response Time:** < 500ms (90th percentile)
- **Database Query Time:** < 100ms (média)

**Carga Esperada:**
- Usuários simultâneos: [número]
- Requests por segundo: [número]
- Crescimento ano 1: [%]
- Crescimento ano 2: [%]

**Estratégias de Otimização:**
- Caching: [onde e como]
- CDN: [sim/não, qual]
- Lazy Loading: [onde aplicar]
- Code Splitting: [estratégia]
- Database Indexing: [campos]

### 4.2 Segurança

**Autenticação:**
- Método: [JWT / Session / OAuth / etc]
- Duração de sessão:
- Refresh token:
- 2FA: [obrigatório / opcional]

**Autorização:**
- Modelo: [RBAC / ABAC / ACL]
- Níveis de acesso:
  1. Admin:
  2. Moderador:
  3. Usuário:
  4. Guest:

**Proteções Necessárias:**
- [ ] XSS (Cross-Site Scripting)
- [ ] CSRF (Cross-Site Request Forgery)
- [ ] SQL Injection
- [ ] Rate Limiting
- [ ] Input Validation
- [ ] Output Encoding
- [ ] Secure Headers

**Dados Sensíveis:**
- PII (Personally Identifiable Information): [quais]
- Criptografia em trânsito: TLS 1.3+
- Criptografia em repouso: [algoritmo]
- Logs de auditoria: [sim/não]

**Compliance:**
- [ ] LGPD (Brasil)
- [ ] GDPR (Europa)
- [ ] HIPAA (Saúde)
- [ ] PCI-DSS (Pagamentos)
- [ ] Outro:

### 4.3 Escalabilidade

**Arquitetura:**
- Tipo: [Monolito / Microserviços / Serverless]
- Horizontal scaling: [sim/não]
- Vertical scaling: [limites]

**Database:**
- Read replicas: [quantas]
- Write scaling: [estratégia]
- Sharding: [necessário?]
- Partitioning: [estratégia]

**Caching Strategy:**
- Layers: [CDN, Application, Database]
- Redis/Memcached: [qual, configuração]
- Cache invalidation: [estratégia]

### 4.4 Disponibilidade e Confiabilidade

**SLA (Service Level Agreement):**
- Uptime esperado: [99.9% / 99.95% / 99.99%]
- Downtime máximo mensal: [horas]
- Janelas de manutenção: [quando]

**Backup e Recovery:**
- Frequência de backup: [diário / semanal]
- Retention: [quanto tempo guardar]
- RPO (Recovery Point Objective): [tempo]
- RTO (Recovery Time Objective): [tempo]

**Monitoramento:**
- Métricas a monitorar:
  - CPU, RAM, Disk I/O
  - Response times
  - Error rates
  - User activity
- Ferramentas: [Grafana, Prometheus, New Relic, etc]
- Alertas: [quando notificar]

### 4.5 Usabilidade

**Acessibilidade:**
- [ ] WCAG 2.1 Level AA
- [ ] Keyboard navigation
- [ ] Screen reader compatible
- [ ] Color contrast ratios
- [ ] Alt text para imagens

**Responsividade:**
- Breakpoints:
  - Mobile: 320px - 480px
  - Tablet: 481px - 768px
  - Desktop: 769px+
- Touch targets: min 44x44px
- Orientação: portrait e landscape

**Internacionalização:**
- Idiomas suportados:
- RTL support: [sim/não]
- Timezone handling:
- Currency/number formats:

### 4.6 Manutenibilidade

**Código:**
- Style guide: [Airbnb / Google / Standard]
- Linting: [ESLint / Prettier configuração]
- Type checking: [TypeScript / Flow / JSDoc]
- Code coverage mínimo: [%]

**Documentação:**
- [ ] README completo
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Inline comments (apenas o necessário)
- [ ] Architecture Decision Records (ADRs)
- [ ] Runbook para operações

**Testing:**
- Unit tests: [meta de coverage %]
- Integration tests: [cobertura]
- E2E tests: [fluxos críticos]
- Performance tests: [quando rodar]

---

## 5. ARQUITETURA TÉCNICA

### 5.1 Diagrama de Arquitetura
```
[Inserir diagrama ou descrição textual]

Exemplo:
Cliente (Browser/Mobile)
    ↓
CDN (Cloudflare)
    ↓
Load Balancer
    ↓
API Gateway
    ↓
Application Servers (3x)
    ↓
├─ Cache (Redis)
└─ Database (PostgreSQL Primary + 2 Read Replicas)
```

### 5.2 Stack Tecnológica Completa

**Frontend:**
- Framework: [React / Vue / Angular / Next.js]
- Versão:
- State Management: [Redux / Zustand / Context]
- Routing: [React Router / Next.js routing]
- Styling: [Tailwind / Styled Components / CSS Modules]
- Build Tool: [Vite / Webpack / Parcel]
- Package Manager: [npm / yarn / pnpm]

**Backend:**
- Linguagem: [Node.js / Python / Go / Java]
- Versão:
- Framework: [Express / Fastify / Django / Flask]
- API Type: [REST / GraphQL / gRPC]
- Authentication: [Passport / JWT / OAuth2]
- ORM/Query Builder: [Prisma / TypeORM / Sequelize]

**Database:**
- Tipo: [PostgreSQL / MySQL / MongoDB]
- Versão:
- Connection Pooling:
- Migration Tool: [Prisma Migrate / Knex / Flyway]

**Caching:**
- Sistema: [Redis / Memcached]
- Uso: [Session / Query / Page]

**Message Queue (se aplicável):**
- Sistema: [RabbitMQ / Kafka / SQS]
- Uso:

**Storage:**
- Files: [S3 / GCS / Azure Blob]
- Static Assets: [CDN]

**DevOps:**
- Containerização: [Docker / Podman]
- Orquestração: [Kubernetes / Docker Swarm]
- CI/CD: [GitHub Actions / GitLab CI / Jenkins]
- IaC: [Terraform / Pulumi / CloudFormation]

**Monitoramento:**
- APM: [New Relic / DataDog / AppDynamics]
- Logs: [ELK Stack / Loki / CloudWatch]
- Errors: [Sentry / Rollbar]
- Analytics: [Google Analytics / Mixpanel / Amplitude]

**Infraestrutura:**
- Cloud Provider: [AWS / GCP / Azure / Digital Ocean]
- Hosting: [Vercel / Netlify / Heroku]
- DNS: [Cloudflare / Route53]
- SSL: [Let's Encrypt / Cloudflare]

### 5.3 Estrutura de Diretórios

```
project-root/
├─ src/
│  ├─ components/
│  ├─ pages/
│  ├─ services/
│  ├─ utils/
│  ├─ hooks/
│  ├─ context/
│  ├─ types/
│  └─ config/
├─ public/
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  └─ e2e/
├─ docs/
├─ scripts/
├─ .github/
│  └─ workflows/
└─ [arquivos de configuração]
```

### 5.4 Modelos de Dados

**Entidade 1: User**
```typescript
interface User {
  id: string; // UUID
  email: string; // unique, indexed
  password: string; // hashed (bcrypt)
  name: string;
  role: 'admin' | 'user' | 'guest';
  createdAt: Date;
  updatedAt: Date;
  lastLoginAt: Date | null;
}
```

**Entidade 2: [Nome]**
[Definir estrutura]

**Relacionamentos:**
- User 1:N Posts
- Post N:M Tags
- [etc]

### 5.5 API Endpoints

**Auth:**
```
POST /api/auth/register - Criar nova conta
POST /api/auth/login - Autenticar usuário
POST /api/auth/refresh - Refresh token
POST /api/auth/logout - Fazer logout
```

**Users:**
```
GET    /api/users - Listar usuários
GET    /api/users/:id - Buscar usuário específico
POST   /api/users - Criar usuário
PUT    /api/users/:id - Atualizar usuário
DELETE /api/users/:id - Deletar usuário
```

**[Recurso]:**
[Listar endpoints]

**Rate Limits:**
- Anônimos: 10 req/min
- Autenticados: 100 req/min
- Premium: 1000 req/min

---

## 6. FLUXOS E PROCESSOS

### 6.1 Fluxo de Autenticação
```
1. Usuário acessa /login
2. Insere credenciais
3. Frontend valida formato
4. POST /api/auth/login
5. Backend valida credenciais
6. Se válido → gera JWT token
7. Retorna token + refresh token
8. Frontend armazena em httpOnly cookie
9. Redireciona para dashboard
```

### 6.2 Fluxo de [Processo Importante]
[Descrever passo a passo]

---

## 7. INTEGRAÇÕES

### 7.1 Integração com [Serviço 1]

**Propósito:** [Por que integrar]
**Tipo:** [REST API / GraphQL / SDK / Webhook]
**Autenticação:** [API Key / OAuth / Basic Auth]
**Endpoints Usados:**
- GET /endpoint1
- POST /endpoint2

**Dados Trocados:**
- Enviamos: [formato e estrutura]
- Recebemos: [formato e estrutura]

**Frequência:** [Real-time / Batch / Scheduled]
**Fallback:** [O que fazer se falhar]
**Rate Limits:** [limites da API externa]

### 7.2 Integração com [Serviço 2]
[Repetir estrutura]

---

## 8. TESTES E QUALIDADE

### 8.1 Estratégia de Testes

**Pirâmide de Testes:**
```
        /\
       /E2E\      5%  - Fluxos críticos completos
      /______\
     /  INT  \    15% - Integração entre módulos
    /________\
   /   UNIT   \   80% - Funções e componentes isolados
  /____________\
```

**Unit Tests:**
- Framework: [Jest / Vitest / Mocha]
- Coverage mínimo: 80%
- Executar: Em cada commit (pre-commit hook)

**Integration Tests:**
- Framework: [Jest / Testing Library]
- Cobertura: Integrações críticas
- Executar: Em PRs

**E2E Tests:**
- Framework: [Playwright / Cypress / Puppeteer]
- Cobertura: Fluxos de negócio principais
- Executar: Antes de deploy

**Performance Tests:**
- Framework: [k6 / Lighthouse / WebPageTest]
- Executar: Semanalmente

### 8.2 Casos de Teste Críticos

**Teste 1: Login bem-sucedido**
- Input: Email e senha válidos
- Expected: Redirecionamento + token armazenado
- Priority: P0 (crítico)

**Teste 2: [Nome]**
[Descrever]

### 8.3 Quality Gates

**Não pode mergear se:**
- [ ] Testes unitários falham
- [ ] Coverage < 80%
- [ ] Linter tem erros
- [ ] Build falha
- [ ] Security scan encontra vulnerabilidades críticas

---

## 9. DEPLOYMENT E OPERAÇÕES

### 9.1 Ambientes

**Development:**
- URL: dev.example.com
- Database: dev-db
- Features toggles: Todas ativas

**Staging:**
- URL: staging.example.com
- Database: Cópia de produção (sanitizada)
- Similar a produção

**Production:**
- URL: example.com
- Database: prod-db
- Monitoramento ativo 24/7

### 9.2 CI/CD Pipeline

```
1. Developer → Push to branch
2. GitHub Actions trigger
3. Run linter
4. Run unit tests
5. Build application
6. Run integration tests
7. Deploy to dev (se branch main)
8. Run E2E tests
9. Deploy to staging (se aprovado)
10. Manual approval
11. Deploy to production
12. Run smoke tests
13. Notificar equipe
```

### 9.3 Rollback Strategy

**Quando fazer rollback:**
- Error rate > 5%
- Critical bug descoberto
- Performance degradation > 50%

**Como fazer rollback:**
1. Reverter deployment no Vercel/hosting
2. Notificar equipe
3. Investigar issue
4. Fix e redeploy

### 9.4 Monitoramento Pós-Deploy

**Métricas a observar (primeiras 24h):**
- Error rate
- Response time (p50, p95, p99)
- CPU/Memory usage
- Database connections
- User complaints/feedback

---

## 10. SEGURANÇA

### 10.1 Threat Model

**Ameaça 1: SQL Injection**
- Probabilidade: Média
- Impacto: Crítico
- Mitigação: ORM + prepared statements

**Ameaça 2: [Nome]**
[Listar principais ameaças]

### 10.2 Security Checklist

- [ ] Input validation em todos os endpoints
- [ ] Output encoding
- [ ] HTTPS em todos os ambientes
- [ ] Secure headers (CSP, HSTS, X-Frame-Options)
- [ ] Rate limiting
- [ ] CORS configurado corretamente
- [ ] Secrets não commitados no código
- [ ] Dependencies atualizadas
- [ ] Security scan automatizado (Snyk/Dependabot)

---

## 11. CRONOGRAMA E MILESTONES

### 11.1 Fases do Projeto

**Fase 1: MVP (Semanas 1-4)**
- [ ] Setup de infraestrutura
- [ ] Autenticação básica
- [ ] Funcionalidade core 1
- [ ] Funcionalidade core 2
- [ ] Deploy em staging

**Fase 2: Beta (Semanas 5-8)**
- [ ] Funcionalidades secundárias
- [ ] Testes com usuários beta
- [ ] Ajustes baseados em feedback
- [ ] Performance optimization

**Fase 3: Launch (Semana 9-10)**
- [ ] Security audit
- [ ] Load testing
- [ ] Deploy em produção
- [ ] Monitoramento intensivo

**Fase 4: Pós-Launch (Ongoing)**
- [ ] Bug fixes
- [ ] Feature requests
- [ ] Optimizações

### 11.2 Dependências e Riscos

**Bloqueadores:**
- Aguardando: [o quê]
- Depende de: [projeto/decisão]

**Riscos:**
- Risco 1: [descrição] → Mitigação: [plano]
- Risco 2: [descrição] → Mitigação: [plano]

---

## 12. MÉTRICAS DE SUCESSO

### 12.1 KPIs Técnicos

- **Uptime:** > 99.9%
- **Page Load:** < 2s (p95)
- **API Latency:** < 500ms (p95)
- **Error Rate:** < 0.1%
- **Test Coverage:** > 80%

### 12.2 KPIs de Negócio

- **Usuários Ativos:** [target]
- **Conversão:** [%]
- **Retenção:** [%]
- **NPS:** [score]
- **Revenue:** [valor]

---

## 13. APROVAÇÕES

**Documento Revisado Por:**
- [ ] Product Owner: __________ Data: __________
- [ ] Tech Lead: __________ Data: __________
- [ ] Security: __________ Data: __________
- [ ] DevOps: __________ Data: __________

**Aprovado para Implementação:**
- [ ] Sim, sem alterações
- [ ] Sim, com comentários (ver anexo)
- [ ] Não, precisa revisão

---

## 14. ANEXOS

### A. Glossário
- **Termo 1:** Definição
- **Termo 2:** Definição

### B. Referências
- Documento 1: [link]
- Artigo técnico: [link]
- Especificação: [link]

### C. Histórico de Mudanças

| Versão | Data | Autor | Mudanças |
|--------|------|-------|----------|
| 1.0 | 2025-01-01 | Nome | Versão inicial |
| 1.1 | 2025-01-15 | Nome | Adicionou seção X |

---

**Criado em:** 24/Nov/2025
**Baseado em:** Metodologia Profissional IA - Alan Nicolas
**Versão:** 1.0
