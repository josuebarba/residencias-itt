from __future__ import unicode_literals
from django.db import models

from .especialidad import Especialidad


class MateriaInfo(models.Model):
    id_materia = models.AutoField(primary_key=True)
    # id_reticula se removio
    clave = models.CharField(max_length=128)
    semestre = models.IntegerField(default=0)
    nombre = models.CharField(max_length=128)
    creditos = models.IntegerField()
    horasPractica = models.IntegerField()
    horasTeoria = models.IntegerField()
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, default=0)
    previous = models.IntegerField(default=0)  # guarda el id de la materia previa a esta
    next = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
