from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('perfil', views.UserProfileViewSet)
router.register('estudiante', views.EstudianteViewSet)
router.register('materias', views.MateriaViewSet)
router.register('historico', views.HistoricoViewSet)
router.register('examen_inicial', views.ExamenInicialViewSet)
router.register('examen', views.ExamenViewSet)
router.register('contenido', views.ContenidoViewSet)
router.register('practico', views.PracticoViewSet)
router.register('tema', views.TemaViewSet)
router.register('nota', views.NotaViewSet)
router.register('ejercicio', views.EjercicioViewSet)
router.register('preguntas_examen_inicial',
                views.PreguntasExamenInicialViewSet)
router.register('preguntas_examen', views.PreguntasExamenViewSet)
router.register('preguntas_practico', views.PreguntasPracticoViewSet)


urlpatterns = [
    path('login/', views.UserLoginViewSet.as_view()),
    path('', include(router.urls)),
]
