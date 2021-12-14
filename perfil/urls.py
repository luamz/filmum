from django.urls import path

from perfil import views

app_name = 'perfil'

urlpatterns = [
    path('', views.index, name='index')
]