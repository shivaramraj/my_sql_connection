from django.db import models

# Create your models here.
class Student(models.Model):
    Sname=models.CharField(max_length=20)
    Sage=models.IntegerField()
    email=models.EmailField()
