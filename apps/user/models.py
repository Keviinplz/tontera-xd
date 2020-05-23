from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, primer_nombre, primer_apellido, segundo_apellido, password = None):
        if not email:
            raise ValueError('¡El correo electrónico proporcionado no es valido!')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email), 
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, primer_nombre, primer_apellido, segundo_apellido, password):
        user = self.create_user(
            username=username,
            email=email,            
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            password=password
        )
        user.usuario_administrador = True
        user.save()
        return user


class Usuario(AbstractBaseUser):
    username = models.CharField(unique = True, max_length=100, verbose_name='Nombre de usuario')
    email = models.EmailField(max_length=254, unique = True, verbose_name='Correo Electrónico')
    primer_nombre = models.CharField(max_length=200, blank = True, null = True, verbose_name='Primer Nombre')
    primer_apellido = models.CharField(max_length=200, blank = True, null = True, verbose_name='Apellido Paterno')
    segundo_apellido = models.CharField(max_length=200, blank = True, null = True, verbose_name='Apellido Materno')
    imagen = models.ImageField(upload_to='perfil/', max_length=200, blank = True, null = True, verbose_name='Foto de Perfil')
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','primer_nombre', 'primer_apellido', 'segundo_apellido']

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        return self.usuario_administrador