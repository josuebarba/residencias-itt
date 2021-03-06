from __future__ import unicode_literals
from django.db import models

from .docente import Docente
from .materia import Materia


class DocenteMateria(models.Model):
    periodo = models.IntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s - %s (%s)' % (self.docente.nombre, self.docente.apellido_paterno,
                                       self.docente.apellido_materno, self.materia.nombre, self.periodo)
