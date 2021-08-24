from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    like_dislike = BooleanField()


# class Reply(models.Model):
#         comment = use a FK to locate it need to see how to make a FK in data base
#     text = models.CharField(max_length=200)