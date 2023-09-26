from django.contrib import admin
from web.models.prestamo import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','monto','aceptado','fecha_de_alta','fecha_de_modificacion']