
from rest_framework import serializers
from livetapes_api.models import Track
class TrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = ('id', 'name', 'url', 'track_number')
     
class CreateTrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = ['name','url','track_number']
        