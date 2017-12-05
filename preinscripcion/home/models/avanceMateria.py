from __future__ import unicode_literals
from django.db import models

from .materia import Materia
from .materiaInfo import MateriaInfo
from .alumno import Alumno


class AvanceMateria(models.Model):
    id_avance = models.AutoField(primary_key=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)  # materia con profesor y calif
    materia_info = models.ForeignKey(MateriaInfo, on_delete=models.CASCADE, default=0)  # materia con la informacion para validar;;;;;;; & previous ==AvanceMateria.id_materiainfo entonces ya la paso y muestra la materia
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=0)
    calificacion = models.IntegerField()
    # periodo = models.CharField(max_length=128)
    # profesor = models.CharField(max_length=128) #Este debe ser un id_profesor pero no es relevante por el momento
    oportunidad = models.IntegerField()
    semestre = models.IntegerField()
    # clave = models.CharField(max_length=128)
    intentos = models.IntegerField(default=0)
    pasado = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s --> %s' % (self.alumno.nombre, self.alumno.ap_pat, self.materia.nombre)