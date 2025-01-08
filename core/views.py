from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from core.models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': "Programação Web com Django",
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contato.html')

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