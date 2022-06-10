from django.db import models
from django.contrib.auth.models import User
class Track(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    show = show = models.ForeignKey("Show", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, through='FavoriteTrack', related_name='favorite_tracks')