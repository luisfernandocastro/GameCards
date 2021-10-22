from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User= get_user_model()

# Register your models here.


# admin.site.register(Sala)

# class SalaAdmin(admin.ModelAdmin):
# pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    search_fields = ['username']
    # list_editable = ['nombre']
    list_filter = ['email']
    list_per_page = 10
    pass



@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre')
    list_display = ('nombre',)
    search_fields = ['nombre']
    # list_editable = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    pass


@admin.register(Error)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre','imagen')
    list_display = ('nombre',)
    search_fields = ['nombre']
    # list_editable = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    pass

@admin.register (Programador)
class ProgramadorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    pass


@admin.register (Jugadores)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    search_fields = ['nombre']
    # list_editable = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10
    pass


@admin.register (Categoria)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('programador', 'modulo','error')
    search_fields = ['programador']
    # list_editable = ['nombre']
    list_filter = ['programador']
    list_per_page = 10
    pass


@admin.register (Cartas)
class CartaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    # list_editable = ['nombre']    
    list_filter = ['nombre']
    list_per_page = 10
    pass



