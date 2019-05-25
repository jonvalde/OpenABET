from django.db import models
from departments.models import Department

class Professor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name