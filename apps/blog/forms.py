from django import forms
from .models import BlogPosts

class PostCreationForm(UserCreationForm):
    class Meta:
        model = BlogPosts
        fields = ('title','shortText','text','photo','published')
        labels = {
            "title":"Post title:",
            "shortText":"Short Text (max 300 characters):",
            "text":"Full text:",
            "photo":"Photo to post",
            "published":"Should the post be public:"
        }