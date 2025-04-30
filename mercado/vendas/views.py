from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Produtos, Clientes, Vendas, Carrinho
from .forms import ProdutoForm, CustomUserCreationForm
from .serializers import ProdutosSerializer, ClientesSerializer, VendasSerializer, CarrinhoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from PIL import Image

# --- ViewSets da API ---
class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = [IsAuthenticated]

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [IsAuthenticated]

class VendasViewSet(viewsets.ModelViewSet):
    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer
    permission_classes = [IsAuthenticated]

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

# --- Views de template ---
@login_required
def index(request):
    try:
        produtos = Produtos.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def produtos_usuario(request):
    try:
        produtos = Produtos.objects.filter(user=request.user)
        return render(request, 'produtos_usuario.html', {'produtos': produtos})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            if Produtos.objects.filter(user=request.user, nome=nome).exists():
                form.add_error('nome', 'Você já possui um produto com esse nome.')
            else:
                produto = form.save(commit=False)
                produto.user = request.user
                produto.save()
                return JsonResponse({'message': 'Produto adicionado com sucesso!'}, status=201)
        return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produtos, id=id, user=request.user)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Produto atualizado com sucesso!'})
        return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produtos, id=id, user=request.user)
    produto.delete()
    return JsonResponse({'message': 'Produto excluído com sucesso!'})

@login_required
def adicionar_ao_carrinho(request, id):
    produto = get_object_or_404(Produtos, id=id)
    carrinho_item, created = Carrinho.objects.get_or_create(cliente=request.user, produto=produto)
    if not created:
        carrinho_item.quantidade += 1
        carrinho_item.save()
    return JsonResponse({'message': 'Produto adicionado ao carrinho.'})

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(Carrinho, id=item_id, cliente=request.user)
    item.delete()
    return JsonResponse({'message': 'Produto removido do carrinho.'})

@login_required
def carrinho(request):
    itens = Carrinho.objects.filter(cliente=request.user)
    total = sum(item.total() for item in itens)
    return render(request, 'carrinho.html', {'cart_items': itens, 'total': total})

# ✅ View para fluxo da aplicação (HTML)
@login_required
def finalizar_compra(request):
    if request.method == "POST":
        itens = Carrinho.objects.filter(cliente=request.user)
        if not itens.exists():
            return render(request, 'erro.html', {'mensagem': 'Carrinho vazio.'})
        total = sum(i.total() for i in itens)
        Vendas.objects.create(cliente=request.user, total=total)
        itens.delete()
        return redirect('compra_sucesso')
    return render(request, 'erro.html', {'mensagem': 'Método não permitido.'})

# ✅ View para API REST (utilizada no teste)
@login_required
def api_finalizar_compra(request):
    if request.method == "POST":
        itens = Carrinho.objects.filter(cliente=request.user)
        if not itens.exists():
            return JsonResponse({"error": "Carrinho vazio"}, status=400)
        total = sum(i.total() for i in itens)
        Vendas.objects.create(cliente=request.user, total=total)
        itens.delete()
        return JsonResponse({"message": "Compra finalizada com sucesso"}, status=200)
    return JsonResponse({"error": "Método não permitido"}, status=405)

# --- Cadastro/Login ---
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # ✅ Retorna 302, como esperado
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next', 'index'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def compra_sucesso(request):
    return render(request, 'compra_sucesso.html')
