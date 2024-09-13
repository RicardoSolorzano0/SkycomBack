from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Avg,Count
from .serializer import ProfesorSerializer, AlumnoSerializer, MateriaSerializer, NotaSerializer
from .models import Profesor, Alumno, Materia, Nota

# Create your views here.

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    # Generar reporte de alumnos que aprobaron o repobaron cada materia
    @action(detail=False, methods=['get'])
    def reporte_aprobados_reprobados(self, request):
        # Agrupar por alumno y materia, calcular el promedio
        notas_promedio= Nota.objects.values('alumno', 'materia').annotate(
            count_notas=Count('id'),
            promedio=Avg('nota')
        )
        
        resultados = []
        
        # Iterar sobre las notas promedios
        for nota in notas_promedio:
            alumno = Alumno.objects.get(id=nota['alumno'])
            materia = Materia.objects.get(id=nota['materia'])
            promedio = nota['promedio']
            count_notas = nota['count_notas']
            
            # ajustar el promedio para que sea entre 3 
            if count_notas < 3:
                promedio_ajustado = (promedio * count_notas) / 3
            else :
                promedio_ajustado = promedio
                
            # determinar si el alumno aprueba o reprueba
            estado = 'Aprobado' if promedio_ajustado >= 6 else 'Reprobado'
            
            # agregar el resultado al reporte
            resultados.append({
                'alumno': f"{alumno.nombre} {alumno.apellido}",
                'materia': materia.nombre,
                'promedio': promedio_ajustado.__round__(2),
                'estado': estado
            })
            
        return Response(resultados)
            