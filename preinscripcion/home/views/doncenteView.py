from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Docente, DocenteMateria, Materia
from preinscripcion.home.utilities.serializers import DocenteSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

    @list_route(methods=['get'])
    def get_by_materia(self, request, pk=None):
        materia = Materia.objects.get(id_materia=pk)
        docentes = DocenteMateria.objects.filter(materia=materia).values('docente')
        serializer = self.serializer_class(docentes, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_by_periodo(self, request, pk=None):
        docentes = DocenteMateria.objects.filter(periodo=pk).values('docente')
        serialier = self.serializer_class(docentes, many=True)
        return Response(serialier.data)
