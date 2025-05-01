# Sistema Mercado

Projeto web desenvolvido com Django que simula um sistema de gestão de produtos e vendas, incluindo funcionalidades como:

- Cadastro de usuários
- Login/logout
- Adição, edição e remoção de produtos
- Carrinho de compras
- Finalização de compras
- Testes automatizados com Pytest e Cypress

---

## Tecnologias

- Python 3.10+
- Django 5.2
- SQLite (ou PostgreSQL, configurável)
- Pytest
- Cypress
- HTML/CSS (Bootstrap)
- JavaScript (para interações simples)

---

## Pré-requisitos

- [Python](https://www.python.org/downloads/)
- [Node.js e npm](https://nodejs.org/) (para Cypress)
- [Git](https://git-scm.com/)

---

## Instalação e uso

### Clone o repositório

    git clone https://github.com/carol-zaiatz/sistema-mercado.git
    cd sistema-mercado


## Crie e ative um ambiente virtual

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows

## Instale as dependências do backend
    pip install -r requirements.txt

##  Execute as migrações e o servidor
    python manage.py migrate
    python manage.py runserver

---

##  Testes de backend (unitários, API, E2E funcional):
    npm install         # instala Cypress
    npx cypress open    # abre a interface interativa

# Evidências dos Testes — Sistema Mercado

Este documento apresenta as evidências de execução dos testes realizados no projeto `sistema-mercado`, incluindo testes unitários, de API e E2E.

---

## Ferramentas Utilizadas

| Tipo de Teste   | Ferramenta       |
|------------------|------------------|
| Testes Unitários | Pytest           |
| Testes de API    | Pytest (DRF)     |
| Testes E2E       | Cypress           |

---

## Ambiente de Execução

- macOS (MacBook de desenvolvimento)
- Python 3.13
- Django 5.2
- Cypress 13+
- Node.js 20+
- npm 10+

---

## Execução dos Testes

###  Pytest

- Todos os testes unitários e de API foram executados com o comando:

```bash
pytest > pytest_log.txt
```
## Cypress (E2E)
npx cypress open
# ou
npm run test:e2e

Teste principal: cadastro_login_compra.cy.js

Fluxo testado:

    Cadastro de novo usuário

    Login automático

    Acesso à tela inicial

    Adição de produto ao carrinho

    Finalização de compra

V    erificação de sucesso

Evidências:

    Prints de execução: cypress/screenshots/ (em caso de falha)

    Resultado final visível na interface Cypress

