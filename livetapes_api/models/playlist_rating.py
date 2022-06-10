from django.db import models
from django.contrib.auth.models import User
class PlaylistRating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE, related_name="playlist_ratings")
    rating = models.IntegerField()