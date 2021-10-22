from django.contrib.admin.sites import DefaultAdminSite
from django.db import models

#modelo de la base de datos 

# modelo jugadores recibe datos de nombre de tipo texto y estado de tipo bool
class Jugadores(models.Model):
    nombre = models.CharField(max_length=100,null=True) # Turnos
    estado = models.BooleanField(default='True',null=True)

#renombrar tabla
    class Meta:
        verbose_name_plural = 'Jugadores'

#modelo para tabla cartas recibe datos de nombre de tipo texto y image donde se cargan la imagenes en la carpeta cartas
class Cartas(models.Model):
    nombre = models.CharField(max_length=100,null=True) # Turnos
    image = models.ImageField(upload_to="cartas",null=True,default=None)


#renombrar la tabla cartas 
    class Meta:
        verbose_name_plural = 'Cartas'


    
#modelo para tabla cartegoria con la relacion con las tablas programador,modulo,error
class Categoria(models.Model): # Imagenes 
    programador = models.ForeignKey('Programador', models.DO_NOTHING, db_column='Programador',default=None)  
    modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='Modulo',default=None)  
    error = models.ForeignKey('Error', models.DO_NOTHING, db_column='Error',default=None)  

#renombrar la tabla categoria
    class Meta:
        verbose_name_plural = 'Categoria'

#modelo programador recibe datos de nombre de tipo texto image donde se cargan las imagenes en la programadores
class Programador(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="programadores",null=True,default=None)
#renombrar la tabla programadores 
    class Meta:
        verbose_name_plural = 'Programador'
#modelo modulo recibe los datos de nombre de tipo texto image donde se encarga las imagenes en la carpeta modulos
class Modulo(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="modulos",null=True,default=None)
#renombrar la tabla modulo
    class Meta:
        verbose_name_plural = 'Modulo'
#modelo error donde recibe el nombre de tipo texto image donde se cargan las imagenes en la carpeta errores
class Error(models.Model):
    nombre = models.CharField(max_length=100,default=None,null=True)
    image = models.ImageField(upload_to="errores",null=True,default=None)

    class Meta:
        verbose_name_plural = 'Error'
    
#modelo codigo donde recibe el nombre de tipo texto con una maximo de 5 caracteres alfanumericos
class Code(models.Model):
    nombre = models.CharField(max_length=5,null=True)
