from rest_framework import viewsets
from preinscripcion.home.models import Disponibilidad
from preinscripcion.home.utilities.serializers import DisponibilidadSerializer


class DisponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    serializer_class = DisponibilidadSerializer
