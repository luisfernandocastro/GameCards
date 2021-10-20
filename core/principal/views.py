from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request,'templ_principal/index.html')



def tablero(request):
    return render(request,'templ_principal/tablero.html')

def sala(request):
    return render(request, 'templ_principal/sala.html')

