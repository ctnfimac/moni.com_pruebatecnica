from django.contrib import admin
from web.models.prestamo import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    pass