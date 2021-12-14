from django.contrib import admin
from .models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'slug']
    search_fields = ['nickname', 'slug']
    prepopulated_fields = {'slug': ('nickname',)}


admin.site.register(Perfil, PerfilAdmin)
