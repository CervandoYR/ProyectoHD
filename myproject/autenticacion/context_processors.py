# autenticacion/context_processors.py
from .models import Usuario

def user_permissions(request):
    context = {}
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            context['user_role'] = usuario.rol
            context['is_admin'] = usuario.rol == 'Administrador'
            context['is_profesor'] = usuario.rol == 'Profesor'
            context['is_estudiante'] = usuario.rol == 'Estudiante'
        except Usuario.DoesNotExist:
            context['user_role'] = None
    return context
