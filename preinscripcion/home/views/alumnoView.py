from rest_framework import viewsets

from preinscripcion.home.models import Alumno
from preinscripcion.home.utilities.serializers import AlumnoSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
