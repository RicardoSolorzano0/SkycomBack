from rest_framework import serializers
from .models import Profesor, Alumno, Materia, Nota

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
        
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    profesor_nombre = serializers.SerializerMethodField()
    class Meta:
        model = Materia
        fields = ["id", "nombre", "profesor", "profesor_nombre"]
        
    def get_profesor_nombre(self, obj):
        return obj.profesor.nombre

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        