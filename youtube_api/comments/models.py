from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

class Reply (models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)