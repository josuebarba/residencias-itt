from __future__ import unicode_literals
from django.db import models

from .docente import Docente


class Disponibilidad(models.Model):
    id_disponibilidad = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=250)
    ano = models.IntegerField()
    dia_semana = models.IntegerField()
    hora_comienzo = models.IntegerField()
    hora_final = models.IntegerField()
    fecha_de_devolucion = models.DateField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s: %s %d:00 - %d:00' % (self.docente.nombre, self.docente.apellido_paterno,
                                               self.docente.apellido_materno, self.dia_semana, self.hora_comienzo,
                                               self.hora_final)
