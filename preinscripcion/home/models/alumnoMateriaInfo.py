from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno
from .materiaInfo import MateriaInfo


class AlumnoMateriaInfo(models.Model):  # Las materias que tomara el alumno
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=0)
    materia_info = models.ForeignKey(MateriaInfo, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s tomara la materia: %s' % (self.alumno.nombre, self.materia_info.nombre)
