from django import forms
class TareaForm(forms.Form):
    Titulo = forms.CharField(label="Titulo de la tarea", max_length=100)
    Descripcion = forms.CharField(label="Descripcion de la tarea", max_length=100)
