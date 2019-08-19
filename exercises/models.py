from django.db import models

# Create your models here.
class Exercise(models.Model):
    exercise = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    video = models.URLField(blank=True, null=True, max_length=255)
    is_added = models.BooleanField(default=False)
    def __str__(self):
        return self.exercise