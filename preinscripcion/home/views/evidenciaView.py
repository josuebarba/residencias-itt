from rest_framework import viewsets

from home.models import Evidencia
from home.utilities.serializers import EvidenciaSerializer


class EvidenciaViewSet(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer