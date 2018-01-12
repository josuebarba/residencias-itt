from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno


class Kardex(models.Model):
    id_kardex = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    avance = models.IntegerField(default=0)

    def __str__(self):
        return '%d - %d' % (self.alumno.no_control, self.avance)
