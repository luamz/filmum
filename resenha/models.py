from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from filme.models import Filme
from perfil.models import Perfil


class Resenha(models.Model):
    filme = models.ForeignKey(Filme, related_name='filme_resenha', on_delete=models.DO_NOTHING)
    perfil = models.ForeignKey(Perfil, related_name='perfil_resenha', on_delete=models.DO_NOTHING)
    estrelas = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    curtidas = models.IntegerField(default=0)
    texto = models.TextField(default=" ")
    data_cadastro = models.DateField()

    class Meta:
        db_table = 'resenha'

