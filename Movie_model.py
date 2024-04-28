from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration_minutes = models.IntegerField()
