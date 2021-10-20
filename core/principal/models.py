from django.db import models

# Create your models here.

class Sala(models.Model):
    asignarsala = models.CharField(max_length=100,null=True) # #Generar el codigo


class Jugadores(models.Model):
    jugador = models.CharField(max_length=100,null=True) # Turnos

    

class Categoria(models.Model): # Imagenes 
    image_programador=models.ImageField(upload_to="programadores")
    image_modulo=models.ImageField(upload_to="modulo")
    image_error=models.ImageField(upload_to="error")
