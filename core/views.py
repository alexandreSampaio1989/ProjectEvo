from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Produto
from .forms import ContatoForm


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': "Programação Web com Django",
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contact(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            print(f'Nome: {nome}')
            print(f'E-Mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-Mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'contato_form': form
    }
    return render(request, 'contato.html', context)

def product(request, pk):
    #_produto = Produto.objects.get(id=pk)
    _produto = get_object_or_404(Produto, id=pk)

    context = {
        'produto': _produto,
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)