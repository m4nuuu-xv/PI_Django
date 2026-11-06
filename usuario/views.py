
from django.shortcuts import render, redirect
from django.contrib import messages
from functools import wraps

from .forms import LoginForm


# Verifica se o aluno já informou uma matrícula válida
def matricula_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.session.get('matricula'):
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return wrapper


# Tela de login
def login_view(request):

    # Se já estiver na sessão, vai direto para a biblioteca
    if request.session.get('matricula'):
        return redirect('home')

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            matricula = form.cleaned_data['matricula']

            # Guarda a matrícula na sessão
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


# Sair da biblioteca
def logout_view(request):

    request.session.flush()

    return redirect('login')


# Página principal da biblioteca
@matricula_required
def home(request):

    matricula = request.session.get('matricula')

    return render(
        request,
        'home.html',
        {'matricula': matricula}
    )

# Página de agendamento
@matricula_required
def agendar(request):

    return render(
        request,
        'agendar.html',
        {
            'matricula': request.session.get('matricula')
        }
    )


# Página de favoritos
@matricula_required
def favoritos(request):

    return render(
        request,
        'favoritos.html',
        {
            'matricula': request.session.get('matricula')
        }
    )



# Perfil do aluno
# Perfil do aluno
@matricula_required
def perfil(request):

    return render(
        request,
        'perfil.html',
        {
            'matricula': request.session.get('matricula')
        }
    )

