
from django.contrib import admin
from django.urls import path
from core.principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('tablero/',views.tablero,name='tablero'),
    path('sala/', views.sala, name='sala'),
    path('tablero_personal/',views.tablero_personal, name='tablero_personal')
]


