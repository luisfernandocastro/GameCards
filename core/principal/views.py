from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *

#Librerias Ramdom  

import random
import string 

#Lista de vistas 


def index(request):
    return render(request,'templ_principal/index.html')

def tablero(request):
    return render(request,'templ_principal/tablero_personal.html')

def sala(request):

    programador = list(Programador.objects.all())
    modulo = list(Modulo.objects.all())
    error = list(Error.objects.all())

    cartas = programador + modulo + error

    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())

    random_secrets = random.sample(cartas,4)
    random_item = random.choice(programador)

    random_player = random.sample(cartas,4)
    random_item = random.choice(programador)


    return render(request, 'templ_principal/sala.html',{'random_items':random_secrets,'random_player':random_player})


class Ingresar_code(TemplateView):  
    template_name = "templ_principal/ingresar_code.html"

    def code(self):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print ("Codigo generado por Alejandro", x)

def tablero_personal(request):
    return render(request, 'templ_principal/tablero_personal.html')











