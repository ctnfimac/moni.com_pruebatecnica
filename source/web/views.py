from django.shortcuts import render

# Create your views here.
def prestamo(request):
    return render(request, 'prestamo/index.html')