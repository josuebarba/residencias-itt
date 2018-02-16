from rest_framework import serializers
from home.models import *


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"


class AlumnoMateriaInfoSerializer(serializers.Serializer):
    class Meta:
        model = AlumnoMateria
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class AvanceMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvanceMateria
        fields = "__all__"


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = "__all__"


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = "__all__"


class DocenteMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocenteMateria
        fields = "__all__"


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = "__all__"


class EvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencia
        fields = "__all__"


class KardexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kardex
        fields = "__all__"


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"


class MateriaAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaArea
        fields = "__all__"


class MateriaCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaCarrera
        fields = "__all__"


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"
