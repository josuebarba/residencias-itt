from __future__ import unicode_literals
from django.db import models


class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    apellido_paterno = models.CharField(max_length=250)
    apellido_materno = models.CharField(max_length=250)
    no_empleado = models.CharField(max_length=250)
    plaza = models.CharField(max_length=250)
    correo_electronico = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    carrera = models.CharField(max_length=250)
    nivel_de_estudios = models.CharField(max_length=250)
    especialidad = models.CharField(max_length=250)

    def __str__(self):
        return '%s - %s %s %s' % (self.no_empleado, self.nombre, self.apellido_paterno, self.apellido_materno)
