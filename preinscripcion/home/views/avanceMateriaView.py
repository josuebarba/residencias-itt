from rest_framework import viewsets

from home.models import AvanceMateria
from home.utilities.serializers import AvanceMateriaSerializer


class AvanceMateriaViewSet(viewsets.ModelViewSet):
    queryset = AvanceMateria.objects.all()
    serializer_class = AvanceMateriaSerializer