from django.shortcuts import render
from random import choice

from lista.models import Lista
from perfil.models import Perfil
from resenha.models import Resenha


def index(request):
    perfil = choice(Perfil.objects.all())
    vistos = 0
    listas = 0
    for i in perfil.filmes_vistos.all():
        vistos += 1
    listas_perfil = Lista.objects.all().filter(perfil=perfil)
    for j in listas_perfil:
        listas += 1

    favoritos = perfil.favoritos.all()
    ultimos = perfil.filmes_vistos.all().order_by('-id')[:4]
    resenhas_populares = Resenha.objects.all().filter(perfil=perfil)[:2]
    resenhas_recentes = Resenha.objects.all().filter(perfil=perfil).order_by('-id')[:2]
    return render(request, 'perfil/index.html', {'perfil': perfil, 'vistos': vistos,
                                                 'listas': listas, 'favoritos': favoritos,
                                                 'ultimos': ultimos, 'listas_perfil': listas_perfil,
                                                 'resenhas_recentes': resenhas_recentes,
                                                 'resenhas_populares': resenhas_populares
                                                 })
