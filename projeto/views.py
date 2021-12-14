from django.shortcuts import render

from filme.models import Filme
from lista.models import Lista
from perfil.models import Perfil
from resenha.models import Resenha


def index(request):
    filmes = Filme.objects.all().order_by('-id')[:6]
    resenhas = Resenha.objects.all().order_by('-id')[:4]
    perfis = Perfil.objects.all().order_by('-id')[:4]
    listas = Lista.objects.all().order_by('-id')[:4]
    print(filmes)
    return render(request, 'index.html', {'filmes': filmes,
                                          'resenhas': resenhas,
                                          'perfis': perfis,
                                          'listas': listas})
