from rest_framework import serializers
from home.models import *


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"


class AlumnoMateriaInfoSerializer(serializers.Serializer):
    # materia_count = serializers.SerializerMethodField()
    # print materia_count
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=128)
    cuenta = serializers.IntegerField()

    # class Meta:
    #     model = AlumnoMateriaInfo
    #     fields = ('id','id_materia','nombre','materia_count')
    # def get_id_materia_count(self, obj):
    #         return obj.user_set.count()


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


# class MateriaInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MateriaInfo
#         fields = "__all__"


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"
