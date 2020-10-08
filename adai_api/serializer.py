from rest_framework import serializers

from adai_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'lastname',
                  'date_of_birth', 'gender', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class EstudianteSerializado(serializers.ModelSerializer):
    """Serializar datos del estudiante"""

    class Meta:
        model = models.Estudiante
        fields = ('id', 'user_profile', 'student_name',
                  'student_lastname', 'date_of_birth', 'gender')
        extra_kwargs = {'user_profile': {'read_only': True}}


class CursoSerializado(serializers.ModelSerializer):
    """Serializar datos de la materia"""

    class Meta:
        model = models.Curso
        fields = ('id', 'grado')


class MateriaSerializado(serializers.ModelSerializer):
    """Serializar datos de la materia"""

    class Meta:
        model = models.Materias
        fields = ('id', 'subject_name')


class HistoricoSerializado(serializers.ModelSerializer):
    """Serializar datos del historico"""

    class Meta:
        model = models.Historico
        fields = ('id', 'alumno_id', 'promedio')


class ExamenInicialSerializado(serializers.ModelSerializer):
    """Serializar datos del Examen Inicial"""

    class Meta:
        model = models.ExamenInicial
        fields = ('id', 'alumno_id', 'nota')


class ExamenSerializado(serializers.ModelSerializer):
    """Serializar datos del Examen"""

    class Meta:
        model = models.Examen
        fields = ('id', 'tema_id', 'cantidad_ejercicio')


class ContenidoSerializado(serializers.ModelSerializer):
    """Serializar datos del Contenido"""

    class Meta:
        model = models.Contenido
        fields = ('id', 'tema_id', 'tipo', 'elemento')


class TemaSerializado(serializers.ModelSerializer):
    """Serializar datos de Tema"""

    class Meta:
        model = models.Tema
        fields = ('id', 'materia_id', 'curso_id', 'titulo', 'duracion')


class NotaSerializado(serializers.ModelSerializer):
    """Serializar datos de Nota"""

    class Meta:
        model = models.Nota
        fields = ('id', 'historico_id', 'tema_id', 'nota')


class EjercicioSerializado(serializers.ModelSerializer):
    """"Serializar datos de Ejercicio"""

    class Meta:
        model = models.Ejercicio
        fields = ('id', 'pregunta', 'tipo')


class EjercicioExamenInicialSerializado(serializers.ModelSerializer):
    """Serializar datos de Preguntas de Examen Inicial"""

    class Meta:
        model = models.EjercicioExamenInicial
        fields = ('id', 'ejercicio_id', 'examen_inicial_id')


class EjercicioExamenSerializado(serializers.ModelSerializer):
    """Serializar datos de Preguntas de Examen"""

    class Meta:
        model = models.EjercicioExamen
        fields = ('id', 'ejercicio_id', 'examen_id')


class RespuestaSerializado(serializers.ModelSerializer):
    """Serializar datos de Preguntas de Exmane"""

    class Meta:
        model = models.Respuesta
        fields = ('id', 'ejercicio_id', 'contenido', 'esCorrecto')
