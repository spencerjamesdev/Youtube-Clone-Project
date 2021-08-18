from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)
    like_dislike = BooleanField()