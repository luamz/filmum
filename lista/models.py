from django.db import models
from filme.models import Filme
from perfil.models import Perfil


class Lista(models.Model):
    filmes = models.ManyToManyField(Filme, related_name='filmes')
    perfil = models.ForeignKey(Perfil, related_name='perfil', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100)
    curtidas = models.IntegerField(default=0)
    data_cadastro = models.DateField()

    class Meta:
        db_table = 'lista'

    def __str__(self):
        return self.nome