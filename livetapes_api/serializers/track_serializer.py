
from rest_framework import serializers
from livetapes_api.models import Track
class TrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = ('id', 'title', 'show', 'url', 'track_number')
        depth = 2
class CreateTrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = ['title','url','track_number']
        