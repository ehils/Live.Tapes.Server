from django.db import models
from django.contrib.auth.models import User
class FavoriteShow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    show = models.ForeignKey("Show", on_delete=models.CASCADE)