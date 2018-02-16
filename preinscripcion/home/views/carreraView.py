from rest_framework import viewsets

from home.models import Carrera
from home.utilities.serializers import CarreraSerializer


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer