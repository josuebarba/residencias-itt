from rest_framework import viewsets

from home.models import Area
from home.utilities.serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer