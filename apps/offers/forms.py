from django.forms import ModelForm
from .models import Passes

class PassForm(ModelForm):
    class Meta:
        model = Passes
        fields = ['namePass','daysOfUse','price']
        labels = {
            "namePass":"Name of pass:",
            "daysOfUse":"Days of use:",
            "price":"Price:"
        }