from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(TimeStampedModel):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phoneno = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
