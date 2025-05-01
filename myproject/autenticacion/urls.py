from django.urls import path
from .views import login_view, logout_view
from marcacion.views import empleados  

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('empleados/', empleados, name='empleados'),  
]
