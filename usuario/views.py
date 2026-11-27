
from django.shortcuts import render, redirect
from django.contrib import messages
from functools import wraps

from .forms import LoginForm


# ==========================================
# VERIFICAR SE O ALUNO ESTÁ LOGADO
# ==========================================

def matricula_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.session.get('matricula'):
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return wrapper


# ==========================================
# LOGIN
# ==========================================

def login_view(request):

    if request.session.get('matricula'):
        return redirect('home')

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            matricula = form.cleaned_data['matricula']

            request.session['matricula'] = matricula

            messages.success(
                request,
                'Acesso realizado com sucesso!'
            )

            return redirect('home')

        else:

            messages.error(
                request,
                'Confira a matrícula e preencha os campos corretamente.'
            )

    else:

        form = LoginForm()

    return render(
        request,
        'usuario/login.html',
        {'form': form}
    )


# ==========================================
# LOGOUT
# ==========================================

def logout_view(request):

    request.session.flush()

    return redirect('login')


# ==========================================
# HOME
# ==========================================

@matricula_required
def home(request):

    matricula = request.session.get('matricula')

    return render(
        request,
        'home.html',
        {'matricula': matricula}
    )


# ==========================================
# AGENDAMENTO
# ==========================================

@matricula_required
def agendar(request):

    matricula = request.session.get('matricula')

    return render(
        request,
        'agendar.html',
        {'matricula': matricula}
    )


# ==========================================
# FAVORITOS
# ==========================================

@matricula_required
def favoritos(request):

    matricula = request.session.get('matricula')

    return render(
        request,
        'favoritos.html',
        {'matricula': matricula}
    )


# ==========================================
# PERFIL
# ==========================================

@matricula_required
def perfil(request):

    matricula = request.session.get('matricula')

    dados = {
        'matricula': matricula,
    }

    return render(
        request,
        'perfil.html',
        dados
    )


# ==========================================
# DETALHES DO LIVRO
# ==========================================

@matricula_required
def livro_detalhes(request):

    matricula = request.session.get('matricula')

    return render(
        request,
        'livro_detalhes.html',
        {'matricula': matricula}
    )
