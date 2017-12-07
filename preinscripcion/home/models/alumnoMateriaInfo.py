from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno
from .materiaInfo import MateriaInfo
from .avanceMateria import AvanceMateria


class AlumnoMateriaInfo(models.Model):  # Las materias que tomara el alumno
    avance = models.ForeignKey(AvanceMateria, on_delete=models.CASCADE, default=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=0)
    materia_info = models.ForeignKey(MateriaInfo, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s tomara la materia: %s' % (self.alumno.nombre, self.materia_info.nombre)
