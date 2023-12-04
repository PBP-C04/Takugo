from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from main.models import TakugoUser
class Post(models.Model):
    title = models.CharField(max_length=400, default='')
    author = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, default='')
    date = models.DateTimeField(default=now)
class Reply(models.Model):
    author = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, default='')
    date = models.DateTimeField(default=now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)