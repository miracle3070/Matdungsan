from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField(default="(제목 없음)", blank=False)
    image = models.ImageField(blank=True, upload_to="images/")
    content = models.TextField(blank=True)
    username = models.CharField(max_length=20)