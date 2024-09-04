from django.shortcuts import render, redirect
from .models import Listar
from .form import ListarForm


# Create your views here.

def crear(request):
    if request.method == 'POST':
        form = ListarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = ListarForm()
    return render(request, 'crear.html', {'form': form})

def listar(request):
    tareas = Listar.objects.all()
    return render(request, 'listar.html', {'tareas': tareas})
    
