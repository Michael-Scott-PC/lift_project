from django.db import models
from exercises.models import Exercise

# Create your models here.
class Event(models.Model):
    title = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title.exercise