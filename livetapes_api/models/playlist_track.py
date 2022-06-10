from django.db import models

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)