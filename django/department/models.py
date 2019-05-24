from django.db import models

# Create your models here.
class Department(models.Model):
    Department_Name = models.CharField(max_length=25)
    Department_Number = models.CharField(max_length=25)