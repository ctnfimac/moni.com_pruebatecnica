from django.urls import path
from web.views import prestamo

app_name = 'web'

urlpatterns = [
    path("prestamo", prestamo, name='prestamo')
]