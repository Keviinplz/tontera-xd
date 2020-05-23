from django.urls import path

from .views import Login, RegistroUsuario

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('register', RegistroUsuario.as_view(), name='register')
]