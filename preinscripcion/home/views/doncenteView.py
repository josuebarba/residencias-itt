from rest_framework import viewsets
from preinscripcion.home.models import Docente
from preinscripcion.home.utilities.serializers import DocenteSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
