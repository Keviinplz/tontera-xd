from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('', login_required(ListaProyectos.as_view()), name='dashboard'),
    path('proyecto/ver/<int:pk>', login_required(ListaTareas.as_view()), name='proyecto'),
    path('proyecto/crear', login_required(CrearProyecto.as_view()), name='crear_proyecto'),
    path('proyecto/editar/<int:pk>', login_required(EditarProyecto.as_view()), name='editar_proyecto'),
    path('proyecto/eliminar/<int:pk>', login_required(EliminarProyecto.as_view()), name='eliminar_proyecto'),
    path('tarea/crear/', login_required(CrearTarea.as_view()), name='crear_tarea'),
    path('tarea/ver/<int:pk>', login_required(VerTareaEspecifica.as_view()), name='ver_tarea'),
    path('tarea/eliminar/<int:pk>', login_required(EliminarTarea.as_view()), name='eliminar_tarea'),
    path('tarea/editar/<int:pk>', login_required(EditarTarea.as_view()), name='editar_tarea'),
]
