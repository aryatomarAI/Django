from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    release_year=models.IntegerField()
    length=models.IntegerField()

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name=models.CharField(max_length=200)
    second_name=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + " " + self.second_name
