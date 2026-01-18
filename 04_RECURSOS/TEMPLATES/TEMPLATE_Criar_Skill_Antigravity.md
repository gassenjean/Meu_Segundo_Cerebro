# 📄 TEMPLATE: Criar Nova Skill Antigravity

Uso: Copie este arquivo para `.gemini/skills/nova-skill/skill.md`

---

## 1. Estrutura de Pastas Obrigatória

```
.gemini/skills/nome-da-skill/
├── skill.md           # Este arquivo (preenchido)
└── scripts/           # Pasta de scripts
    ├── __init__.py    # Arquivo vazio (para importar modulo)
    ├── main.py        # Script principal
    └── utils.py       # (Opcional) Funções auxiliares
```

---

## 2. Conteúdo do `skill.md` (Metadados)

```yaml
---
name: nome-da-skill-kebab-case
description: Descrição curta e objetiva do que a skill faz (max 100 caracteres)
version: 1.0
triggers:
  - "trigger principal"
  - "sinonimo 1"
  - "sinonimo 2"
author: Gemini 3 Pro
created: DD/MMM/YYYY
---

# Nome da Skill (Título Humano)

Descrição detalhada da skill. Explique o problema que ela resolve e o contexto necessário.

## Funcionalidades

- ✅ Funcionalidade 1
- ✅ Funcionalidade 2
- ✅ Funcionalidade 3

## Como Usar

**Linguagem Natural:**

- "Exemplo de frase 1"
- "Exemplo de frase 2"

## Workflow

1. **Passo 1:** O que o script faz primeiro (Scan/Input)
2. **Passo 2:** Processamento
3. **Passo 3:** Ação (Output)

## Script

Executa `scripts/main.py` que implementa a lógica.
```

---

## 3. Template Python Base (`scripts/main.py`)

```python
import os
import sys
import shutil
from datetime import datetime

# Configuração
TARGET_DIR = "C:/Users/Gassen/OneDrive/Meu_Segundo_Cerebro"  # Ajustar se necessario ou usar relative path
BACKUP_EXT = ".bak"

def log(message: str, level: str = "INFO"):
    """Função de log padronizada com emojis."""
    emojis = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌"}
    print(f"{emojis.get(level, '')} [{level}] {message}")

def create_backup(file_path: str) -> bool:
    """Cria backup antes de modificar arquivo."""
    try:
        if os.path.exists(file_path):
            backup_path = f"{file_path}{BACKUP_EXT}"
            shutil.copy2(file_path, backup_path)
            log(f"Backup criado: {backup_path}", "INFO")
            return True
        return False
    except Exception as e:
        log(f"Erro ao criar backup: {e}", "ERROR")
        return False

def main():
    """Função principal da skill."""
    log("Iniciando Skill...", "INFO")
    
    # 1. Validação
    # Verifique pré-requisitos aqui
    
    # 2. Execução (Exemplo)
    try:
        # Lógica da skill vai aqui
        pass
        
    except Exception as e:
        log(f"Falha crítica: {e}", "ERROR")
        sys.exit(1)
        
    log("Skill finalizada com sucesso.", "SUCCESS")

if __name__ == "__main__":
    main()
```

---

## 4. Checklist de Validação (Quality Assurance)

Antes de aprovar a skill:

- [ ] A estrutura de pastas está correta?
- [ ] O `skill.md` tem metadados válidos (YAML)?
- [ ] O script Python roda sem erros de sintaxe?
- [ ] Existe log claro para o usuário?
- [ ] Existe mecanismo de backup/segurança?
- [ ] O encoding está setado como `utf-8` para arquivos de texto?
- [ ] A skill foi testada em um cenário real?

---

**Fim do Template**
