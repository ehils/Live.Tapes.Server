from django.db import models
from django.contrib.auth.models import User
class Artist(models.Model):
    name = models.CharField(max_length=100)
    favorites = models.ManyToManyField(User, through='Favoriteartist', related_name='favorite_artists')