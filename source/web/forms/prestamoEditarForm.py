from django import forms
from web.models.prestamo import Prestamo


class PrestamoEditarForm(forms.ModelForm):
    aceptado_auxiliar = forms.BooleanField(required=False)

    class Meta:
        model = Prestamo
        fields = ['monto','aceptado','aceptado_auxiliar']

    class Media:
        js = ('js/web/prestamoEditarForm.js',)

    def save(self, commit: bool = True):
        instancia = super(PrestamoEditarForm, self).save(commit=False)
        
        instancia.aceptado = True if self.cleaned_data['aceptado_auxiliar'] else False

        if commit:
            instancia.save()
        return instancia
    
    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if int(monto) <= 0:
            self.add_error('monto', 'El monto ingresado tiene que ser mayor a $0')
        return monto
