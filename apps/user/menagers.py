from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        if user.is_superuser:
            from .models import Wallet
            wallet = Wallet(user=user)
            wallet.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 2)
        return self.create_user(email, password, **extra_fields)