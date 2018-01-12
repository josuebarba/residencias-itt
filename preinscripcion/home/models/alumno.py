from __future__ import unicode_literals
from django.db import models


class Alumno(models.Model):
    no_control = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=64, default=123)
    semestre = models.IntegerField(default=1)
    nombre = models.CharField(max_length=128)
    apellido_paterno = models.CharField(max_length=128)
    apellido_materno = models.CharField(max_length=128)
    status = models.IntegerField(default=0)

    def __str__(self):
        return '%d - %s %s %s' % (self.no_control, self.nombre, self.apellido_paterno, self.apellido_materno)
