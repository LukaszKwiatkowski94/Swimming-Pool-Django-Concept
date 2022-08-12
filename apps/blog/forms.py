from django.forms import ModelForm
from .models import BlogPosts

class PostCreationForm(ModelForm):
    class Meta:
        model = BlogPosts
        fields = ['title','text','photo','photoAlt','published']
        labels = {
            "title":"Post title:",
            "text":"Full text:",
            "photo":"Photo to post:",
            "photoAlt":"Alt to photo:",
            "published":"Should the post be public:"
        }