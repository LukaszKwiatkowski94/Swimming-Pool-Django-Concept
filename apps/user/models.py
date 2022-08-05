from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .menagers import MyUserManager

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    ROLE_CHOICES = (
        (1, 'Client'),
        (2, 'Administrator'),
        (3, 'Cashier'),
        (4, 'Customer service'),
        (5, 'Accountant'),
        (6, 'Press spokesman'),
        (7, 'Management'),
    )
    nameUser = models.CharField(max_length=30, verbose_name="nameUser")
    surnameUser = models.CharField(max_length=50, verbose_name="surnameUser")
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=1, default=1, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def setRole(self,newRole):
        self.role=newRole

    def get_role(self):
        return self.role

