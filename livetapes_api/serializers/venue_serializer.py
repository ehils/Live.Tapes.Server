from rest_framework import serializers
from livetapes_api.models import Venue
class VenueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venue
        fields = ('id', 'venue')

