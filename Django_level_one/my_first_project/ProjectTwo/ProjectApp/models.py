from django.db import models

# Create your models here.

class Userinfo(models.Model):
    name=models.CharField(max_length=170)
    l_name=models.CharField(max_length=170)
    email=models.EmailField(max_length=250,unique=True)
