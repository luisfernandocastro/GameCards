#Librerias destinadas a la autenticacion de usuarios y creacion de usuarios 

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

User = get_user_model()

#formulario de autenticacion de jugadores 
class LoginForm (AuthenticationForm):
    def __init__(self, *args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs) #inilizacion de formulario
        self.fields['username'] # input para ingresar el campo de usuario
        self.fields['password'] # input para ingresar el campo de contraseña

#formulario de registro de cjugadores
class CustomUserCreationForm(UserCreationForm):
    class Meta:        
        model = User #usara el modelo usuarios
        fields= ["username","email","first_name","last_name","password1", "password2"] #input para ingresar el usuario,email,nombre,apellido,contrasena,confirmar contraseña
    