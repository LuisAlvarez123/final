from django.contrib import admin
from .models import *

# Register your models here. 
class AlumnosAdmin(admin.ModelAdmin):
    fields = ('nombre', 'apellido',)

class CursosAdmin(admin.ModelAdmin):
    fields = ('nombre',)

class AsignacionAdmin(admin.ModelAdmin):
    fields = ('alumnos', 'cursos', 'fecha_asignacion',)

admin.site.register(Alumnos, AlumnosAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Asignacion, AsignacionAdmin)