from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from adai_api import serializer
from adai_api import models
from adai_api import permissions

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles"""

    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginViewSet(ObtainAuthToken):
    """Checks email and password and returns an auth token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        response = super(UserLoginViewSet, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'id': token.user_id, 'token': token.key})


class EstudianteViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializer.EstudianteSerializado
    queryset = models.Estudiante.objects.all()
    permission_classes = (permissions.PermisoSobreEstudiante, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)


class MateriaViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.MateriaSerializado
    queryset = models.Materias.objects.all()


class HistoricoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.HistoricoSerializado
    queryset = models.Historico.objects.all()


class ExamenInicialViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.ExamenInicialSerializado
    queryset = models.ExamenInicial.objects.all()


class ExamenViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.ExamenSerializado
    queryset = models.Examen.objects.all()


class ContenidoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.ContenidoSerializado
    queryset = models.Contenido.objects.all()


class PracticoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.PracticoSerializado
    queryset = models.Practico.objects.all()


class TemaViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.TemaSerializado
    queryset = models.Tema.objects.all()


class NotaViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.NotaSerializado
    queryset = models.Nota.objects.all()


class EjercicioViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.EjercicioSerializado
    queryset = models.Ejercicio.objects.all()


class PreguntasExamenInicialViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.PreguntasExamenInicialSerializado
    queryset = models.PreguntasExamenInicial.objects.all()


class PreguntasExamenViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.PreguntasExamenSerializado
    queryset = models.PreguntasExamen.objects.all()


class PreguntasPracticoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializer.PreguntasPracticoSerializado
    queryset = models.PreguntasPractico.objects.all()
