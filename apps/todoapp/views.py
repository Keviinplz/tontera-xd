import re

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

# Create your views here.
class ListaProyectos(ListView):
  model = Proyecto
  template_name="todoapp/dashboard.html"
  context_object_name = 'proyectos'

  def get_queryset(self):
    return self.model.objects.filter(usuario=self.request.user)

class CrearProyecto(CreateView):
  model = Proyecto
  template_name = "todoapp/crear_proyecto.html"
  form_class = ProyectoForm
  success_url = reverse_lazy('todoapp:dashboard')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['proyectos'] = self.model.objects.filter(usuario=self.request.user)
    return context 

  def post(self, request, *args, **kwargs):
    form = self.form_class(self.request.POST)
    if form.is_valid():
      new_proyect = Proyecto(
        nombre = form.cleaned_data.get('nombre'),
        descripcion = form.cleaned_data.get('descripcion'),
        usuario = self.request.user
      )
      new_proyect.save()
      return redirect('todoapp:dashboard')

class EditarProyecto(UpdateView):
  model = Proyecto
  template_name = "todoapp/crear_proyecto.html"
  form_class = ProyectoForm
  success_url = reverse_lazy('todoapp:dashboard')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['proyectos'] = self.model.objects.filter(usuario=self.request.user)
    return context 

class EliminarProyecto(DeleteView):
  model = Proyecto
  success_url = reverse_lazy('todoapp:dashboard')

class ListaTareas(View):
  model = Tarea
  template_name="todoapp/todolist.html"
  
  def get(self, request, pk, *args, **kwargs):
    contexto = {}
    proyecto = Proyecto.objects.filter(id=pk)[0]
    proyectos_usuario = Proyecto.objects.filter(usuario=self.request.user)
    contexto['proyecto_pedido'] = proyecto
    contexto['tareas'] = self.model.objects.filter(proyecto=proyecto)
    contexto['proyectos'] = proyectos_usuario
    return render(request, self.template_name, contexto)

class CrearTarea(CreateView):
  model = Tarea
  template_name = "todoapp/crear_todo.html"
  form_class = TareaForm
  success_url = reverse_lazy('todoapp:dashboard')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['proyectos'] = Proyecto.objects.filter(usuario=self.request.user)
    return context 

  def post(self, request, *args, **kwargs):
    form = self.form_class(self.request.POST)
    if form.is_valid():
      new_task = Tarea(
        titulo = form.cleaned_data.get('titulo'),
        descripcion = form.cleaned_data.get('descripcion'),
        fecha_inicio = form.cleaned_data.get('fecha_inicio'),
        proyecto = form.cleaned_data.get('proyecto'),
        esta_completada = form.cleaned_data.get('esta_completada')
      )
      new_task.save()
      return redirect('todoapp:dashboard')

class EditarTarea(UpdateView):
  model = Tarea
  template_name = "todoapp/crear_todo.html"
  form_class = TareaForm
  success_url = reverse_lazy('todoapp:dashboard')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['proyectos'] = Proyecto.objects.filter(usuario=self.request.user)
    return context 

class EliminarTarea(DeleteView):
  model = Tarea
  success_url = reverse_lazy('todoapp:dashboard')

class VerTareaEspecifica(View):
  model = Tarea
  template_name = 'todoapp/ver_tarea.html'

  def get(self, request, pk, *args, **kwargs):
    contexto = {}
    proyectos = Proyecto.objects.filter(usuario=self.request.user)
    contexto['tarea'] = self.model.objects.filter(id=pk)[0]
    contexto['proyectos'] = proyectos
    print(self.model.objects.filter(id=pk)[0])
    return render(request, self.template_name, contexto)