
#librerias para respuesta de url

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from core.principal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url principal
    path('adminGameCard/', admin.site.urls),
    path('',views.index,name='index'),
    #url ingresar codigo
    path('ingresar_code/',views.Ingresar_code.as_view(),name='ingresarcode'),
    #url ingresar sala
    path('sala/', views.sala, name='sala'),
    #url ingresar tablero personal
    path('tablero_personal/',views.tablero_personal, name='tablero_personal'),
    path('partida/',views.partida, name='partida'),
    path('', include('core.usuario.urls')),

    # path('thread/<int:pk>/add/', add_message, name='add'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # Mostrar imagenes


