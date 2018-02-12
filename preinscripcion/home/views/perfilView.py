from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Perfil
from preinscripcion.home.utilities.serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    @list_route(methods=['get'])
    def get_by_docente(self, request, pk=None):
        perfiles = self.queryset.filter(docente__id_docente=pk)
        serializer = self.serializer_class(perfiles, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_by_area(self, request, pk=None):
        perfiles = self.queryset.filter(area__id_area__in=pk)
        serializer = self.serializer_class(perfiles, many=True)
        return Response(serializer.data)
