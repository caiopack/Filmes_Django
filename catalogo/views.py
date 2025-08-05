from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Filme
from .forms import FilmeForm

@login_required
def lista_filmes(request):
    """Exibe todos os filmes cadastrados."""
    filmes_qs = Filme.objects.filter(usuario=request.user).order_by('-data_cadastro')
    contexto = {'filmes': filmes_qs}
    return render(request, 'catalogo/lista_filmes.html', contexto)

@login_required
def novo_filme(request):
    """Adiciona um novo filme."""
    if request.method != 'POST':
        form = FilmeForm()
    else:
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            novo_filme_obj = form.save(commit=False)
            novo_filme_obj.usuario = request.user
            novo_filme_obj.save()
            return redirect('catalogo:lista_filmes')
    
    contexto = {'form': form}
    return render(request, 'catalogo/novo_filme.html', contexto)

@login_required
def editar_filme(request, filme_id):
    """Edita um filme existente."""
    filme = Filme.objects.get(id=filme_id)
    if filme.usuario != request.user:
        raise Http404

    if request.method != 'POST':
        form = FilmeForm(instance=filme)
    else:
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_filmes')

    contexto = {'filme': filme, 'form': form}
    return render(request, 'catalogo/editar_filme.html', contexto)

@login_required
def apagar_filme(request, filme_id):
    """Apaga um filme existente."""
    filme = Filme.objects.get(id=filme_id)
    if filme.usuario != request.user:
        raise Http404
    
    if request.method == 'POST':
        filme.delete()
        return redirect('catalogo:lista_filmes')
    context = {'filme': filme}
    return render(request, 'catalogo/apagar_filme.html', context)