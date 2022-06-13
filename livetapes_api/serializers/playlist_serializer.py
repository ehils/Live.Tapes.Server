
from rest_framework import serializers
from livetapes_api.models import Playlist
class PlaylistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Playlist
        fields = ('id', 'name', 'user','tracks')
        depth = 1
class CreatePlaylistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Playlist
        fields = ['id', 'name']
        depth = 1