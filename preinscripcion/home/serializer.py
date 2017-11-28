from rest_framework import serializers
from .models import Alumno,Especialidad,Materia, AvanceMateria, MateriaInfo, Kardex, AlumnoMateriaInfo

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
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = "__all__"

class MateriaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaInfo
        fields = "__all__"

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"

class AvanceMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvanceMateria
        fields = "__all__"
