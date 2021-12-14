from django.contrib import admin
from .models import Filme


class FilmeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Filme, FilmeAdmin)
