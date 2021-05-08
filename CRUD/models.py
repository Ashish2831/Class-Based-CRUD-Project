from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    rollno = models.IntegerField()
    password = models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50, null=True)