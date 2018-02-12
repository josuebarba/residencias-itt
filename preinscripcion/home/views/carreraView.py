from rest_framework import viewsets

from preinscripcion.home.models import Carrera
from preinscripcion.home.utilities.serializers import CarreraSerializer


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer