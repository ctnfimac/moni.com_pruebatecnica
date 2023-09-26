from django.contrib import admin
from web.models.genero import Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
        list_display = ['tipo','fecha_de_alta','fecha_de_modificacion']
