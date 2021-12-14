from django.db import models
from genero.models import Genero


class Filme(models.Model):
    genero = models.ManyToManyField(Genero, related_name='generos')
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100)
    nome_original = models.CharField(max_length=100, blank=True)
    sinopse = models.TextField(default="Esse filme ainda não tem uma sinopse.")
    ano = models.CharField(max_length=4, default='0000', blank=True)
    duracao = models.IntegerField(blank=True)
    diretor = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    imagem = models.CharField(max_length=100)
    banner = models.CharField(max_length=100, blank=True)
    nota_publico = models.DecimalField(max_digits=2, decimal_places=1)
    data_cadastro = models.DateField()

    class Meta:
        db_table = 'filme'

    def __str__(self):
        return self.nome