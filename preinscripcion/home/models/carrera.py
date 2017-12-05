from __future__ import unicode_literals
from django.db import models


class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.nombre