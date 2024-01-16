from django.db import models
from django.urls import reverse


# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Date')

    def __str__(self):
        return f"{self.name} was done on {self.date}"
    
    def get_absolute_url(self):
        return reverse('workout_detail', kwargs={'workout_id': self.id})

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

