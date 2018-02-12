from rest_framework import viewsets

from preinscripcion.home.models import AvanceMateria
from preinscripcion.home.utilities.serializers import AvanceMateriaSerializer


class AvanceMateriaViewSet(viewsets.ModelViewSet):
    queryset = AvanceMateria.objects.all()
    serializer_class = AvanceMateriaSerializer