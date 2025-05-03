from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UsuarioForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('empleados')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('empleados')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'autenticacion/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  

@login_required
def editar_perfil(request):
    user = request.user
    usuario = user.usuario
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        
        if user_form.is_valid() and usuario_form.is_valid():
            user_form.save()
            usuario_form.save()
            # Redirección correcta con parámetros
            return redirect(f"{reverse('editar_perfil')}?success=1")
    
    else:
        user_form = UserForm(instance=user)
        usuario_form = UsuarioForm(instance=usuario)
    
    return render(request, 'autenticacion/editar_perfil.html', {
        'user_form': user_form,
        'usuario_form': usuario_form
    })