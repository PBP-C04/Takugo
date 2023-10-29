from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from main.models import TakugoUser
from tinymce.models import HTMLField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=400)
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")

    def __str__(self):
        return self.title


    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")
    
class Reply(models.Model):
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"

class Comment(models.Model):
    user = models.ForeignKey(TakugoUser, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]