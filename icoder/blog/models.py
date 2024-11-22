from django.db import models
from home.models import TimeStampedModel

# Create your models here.

class Post(TimeStampedModel):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    