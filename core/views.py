from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Produto
from .forms import ContatoForm, ProdutoModelForm


def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-Mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'contato_form': form
    }
    return render(request, 'contato.html', context)

def form_produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar Produto')
        form = ProdutoModelForm()
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'form_produto.html', context)


def produto(request, pk):
    #_produto = Produto.objects.get(id=pk)
    _produto = get_object_or_404(Produto, id=pk)

    context = {
        'produto': _produto,
    }
    return render(request, 'produto.html', context)

"""
 HANDLERS PARA PAGE NOT FOUND E ERRO 500
"""
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)