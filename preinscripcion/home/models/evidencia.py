from __future__ import unicode_literals
from django.db import models


class Evidencia(models.Model):
    id_evidencia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.descripcion
