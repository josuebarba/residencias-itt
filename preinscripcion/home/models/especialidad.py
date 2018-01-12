from __future__ import unicode_literals
from django.db import models


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return '%s' % self.nombre
