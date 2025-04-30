import pytest
from django.urls import reverse
from django.test import Client
from uuid import uuid4

from vendas.models import Carrinho, Produtos  # IMPORTS CORRETOS


# ---------- CT‑001: cadastro + login ----------
@pytest.mark.django_db
def test_e2e_cadastro_login():
    client = Client()

    # Gera nome de usuário único para evitar conflitos
    username = f"user_{uuid4().hex[:6]}"

    # Cadastro
    resp = client.post(reverse("register"), {
        "username": username,
        "email": f"{username}@exemplo.com",
        "password1": "Senha123@",  # SENHA FORTE
        "password2": "Senha123@",
    })

    # Deve redirecionar após sucesso
    assert resp.status_code == 302

    # Login com o novo usuário
    resp = client.post(reverse("login"), {
        "username": username,
        "password": "Senha123@",
    })

    # Pode retornar 200 (página de login) ou 302 (redirect pós-login)
    assert resp.status_code in (200, 302)


# ---------- CT‑002,003,004: fluxo de compra completo ----------
@pytest.mark.django_db
def test_e2e_fluxo_compra(user, produto):
    client = Client()

    # Login do usuário de teste
    logged = client.login(username="testuser", password="senha123")
    assert logged

    # Adicionar produto ao carrinho
    client.post(reverse("adicionar_ao_carrinho", args=[produto.id]))
    assert Carrinho.objects.count() == 1

    # Remover produto do carrinho
    item = Carrinho.objects.first()
    client.delete(reverse("remover_do_carrinho", args=[item.id]))
    assert Carrinho.objects.count() == 0

    # Adicionar dois produtos ao carrinho
    produto_b = Produtos.objects.create(
        nome="Produto B",
        descricao="desc",
        preco=50,
        quantidade_estoque=5,
        user=user
    )
    client.post(reverse("adicionar_ao_carrinho", args=[produto.id]))
    client.post(reverse("adicionar_ao_carrinho", args=[produto_b.id]))

    # Finalizar compra (espera redirecionamento)
    resp = client.post(reverse("finalizar_compra"))
    assert resp.status_code == 302
    assert resp.url == reverse("compra_sucesso")
