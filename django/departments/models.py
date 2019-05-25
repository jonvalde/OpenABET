from django.db import models
from campuses.models import Campus

# Create your models here.

class Department(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name