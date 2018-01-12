from __future__ import unicode_literals
from django.db import models

from .materia import Materia
from .area import Area


class MateriaArea(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '%s pertenece al area de: %s' % (self.materia.nombre, self.area.nombre)
