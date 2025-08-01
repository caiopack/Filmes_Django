from django.shortcuts import render, redirect
from .models import Filme
from .forms import FilmeForm

def lista_filmes(request):
    """Exibe todos os filmes cadastrados."""
    filmes_qs = Filme.objects.order_by('-data_cadastro')
    contexto = {'filmes': filmes_qs}
    return render(request, 'catalogo/lista_filmes.html', contexto)

def novo_filme(request):
    """Adiciona um novo filme."""
    if request.method != 'POST':
        form = FilmeForm()
    else:
        form = FilmeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_filmes')
    
    contexto = {'form': form}
    return render(request, 'catalogo/novo_filme.html', contexto)