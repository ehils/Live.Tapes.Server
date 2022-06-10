from django.db import models
from django.contrib.auth.models import User
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    tracks = models.ManyToManyField("Track", through="PlaylistTrack", related_name="playlist_tracks")
    favorites = models.ManyToManyField(User, through='FavoritePlaylist', related_name='favorite_playlists')
    