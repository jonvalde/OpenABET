from django.db import models
from Universities.models import University

# Create your models here.

class Campus(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.TextField()
    
    def __str__(self):
        return self.name