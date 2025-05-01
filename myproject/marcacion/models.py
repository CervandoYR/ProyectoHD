from django.db import models
from django.db.models import Max

class Empleado(models.Model):
    codigo = models.CharField(max_length=2000, unique=True, blank=True)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)


    def save(self, *args, **kwargs):
        if not self.codigo:
            
            last_codigo = Empleado.objects.aggregate(Max('codigo'))['codigo__max']
            if last_codigo:
                
                self.codigo = str(int(last_codigo) + 1)
            else:
                self.codigo = '1'  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
