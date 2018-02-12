from rest_framework import viewsets

from preinscripcion.home.models import Area
from preinscripcion.home.utilities.serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer