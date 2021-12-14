from django.shortcuts import render
from random import choice
from filme.models import Filme
from resenha.models import Resenha


def index(request):
    filme = choice(Filme.objects.all())
    generos = filme.genero.all()
    resenhas_populares = Resenha.objects.filter(filme=filme)[:2]
    resenhas_recentes = Resenha.objects.filter(filme=filme).order_by('-id')[:2]
    return render(request, 'filme/index.html', {'filme': filme, 'generos': generos,
                                                'resenhas_populares': resenhas_populares,
                                                'resenhas_recentes': resenhas_recentes})
