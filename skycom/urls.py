from django.urls import path, include
from rest_framework import routers
from .views import ProfesorViewSet, AlumnoViewSet, MateriaViewSet, NotaViewSet

router = routers.DefaultRouter()
router.register(r'profesores', ProfesorViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]