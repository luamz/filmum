
from django.urls import path, include
from lista import views

app_name = 'lista'

urlpatterns = [
    path('', views.index, name='index'),
    path('filme/', include('filme.urls')),
    path('perfil/', include('perfil.urls')),
]