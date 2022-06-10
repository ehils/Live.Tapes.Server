from django.db import models
from django.contrib.auth.models import User
class FavoriteTrack(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    track = models.ForeignKey("Track", on_delete=models.CASCADE)