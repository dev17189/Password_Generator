from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class client(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL , null=True,blank=True)
    description=models.CharField(max_length=100)
    timestamp=models.DateTimeField(default=timezone.now())
    username=models.CharField(max_length=20,default=None,null=True)
    password=models.CharField(max_length=20)
    encryption_key = models.BinaryField(max_length=32,null=True)