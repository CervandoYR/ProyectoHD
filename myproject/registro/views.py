from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RegistroForm
from autenticacion.models import Usuario
from django.contrib.auth.models import User

@login_required
def registro_view(request):
    # Comprobar si el usuario tiene el rol de admin o profesor
    if request.user.usuario.rol not in ['Administrador', 'Profesor']:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # 1. Guarda el usuario principal
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            
            # 2. Guarda el perfil de usuario con el rol
            Usuario.objects.update_or_create(
                user=user,
                defaults={'rol': form.cleaned_data['rol']}
            )
            
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})
