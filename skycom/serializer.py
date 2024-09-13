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
        fields = ["id","alumno", "materia", "nota", "tipo_evaluacion"]

    #validacion personalizada para limitar las notas por alumno y materia
    def validate(self, data):
        alumno= data["alumno"]
        materia= data["materia"]
        
        #contar cuantas notas existen ya para este alumno y materia
        notas_existentes = Nota.objects.filter(alumno=alumno, materia=materia).count()
        
        if notas_existentes >= 3:
            raise serializers.ValidationError("Ya existen 3 notas para este alumno y materia")
        return data