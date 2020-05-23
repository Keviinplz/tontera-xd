from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.user.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['password'].widget.attrs['class'] = 'input100'
    
class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de un Usuario en la base de datos

    Variables:

        - password1:    Contraseña
        - password2:    Verificación de la contraseña

    """
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'input100',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Confirmación de Contraseña', widget = forms.PasswordInput(
        attrs={
            'class': 'input100',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'primer_nombre', 'primer_apellido', 'segundo_apellido')
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class': 'input100',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'input100',
                }
            ),
            'primer_nombre': forms.TextInput(
                attrs={
                    'class': 'input100',
                }
            ),
            'primer_apellido': forms.TextInput(
                attrs = {
                    'class': 'input100',
                }                
            ),
            'segundo_apellido': forms.TextInput(
                attrs = {
                    'class': 'input100',
                }                
            ),
        }

    def clean_password2(self):
        """ Validación de Contraseña

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('¡Las contraseñas ingresadas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user