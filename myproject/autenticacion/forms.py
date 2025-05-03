# autenticacion/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['bio', 'intereses', 'historial_actividad']