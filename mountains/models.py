from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mountain(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()

# 완등한 산의 id를 저장하는 모델
class CompletedMT(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    mountain_id = models.ForeignKey(Mountain, on_delete=models.CASCADE, db_column="mountain_id")
    mountain_name = models.CharField(max_length=20)