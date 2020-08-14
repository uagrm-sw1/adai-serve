from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Ayuda a Django a trabajar con nuestro modelo personalizado de usuario"""

    def create_user(self, email, name, lastname, date_of_birth, gender, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, lastname=lastname, date_of_birth=date_of_birth, gender=gender)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, lastname, date_of_birth, gender, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, lastname, date_of_birth, gender, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False, default="2020-01-01")
    gender = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shot name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class Estudiante(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    student_name = models.CharField(max_length=255)
    student_lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.BooleanField(default=True)

    def __str__(self):
        """Return the model as a string"""
        return self.student_name

class Materias(models.Model):
    """Modelo para las Materias"""

    subject_name = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.subject_name

class Historico(models.Model):
    """Modelo para el Historico"""

    average = models.FloatField()

class ExamenFinal(models.Model):
    """Modelo para el Examen Final"""
