from django.db import models

class Venue(models.Model):
    venue = models.CharField(max_length=150)