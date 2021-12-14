from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),
    path('filme/', include('filme.urls')),
    path('admin/', admin.site.urls),
]

