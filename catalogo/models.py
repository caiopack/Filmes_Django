from django.db import models
from django.utils import timezone

# Create your models here.

class Filme(models.Model):
    """Um modelo pra representar um filme que o usuário assistiu."""
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    sinopse = models.TextField()
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Retorna uma representação legível do título do filme."""
        return self.titulo

