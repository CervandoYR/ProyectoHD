# marcacion/forms.py
from django import forms

from .validators import validar_codigo, validar_dni
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['codigo', 'dni','nombre', 'apellido', 'telefono']
        
       
        
        # Aplicar validadores a cada campo
    codigo = forms.CharField(validators=[validar_codigo])
    nombre = forms.CharField( max_length=100)
    apellido = forms.CharField( max_length=100)
    dni = forms.CharField(validators=[validar_dni], max_length=8)
    telefono = forms.CharField(max_length=9)
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise forms.ValidationError("El código solo puede contener letras y números.")
        return codigo
    
    