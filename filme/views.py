from django.shortcuts import render


def index(request):
    frase = "index de filme"
    return render(request, 'filme/index.html', {'frase': frase})
