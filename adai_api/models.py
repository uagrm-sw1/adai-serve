from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Ayuda a Django a trabajar con nuestro modelo personalizado de usuario"""

    def create_user(self, email, name, password=None):
        """Crea un nuevo perfil de usuario"""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Crea y guarda un nuevo superusuario con detalles dados"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Representa un "perfil de usuario" dentro del sistema. Almacena todas las cuentas, 
    asi como los 'correos electronicos' y 'nombres'. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django usa esto cuando necesita obtener el nombre completo del usuario"""

        return self.name

    def get_short_name(self):
        """Django usa esto cuando necesita obtener la abrevacion del nombre de usuario"""

        return self.name

    def __str__(self):
        """Django usa esto cuando necesita convertir el objeto a texto"""

        return self.email