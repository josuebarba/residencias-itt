from __future__ import unicode_literals
from django.db import models


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.descripcion
