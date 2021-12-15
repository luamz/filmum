from django.urls import path, include
from filme import views

app_name = 'filmes'

urlpatterns = [
    path('', views.index, name='index'),
]