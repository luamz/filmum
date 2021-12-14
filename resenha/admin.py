from django.contrib import admin
from .models import Resenha


class ResenhaAdmin(admin.ModelAdmin):
    list_display = ['filme', 'perfil']
    search_fields = ['filme', 'perfil']


admin.site.register(Resenha, ResenhaAdmin)
