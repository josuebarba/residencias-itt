from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno
from .materia import Materia
from .avanceMateria import AvanceMateria


class AlumnoMateria(models.Model):
    avance = models.ForeignKey(AvanceMateria, on_delete=models.CASCADE, default=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=0)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s - %s' % (self.alumno.nombre, self.materia.nombre)
