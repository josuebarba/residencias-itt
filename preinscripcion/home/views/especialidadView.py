from rest_framework import viewsets

from preinscripcion.home.models import Especialidad
from preinscripcion.home.utilities.serializers import EspecialidadSerializer


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer