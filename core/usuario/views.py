from django.shortcuts import redirect, render
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login  as auth_login
from django.contrib.auth.views import LoginView
from django.conf import settings as setting
from django.contrib.auth import get_user_model

User = get_user_model()


#Vista ingresar

class Login(LoginView):
    template_name = 'registration/login.html' # plantilla html a usar para mostrar el login

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: # evita que el usuario logueado ingrese a la vista login
            return redirect(setting.LOGIN_REDIRECT_URL) # lo redirecciona al home
        return super().dispatch(request, *args, **kwargs)

    # variables a usar en el template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context




# funcion paea regitro de usuarios
def registrarse(request):
    data = {
        # Formulario personalizado  que se trae desde el forms.py
        'form': CustomUserCreationForm(),
    }
    if request.user.is_authenticated:
        return redirect(setting.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        # request.FILES ,necesario para subir imagenes
        formulario = CustomUserCreationForm(
            data=request.POST, files=request.FILES)
        if formulario.is_valid():  # validacion de los datos ingresados (si son correctos se procede a guardar estos datos)
            formulario.save()  # Guardado de datos
            # Si  los datos ingresados son correctos el usuario queda logueado al momento
            user = authenticate(
                email=formulario.cleaned_data['email'], password=formulario.cleaned_data['password1'])
            auth_login(request, user)
            # messages.success(request, "Te has registrado correctamente")
            # redireccion de los datos validados correctamente a la ventana de exito
            return redirect(to='partida')
        data['form'] = formulario

    return render(request, 'registration/registrarse.html', data)