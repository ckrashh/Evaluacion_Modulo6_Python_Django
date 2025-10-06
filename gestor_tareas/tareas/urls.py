from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # aquí se define 'home'
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tarea/<str:tarea_titulo>/', views.detalles_tarea, name='detalles_tarea'),
    path('tareas/', views.TareasView.as_view(), name='tareas'),
    path('agregar_tarea/', views.AgegarTareaView.as_view(), name='agregar_tarea'),
    path('eliminar_tarea/', views.EliminarTareaView.as_view(), name='eliminar_tarea'),
    path('elminar_tarea/<str:tarea_titulo>/', views.eliminar_tarea, name='eliminar_tarea_confirmar'),
]