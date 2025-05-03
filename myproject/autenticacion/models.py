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
    rol = models.CharField(max_length=50, choices=ROLES, default='Estudiante')
    bio = models.TextField(blank=True, null=True)
    intereses = models.TextField(blank=True, null=True)
    historial_actividad = models.TextField(blank=True, null=True)

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'usuario'):
        Usuario.objects.create(user=instance)
