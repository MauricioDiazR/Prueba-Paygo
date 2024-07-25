from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Definición de lexers y estilos
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,unique=True)
    permission = models.ManyToManyField(Permission, related_name='roles')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username =models.CharField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=200, default='defalut_password')
    name = models.CharField(max_length=200, null=False)
    role = models.ManyToManyField (Role, related_name='users')

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username