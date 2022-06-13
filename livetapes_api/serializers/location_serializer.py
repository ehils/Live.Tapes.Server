from rest_framework import serializers
from livetapes_api.models import Location
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Location
        fields = ('id', 'location')

