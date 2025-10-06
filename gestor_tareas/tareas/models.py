from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("view_tareas", "Puede ver la sección de tareas"),
            ("agregar_tareas", "Puede ver la sección de agregar tareas"),
            ("eliminar_tareas", "Puede ver la sección de eliminar tareas"),            
        ]    