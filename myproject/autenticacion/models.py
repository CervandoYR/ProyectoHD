# autenticacion/models.py
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Usuario(models.Model):
    ROLES = (
        ('Administrador', 'Administrador'),
        ('Profesor', 'Profesor'),
        ('Estudiante', 'Estudiante'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    rol = models.CharField(max_length=50, choices=ROLES, default='Estudiante')  # Añade default aquí

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'usuario'):  # Solo crear si no existe
        Usuario.objects.create(user=instance)