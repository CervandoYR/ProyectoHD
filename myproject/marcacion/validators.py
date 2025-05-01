import re
from django.core.exceptions import ValidationError

def validar_codigo(value):
    # Verifica que solo contenga números
    if not value.isdigit():
        raise ValidationError('El código debe contener solo números.')

def validar_nombre(value):
    # Verifica que solo contenga letras (sin números ni caracteres especiales)
    if not value.isalpha():
        raise ValidationError('El nombre debe contener solo letras.')

def validar_dni(value):
    # Verifica que no haya caracteres especiales en la descripción
    if not re.match(r'^[a-zA-Z0-9\s]*$', value):  # Permite letras, números y espacios
        raise ValidationError('La descripción no debe contener caracteres especiales.')

