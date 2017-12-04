from __future__ import unicode_literals
from django.db import models

from .alumno import Alumno


class Kardex(models.Model):
    no_control = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    avance = models.IntegerField(default=0)

    def __str__(self):
        return '%d - %d' % (self.no_control.no_control, self.avance)
