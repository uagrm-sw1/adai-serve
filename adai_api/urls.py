from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('perfil', views.UserProfileViewSet)
router.register('estudiante', views.EstudianteViewSet)
router.register('materias', views.MateriaViewSet)

urlpatterns = [
    path('login/', views.UserLoginViewSet.as_view()),
    path('', include(router.urls)),
]
