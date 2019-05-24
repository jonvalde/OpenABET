from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name 

