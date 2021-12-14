from django.shortcuts import render
from django.core.paginator import Paginator
from random import choice
from lista.models import Lista


def index(request):
    lista = Lista.objects.all()[:1].get()
    filmes = lista.filmes.all()
    paginator = Paginator(filmes, 6)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    return render(request, 'lista/index.html', {'lista': lista, 'filmes': page_obj})
