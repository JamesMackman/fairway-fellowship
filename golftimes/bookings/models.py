from django.db import models

# Create your models here.
from django.db import models

class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
