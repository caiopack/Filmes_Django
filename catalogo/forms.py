from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'ano_lancamento', 'sinopse']
        labels = {
            'titulo': 'Título do Filme',
            'ano_lancamento': 'Ano de Lançamento',
            'sinopse': 'Sinopse',
        }