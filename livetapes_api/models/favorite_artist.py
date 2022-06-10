from django.db import models
from django.contrib.auth.models import User

class FavoriteArtist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)