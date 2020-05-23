from django import forms
from .models import Proyecto, Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre','descripcion')
        label = {
            'nombre':'Título del Proyecto',
            'descripcion': 'Descripción del Proyecto',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Título del Proyecto'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder' : 'Breve Descripción del Proyecto'
                }
            )
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'proyecto', 'esta_completada']
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Título de la Tarea'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Breve descripción de su Tarea'
                }
            ),
            'fecha_inicio': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'proyecto': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'esta_completada': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control',
                }
            )
        }