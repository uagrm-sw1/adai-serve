from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

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