from __future__ import unicode_literals
from django.db import models

from .docente import Docente


class AvanceMateria(models.Model):
    id_avance = models.AutoField(primary_key=True)
    calificacion = models.IntegerField()
    periodo = models.CharField(max_length=128)
    profesor = models.ForeignKey(Docente, on_delete=models.CASCADE, default=None)
    oportunidad = models.IntegerField()
    semestre = models.IntegerField()
    clave = models.CharField(max_length=128)
    acreditado = models.BooleanField(default=True)

    def __str__(self):
        return '%s %d' % (self.calificacion, self.oportunidad)
