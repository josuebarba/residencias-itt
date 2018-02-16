from django.db import connection
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from home.models import AlumnoMateria
from home.utilities.serializers import AlumnoMateriaInfoSerializer


class AlumnoMateriaViewSet(viewsets.ModelViewSet):
    queryset = AlumnoMateria.objects.all()
    serializer_class = AlumnoMateriaInfoSerializer

    # Descripcion: Inserta en la tabla relacional los registros correspondietes, siendo las materias solicitadas por
    # los alumnos, en la tabla home_alumnomateria.
    # Metodos: POST
    # Parametros:
    #   ?
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/materias/insertar_multiples_registros/
    def insertar_multiples_registros(self, request):
        row = ''
        b = 0
        if request.method == "POST":
            print (request.session['status'])
            if request.session['status'] == 0:
                materias = request.POST.get('materias')
                res = materias.split(',')
                for o in res:
                    with connection.cursor() as cursor:
                        cursor.execute("insert into home_alumnomateria(materia_id,alumno_id) values (" + str(o) + "," + str(request.session['no_control']) + ")")
                        row = cursor.fetchall()
                        b = 1
                with connection.cursor() as cursor:
                    cursor.execute("update home_alumno set status = 1 where no_control =" + str(request.session['no_control']))
                    request.session['status'] = 1
        if b == 1:
            return HttpResponse('200')
        else:
            return HttpResponse('201')

    # Descripcion: Se obtiene la cantidad de solicitudes que tiene cada materia.
    # Metodos: POST
    # Parametros:
    #   ?
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/materias/obtener_cantidad_solicitudes/
    @list_route(methods=['post'])
    def obtener_cantidad_solicitudes(self, request):
        queryset = AlumnoMateria.objects.raw('Select home_alumnomateria.id as id, home_materia.nombre as nombre, count(home_alumnomateria.materia_id) as cuenta from home_materia, home_alumnomateria where home_materia.id_materia = home_alumnomateria.materia_id group by home_alumnomateria.materia_id')
        serializer = AlumnoMateriaInfoSerializer(queryset, many=True)
        return Response(serializer.data)
