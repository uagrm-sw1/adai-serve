from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# 1


class UserProfileManager(BaseUserManager):
    """Ayuda a Django a trabajar con nuestro modelo personalizado de usuario"""

    def create_user(self, email, name, lastname, date_of_birth, gender, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, lastname=lastname,
                          date_of_birth=date_of_birth, gender=gender)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, lastname, date_of_birth, gender, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, lastname,
                                date_of_birth, gender, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# 1


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, default="2020-01-01")
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

# 2


class Estudiante(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    student_name = models.CharField(max_length=255)
    student_lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.BooleanField(default=True)

    def __str__(self):
        """Return the model as a string"""
        return self.student_name

# 3


class Materias(models.Model):
    """Modelo para las Materias"""

    subject_name = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.subject_name

# 4


class Historico(models.Model):
    """Modelo para el Historico"""

    alumno_id = models.IntegerField()
    average = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.average

# 5


class ExamenInicial(models.Model):
    """Modelo para el Examen Inicial"""

    alumno_id = models.IntegerField()
    nota = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nota

# 6


class Examen(models.Model):
    """Modelo para el Examen"""

    tema_id = models.IntegerField()
    nota = models.FloatField()
    cantidad_ejercicio = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nota

# 7


class Contenido(models.Model):
    """Contenido de las materias"""

    tema_id = models.IntegerField()
    tipo = models.CharField(max_length=50)
    elemento = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.tipo

# 8


class Practico(models.Model):
    """Modelo para el Practico"""

    tema_id = models.IntegerField()
    nombre = models.CharField(max_length=50)
    nota = models.FloatField()
    cantidad_ejercicio = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nombre

# 9


class Tema(models.Model):
    """Modelo para el Tema"""

    materia_id = models.IntegerField()
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.titulo

# 10


class Nota(models.Model):
    """Modelo para el Nota"""

    historico_id = models.IntegerField()
    alumno_id = models.IntegerField()
    materias_id = models.IntegerField()
    nota = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nota

# 11


class Ejercicio(models.Model):
    """Modelo para los ejercicios"""

    pregunta = models.CharField(max_length=255)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.pregunta

# 12


class PreguntasExamenInicial(models.Model):
    """Modelo para la relacion entre Ejercicio y sus Composiciones"""

    ejercicio_id = models.IntegerField()
    examen_inicial_id = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.ejercicio_id

# 13


class PreguntasExamen(models.Model):
    """Modelo para la relacion entre Ejercicio y sus Composiciones"""

    ejercicio_id = models.IntegerField()
    examen_id = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.ejercicio_id

# 14


class PreguntasPractico(models.Model):
    """Modelo para la relacion entre Ejercicio y sus Composiciones"""

    ejercicio_id = models.IntegerField()
    practica_id = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.ejercicio_id
