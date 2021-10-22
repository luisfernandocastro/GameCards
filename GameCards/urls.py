
from django.contrib import admin
from django.urls import path
from core.principal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminGameCard/', admin.site.urls),
    path('',views.index,name='index'),
    path('ingresar_code/',views.Ingresar_code.as_view(),name='ingresarcode'),
    path('sala/', views.sala, name='sala'),
    path('tablero_personal/',views.tablero_personal, name='tablero_personal'),
    path('login/',views.login, name='login')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # Mostrar imagenes 


