from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)

## 340612---HW---CCC
class Tech(models.Model):
    name = models.CharField(max_length=200)
    revenue1 = models.IntegerField()
    employees = models.CharField(max_length=200)
    revenue2 = models.IntegerField()
    country = models.CharField(max_length=200)
    headquarter = models.CharField(max_length=200)
