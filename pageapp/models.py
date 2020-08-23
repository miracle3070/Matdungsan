from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField()
    username = models.CharField(max_length=20)
    content = models.TextField()