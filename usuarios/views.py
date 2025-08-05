from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def registro(request):
    """Registra um novo usuário"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
        login(request, new_user)
        return redirect('catalogo:lista_filmes')
    context = {'form': form}
    return render(request, 'usuarios/registro.html', context)

def logout_view(request):
    """Desloga o usuário atual"""
    logout(request)
    return redirect('catalogo:lista_filmes')
    