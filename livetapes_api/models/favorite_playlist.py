from django.db import models
from django.contrib.auth.models import User

class FavoritePlaylist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)