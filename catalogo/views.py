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

def editar_filme(request, filme_id):
    """Edita um filme existente."""
    filme = Filme.objects.get(id=filme_id)
    if request.method != 'POST':
        form = FilmeForm(instance=filme)
    else:
        form = FilmeForm(instance=filme, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_filmes')
    context = {'filme': filme, 'form': form}
    return render(request, 'catalogo/editar_filme.html', context)

def apagar_filme(request, filme_id):
    """Apaga um filme existente."""
    filme = Filme.objects.get(id=filme_id)
    if request.method == 'POST':
        filme.delete()
        return redirect('catalogo:lista_filmes')
    context = {'filme': filme}
    return render(request, 'catalogo/apagar_filme.html', context)