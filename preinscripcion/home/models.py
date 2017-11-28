# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class MateriaInfo(models.Model):
    id_materia = models.AutoField(primary_key = True)
    #id_reticula se removio
    clave = models.CharField(max_length=128)
    semestre = models.IntegerField(default=0)
    nombre = models.CharField(max_length=128)
    creditos = models.IntegerField()
    horasPractica = models.IntegerField()
    horasTeoria = models.IntegerField()
    id_especialidad = models.ForeignKey(Especialidad, on_delete= models.CASCADE, default=0)
    previous = models.IntegerField(default = 0) #guarda el id de la materia previa a esta
    next = models.IntegerField(default = 0)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    clave = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128,default = '')
    periodo = models.CharField(max_length=128)
    profesor = models.CharField(max_length=128)
    clave = models.CharField(max_length=128)

    def __str__(self):
        return '[ ' +self.periodo +' ] ' + self.nombre +' '+ self.clave +' '+ self.profesor

class Alumno(models.Model):
    no_control = models.IntegerField(primary_key = True)
    password = models.CharField(max_length=64, default=123)
    semestre = models.IntegerField(default=1)
    nombre = models.CharField(max_length=128)
    ap_pat = models.CharField(max_length=128)
    ap_mat = models.CharField(max_length=128)
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.nombre +' '+ self.ap_pat

class AlumnoMateriaInfo(models.Model): #Las materias que tomara el alumno
    no_control = models.ForeignKey(Alumno, on_delete=models.CASCADE,default=0)
    id_materia = models.ForeignKey(MateriaInfo, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.no_control.nombre + ' tomara la materia: ' + self.id_materia.nombre

class AvanceMateria(models.Model):
    id_materia = models.ForeignKey(Materia,on_delete=models.CASCADE,default=0) #materia con profesor y calif
    id_materiainfo = models.ForeignKey(MateriaInfo,on_delete=models.CASCADE,default=0) #materia con la informacion para validar;;;;;;; & previous ==AvanceMateria.id_materiainfo entonces ya la paso y muestra la materia
    no_control = models.ForeignKey(Alumno, on_delete=models.CASCADE,default=0)
    calificacion = models.IntegerField()
    #periodo = models.CharField(max_length=128)
    #profesor = models.CharField(max_length=128) #Este debe ser un id_profesor pero no es relevante por el momento
    oportunidad = models.IntegerField()
    semestre = models.IntegerField()
    #clave = models.CharField(max_length=128)
    intentos = models.IntegerField(default=0)
    pasado = models.BooleanField(default=True)

    def __str__(self):
        return self.no_control.nombre + self.no_control.ap_pat +' --> '+ self.id_materia.nombre

class Kardex(models.Model):
    no_control = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    avance = models.IntegerField(default=0)
