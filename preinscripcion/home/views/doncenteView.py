from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from home.models import Docente, DocenteMateria, Materia
from home.utilities.serializers import DocenteSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

    # Descripcion: Obtiene todos los docentes por la materia que se indique
    # Metodos: GET
    # Parametros:
    #   pk  => ID de materia
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/docentes/obtener_por_materia/[pk]
    @list_route(methods=['get'])
    def obtener_por_materia(self, request, pk=None):
        materia = Materia.objects.get(id_materia=pk)
        docentes = DocenteMateria.objects.filter(materia=materia).values('docente')
        serializer = self.serializer_class(docentes, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los docentes por el periodo que se indique
    # Metodos: GET
    # Parametros:
    #   pk  => ID de periodo
    # Url: http://[IP|DOMINIO]:[PUERTO]/api/docentes/obtener_por_periodo/[pk]
    @list_route(methods=['get'])
    def obtener_por_periodo(self, request, pk=None):
        docentes = DocenteMateria.objects.filter(periodo=pk).values('docente')
        serialier = self.serializer_class(docentes, many=True)
        return Response(serialier.data)
