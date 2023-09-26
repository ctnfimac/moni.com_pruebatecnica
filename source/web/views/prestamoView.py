# import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from web.forms.prestamoForm import PrestamoForm
from web.common.aprobacion_del_prestamo import aprobacion_del_prestamo

def prestamo(request):
    context = {
        'prestamoForm': PrestamoForm() 
    }
    return render(request, 'prestamo/index.html', context)


class PrestamoView(FormView):
    form_class = PrestamoForm
    template_name = reverse_lazy('web:prestamo')
    success_name = reverse_lazy('web:prestamo')

    def form_valid(self, form):
        try:
            dni = form.cleaned_data['dni']
            respuesta = aprobacion_del_prestamo(dni)

            if respuesta['status'] == 'approve' and respuesta['has_error'] == False:
                prestamo = form.save(aceptado=True)
                return JsonResponse({'msg': f'{prestamo.usuario.nombre} {prestamo.usuario.apellido} su prestamo fue aceptado!!!','error':False}, status=201)
            
            elif respuesta['status'] == 'rejected' and respuesta['has_error'] == False:
                prestamo = form.save(aceptado=False)
                return JsonResponse({'msg': f'{prestamo.usuario.nombre} {prestamo.usuario.apellido} lamentablemente su solicitud fue rechazada','error':True}, status=201)
            
            else:
                return JsonResponse({'msg': 'Hubo un error con la solicitud, Intentar Luego','error':True}, status=400)
            
        except Exception as e:
            return JsonResponse({'errors': e.__str__()}, status=400)


    def form_invalid(self, form) -> JsonResponse:
        errors = form.errors
        return JsonResponse({'errors': errors}, status=400)
