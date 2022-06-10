from django.db import models
from django.contrib.auth.models import User
class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    show = models.ForeignKey("Show", on_delete=models.CASCADE, related_name="show_notes")
    note = models.CharField(max_length=255)
    