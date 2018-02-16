from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from home.models import Disponibilidad
from home.utilities.serializers import DisponibilidadSerializer


class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer

    # Descripcion: Obtiene todos los registros de horarios por docente indicado
    # Metodos: GET
    # Parametros:
    #   pk  => ID de docente
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/disponibilidad/obtener_por_docente/[pk]
    @list_route(methods=['get'], url_path='obtener_por_docente/(?P<pk>[^/.]+)')
    def obtener_por_docente(self, request, pk=None):
        disponibilidad = self.queryset.filter(docente__id_docente=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los registros de horarios por dia de la semana indicado
    # Metodos: GET
    # Parametros:
    #   pk  => Valor numerico de dia de la semana (1 - 7)
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/disponibilidad/obtener_por_dia_semana/[pk]
    @list_route(methods=['get'], url_path='obtener_por_dia_semana/(?P<pk>[^/.]+)')
    def obtener_por_dia_semana(self, request, pk=None):
        disponibilidad = self.queryset.filter(dia_semana=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los registros de horarios por hora de comienzo de disponibilidad indicado
    # Metodos: GET
    # Parametros:
    #   pk  => Valor numerico de hora de comienzo (0 - 23)
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/disponibilidad/obtener_por_hora_comienzo/[pk]
    @list_route(methods=['get'], url_path='obtener_por_hora_comienzo/(?P<pk>[^/.]+)')
    def obtener_por_hora_comienzo(self, request, pk=None):
        disponibilidad = self.queryset.filter(hora_comienzo=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los registros de horarios por hora final de disponibilidad indicado
    # Metodos: GET
    # Parametros:
    #   pk  => Valor numerico de hora final (0 - 23)
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/disponibilidad/obtener_por_hora_final/[pk]
    @list_route(methods=['get'], url_path='obtener_por_hora_final/(?P<pk>[^/.]+)')
    def obtener_por_hora_final(self, request, pk=None):
        disponibilidad = self.queryset.filter(hora_final=pk)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)

    # Descripcion: Obtiene todos los registros de horarios por rango de horas
    # Metodos: POST
    # Parametros:
    #   hora_comienzo   => Valor numerico de hora de comienzo (0 - 23)
    #   hora_final      => Valor numerico de hora final (0 - 23)
    # URL: http://[IP|DOMINIO]:[PUERTO]/api/disponibilidad/obtener_por_rango_hora/
    @list_route(methods=['post'], url_path='obtener_por_rango_hora')
    def obtener_por_rango_hora(self, request):
        disponibilidad = self.queryset.filter(hora_comienzo=request.hora_comienzo).filter(hora_final=request.hora_final)
        serializer = self.serializer_class(disponibilidad, many=True)
        return Response(serializer.data)
