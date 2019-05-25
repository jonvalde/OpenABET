from django.db import models
from professors.models import Professor

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=120)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True)
    total_score = models.IntegerField()
    def __str__(self):
        return self.name