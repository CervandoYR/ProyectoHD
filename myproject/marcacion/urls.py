# marcacion/urls.py
from django.urls import path
from .views import empleados, actualizar_empleado, eliminar_empleado

urlpatterns = [
    path('empleados/', empleados, name='empleados'),
    path('reportes/', empleados, name='reportes'),
    path('configuracion/', empleados, name='configuracion'),
    path('empleados/actualizar/<int:id>/', view=actualizar_empleado, name='actualizar_empleado'),

    path('empleados/eliminar/<int:id>/', view=eliminar_empleado, name='eliminar_empleado'),
]
