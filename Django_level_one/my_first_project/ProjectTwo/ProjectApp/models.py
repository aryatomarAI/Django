from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=170,unique=True)
    l_name=models.CharField(max_length=170,unique=True)
    email=models.EmailField(max_length=250)
