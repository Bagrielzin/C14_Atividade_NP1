# Pokémon Battle API

[![CI/CD Pipeline](https://github.com/Bagrielzin/C14_Atividade_NP1/actions/workflows/blank.yml/badge.svg)](https://github.com/Bagrielzin/C14_Atividade_NP1/actions)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)](https://pytest.org/)
[![License](https://img.shields.io/github/license/Bagrielzin/C14_Atividade_NP1.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Bagrielzin/C14_Atividade_NP1)](https://github.com/Bagrielzin/C14_Atividade_NP1/commits)

## Visão Geral

Este projeto implementa um sistema de batalhas inspirado em Pokémon, utilizando Python e boas práticas de engenharia de software, com foco em:

- Arquitetura modular
- Testes unitários robustos
- Pipeline completo de CI/CD
- Automação de build, release e notificações

## Funcionalidades

- Registro de jogadores com coleção de pokémons
- Montagem de decks
- Sistema de batalha baseado em regras de fraqueza
- Leitura de dados via JSON
- Validações robustas com Pydantic
- Cobertura de testes unitários

## Estrutura do Projeto

```
├── app/
│   ├── data/              # Base de dados JSON
│   ├── schemas/           # Modelos (Pydantic)
│   ├── services/          # Regras de negócio
│   ├── utils/             # Constantes e utilidades
│   └── main.py            # Execução principal
│
├── tests/
│   ├── fixtures/          # Dados mockados
│   ├── unit/              # Testes unitários
│   └── conftest.py        # Configuração global do pytest
│
├── .github/workflows/     # Pipeline CI/CD
├── notify.py              # Script de notificação por email
├── requirements.txt
├── pytest.ini
└── README.md
```

# Testes

## Tecnologias utilizadas:
- `pytest`
- `unittest.mock`
- Fixtures reutilizáveis
- Testes isolados por camada

## Executar testes localmente

```bash
pytest -v
```

## Tipos de testes implementados

Testes de fluxo normal:
- Execução completa de batalhas
- Registro de jogadores
- Montagem de deck

Testes de exceção:
- Tipos inválidos
- Jogadores não registrados
- IDs inválidos
- Arquivo inexistente

# CI/CD Pipeline

O projeto utiliza GitHub Actions para automação completa.

## Etapas do Pipeline

### 1. Test
- Instala dependências
- Executa testes com `pytest`
- Gera relatório (`test-report.txt`)
- Salva como artifact

### 2. Build

- Gera pacote `.zip` do projeto
- Utiliza `git archive`
- Armazena como artifact

### 3. Deploy (Release)

- Cria uma release automaticamente no GitHub
- Versionamento baseado no número da execução:
```bash
v1.0.${{ github.run_number }}
```
- Anexa:
    - Pacote do projeto
    - Relatório de testes

### 4. Notify

- Envia email com status da pipeline
- Usa SMTP (Gmail)
- Suporte a múltiplos destinatários

## Notificações

O Script `notify.py` envia emails com:
- Status do pipeline (✅ ou ❌)
- Nome do relatório
- Número de execução

## Validações

- Tipagem forte com Pydantic
- Tratamento de erros com exceptions
- Garantia de integridade dos dados

## Boa Práticas Aplicadas

- Separação de responsabilidades (services, schemas, utils)
- Testes independentes
- Uso de mocks
- Pipeline automatizada
- Versionamento automático
- Código desacoplado

## Possíveis Melhorias Futuras

- Cobertura de testes com pytest-cov
- Docker + Docker Compose
- API com FastAPI
- Testes de integração

## Autores

- [Gabriel Soares](https://github.com/Bagrielzin)
- [Eduardo Pereira](https://github.com/odraude222k)
- [Maria Clara Ignácio](https://github.com/mariaclaraig)
- [Matheus Netto](https://github.com/MatheusNetto1)