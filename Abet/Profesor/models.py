from django.db import models

# Create your models here.
#Josue Velazquez Molina
#93803


class Profesor(models.Model):
        First_Name = models.CharField(max_length=25)
        Last_Name = models.CharField(max_length=25)
        Email = models.EmailField(max_length=254, blank=True)






