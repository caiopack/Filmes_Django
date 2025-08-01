from django.shortcuts import render
from .models import Filme

# Create your views here.

def lista_filmes(request):
    """View da página inicial que lista os filmes"""
    filmes = Filme.objects.order_by('-data_cadastro')
    context = {'filmes': filmes}
    return render(request, 'catalogo/lista_filmes.html', context)