from rest_framework import viewsets

from home.models import Alumno
from home.utilities.serializers import AlumnoSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
