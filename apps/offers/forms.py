from django.forms import ModelForm
from .models import Passes

class PostCreationForm(ModelForm):
    class Meta:
        model = Passes
        fields = ['namePass','daysOfUse','price','active']
        labels = {
            "namePass":"Post title:",
            "daysOfUse":"Full text:",
            "price":"Photo to post:",
            "active":"Alt to photo:"
        }