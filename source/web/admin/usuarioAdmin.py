from django.contrib import admin
from web.models.usuario import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass