from django.db import models

from assesments.models import Assesment

# Create your models here.

class AssessmentPart(models.Model):
    assesment = models.ForeignKey(Assesment, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name