# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Alumno,Especialidad,Materia, AvanceMateria, MateriaInfo, Kardex, AlumnoMateriaInfo
# Register your models here.
admin.site.register(Alumno)
admin.site.register(AvanceMateria)
admin.site.register(MateriaInfo)
admin.site.register(Kardex)
admin.site.register(Especialidad)
admin.site.register(Materia)
admin.site.register(AlumnoMateriaInfo)
