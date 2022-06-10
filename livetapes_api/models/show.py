from django.db import models
from django.contrib.auth.models import User

from livetapes_api.models.artist import Artist
from livetapes_api.models.track_rating import TrackRating

class Show(models.Model):
    date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, through='FavoriteShow', related_name='favorite_shows')
    
    
    
    # @property
    # # takes method as arguement
    # # returns a descriptor object
    # def average_rating(self):
    #     """Average rating calculated attribute for each track"""
    #     # coming from rating model,
    #     # filters all rating for each game instance
    #     ratings = TrackRating.objects.filter(track=self)
    #     # Sum all of the ratings for the game
    #     if len(ratings) == 0:
    #         # cant return a variable = thing
    #         average_rating = 0
    #     else:    
    #         total_rating = 0
    #         for rating in ratings:
    #             total_rating += rating.rating
    #         average_rating = total_rating/len(ratings)
    
    #     return average_rating
    #     #return the result
        
    