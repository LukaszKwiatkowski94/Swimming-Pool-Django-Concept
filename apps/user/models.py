from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class UserType(models.Model):
    typeName = models.CharField(max_length=30, verbose_name="nameUser")
    active=models.BooleanField(default=True,verbose_name="active")

class User(AbstractUser):
    username = None
    nameUser=models.CharField(max_length=30, verbose_name="nameUser")
    surnameUser=models.CharField(max_length=50, verbose_name="surnameUser")
    email = models.EmailField(_('email address'), unique=True)
    active=models.BooleanField(default=False,verbose_name="active")
    typeUser = models.ForeignKey(UserType, default=1, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

