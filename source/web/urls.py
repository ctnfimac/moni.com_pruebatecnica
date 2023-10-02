from django.urls import path
from web.views.prestamoView import prestamo, PrestamoView
from web.views.administradorView import AdministradorView,PrestamoEliminarView,PrestamoEditarView

app_name = 'web'

urlpatterns = [
    path("", prestamo, name='prestamo'),
    path("administrador", AdministradorView.as_view(), name='administrador'),
    path("administrador/pretamo/eliminar/<int:pk>", PrestamoEliminarView.as_view(), name='eliminar_prestamo'),
    path("administrador/pretamo/editar/<int:pk>", PrestamoEditarView.as_view(), name='editar_prestamo'),
    path("prestamo", PrestamoView.as_view(), name='solicitar_prestamo')
]