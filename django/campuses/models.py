from django.db import models
from universities.models import University

class Campus(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name