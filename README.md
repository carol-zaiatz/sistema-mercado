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


