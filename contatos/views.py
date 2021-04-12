from django.shortcuts import render, get_object_or_404, redirect  # atalho para trabalhar erros
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value  # para consultas mais complexas
from django.db.models.functions import Concat  # para concatenar os campos
from django.contrib import messages  # para importar as mensagens de erro


def index(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)  # (2) - README - contatos/README.md
    # ordenar por id. o sinal de menos é pra ordem invertida ('-id')
    # .filter equivale ao if feito no html, mas deixa o código mais limpo diretamente feito no back-end
    # contatos = Contato.objects.all()  # pegar todos os objetos da classe Contato e coloca dentro da variável contato

    paginator = Paginator(contatos, 10)  # Show x contacts per page.

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'pages/index.html', {
        'contatos': contatos
    })


# usando o get_object_or_404
def detalhes(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        # raise Http404()
        messages.add_message(
            request,
            messages.ERROR,
            'Este ID não está disponível'
        )
        return redirect('index')

    # contato = Contato.objects.get(id=contato_id)  # pegar o id do contato

    return render(request, 'pages/detalhes.html', {
        'contato': contato
    })


# Fazendo manual:
'''
def detalhes(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)  # pegar o id do contato
        return render(request, 'pages/detalhes.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:  # transformando erro 500 em 404 (quando é problema do servidor).
        # DoesNotExist é o nome do erro.
        raise Http404'''  # (1) - README - contatos/README.md


def busca(request):
    termo = request.GET.get('termo')  # pegar o termo

    if termo is None or not termo:
        # raise Http404
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')  # (3) - README - contatos/README.md
    contatos = Contato.objects.annotate(  # (4) - README - contatos/README.md
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
        # procura por nome e sobrenome OU telefone - uso do Q
    )
    
    '''
    contatos = Contato.objects.order_by('id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),  # esse __icontains pega o resultado parcial do nome
        # o Q é para transformar as buscar de AND para OR
        mostrar=True
    )

    -> usando o Concat tem que fazer de outra forma pois desse jeito, continua sem pegar os dois nomes
    '''

    paginator = Paginator(contatos, 10)  # Show 5 contacts per page.

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'pages/busca.html', {
        'contatos': contatos
    })
