from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/images/', blank=True)
    url = models.URLField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
