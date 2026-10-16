from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm
from .forms import LoginForm, CadastroForm


def login_view(request):
    """
    View responsável por exibir e processar o formulário de login.
    - GET: mostra a página de login
    - POST: valida as credenciais e loga o usuário
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm(request)

    return render(request, 'usuario/login.html', {'form': form})


def logout_view(request):
    """Desloga o usuário e redireciona para o login."""
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')


def home(request):
    """Página inicial simples (por enquanto)."""
    return render(request, 'home.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = CadastroForm()

    return render(request, 'usuario/cadastro.html', {'form': form})