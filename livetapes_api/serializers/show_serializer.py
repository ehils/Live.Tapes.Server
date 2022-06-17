
from rest_framework import serializers
from livetapes_api.models import Show
class ShowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Show
        fields = ('id', 'date', 'created_on', 'user', 'artist', 'venue', 'location', 'tracks')
        depth = 2
class CreateShowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Show
        fields = ['id', 'date','user', 'artist', 'venue', 'location']
        depth = 2