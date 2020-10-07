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


class Curso(models.Model):

    grado = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.grado


# 4


class Materias(models.Model):
    """Modelo para las Materias"""

    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.subject_name

# 5


class Historico(models.Model):
    """Modelo para el Historico"""

    alumno_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    average = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.average

# 6


class ExamenInicial(models.Model):
    """Modelo para el Examen Inicial"""

    alumno_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nota

# 7


class Tema(models.Model):
    """Modelo para el Tema"""

    materia_id = models.ForeignKey(Materias, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.titulo


# 8

class Examen(models.Model):
    """Modelo para el Examen"""

    tema_id = models.ForeignKey(Tema, on_delete=models.CASCADE)
    cantidad_ejercicio = models.IntegerField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.cantidad_ejercicio

# 9


class Contenido(models.Model):
    """Contenido de las materias"""

    tema_id = models.ForeignKey(Tema, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    elemento = models.CharField(max_length=255)

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.tipo

# 10


class Nota(models.Model):
    """Modelo para el Nota"""
    historico_id = models.ForeignKey(Historico, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    materias_id = models.ForeignKey(Materias, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.nota

# 11


class Ejercicio(models.Model):
    """Modelo para los ejercicios"""

    pregunta = models.CharField(max_length=255)
    tipo = models.CharField(max_length=32, default="selector")

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.pregunta

# 12


class EjercicioExamen(models.Model):
    """Modelo para los ejercicios"""

    examen_id = models.ForeignKey(Examen, on_delete=models.CASCADE)
    ejercicio_id = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

    def __str__(self):
        """Retorna el modelo como una cadenas"""
        return self.examen_id

# 13


class EjercicioExamenInicial(models.Model):
    """Modelo para los ejercicios"""

    examen_inicial_id = models.ForeignKey(
        ExamenInicial, on_delete=models.CASCADE)
    ejercicio_id = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

    def __str__(self):
        """Retorna el modelo como una cadenas"""
        return self.examen_inicial_id

# 14


class Respuesta(models.Model):
    """Modelo para almacenar distintas respuestas"""

    ejercicio_id = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=128)
    esCorrecto = models.BooleanField()

    def __str__(self):
        """Retorna el modelo como una cadena"""
        return self.contenido
