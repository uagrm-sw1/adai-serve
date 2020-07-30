from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PermisoSobreEstudiante(permissions.BasePermission):
    """Permite al usuario actualizar datos sobre el estudiante"""

    def has_object_permission(self, request, view, obj):
        """Verifica si el usuario que esta actualizando sea el propietario"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id