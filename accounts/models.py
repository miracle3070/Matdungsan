from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=False)
    age_group = models.IntegerField(blank=False)
    complete_count = models.IntegerField(blank=False)
    grade = models.CharField(max_length=10, blank=False)
    completeMT = models.CharField(max_length=20, blank=True)


