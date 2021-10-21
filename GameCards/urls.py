
from django.contrib import admin
from django.urls import path
from core.principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('ingresar_code/',views.Ingresar_code.as_view(),name='ingresarcode'),
    path('sala/', views.sala, name='sala'),
    path('tablero_personal/',views.tablero_personal, name='tablero_personal')
]


