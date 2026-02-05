from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(max_length=10, unique=True)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=120)
    sem = models.IntegerField()

    def __str__(self):
        return super().__str__()