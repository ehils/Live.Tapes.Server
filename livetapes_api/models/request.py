from django.db import models
from django.contrib.auth.models import User
class Request(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    show = models.ForeignKey("Show", on_delete=models.CASCADE, related_name="show_requests")
    request = models.CharField(max_length=255)
    