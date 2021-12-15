from django.db import models

from filme.models import Filme


class Perfil(models.Model):

    nickname = models.SlugField(max_length=100)
    foto = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    seguidores = models.IntegerField(default=0)
    seguindo = models.IntegerField(default=0)
    data_cadastro = models.DateField()
    favoritos = models.ManyToManyField(Filme, related_name='favoritos')
    filmes_vistos = models.ManyToManyField(Filme, related_name='filmes_perfil')
    total_filmes_vistos = models.IntegerField(default=0)

    class Meta:
        db_table = 'perfil'

    def __str__(self):
        return self.nickname
