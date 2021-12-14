from django.db import models


class Perfil(models.Model):

    nickname = models.SlugField(max_length=100)
    foto = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    seguidores = models.IntegerField(default=0)
    seguindo = models.IntegerField(default=0)
    filmes_vistos = models.IntegerField(default=0)
    data_cadastro = models.DateField()

    class Meta:
        db_table = 'perfil'

    def __str__(self):
        return self.nickname
