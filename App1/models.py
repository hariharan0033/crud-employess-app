from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    salary = models.FloatField()
