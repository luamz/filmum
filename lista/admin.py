from django.contrib import admin
from .models import Lista


class ListaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'perfil']
    search_fields = ['nome', 'perfil']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Lista, ListaAdmin)
