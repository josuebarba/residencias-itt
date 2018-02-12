from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Perfil
from preinscripcion.home.utilities.serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    # Descripcion: Obtiene todos los perfiles por el docente indicado
    # Metodos: GET
    # Parametros:
    #   pk  => ID de docente
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/perfiles/obtener_por_docente/[pk]
    @list_route(methods=['get'])
    def obtener_por_docente(self, request, pk=None):
        perfiles = self.queryset.filter(docente__id_docente=pk)
        serializer = self.serializer_class(perfiles, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los perfiles por el area indicada
    # Metodos: GET
    # Parametros:
    #   pk  => ID de area
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/perfiles/obtener_por_area/[pk]
    @list_route(methods=['get'])
    def obtener_por_area(self, request, pk=None):
        perfiles = self.queryset.filter(area__id_area=pk)
        serializer = self.serializer_class(perfiles, many=True)
        return Response(serializer.data)
