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


class MateriaSerializado(serializers.ModelSerializer):
    """Serializar datos de la materia"""

    class Meta:
        model = models.Materias
        fields = ('id', 'subject_name')
