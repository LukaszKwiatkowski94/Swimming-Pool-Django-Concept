from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','nameUser', 'surnameUser')
        labels = {
            "email":"Your email address:",
            "nameUser":"Your name:",
            "surnameUser":"Your sourname:"
        }

# UserChangeForm in the future