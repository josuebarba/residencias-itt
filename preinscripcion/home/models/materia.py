from __future__ import unicode_literals
from django.db import models


class Materia(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    clave = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128, default='')
    periodo = models.CharField(max_length=128)
    profesor = models.CharField(max_length=128)

    def __str__(self):
        return '[%s] %s %s - %s' % (self.periodo, self.clave, self.nombre, self.profesor)
