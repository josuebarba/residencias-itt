from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno
from .materiaInfo import MateriaInfo


class AlumnoMateriaInfo(models.Model): #Las materias que tomara el alumno
    no_control = models.ForeignKey(Alumno, on_delete=models.CASCADE,default=0)
    id_materia = models.ForeignKey(MateriaInfo, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.no_control.nombre + ' tomara la materia: ' + self.id_materia.nombre
