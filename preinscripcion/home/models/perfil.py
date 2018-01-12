from __future__ import unicode_literals
from django.db import models

from .area import Area
from .evidencia import Evidencia
from .docente import Docente


class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s (%s): %s' % (self.docente.nombre, self.docente.apellido_paterno, self.docente.apellido_materno,
                                      self.area.descripcion, self.descripcion)
