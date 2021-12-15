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

    banner = Filme.objects.all().exclude(banner='')[:5]
    banner0 = banner[0]
    banner1 = banner[1]
    banner2 = banner[2]
    print(banner2)
    banner3 = banner[3]
    banner4 = banner[4]

    return render(request, 'index.html', {'filmes': filmes,
                                          'resenhas': resenhas,
                                          'perfis': perfis,
                                          'listas': listas,
                                          'banner0': banner0,
                                          'banner1': banner1,
                                          'banner2': banner2,
                                          'banner3': banner3,
                                          'banner4': banner4, })
