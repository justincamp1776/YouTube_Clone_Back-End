from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=500)
    likes = IntegerField(default=0)
    dislikes = IntegerField(default=0)
    videoId = models.CharField(max_length=50, null=True)

class Reply (models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    text = models.CharField(max_length=500) 