from django.db import models

from apps.user.models import Usuario

# Create your models here.
class Proyecto(models.Model):
  nombre = models.CharField(max_length=100, verbose_name='Nombre del Proyecto')
  descripcion = models.TextField(max_length=300, verbose_name='Descripción del Proyecto')
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

  class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['nombre']

  def __str__(self):
      return f'{self.nombre}'

class Tarea(models.Model):
  proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
  titulo = models.CharField(max_length=100, verbose_name='Título de la Tarea')
  descripcion = models.TextField(max_length=300, verbose_name='Descripción de la Tarea', blank=True, null=True)
  fecha_inicio = models.DateField(verbose_name='Fecha de Inicio', blank=True, null=True)
  fecha_termino = models.DateField(verbose_name='Fecha de Termino', blank=True, null=True)
  esta_completada = models.BooleanField(verbose_name='¿Está Completada?', default=False)

  class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['proyecto']

  def __str__(self):
      return f'{self.titulo}'

