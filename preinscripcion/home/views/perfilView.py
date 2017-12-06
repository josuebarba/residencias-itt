from rest_framework import viewsets
from preinscripcion.home.models import Perfil
from preinscripcion.home.utilities.serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
