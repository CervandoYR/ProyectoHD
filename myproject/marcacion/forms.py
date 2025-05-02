# marcacion/forms.py
from django import forms

from .validators import validar_codigo, validar_dni, validar_nombre
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Formulario para el modelo Empleado con validaciones personalizadas."""
    
    # Definimos los campos una sola vez con sus validadores
    codigo = forms.CharField(
        validators=[validar_codigo],
        help_text="Ingrese un código alfanumérico"
    )
    nombre = forms.CharField(
        validators=[validar_nombre],
        max_length=100,
        help_text="Ingrese el nombre completo"
    )
    dni = forms.CharField(
        validators=[validar_dni],
        max_length=8,
        help_text="Ingrese el DNI (8 dígitos)"
    )
    
    class Meta:
        model = Empleado
        fields = ['codigo', 'dni', 'nombre']
    
    def clean_codigo(self):
        """Validación adicional para el campo código."""
        codigo = self.cleaned_data.get('codigo')
        if not codigo.isalnum():
            raise forms.ValidationError("El código solo debe contener letras y números.")
        return codigo