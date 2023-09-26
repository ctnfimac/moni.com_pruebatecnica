from django.urls import path
from web.views.prestamoView import prestamo, PrestamoView

app_name = 'web'

urlpatterns = [
    path("", prestamo, name='prestamo'),
    path("prestamo", PrestamoView.as_view(), name='solicitar_prestamo')
]