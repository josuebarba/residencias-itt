from __future__ import unicode_literals

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from home.utilities.serializers import AlumnoMateriaInfoSerializer, EspecialidadSerializer, \
    MateriaSerializer, AlumnoSerializer, AvanceMateriaSerializer
from home.models import *
# from home.models.especialidad import Especialidad
import pandas as pd

# import xlrd
# import os
# Create your views here.
# request.session['no_control'] = 0;
# request.session['password'] = 'none';


def getCount(request): #Obtiene todas las materias que han sido solicitadas y la cantidad de solicitudes que tiene cada una, lo despliega en la vista html "series"
    lista = AlumnoMateria.objects.raw("Select home_alumnomateria.id as id, home_materia.nombre as nombre,  home_materia.clave,  home_materia.semestre, count(home_alumnomateria.materia_id) as cuenta from home_materia, home_alumnomateria where home_materia.id_materia = home_alumnomateria.materia_id group by home_alumnomateria.materia_id order by home_materia.semestre")

    context = {
    "object_list" : lista,
    }

    return render(request,'series.html',context)


def materiasPost(request): #Inserta en la tabla relacional los registros correspondietes, siendo las materias solicitadas por los alumnos, en la tabla home_alumnomateria
    row =''
    b=0
    if request.method == "POST":
        print (request.session['status'])
        if request.session['status'] == 0:
            materias = request.POST.get('materias')
            res = materias.split(',')
            for o in res:
                with connection.cursor() as cursor:
                    cursor.execute("insert into home_alumnomateria(materia_id,alumno_id) values ("+str(o)+","+str(request.session['no_control'])+")")
                    row = cursor.fetchall()
                    b=1
            with connection.cursor() as cursor:
                cursor.execute("update home_alumno set status = 1 where no_control ="+str(request.session['no_control']))
                request.session['status'] = 1
    if(b==1):
        return HttpResponse('200')
    else:
        return HttpResponse('201')

    # return render(request,"pick.html",{"rows":row})



def pick(request): #Muestra las materias para elegir el semestre correspondiente si aun no se han elegido, de lo contrario muestra las que se eligieron.
    flag=False;
    if(request.session['status']==0):           #Se muestran materias para elegir
        listaPre = Materia.objects.all()
        sem = request.session['semestre'] + 1
        lista = listaPre.filter(semestre=sem)
        flag=False
    else:                                       #Se muestran materias elegidas
        lista = AlumnoMateria.objects.raw("select home_alumnomateria.id, home_alumnomateria.materia_id,home_materia.nombre, home_materia.semestre, home_materia.creditos, home_materia.horas_teoricas, home_materia.horas_practicas from home_materia,home_alumnomateria where home_alumnomateria.alumno_id ="+ str(request.session['no_control']) +" and home_materia.id_materia = home_alumnomateria.materia_id")
        flag=True

    context= {
        "object_list": lista,
        "nombre": request.session['nombre'],
        "status": flag
    }
    return render(request,'pick.html',context)

class CountViewSet(viewsets.ModelViewSet): #Se obtiene la cantidad de solicitudes que tiene cada materia.
    queryset = AlumnoMateria.objects.raw('Select home_materia.id_materia, home_materia.nombre, count(home_alumnomateria.materia_id) as materia_count from home_materia, home_alumnomateria where home_materia.id_materia = home_alumnomateria.materia_id group by home_alumnomateria.materia_id')
    serializer_class = AlumnoMateriaInfoSerializer

    def list(self,request):
        queryset = AlumnoMateria.objects.raw('Select home_alumnomateria.id as id, home_materia.nombre as nombre, count(home_alumnomateria.materia_id) as cuenta from home_materia, home_alumnomateria where home_materia.id_materia = home_alumnomateria.materia_id group by home_alumnomateria.materia_id')
        # queryset = AlumnoMateriaInfo.objects.all()
        serializer = AlumnoMateriaInfoSerializer(queryset, many=True)
        return Response(serializer.data)
