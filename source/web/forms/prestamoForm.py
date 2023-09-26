from django import forms
from web.models.usuario import Usuario
from web.models.prestamo import Prestamo
from web.models.genero import Genero


class PrestamoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length='30')
    apellido = forms.CharField(label='Apellido',max_length='30')
    email = forms.EmailField(label='Email', max_length='30')
    dni = forms.CharField(label='DNI', max_length='8')
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())

    class Meta:
        model = Prestamo
        fields = ['dni','email','nombre','apellido','genero','monto']

    class Media:
        js = ('js/web/prestamoForm.js',)

    def save(self, commit = True, aceptado=False):
        genero = Genero.objects.get(tipo=self.cleaned_data['genero'])
        
        obj_usuario, creado = Usuario.objects.get_or_create(
            nombre = self.cleaned_data['nombre'],
            apellido = self.cleaned_data['apellido'],
            email = self.cleaned_data['email'],
            dni = self.cleaned_data['dni'],
            genero = genero
        )

        obj_prestamo = Prestamo.objects.create(
            monto = self.cleaned_data['monto'],
            usuario = obj_usuario,
            aceptado = aceptado
        )

        if commit:
            obj_prestamo.save()
        return obj_prestamo


    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if int(monto) <= 0:
            self.add_error('monto', 'El monto ingresado tiene que ser mayor a $0')
        return monto

        
       

