from django.contrib import admin
from web.models.genero import Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass