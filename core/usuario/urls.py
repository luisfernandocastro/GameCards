from django.urls import path
from core.usuario import views

urlpatterns = [
    path('accounts/login',views.Login.as_view(),name='login'),
    path('registro/',views.registrarse,name='registro')
]