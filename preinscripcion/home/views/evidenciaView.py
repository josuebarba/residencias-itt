from rest_framework import viewsets

from preinscripcion.home.models import Evidencia
from preinscripcion.home.utilities.serializers import EvidenciaSerializer


class EvidenciaViewSet(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer