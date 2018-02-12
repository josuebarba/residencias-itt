from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Materia, Docente, DocenteMateria, Perfil, MateriaArea
from preinscripcion.home.utilities.serializers import MateriaSerializer


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
