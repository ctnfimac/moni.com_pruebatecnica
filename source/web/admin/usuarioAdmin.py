from django.contrib import admin
from web.models.usuario import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['dni','nombre','apellido','email','genero','fecha_de_alta','fecha_de_modificacion']