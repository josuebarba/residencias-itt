from __future__ import unicode_literals
from django.db import models

from .carrera import Carrera
from .materia import Materia


class MateriaCarrera(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s pertenece a la carrera: %s' % (self.materia.nombre, self.carrera.nombre)
