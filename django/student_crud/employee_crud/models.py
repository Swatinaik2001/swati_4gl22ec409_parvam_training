from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=50, unique=True)
    qualification = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    salary = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name
