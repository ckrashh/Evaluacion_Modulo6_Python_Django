from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from .models import CustomUser
from .mixins import ProtectedTemplateView, PermissionProtectedTemplateView
from .forms import TareaForm

# Lista en memoria para guardar los datos
tareas = []

def index(request):
    if request.user.is_authenticated:
        global tareas
        # Filtrar las tareas para mostrar solo las del usuario autenticado
        tareas = [tarea for tarea in tareas if tarea['Usurario'] == request.user.username]
        return render(request, 'index.html' , {'tareas': tareas})
    
    return redirect('login')

class TareasView(ProtectedTemplateView):
    """Vista protegida para tareas - requiere autenticación"""
    template_name = 'tareas.html'
    permission_required = 'tareas.view_tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = [tarea for tarea in tareas if tarea['Usurario'] == self.request.user.username]
        return context

class EliminarTareaView(ProtectedTemplateView):
    """Vista protegida para tareas - requiere autenticación"""
    template_name = 'eliminar_tarea.html'
    permission_required = 'tareas.eliminar_tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = [tarea for tarea in tareas if tarea['Usurario'] == self.request.user.username]
        return context

class AgegarTareaView(ProtectedTemplateView):
    """Vista protegida para tareas - requiere autenticación"""
    permission_required = 'tareas.agregar_tareas'
    
    def get(self, request):
        form = TareaForm()
        return render(request, 'agregar_tarea.html', {'form': form})

    def post(self, request):
        form = TareaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['Titulo']
            descripcion = form.cleaned_data['Descripcion']
            global tareas
            tareas.append({'Usurario': request.user.username, 'Titulo': nombre, 'Descripcion': descripcion})
            return redirect('index')
        
        return render(request, 'agregar_tarea.html', {'form': form})


def detalles_tarea(request, tarea_titulo):
    global tareas
    for tarea in tareas:
        if tarea['Titulo'] == tarea_titulo and tarea['Usurario'] == request.user.username:
            return render(request, 'detalles_tarea.html', {'tarea': tarea})
    return redirect('tareas')
def register(request):
    from django.contrib.auth.models import Group
    
    # Creamos una clase inline que use CustomUser
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)"""
    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)"""
    return render(request, '404.html', status=404)

def eliminar_tarea(request, tarea_titulo):
    global tareas
    tareas = [tarea for tarea in tareas if tarea['Titulo'] != tarea_titulo]
    return redirect('tareas')
    
    
    
