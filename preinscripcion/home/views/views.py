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

def ReadXls(request): # Recorre el archivo Excel que contiene todos los alumnos y los guarda en la base de datos.
    # file_loc = "ISC.xls"
    # df = pd.read_excel(file_loc, index_col = 0, na_values=['NA'], usecols = "A,C:AA")
    # # xlsx = pd.ExcelFile("ISC.xls")
    # print df
    xls = pd.ExcelFile("ISC2.xls")
    print(xls.sheet_names)
    df=xls.parse('x34300')
    print(df.index)

    for index, item in enumerate(df.index):
        p = Alumno(no_control=df.cc_ctr[index],password="123",semestre=df.cc_npe[index],nombre=df.cc_nom[index],status=0)
        p.save()
    return HttpResponse('200')

def addMaterias(requiest): #Recorre el archivo que contiene todas las materias y los guarda en la base de datos.
    xls = pd.ExcelFile("ISC2.xls")
    df= xls.parse("Sheet2")

    for index, item in enumerate(df.index):
        p = Materia(clave=df.Clave[index], semestre=df.Semestre[index], nombre=df.Nombre[index],creditos=df.Creditos[index],horas_teoricas=df.Teoria[index],horas_practicas=df.Practica[index],previous=df.Previous[index],next=df.Next[index])
        p.save()
    return HttpResponse('200')

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

def login(request): #Se realiza el login a la plataforma, se valida que la password sea la misma que la obtenida en la consulta
    if request.method == "POST":
        m = Alumno.objects.get(no_control=request.POST['no_control']) #Consulta la informacion del usuario ingresado
        if m.password == request.POST['password']:
            request.session['no_control'] = m.no_control
            request.session['semestre'] = m.semestre
            request.session['status'] = m.status
            request.session['nombre'] = m.nombre
            return redirect('pick_view')
        else:
            return render(request,"login.html")

#     if request.session['no_control']:
#         return redirect('pick_view')
    else:
        return render(request,"login.html")


def logout(request): # Elimina los datos de la sesion para salir de la misma.
    request.session['no_control'] = 0
    return render(request,"login.html")

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

class EspecialidadView(viewsets.ModelViewSet): #Retorna las Especialidades existentes
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

    def list(self,request):
        queryset = Especialidad.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

class MateriaView(viewsets.ModelViewSet): #Retorna las Materias existentes
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def list(self,request):
        queryset = Materia.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

class AlumnoView(viewsets.ModelViewSet): #Retorna los Alumnos existentes
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def list(self,request):
        queryset = Alumno.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

# class MateriaInfoView(viewsets.ModelViewSet):
#     queryset = MateriaInfo.objects.all()
#     serializer_class = MateriaInfoSerializer
#
#     def list(self,request):
#         queryset = MateriaInfo.Objects.all()
#         serializer = self.serializer_class(queryset,many=True)
#         return Response(serializer.data)
# class MateriaView(APIView):
#     serializer_class = MateriaSerializer

#     def get(self,request):
#         materias = Materia.objects.all()
#         response = self.serializer_class(materias,many=True)
#         return Response(response.data)
class AvanceMateriaView(viewsets.ModelViewSet): #Retorna el avance de los alumnos. De la tabla que guarda la relacion entre materias y alumnos.    queryset = AvanceMateria.objects.all()
    serializer_class = AvanceMateriaSerializer

    def list(self,request):
        queryset = AvanceMateria.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
