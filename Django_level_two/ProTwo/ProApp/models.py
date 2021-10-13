from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=164)
    l_name=models.CharField(max_length=164)
    email=models.EmailField(max_length=164,unique=True)
