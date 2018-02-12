from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from preinscripcion.home.models import Disponibilidad
from preinscripcion.home.utilities.serializers import DisponibilidadSerializer


class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    @list_route(methods=['get'])
    def get_by_docente(self, request, pk=None):
        disponibilidad = self.queryset.filter(docente__id_docente=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_by_dia_semana(self, request, pk=None):
        disponibilidad = self.queryset.filter(dia_semana=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_by_hora_comienzo(self, request, pk=None):
        disponibilidad = self.queryset.filter(hora_comienzo=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def get_by_hora_final(self, request, pk=None):
        disponibilidad = self.queryset.filter(hora_final=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def get_by_rango_hora(self, request):
        disponibilidad = self.queryset.filter(hora_comienzo=request.hora_comienzo).filter(hora_final=request.hora_final)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)
