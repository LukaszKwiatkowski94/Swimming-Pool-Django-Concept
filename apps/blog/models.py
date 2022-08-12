from django.db import models
from apps.user.models import User
from datetime import datetime
from django.conf import settings

class BlogPosts(models.Model):
    title = models.CharField(max_length=150,verbose_name="Title")
    shortText = models.CharField(max_length=300,verbose_name="Short Text")
    text = models.TextField(verbose_name="Text Content")
    author = models.ForeignKey(User, on_delete = models.CASCADE,verbose_name="Author")
    created = models.DateTimeField(default=datetime.now,verbose_name="Created")
    liked = models.IntegerField(default=0,verbose_name="Liked")
    photo = models.FileField(upload_to='blogPhoto/', verbose_name="Photo")
    photoAlt = models.CharField(max_length=100,verbose_name="Photo Alt")
    published = models.BooleanField(default=False,verbose_name="Published")

    def giveLike(self):
        self.liked += 1

