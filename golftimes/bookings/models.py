from django.db import models

# Create your models here.
class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class TeeTime(models.Model):
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    availability = models.IntegerField(default=0)

class Booking(models.Model):
    tee_time = models.ForeignKey(TeeTime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)