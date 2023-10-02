from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from web.models.prestamo import Prestamo
from web.forms.prestamoEditarForm import PrestamoEditarForm
from django.http import JsonResponse
from django.views.generic import(
    ListView,
    DeleteView,
    UpdateView
)



class AdministradorView(LoginRequiredMixin,ListView):
    """
    lista todos los prestamos solicitados ordenados por id de
    forma descendente.
    Solo se puede ingresar si esta logueado
    """
    template_name = 'prestamo/administrador.html'
    model = Prestamo
    context_object_name = 'prestamos'
    ordering = ['-id']


class PrestamoEliminarView(LoginRequiredMixin,DeleteView):
    model = Prestamo
    template_name = 'prestamo/confirmar_eliminar_prestamo.html'
    success_url = reverse_lazy('web:administrador')


class PrestamoEditarView(LoginRequiredMixin,UpdateView):
    model = Prestamo
    form_class = PrestamoEditarForm
    template_name = 'prestamo/editar.html'
    context_object_name = 'prestamo'
    success_url = reverse_lazy('web:administrador')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        errors = form.errors
        return JsonResponse({'errors': errors}, status=400)
    
