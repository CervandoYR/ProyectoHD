# registro/forms.py


from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuario
from django.core.exceptions import ValidationError
import re

# Opciones de rol
ROLES = (
    ('Administrador', 'Administrador'),
    ('Profesor', 'Profesor'),
    ('Estudiante', 'Estudiante'),
)

class RegistroForm(forms.ModelForm):
    rol = forms.ChoiceField(choices=ROLES, label="Rol")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso. Elija otro.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso. Elija otro.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", first_name):
            raise ValidationError("El nombre solo puede contener letras.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", last_name):
            raise ValidationError("El apellido solo puede contener letras.")
        return last_name

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # Verifica si ya existe para no crear dos
            if not hasattr(user, 'usuario'):
                Usuario.objects.create(
                    user=user,
                    rol=self.cleaned_data['rol']
                )
        return user