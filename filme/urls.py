from django.urls import path

from filme import views

app_name = 'filmes'

urlpatterns = [
    path('', views.index, name='index')
]