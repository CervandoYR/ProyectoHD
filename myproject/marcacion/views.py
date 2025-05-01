from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def empleados(request):
    form = EmpleadoForm()
    empleados = Empleado.objects.all().order_by('codigo') 

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

    return render(request, 'marcacion/empleados.html', {'form': form, 'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id) 
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)  
        if form.is_valid():
            form.save() 
            return redirect('empleados')
    else:
        form = EmpleadoForm(instance=empleado) 

    # Renderiza solo el formulario si es una solicitud GET (para AJAX)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'marcacion/edit_form.html', {'form': form})

    # Renderiza una página completa en caso de no ser AJAX
    return render(request, 'marcacion/empleados.html', {'form': form})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados')
    return render(request, 'marcacion/confirmar_eliminacion.html', {'empleado': empleado})

def reportes(request):
    empleados = Empleado.objects.all()
    return render(request, 'marcacion/reportes.html', {'empleados': empleados})

def configuracion(request):
    return render(request, 'marcacion/configuracion.html')

