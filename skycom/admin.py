from django.contrib import admin
from .models import Profesor, Alumno, Materia, Nota

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Nota)
