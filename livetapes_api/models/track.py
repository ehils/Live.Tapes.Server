from django.db import models
from django.contrib.auth.models import User
class Track(models.Model):
    title = models.CharField(max_length=100)
    track_number = models.IntegerField()
    url = models.URLField(max_length=500)
    show = models.ForeignKey("Show", on_delete=models.CASCADE, related_name="tracks")
    favorites = models.ManyToManyField(User, through='FavoriteTrack', related_name='favorite_tracks')