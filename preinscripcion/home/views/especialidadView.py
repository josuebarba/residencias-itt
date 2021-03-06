from rest_framework import viewsets

from home.models import Especialidad
from home.utilities.serializers import EspecialidadSerializer


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer