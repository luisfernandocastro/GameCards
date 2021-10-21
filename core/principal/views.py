from django.shortcuts import render
from django.views.generic.base import TemplateView

#Librerias Ramdom  

import random
import string 

#Lista de vistas 


def index(request):
    return render(request,'templ_principal/index.html')

def tablero(request):
    return render(request,'templ_principal/tablero_personal.html')

def sala(request):
    return render(request, 'templ_principal/sala.html')

class Ingresar_code(TemplateView):  
    template_name = "templ_principal/ingresar_code.html"

    def code(self):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print ("Codigo generado por Alejandro", x)

def tablero_personal(request):
    return render(request, 'templ_principal/tablero_personal.html')











