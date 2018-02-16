from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from home.models import Materia, Docente, DocenteMateria, Perfil, MateriaArea, AlumnoMateria
from home.utilities.serializers import MateriaSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    # Descripcion: Obtiene todas las materias por el periodo que se indique
    # Metodos: POST
    # Parametros:
    #   id_docente  => ID de docente
    #   periodos    => Arreglo con los valores de los periodos
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/materias/obtener_por_periodos/
    @list_route(methods=['post'])
    def obtener_por_periodos(self, request):
        docente = Docente.objects.filter(id_docente=request.id_docente)
        materias = DocenteMateria.objects.filter(docente=docente).filter(periodo__in=request.periodos)
        serializer = self.serializer_class(materias, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todas las materias que se permiten impartir al docente indicado segun sus areas fuertes de
    # desempeno
    # Metodos: GET
    # Parametros:
    #   pk  => ID de docente
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/materias/obtener_permitidas_por_docente/[pk]
    @list_route(methods=['get'])
    def obtener_permitidas_por_docente(self, request, pk=None):
        areas = Perfil.objects.filter(docente__id_docente=pk).values('area')
        ids = areas.values_list('id_area')
        materias = MateriaArea.objects.filter(area__id_area__in=ids)
        serializer = self.serializer_class(materias, many=True)
        return Response(serializer.data)

    # Descripcion: Muestra las materias para elegir el semestre correspondiente si aun no se han elegido, de lo
    # contrario muestra las que se eligieron.
    # Metodos: POST
    # Parametros:
    #   id de alumno    => ID de alumno
    #   semestre        => Semestre actual del alumno
    #   status          => Estado del alumno (0 si no ha elegido | 1 si ya las eligio)
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/materias/obtener_permitidas_para_seleccion_alumno/
    @list_route(methods=['post'])
    def obtener_permitidas_para_seleccion_alumno(self, request):
        if request.session['status']==0: # Se muestran materias para elegir
            materias = self.queryset.filter(semestre=request.semestre+1)
        else: # Se muestran materias elegidas
            materias = AlumnoMateria.objects.raw("select home_alumnomateria.id, home_alumnomateria.materia_id,home_materia.nombre, home_materia.semestre, home_materia.creditos, home_materia.horas_teoricas, home_materia.horas_practicas from home_materia,home_alumnomateria where home_alumnomateria.alumno_id ="+ str(request.session['no_control']) +" and home_materia.id_materia = home_alumnomateria.materia_id")

        serializer = self.serializer_class(materias, many=True)
        return Response(serializer.data)
