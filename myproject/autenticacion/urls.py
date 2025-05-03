from django.urls import path
from .views import editar_perfil, login_view, logout_view
from marcacion.views import empleados  

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('empleados/', empleados, name='empleados'), 
    path('perfil/', empleados, name='perfil'),  
    path('perfil/editar/', editar_perfil, name='editar_perfil'), 
]