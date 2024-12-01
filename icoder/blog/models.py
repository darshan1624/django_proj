from django.db import models
from home.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.

class Post(TimeStampedModel):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class BlogComment(TimeStampedModel):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user}: {self.comment}'