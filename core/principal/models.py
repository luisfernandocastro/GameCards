from django.contrib.admin.sites import DefaultAdminSite
from django.db import models

# Create your models here.


class Jugadores(models.Model):
    nombre = models.CharField(max_length=100,null=True) # Turnos
    estado = models.BooleanField(default='True',null=True)


    class Meta:
        verbose_name_plural = 'Jugadores'

    

class Categoria(models.Model): # Imagenes 
    programador = models.ForeignKey('Programador', models.DO_NOTHING, db_column='Programador',default=None)  
    modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='Modulo',default=None)  
    error = models.ForeignKey('Error', models.DO_NOTHING, db_column='Error',default=None)  


    class Meta:
        verbose_name_plural = 'Categoria'


class Programador(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="programadores",null=True,default=None)

    class Meta:
        verbose_name_plural = 'Programador'

class Modulo(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="modulos",null=True,default=None)

    class Meta:
        verbose_name_plural = 'Modulo'

class Error(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="errores",null=True,default=None)

    class Meta:
        verbose_name_plural = 'Error'
    

class Code(models.Model):
    nombre = models.CharField(max_length=5,null=True)
