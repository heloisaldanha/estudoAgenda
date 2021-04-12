from django.shortcuts import render, redirect
from django.contrib import messages, auth  # auth é pra verificar se a solicitação de usuário e senha está ok para login
from django.core.validators import validate_email  # para validar o email do formulário
from django.contrib.auth.models import User  # para garantir que nenhum email ou usuário sejam iguais
from django.contrib.auth.decorators import login_required  # a página só abre se tiver feito login
from .models import FormContato


def login(request):
    if request.method != 'POST':  # se não postarem nada, retorna apenas a página de login normal
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    # verificar a autenticação de usuário e senha.
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha incorreta')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login feito com sucesso!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    # messages.success(request, 'Requisição feita com sucesso!')
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    # pegar os valores do formulário
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha deve conter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'O usuário deve conter 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem. As duas senhas precisam ser iguais')
        return render(request, 'accounts/cadastro.html')

    # para verificar se já existe um usuário com esse mesmo nome:
    if User.objects.filter(username=usuario).exists():
        # username é a chave e usuario é a variável criada ali em cima
        messages.error(request, 'Usuário já existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        # email é a chave.
        messages.error(request, 'Email já cadastrado')
        return render(request, 'accounts/cadastro.html')

    # criando o objeto usuário (pegando todos os dados de validação do usuário)
    user = User.objects.create_user(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha)
    # salvando no sistema
    user.save()

    messages.success(request, 'Cadastro feito com sucesso!')
    return redirect('login')


@login_required(redirect_field_name='login')  # (1) - README - accounts/README.md
def dashboard(request):
    if request.method != 'POST':  # se nada for postado, retorna a página de dashboard normalmente
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)  # Esse files é porque tem imagem no campo

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário')
        form = FormContato(request.POST)  # para não apagar o que foi escrito na página
        return render(request, 'accounts/dashboard.html', {'form': form})

    '''
    supondo que eu queira mexer em alguma coisa dos campos, como por exemplo,
    que o texto da descrição tenha mais que 5 caracteres:
    '''

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Texto muito curto')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} {request.POST.get("sobrenome")} salvo com sucesso!')
    return redirect('index')

'''
@login_required é uma anotação para que essa página em específica só abra se tiver feito login. Caso o login não
tenha sido feito, redireciona para a página de login (redirect_field_name='login')
'''

