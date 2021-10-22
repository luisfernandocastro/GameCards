from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *

# from .views import ThreadListView, ThreadDetailView,add_message

#Librerias Ramdom  

import random
import string 

#Lista de vistas 

#vista inicial del juego 

def index(request):
    return render(request,'templ_principal/index.html')

#vista para el tablero
def tablero(request):
    return render(request,'templ_principal/tablero_personal.html')

def partida(request):
    return render(request,'templ_principal/partida.html')




#Vista sala 
def sala(request):

    # programador = list(Programador.objects.all())
    # modulo = list(Modulo.objects.all())
    # error = list(Error.objects.all())
    
#declaramos una variable en cartas para llamar una lista de la tabla cartas en la base de datos 
    cartas = list(Cartas.objects.all())

    # cartas = programador + modulo + error

    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())
    
    random_secrets = random.sample(cartas,4) #reparte 4 cartas de forma secreta de la baraja
    random_item = random.choice(cartas) #listar de baraja de cartas 
    random_player = random.sample(cartas,4) #reparte 4 cartas de la baraja a los jugadores
    random_item = random.choice(cartas) #listar las cartas de la baraja

    #retorna la respuesta en el template sala

    return render(request, 'templ_principal/sala.html',{'random_items':random_secrets,'random_player':random_player})
#vista_sala_dos
def sala_dos(request):
    
    # programador = list(Programador.objects.all())
    # modulo = list(Modulo.objects.all())
    # error = list(Error.objects.all())

    #declaramos la variable cartas para mostrar una lista las cartas de error 

    cartas = Cartas = list(Error.objects.all())

    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())

    #reparte 4 cartas secretas 

    random_secrets = random.sample(cartas,4)

    #reparte 4 cartas a los jugador dos

    random_player = random.sample(cartas,4)


    return render(request, 'templ_principal/sala.html',{'random_items':random_secrets,'random_player':random_player})
#vista para sala tres
def sala_tres(request):
    #consulta en la tabla programador,modulo,error,cartas y lo guarda en cada una de la variables 
    programador = list(Programador.objects.all())
    modulo = list(Modulo.objects.all())
    error = list(Error.objects.all())
    cartas = programador + modulo + error

    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())
#reparte 4 cartas 
    random_secrets = random.sample(cartas,4)
    random_item = random.choice(programador)
#reparte 4 al jugador tres 
    random_player = random.sample(cartas,4)
    random_item = random.choice(programador)
#retorna la respusta en el template 
    return render(request, 'templ_principal/sala.html',{'random_items':random_secrets,'random_player':random_player})
#vista sala cuatro 
def sala_cuatro(request):
    #consulta en la tabla programador,modulo,error,cartas y lo guarda en cada una de la variables 
    programador = list(Programador.objects.all())
    modulo = list(Modulo.objects.all())
    error = list(Error.objects.all())
    
    

    cartas = programador + modulo + error

    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())
#reparte cuatro cartas secretas
    random_secrets = random.sample(cartas,4)
    random_item = random.choice(programador)
#reparte cuatro cartas al jugador
    random_player = random.sample(cartas,4)
    random_item = random.choice(programador)

    

    
    return render(request, 'templ_principal/sala.html',{'random_items':random_secrets,'random_player':random_player})
        
#vista basadas en clases para generar el codigo 
class Ingresar_code(TemplateView):  
    template_name = "templ_principal/ingresar_code.html"
#funcion generar codigo 
    def code(self):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        #para generar el codigo alfanumerico de 5 digitos (String + INT) del rango 5 
        print ("su codigo es", x) #imprime el codigo de 5 digitos alfanumericos
                                

#Vista tablero jugador/ personal 
def tablero_personal(request):
    
    #consulta en la tabla programador,modulo,error y lo guarda en cada una de la varibles 
    programador = list(Programador.objects.all())
    modulo = list(Modulo.objects.all())
    error = list(Error.objects.all())
    
    #une todas las listas de programador,modulo,error para la variable cartas 
    cartas = list(Cartas.objects.all())
    # modulo = list(Modulo.objects.all(),Error.objects.all())
    # error = list(Programador.objects.all(),Modulo.objects.all(),Error.objects.all())

    random_secrets = random.sample(cartas,4)#reparte 4 cartas secretas 

    random_player = random.sample(cartas,4)#reparte 4 cartas secretas al jugador
#respuesta de la template
    return render(request, 'templ_principal/tablero_personal.html',{'random_player':random_player})

#vista hilos de comunicacion 
# class ThreadListView(ListView):
#     model = Thread

# class ThreadDetailView(DetailView):
#     model = Thread


#     def add_message(request, pk):
    
#         pass











