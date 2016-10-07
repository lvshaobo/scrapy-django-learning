from django.db import models

# Create your models here.

class Direction(models.Model):
    def __str__(self):
        return self.direction_title
    direction_title = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
