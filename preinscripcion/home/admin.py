from __future__ import unicode_literals
from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Area)
admin.site.register(Evidencia)
admin.site.register(Especialidad)

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Carrera)

admin.site.register(MateriaInfo)
admin.site.register(AvanceMateria)
admin.site.register(Kardex)
admin.site.register(Disponibilidad)
admin.site.register(Perfil)

admin.site.register(AlumnoMateriaInfo)
admin.site.register(DocenteMateria)
admin.site.register(MateriaCarrera)
admin.site.register(MateriaArea)
