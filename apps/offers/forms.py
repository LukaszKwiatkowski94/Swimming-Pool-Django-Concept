from django.forms import ModelForm
from .models import Passes

class PassForm(ModelForm):
    class Meta:
        model = Passes
        fields = ['namePass','daysOfUse','price']
        labels = {
            "namePass":"Post title:",
            "daysOfUse":"Full text:",
            "price":"Photo to post:"
        }