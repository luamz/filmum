from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table = 'genero'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

