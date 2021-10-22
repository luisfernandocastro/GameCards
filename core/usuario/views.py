from django.shortcuts import redirect, render
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login as Auth_login, logout
from django.contrib.auth.views import LoginView
from django.conf import settings as setting

# Create your views here.


class Login(LoginView):
    template_name = 'registration/login.html' # plantilla html a usar para mostrar el login

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: # evita que el usuario logueado ingrese a la vista login  
            return redirect(setting.LOGIN_REDIRECT_URL) # lo redirecciona al home
        return super().dispatch(request, *args, **kwargs)

    # variabkes a usar en el template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
        

def registrarse(request):   
    data={
        'form': CustomUserCreationForm() #Es un modelo y formulario para el registro
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            Auth_login(request, user)
            #messages.success(request, "Tu registro ha sido exitoso")
            return redirect(to='principal')
        data['form'] = formulario

    return render (request, 'templ_principal/registrarse.html', data)