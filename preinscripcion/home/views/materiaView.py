from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Materia, Docente, DocenteMateria, Perfil, MateriaArea
from preinscripcion.home.utilities.serializers import MateriaSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    @list_route(methods=['post'])
    def get_by_periodos(self, request):
        docente = Docente.objects.filter(id_docente=request.id_docente)
        materias = DocenteMateria.objects.filter(docente=docente).filter(periodo__in=request.periodos)
        serializer = self.serializer_class(materias, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_allowed_by_docente(self, request, pk=None):
        areas = Perfil.objects.filter(docente__id_docente=pk).values('area')
        ids = areas.values_list('id_area')
        materias = MateriaArea.objects.filter(area__id_area__in=ids)
        serializer = self.serializer_class(materias, many=True)
        return Response(serializer.data)
