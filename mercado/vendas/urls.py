from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # --- Autenticação ---
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),

    # --- Página inicial ---
    path('', views.index, name='index'),

    # --- Produtos do usuário ---
    path('produtos/', views.produtos_usuario, name='produtos_usuario'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    # --- Carrinho de compras ---
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/finalizar/', views.finalizar_compra, name='finalizar_compra'),  # HTML view
    path('api/finalizar-compra/', views.api_finalizar_compra, name='api_finalizar_compra'),  # ✅ API JSON view

    # --- Pós-compra ---
    path('compra/sucesso/', views.compra_sucesso, name='compra_sucesso'),
]
