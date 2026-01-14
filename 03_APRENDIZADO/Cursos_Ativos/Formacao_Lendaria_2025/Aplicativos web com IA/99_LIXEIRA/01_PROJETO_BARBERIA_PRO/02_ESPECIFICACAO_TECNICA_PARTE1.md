# 🔧 ESPECIFICAÇÃO TÉCNICA COMPLETA - BARBERIA PRO (Continuação)

## ⚙️ BACKEND - ARQUITETURA DETALHADA

### **API REST Endpoints Completos**

#### **Autenticação & Usuários**

```javascript
// Routes: /api/auth/*
POST   /api/auth/register          // Cadastro barbearia
POST   /api/auth/login             // Login barbeiro/admin
POST   /api/auth/logout            // Logout
POST   /api/auth/refresh           // Refresh token
POST   /api/auth/forgot-password   // Recuperar senha
POST   /api/auth/reset-password    // Resetar senha

// Routes: /api/users/*
GET    /api/users/profile          // Perfil usuário logado
PUT    /api/users/profile          // Atualizar perfil
GET    /api/users/barbeiros        // Listar barbeiros da barbearia
POST   /api/users/barbeiros        // Cadastrar novo barbeiro
PUT    /api/users/barbeiros/:id    // Atualizar dados barbeiro
DELETE /api/users/barbeiros/:id    // Desativar barbeiro
```

#### **Agendamentos Core**

```javascript
// Routes: /api/appointments/*
GET    /api/appointments                    // Listar agendamentos (filtros: data, barbeiro, status)
POST   /api/appointments                    // Criar agendamento
GET    /api/appointments/:id               // Buscar agendamento específico
PUT    /api/appointments/:id               // Atualizar agendamento
DELETE /api/appointments/:id               // Cancelar agendamento
POST   /api/appointments/:id/confirm       // Confirmar agendamento
POST   /api/appointments/:id/complete      // Marcar como concluído
POST   /api/appointments/:id/no-show       // Marcar como falta

// Routes: /api/availability/*
GET    /api/availability/:barberId/:date   // Horários disponíveis
GET    /api/availability/bulk              // Disponibilidade múltiplos dias
POST   /api/availability/block             // Bloquear horários específicos
POST   /api/availability/recurring         // Configurar bloqueios recorrentes
```

#### **Clientes & CRM**

```javascript
// Routes: /api/clients/*
GET    /api/clients                // Listar clientes (busca, filtros)
POST   /api/clients                // Cadastrar cliente
GET    /api/clients/:id           // Perfil completo cliente
PUT    /api/clients/:id           // Atualizar dados cliente
GET    /api/clients/:id/history   // Histórico agendamentos
GET    /api/clients/:id/stats     // Estatísticas cliente (frequência, gastos)
POST   /api/clients/:id/notes     // Adicionar nota ao cliente
GET    /api/clients/search        // Busca avançada clientes
```

#### **WhatsApp Integration**

```javascript
// Routes: /api/whatsapp/*
POST   /api/whatsapp/send                    // Enviar mensagem individual
POST   /api/whatsapp/send-bulk              // Enviar para múltiplos clientes
POST   /api/whatsapp/webhook                // Webhook receber mensagens
GET    /api/whatsapp/templates              // Templates aprovados
POST   /api/whatsapp/templates              // Criar novo template
GET    /api/whatsapp/conversations/:phone   // Histórico conversa
POST   /api/whatsapp/reminder/:appointmentId // Enviar lembrete específico
```

#### **IA Generativa Features**

```javascript
// Routes: /api/ai/*
POST   /api/ai/analyze-patterns              // Análise padrões agendamento
POST   /api/ai/suggest-promotions           // Sugestões campanhas
POST   /api/ai/generate-message             // Gerar mensagem personalizada
POST   /api/ai/predict-no-show              // Predição falta cliente
GET    /api/ai/insights/:period             // Insights período específico
POST   /api/ai/optimize-schedule            // Otimizar agenda automaticamente
```

#### **Sistema Indicação**

```javascript
// Routes: /api/referrals/*
GET    /api/referrals                       // Listar programa indicação
POST   /api/referrals/generate-code         // Gerar código cliente
POST   /api/referrals/validate-code         // Validar código indicação
GET    /api/referrals/:clientId/stats       // Stats indicação cliente
POST   /api/referrals/reward                // Aplicar recompensa
GET    /api/referrals/leaderboard           // Ranking indicadores
```

### **Database Schema Detalhado**

#### **Tabelas Core**

```sql
-- BARBEARIAS
CREATE TABLE barbearias (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome VARCHAR(255) NOT NULL,
    endereco TEXT NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(255),
    cnpj VARCHAR(14),
    plano_ativo VARCHAR(50) DEFAULT 'gratuito',
    configuracoes JSONB DEFAULT '{}',
    whatsapp_token TEXT,
    webhook_url TEXT,
    logo_url TEXT,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- BARBEIROS/FUNCIONÁRIOS
CREATE TABLE barbeiros (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    telefone VARCHAR(20),
    especialidades TEXT[],
    horario_trabalho JSONB DEFAULT '{}',
    comissao_percentual DECIMAL(5,2) DEFAULT 0,
    foto_perfil TEXT,
    biografia TEXT,
    ativo BOOLEAN DEFAULT true,
    role VARCHAR(50) DEFAULT 'barbeiro',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- CLIENTES
CREATE TABLE clientes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(255),
    data_nascimento DATE,
    endereco TEXT,
    preferencias JSONB DEFAULT '{}',
    total_visitas INTEGER DEFAULT 0,
    total_gasto DECIMAL(10,2) DEFAULT 0,
    ultima_visita TIMESTAMP,
    pontos_fidelidade INTEGER DEFAULT 0,
    codigo_indicacao VARCHAR(20) UNIQUE,
    observacoes TEXT,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- SERVIÇOS
CREATE TABLE servicos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    duracao_minutos INTEGER NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(100),
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- AGENDAMENTOS
CREATE TABLE agendamentos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    barbeiro_id UUID REFERENCES barbeiros(id),
    cliente_id UUID REFERENCES clientes(id),
    servico_id UUID REFERENCES servicos(id),
    data_hora_inicio TIMESTAMP NOT NULL,
    data_hora_fim TIMESTAMP NOT NULL,
    status VARCHAR(50) DEFAULT 'confirmado',
    valor DECIMAL(10,2) NOT NULL,
    desconto DECIMAL(10,2) DEFAULT 0,
    forma_pagamento VARCHAR(50),
    observacoes TEXT,
    codigo_confirmacao VARCHAR(10),
    lembrete_enviado BOOLEAN DEFAULT false,
    avaliacao INTEGER CHECK (avaliacao >= 1 AND avaliacao <= 5),
    comentario_avaliacao TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- CAMPANHAS IA
CREATE TABLE campanhas_ia (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    tipo_campanha VARCHAR(100) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    conteudo_gerado TEXT NOT NULL,
    publico_alvo JSONB DEFAULT '{}',
    metricas_performance JSONB DEFAULT '{}',
    status_ativa BOOLEAN DEFAULT true,
    data_inicio TIMESTAMP NOT NULL,
    data_fim TIMESTAMP,
    budget_estimado DECIMAL(10,2),
    roi_atual DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- INDICAÇÕES
CREATE TABLE indicacoes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    cliente_indicador_id UUID REFERENCES clientes(id),
    cliente_indicado_id UUID REFERENCES clientes(id),
    codigo_indicacao VARCHAR(20) NOT NULL,
    data_conversao TIMESTAMP,
    recompensa_aplicada BOOLEAN DEFAULT false,
    valor_recompensa DECIMAL(10,2),
    status VARCHAR(50) DEFAULT 'pendente',
    agendamento_id UUID REFERENCES agendamentos(id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- MENSAGENS WHATSAPP
CREATE TABLE mensagens_whatsapp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    cliente_id UUID REFERENCES clientes(id),
    agendamento_id UUID REFERENCES agendamentos(id),
    telefone VARCHAR(20) NOT NULL,
    tipo_mensagem VARCHAR(100) NOT NULL,
    conteudo TEXT NOT NULL,
    template_usado VARCHAR(255),
    status_entrega VARCHAR(50),
    timestamp_envio TIMESTAMP DEFAULT NOW(),
    timestamp_entrega TIMESTAMP,
    timestamp_leitura TIMESTAMP,
    resposta_cliente TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- ANALYTICS & MÉTRICAS
CREATE TABLE analytics_eventos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    tipo_evento VARCHAR(100) NOT NULL,
    dados_evento JSONB NOT NULL,
    timestamp_evento TIMESTAMP DEFAULT NOW(),
    sessao_id UUID,
    user_agent TEXT,
    ip_address INET,
    created_at TIMESTAMP DEFAULT NOW()
);

-- BLOQUEIOS AGENDA
CREATE TABLE bloqueios_agenda (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbeiro_id UUID REFERENCES barbeiros(id) ON DELETE CASCADE,
    data_inicio TIMESTAMP NOT NULL,
    data_fim TIMESTAMP NOT NULL,
    motivo VARCHAR(255),
    recorrente BOOLEAN DEFAULT false,
    configuracao_recorrencia JSONB,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- LISTA DE ESPERA
CREATE TABLE lista_espera (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    barbearia_id UUID REFERENCES barbearias(id) ON DELETE CASCADE,
    cliente_id UUID REFERENCES clientes(id),
    servico_id UUID REFERENCES servicos(id),
    barbeiro_id UUID REFERENCES barbeiros(id),
    data_desejada DATE,
    horario_inicio TIME,
    horario_fim TIME,
    status VARCHAR(50) DEFAULT 'ativo',
    notificado BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### **Índices Para Performance**

```sql
-- Índices principais para otimização
CREATE INDEX idx_agendamentos_data_barbeiro ON agendamentos(data_hora_inicio, barbeiro_id);
CREATE INDEX idx_agendamentos_barbearia_status ON agendamentos(barbearia_id, status);
CREATE INDEX idx_clientes_telefone ON clientes(telefone);
CREATE INDEX idx_clientes_barbearia ON clientes_barbearias(barbearia_id, cliente_id);
CREATE INDEX idx_campanhas_ativas ON campanhas_ia(barbearia_id, status_ativa, data_inicio);
CREATE INDEX idx_indicacoes_codigo ON indicacoes(codigo_indicacao);
CREATE INDEX idx_mensagens_whatsapp_telefone ON mensagens_whatsapp(telefone, timestamp_envio);
CREATE INDEX idx_analytics_evento_timestamp ON analytics_eventos(tipo_evento, timestamp_evento);
CREATE INDEX idx_lista_espera_ativa ON lista_espera(barbearia_id, status, data_desejada);

-- Índices compostos para queries complexas
CREATE INDEX idx_agendamentos_full_search ON agendamentos(barbearia_id, barbeiro_id, data_hora_inicio, status);
CREATE INDEX idx_clientes_engagement ON clientes(ultima_visita, total_visitas, pontos_fidelidade);
CREATE INDEX idx_campanhas_performance ON campanhas_ia(barbearia_id, tipo_campanha, roi_atual);
```

### **Microserviços Implementation**

#### **1. Authentication Service**

```javascript
// auth-service.js
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
const { supabase } = require("../config/supabase");

class AuthService {
  async register(barbeariaDados) {
    try {
      // 1. Validar dados únicos
      const { data: existingBarbearia } = await supabase
        .from("barbearias")
        .select("id")
        .eq("cnpj", barbeariaDados.cnpj)
        .single();

      if (existingBarbearia) {
        throw new Error("CNPJ já cadastrado");
      }

      // 2. Criar barbearia
      const { data: barbearia, error: barbeariError } = await supabase
        .from("barbearias")
        .insert([barbeariaDados])
        .select("*")
        .single();

      if (barbeariError) throw barbeariError;

      // 3. Criar usuário admin padrão
      const adminData = {
        barbearia_id: barbearia.id,
        nome: barbeariaDados.admin_nome,
        email: barbeariaDados.admin_email,
        telefone: barbeariaDados.admin_telefone,
        role: "admin",
        password_hash: await bcrypt.hash(barbeariaDados.admin_password, 12),
      };

      const { data: admin, error: adminError } = await supabase
        .from("barbeiros")
        .insert([adminData])
        .select("*")
        .single();

      if (adminError) throw adminError;

      // 4. Gerar tokens
      const tokens = this.generateTokens(admin);

      // 5. Criar serviços padrão
      await this.createDefaultServices(barbearia.id);

      return {
        barbearia,
        admin: { ...admin, password_hash: undefined },
        tokens,
      };
    } catch (error) {
      console.error("Erro no registro:", error);
      throw error;
    }
  }

  async login(email, password) {
    try {
      // 1. Buscar usuário
      const { data: user, error } = await supabase
        .from("barbeiros")
        .select(
          `
          *,
          barbearias (
            id, nome, plano_ativo, configuracoes
          )
        `,
        )
        .eq("email", email)
        .eq("ativo", true)
        .single();

      if (error || !user) {
        throw new Error("Usuário não encontrado");
      }

      // 2. Verificar senha
      const validPassword = await bcrypt.compare(password, user.password_hash);
      if (!validPassword) {
        throw new Error("Senha incorreta");
      }

      // 3. Atualizar último login
      await supabase
        .from("barbeiros")
        .update({ last_login: new Date() })
        .eq("id", user.id);

      // 4. Gerar tokens
      const tokens = this.generateTokens(user);

      return {
        user: { ...user, password_hash: undefined },
        tokens,
      };
    } catch (error) {
      console.error("Erro no login:", error);
      throw error;
    }
  }

  generateTokens(user) {
    const payload = {
      userId: user.id,
      barbearia_id: user.barbearia_id,
      role: user.role,
    };

    const accessToken = jwt.sign(payload, process.env.JWT_SECRET, {
      expiresIn: "15m",
    });

    const refreshToken = jwt.sign(payload, process.env.JWT_REFRESH_SECRET, {
      expiresIn: "7d",
    });

    return { accessToken, refreshToken };
  }

  async createDefaultServices(barbearia_id) {
    const defaultServices = [
      {
        barbearia_id,
        nome: "Corte + Barba",
        descricao: "Corte de cabelo + barba alinhada",
        duracao_minutos: 45,
        preco: 45.0,
        categoria: "Completo",
      },
      {
        barbearia_id,
        nome: "Só Corte",
        descricao: "Corte de cabelo masculino",
        duracao_minutos: 30,
        preco: 30.0,
        categoria: "Básico",
      },
      {
        barbearia_id,
        nome: "Só Barba",
        descricao: "Barba + bigode alinhados",
        duracao_minutos: 20,
        preco: 20.0,
        categoria: "Básico",
      },
    ];

    await supabase.from("servicos").insert(defaultServices);
  }
}

module.exports = new AuthService();
```

#### **2. Booking Service**

```javascript
// booking-service.js
const { supabase } = require("../config/supabase");
const NotificationService = require("./notification-service");
const AIService = require("./ai-service");

class BookingService {
  async createAppointment(appointmentData) {
    try {
      // 1. Validar disponibilidade
      const isAvailable = await this.checkAvailability(
        appointmentData.barbeiro_id,
        appointmentData.data_hora_inicio,
        appointmentData.data_hora_fim,
      );

      if (!isAvailable) {
        throw new Error("Horário não disponível");
      }

      // 2. Processar código de indicação se fornecido
      let indicacao_id = null;
      if (appointmentData.codigo_indicacao) {
        indicacao_id = await this.processReferralCode(
          appointmentData.codigo_indicacao,
          appointmentData.cliente_id,
        );
      }

      // 3. Criar agendamento
      const { data: appointment, error } = await supabase
        .from("agendamentos")
        .insert([
          {
            ...appointmentData,
            codigo_confirmacao: this.generateConfirmationCode(),
            indicacao_id,
          },
        ])
        .select(
          `
          *,
          barbeiros (nome, telefone),
          clientes (nome, telefone, email),
          servicos (nome, duracao_minutos, preco)
        `,
        )
        .single();

      if (error) throw error;

      // 4. Atualizar estatísticas cliente
      await this.updateClientStats(appointmentData.cliente_id);

      // 5. Notificações automáticas
      await NotificationService.sendConfirmation(appointment);

      // 6. Agendar lembretes
      await NotificationService.scheduleReminders(appointment);

      // 7. Analytics
      await this.trackEvent("appointment_created", {
        appointment_id: appointment.id,
        barbearia_id: appointment.barbearia_id,
        service_type: appointment.servicos.nome,
        value: appointment.valor,
      });

      return appointment;
    } catch (error) {
      console.error("Erro criando agendamento:", error);
      throw error;
    }
  }

  async checkAvailability(barbeiro_id, start_time, end_time) {
    try {
      // 1. Verificar conflitos com agendamentos existentes
      const { data: conflicts } = await supabase
        .from("agendamentos")
        .select("id")
        .eq("barbeiro_id", barbeiro_id)
        .neq("status", "cancelado").or(`
          and(data_hora_inicio.lte.${start_time},data_hora_fim.gt.${start_time}),
          and(data_hora_inicio.lt.${end_time},data_hora_fim.gte.${end_time}),
          and(data_hora_inicio.gte.${start_time},data_hora_fim.lte.${end_time})
        `);

      if (conflicts && conflicts.length > 0) {
        return false;
      }

      // 2. Verificar bloqueios na agenda
      const { data: blocks } = await supabase
        .from("bloqueios_agenda")
        .select("id")
        .eq("barbeiro_id", barbeiro_id)
        .eq("ativo", true)
        .lte("data_inicio", start_time)
        .gte("data_fim", end_time);

      if (blocks && blocks.length > 0) {
        return false;
      }

      // 3. Verificar horário de trabalho
      const { data: barbeiro } = await supabase
        .from("barbeiros")
        .select("horario_trabalho")
        .eq("id", barbeiro_id)
        .single();

      if (
        !this.isWithinWorkingHours(
          start_time,
          end_time,
          barbeiro.horario_trabalho,
        )
      ) {
        return false;
      }

      return true;
    } catch (error) {
      console.error("Erro verificando disponibilidade:", error);
      return false;
    }
  }

  async getAvailableSlots(barbeiro_id, date, service_duration = 30) {
    try {
      // 1. Buscar horário de trabalho
      const { data: barbeiro } = await supabase
        .from("barbeiros")
        .select("horario_trabalho")
        .eq("id", barbeiro_id)
        .single();

      // 2. Gerar slots possíveis
      const dayOfWeek = new Date(date).getDay();
      const workingHours = barbeiro.horario_trabalho[dayOfWeek];

      if (!workingHours || !workingHours.ativo) {
        return [];
      }

      const slots = this.generateTimeSlots(
        date,
        workingHours.inicio,
        workingHours.fim,
        service_duration,
      );

      // 3. Remover slots ocupados
      const { data: appointments } = await supabase
        .from("agendamentos")
        .select("data_hora_inicio, data_hora_fim")
        .eq("barbeiro_id", barbeiro_id)
        .gte("data_hora_inicio", `${date} 00:00:00`)
        .lt("data_hora_inicio", `${date} 23:59:59`)
        .neq("status", "cancelado");

      // 4. Remover bloqueios
      const { data: blocks } = await supabase
        .from("bloqueios_agenda")
        .select("data_inicio, data_fim")
        .eq("barbeiro_id", barbeiro_id)
        .eq("ativo", true)
        .gte("data_inicio", `${date} 00:00:00`)
        .lt("data_inicio", `${date} 23:59:59`);

      // 5. Filtrar slots disponíveis
      const availableSlots = slots.filter((slot) => {
        return !this.isSlotOccupied(slot, appointments, blocks);
      });

      // 6. IA: Sugerir melhores horários
      const aiSuggestions = await AIService.suggestOptimalSlots(
        barbeiro_id,
        date,
        availableSlots,
      );

      return {
        available: availableSlots,
        ai_suggestions: aiSuggestions,
      };
    } catch (error) {
      console.error("Erro buscando horários disponíveis:", error);
      throw error;
    }
  }

  generateTimeSlots(date, startTime, endTime, duration) {
    const slots = [];
    const start = new Date(`${date} ${startTime}`);
    const end = new Date(`${date} ${endTime}`);

    let current = new Date(start);
    while (current < end) {
      const slotEnd = new Date(current.getTime() + duration * 60000);
      if (slotEnd <= end) {
        slots.push({
          start: new Date(current),
          end: slotEnd,
          duration: duration,
        });
      }
      current = new Date(current.getTime() + 30 * 60000); // Incremento de 30 min
    }

    return slots;
  }

  isSlotOccupied(slot, appointments, blocks) {
    // Verificar conflito com agendamentos
    for (const apt of appointments || []) {
      const aptStart = new Date(apt.data_hora_inicio);
      const aptEnd = new Date(apt.data_hora_fim);

      if (this.timesOverlap(slot.start, slot.end, aptStart, aptEnd)) {
        return true;
      }
    }

    // Verificar conflito com bloqueios
    for (const block of blocks || []) {
      const blockStart = new Date(block.data_inicio);
      const blockEnd = new Date(block.data_fim);

      if (this.timesOverlap(slot.start, slot.end, blockStart, blockEnd)) {
        return true;
      }
    }

    return false;
  }

  timesOverlap(start1, end1, start2, end2) {
    return start1 < end2 && end1 > start2;
  }

  async processReferralCode(codigo, cliente_id) {
    try {
      // 1. Validar código
      const { data: referral } = await supabase
        .from("indicacoes")
        .select("*")
        .eq("codigo_indicacao", codigo)
        .eq("status", "ativo")
        .single();

      if (!referral) {
        throw new Error("Código de indicação inválido");
      }

      // 2. Atualizar indicação
      const { data: updated } = await supabase
        .from("indicacoes")
        .update({
          cliente_indicado_id: cliente_id,
          data_conversao: new Date(),
          status: "convertido",
        })
        .eq("id", referral.id)
        .select("*")
        .single();

      // 3. Aplicar pontos ao indicador
      await supabase
        .from("clientes")
        .update({
          pontos_fidelidade: supabase.raw("pontos_fidelidade + ?", [100]),
        })
        .eq("id", referral.cliente_indicador_id);

      // 4. Aplicar pontos ao indicado
      await supabase
        .from("clientes")
        .update({
          pontos_fidelidade: supabase.raw("pontos_fidelidade + ?", [50]),
        })
        .eq("id", cliente_id);

      return updated.id;
    } catch (error) {
      console.error("Erro processando código indicação:", error);
      // Não falhar o agendamento por erro na indicação
      return null;
    }
  }

  generateConfirmationCode() {
    return Math.random().toString(36).substring(2, 8).toUpperCase();
  }

  async updateClientStats(cliente_id) {
    await supabase
      .from("clientes")
      .update({
        total_visitas: supabase.raw("total_visitas + ?", [1]),
        ultima_visita: new Date(),
      })
      .eq("id", cliente_id);
  }

  async trackEvent(eventType, eventData) {
    await supabase.from("analytics_eventos").insert([
      {
        tipo_evento: eventType,
        dados_evento: eventData,
        timestamp_evento: new Date(),
      },
    ]);
  }
}

module.exports = new BookingService();
```

#### **3. AI Service**

```javascript
// ai-service.js
const OpenAI = require("openai");
const { supabase } = require("../config/supabase");

class AIService {
  constructor() {
    this.openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
  }

  async analyzePatterns(barbearia_id, period_days = 30) {
    try {
      // 1. Buscar dados históricos
      const endDate = new Date();
      const startDate = new Date();
      startDate.setDate(startDate.getDate() - period_days);

      const { data: appointments } = await supabase
        .from("agendamentos")
        .select(
          `
          *,
          barbeiros (nome),
          servicos (nome, categoria),
          clientes (nome, total_visitas)
        `,
        )
        .eq("barbearia_id", barbearia_id)
        .gte("data_hora_inicio", startDate.toISOString())
        .lte("data_hora_inicio", endDate.toISOString());

      // 2. Processar dados para IA
      const analysisData = this.prepareDataForAnalysis(appointments);

      // 3. Prompt para IA
      const prompt = `
        Analise os seguintes dados de agendamentos de uma barbearia e forneça insights:

        Dados dos últimos ${period_days} dias:
        ${JSON.stringify(analysisData, null, 2)}

        Forneça análise em formato JSON com:
        {
          "patterns": {
            "peak_hours": ["horários de pico"],
            "slow_periods": ["períodos lentos"],
            "popular_services": ["serviços mais procurados"],
            "client_behavior": "análise comportamento clientes"
          },
          "recommendations": {
            "promotional_slots": ["horários para promoção"],
            "service_optimization": "sugestões otimização serviços",
            "marketing_focus": "foco marketing recomendado"
          },
          "predictions": {
            "no_show_risk": "análise risco faltas",
            "revenue_forecast": "previsão receita próximos 30 dias",
            "optimal_pricing": "sugestões preços"
          }
        }
      `;

      const completion = await this.openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: prompt }],
        temperature: 0.3,
      });

      const analysis = JSON.parse(completion.choices[0].message.content);

      // 4. Salvar insights
      await supabase.from("campanhas_ia").insert([
        {
          barbearia_id,
          tipo_campanha: "pattern_analysis",
          titulo: `Análise de Padrões - ${new Date().toLocaleDateString()}`,
          conteudo_gerado: JSON.stringify(analysis),
          data_inicio: new Date(),
          status_ativa: true,
        },
      ]);

      return analysis;
    } catch (error) {
      console.error("Erro na análise de padrões:", error);
      throw error;
    }
  }

  async suggestPromotions(barbearia_id) {
    try {
      // 1. Analisar horários com baixa ocupação
      const lowOccupancySlots = await this.findLowOccupancySlots(barbearia_id);

      // 2. Analisar clientes inativos
      const inactiveClients = await this.findInactiveClients(barbearia_id);

      // 3. Gerar sugestões com IA
      const prompt = `
        Com base nos dados de baixa ocupação e clientes inativos, sugira campanhas promocionais:

        Horários com baixa ocupação:
        ${JSON.stringify(lowOccupancySlots)}

        Clientes inativos (${inactiveClients.length} clientes):
        ${JSON.stringify(inactiveClients.slice(0, 10))} // Apenas amostra

        Forneça sugestões em formato JSON:
        {
          "time_based_promotions": [
            {
              "title": "Título da promoção",
              "description": "Descrição",
              "target_slots": ["horários alvo"],
              "discount_percentage": "percentual desconto",
              "whatsapp_message": "mensagem WhatsApp personalizada"
            }
          ],
          "client_reactivation": [
            {
              "title": "Título campanha reativação",
              "target_audience": "perfil clientes alvo",
              "offer": "oferta específica",
              "whatsapp_message": "mensagem personalizada"
            }
          ]
        }
      `;

      const completion = await this.openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: prompt }],
        temperature: 0.7,
      });

      const suggestions = JSON.parse(completion.choices[0].message.content);

      return suggestions;
    } catch (error) {
      console.error("Erro gerando sugestões:", error);
      throw error;
    }
  }

  async generatePersonalizedMessage(cliente_id, message_type, context = {}) {
    try {
      // 1. Buscar dados do cliente
      const { data: client } = await supabase
        .from("clientes")
        .select(
          `
          *,
          agendamentos (
            data_hora_inicio,
            servicos (nome),
            barbeiros (nome)
          )
        `,
        )
        .eq("id", cliente_id)
        .single();

      // 2. Prompt personalizado baseado no tipo
      let prompt = "";

      switch (message_type) {
        case "confirmation":
          prompt = this.getConfirmationPrompt(client, context);
          break;
        case "reminder":
          prompt = this.getReminderPrompt(client, context);
          break;
        case "promotion":
          prompt = this.getPromotionPrompt(client, context);
          break;
        case "reactivation":
          prompt = this.getReactivationPrompt(client, context);
          break;
        default:
          throw new Error("Tipo de mensagem não suportado");
      }

      const completion = await this.openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: prompt }],
        temperature: 0.8,
        max_tokens: 200,
      });

      return completion.choices[0].message.content.trim();
    } catch (error) {
      console.error("Erro gerando mensagem:", error);
      return this.getFallbackMessage(message_type);
    }
  }

  getConfirmationPrompt(client, context) {
    return `
      Gere uma mensagem de confirmação de agendamento personalizada e calorosa para WhatsApp.
      
      Cliente: ${client.nome}
      Histórico: ${client.total_visitas} visitas
      Agendamento: ${context.service} com ${context.barber} em ${context.date} às ${context.time}
      
      A mensagem deve:
      - Ser calorosa e pessoal
      - Confirmar os detalhes
      - Incluir emoji adequado
      - Ser concisa (máx 150 caracteres)
      - Usar tom brasileiro amigável
    `;
  }

  getReminderPrompt(client, context) {
    return `
      Gere uma mensagem de lembrete personalizada para WhatsApp.
      
      Cliente: ${client.nome}
      É cliente ${client.total_visitas > 5 ? "fiel" : "novo"}
      Agendamento: em ${context.hours_until}h
      
      A mensagem deve:
      - Ser um lembrete gentil
      - Personalizada para o histórico do cliente
      - Incluir emoji
      - Dar instruções de chegada
      - Tom amigável brasileiro
    `;
  }

  getPromotionPrompt(client, context) {
    return `
      Gere uma mensagem promocional personalizada para WhatsApp.
      
      Cliente: ${client.nome}
      Última visita: ${client.ultima_visita ? new Date(client.ultima_visita).toLocaleDateString() : "Há muito tempo"}
      Serviços favoritos: ${context.favorite_services || "Corte + Barba"}
      Promoção: ${context.promotion_details}
      
      A mensagem deve:
      - Ser atrativa mas não invasiva
      - Personalizada para histórico do cliente
      - Incluir emoji
      - Call-to-action claro
      - Tom brasileiro amigável
    `;
  }

  getFallbackMessage(message_type) {
    const fallbacks = {
      confirmation:
        "✅ Agendamento confirmado! Te esperamos na data e horário marcados.",
      reminder:
        "⏰ Lembrete: Seu agendamento é hoje! Te esperamos na barbearia.",
      promotion: "🎉 Promoção especial para você! Agende já seu horário.",
      reactivation:
        "😊 Sentimos sua falta! Que tal agendar um horário conosco?",
    };

    return fallbacks[message_type] || "Obrigado por escolher nossa barbearia!";
  }

  async findLowOccupancySlots(barbearia_id) {
    // Implementar lógica para encontrar horários com baixa ocupação
    // Baseado em dados históricos dos últimos 30 dias
  }

  async findInactiveClients(barbearia_id) {
    const { data: inactiveClients } = await supabase
      .from("clientes")
      .select("*")
      .eq("barbearia_id", barbearia_id)
      .lt("ultima_visita", new Date(Date.now() - 60 * 24 * 60 * 60 * 1000)) // 60 dias
      .order("ultima_visita", { ascending: false })
      .limit(50);

    return inactiveClients || [];
  }

  prepareDataForAnalysis(appointments) {
    return {
      total_appointments: appointments.length,
      services_breakdown: this.groupBy(appointments, "servicos.nome"),
      hourly_distribution: this.getHourlyDistribution(appointments),
      daily_distribution: this.getDailyDistribution(appointments),
      no_show_rate: this.calculateNoShowRate(appointments),
      average_value: this.calculateAverageValue(appointments),
      client_frequency: this.getClientFrequency(appointments),
    };
  }

  groupBy(array, key) {
    return array.reduce((result, item) => {
      const group = this.getNestedValue(item, key);
      result[group] = (result[group] || 0) + 1;
      return result;
    }, {});
  }

  getNestedValue(obj, path) {
    return path.split(".").reduce((current, key) => current?.[key], obj);
  }

  getHourlyDistribution(appointments) {
    const hourly = {};
    appointments.forEach((apt) => {
      const hour = new Date(apt.data_hora_inicio).getHours();
      hourly[hour] = (hourly[hour] || 0) + 1;
    });
    return hourly;
  }

  getDailyDistribution(appointments) {
    const daily = {};
    appointments.forEach((apt) => {
      const day = new Date(apt.data_hora_inicio).getDay();
      const dayNames = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"];
      daily[dayNames[day]] = (daily[dayNames[day]] || 0) + 1;
    });
    return daily;
  }

  calculateNoShowRate(appointments) {
    const noShows = appointments.filter((apt) => apt.status === "falta").length;
    return appointments.length > 0
      ? ((noShows / appointments.length) * 100).toFixed(2)
      : 0;
  }

  calculateAverageValue(appointments) {
    const total = appointments.reduce(
      (sum, apt) => sum + parseFloat(apt.valor || 0),
      0,
    );
    return appointments.length > 0
      ? (total / appointments.length).toFixed(2)
      : 0;
  }

  getClientFrequency(appointments) {
    const clients = {};
    appointments.forEach((apt) => {
      const clientId = apt.cliente_id;
      clients[clientId] = (clients[clientId] || 0) + 1;
    });

    const frequencies = Object.values(clients);
    const avg = frequencies.reduce((a, b) => a + b, 0) / frequencies.length;
    return avg.toFixed(2);
  }
}

module.exports = new AIService();
```

---

**DOCUMENTO SALVO PARCIALMENTE**  
**Próxima seção**: WhatsApp Service + Notification Service + Payment Service + Analytics Service

**Status**: 50% concluído da especificação técnica completa
