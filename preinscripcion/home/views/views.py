from __future__ import unicode_literals

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from preinscripcion.home.utilities.serializers import AlumnoMateriaInfoSerializer, EspecialidadSerializer, \
    MateriaInfoSerializer, MateriaSerializer, AlumnoSerializer, AvanceMateriaSerializer
from preinscripcion.home.models import AlumnoMateriaInfo, Especialidad, MateriaInfo, Materia, Alumno, AvanceMateria


# import xlrd
# import os
# Create your views here.
# request.session['no_control'] = 0;
# request.session['password'] = 'none';

# def ReadXls(request):
#     workbook = xlrd.open_workbook('ISC.xls', logfile=open(os.devnull, 'w'))
#     worksheet = workbook.sheet_by_index(0)
#     print worksheet.cell(0,0).value

def materiasPost(request):
    row =''
    b=0
    if request.method == "POST":
        print (request.session['status'])
        if request.session['status'] == 0:
            materias = request.POST.get('materias')
            res = materias.split(',')
            for o in res:
                with connection.cursor() as cursor:
                    cursor.execute("insert into home_alumnomateriainfo(id_materia_id,no_control_id) values ("+str(o)+","+str(request.session['no_control'])+")")
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

def login(request):
    if request.method == "POST":
        m = Alumno.objects.get(no_control=request.POST['no_control'])
        if m.password == request.POST['password']:
            request.session['no_control'] = m.no_control
            request.session['semestre'] = m.semestre
            request.session['status'] = m.status
            request.session['nombre'] = m.nombre
            request.session['ap_pat'] = m.ap_pat
            return redirect('pick_view')
        else:
            return render(request,"login.html")

#     if request.session['no_control']:
#         return redirect('pick_view')
    else:
        return render(request,"login.html")


def logout(request):
    request.session['no_control'] = 0
    return render(request,"login.html")

def pick(request):
    flag=False;
    if(request.session['status']==0):           #Se muestran materias para elegir
        listaPre = MateriaInfo.objects.all()
        sem = request.session['semestre'] + 1
        lista = listaPre.filter(semestre=sem)
        flag=False
    else:                                       #Se muestran materias elegidas
        lista = AlumnoMateriaInfo.objects.raw("select home_alumnomateriainfo.id, home_alumnomateriainfo.id_materia_id,home_materiainfo.nombre, home_materiainfo.semestre, home_materiainfo.creditos, home_materiainfo.horasTeoria, home_materiainfo.horasPractica from home_materiainfo,home_alumnomateriainfo where no_control_id ="+ str(request.session['no_control']) +" and home_materiainfo.id_materia = home_alumnomateriainfo.id_materia_id")
        flag=True

    context= {
        "object_list": lista,
        "nombre": request.session['nombre'] +' '+request.session['ap_pat'],
        "status": flag
    }
    return render(request,'pick.html',context)

class CountViewSet(viewsets.ModelViewSet):
    queryset = AlumnoMateriaInfo.objects.raw('Select home_materiainfo.id_materia, home_materiainfo.nombre, count(home_alumnomateriainfo.id_materia_id) as materia_count from home_materiainfo, home_alumnomateriainfo where home_materiainfo.id_materia = home_alumnomateriainfo.id_materia_id group by home_alumnomateriainfo.id_materia_id')
    serializer_class = AlumnoMateriaInfoSerializer

    def list(self,request):
        queryset = AlumnoMateriaInfo.objects.raw('Select home_alumnomateriainfo.id as id, home_materiainfo.nombre as nombre, count(home_alumnomateriainfo.id_materia_id) as cuenta from home_materiainfo, home_alumnomateriainfo where home_materiainfo.id_materia = home_alumnomateriainfo.id_materia_id group by home_alumnomateriainfo.id_materia_id')
        # queryset = AlumnoMateriaInfo.objects.all()
        serializer = AlumnoMateriaInfoSerializer(queryset, many=True)
        return Response(serializer.data)

class EspecialidadView(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

    def list(self,request):
        queryset = Especialidad.Objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
class MateriaInfoView(viewsets.ModelViewSet):
    queryset = MateriaInfo.objects.all()
    serializer_class = MateriaInfoSerializer

    def list(self,request):
        queryset = MateriaInfo.Objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
class AlumnoView(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def list(self,request):
        queryset = Alumno.Objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

class MateriaInfoView(viewsets.ModelViewSet):
    queryset = MateriaInfo.objects.all()
    serializer_class = MateriaInfoSerializer

    def list(self,request):
        queryset = MateriaInfo.Objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
# class MateriaView(APIView):
#     serializer_class = MateriaSerializer

#     def get(self,request):
#         materias = Materia.objects.all()
#         response = self.serializer_class(materias,many=True)
#         return Response(response.data)
class AvanceMateriaView(viewsets.ModelViewSet):
    queryset = AvanceMateria.objects.all()
    serializer_class = AvanceMateriaSerializer

    def list(self,request):
        queryset = AvanceMateria.Objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)


