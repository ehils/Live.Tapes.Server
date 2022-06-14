from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from livetapes_api.models.playlist import Playlist 
from livetapes_api.serializers.playlist_serializer import CreatePlaylistSerializer, PlaylistSerializer
class PlaylistView(ViewSet):  
    def retrieve(self, request, pk):
        """_summary_"""
        try:
            playlist = Playlist.objects.get(pk=pk)
            serializer = PlaylistSerializer(playlist)
            return Response(serializer.data)
        except Playlist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """_summary_"""
        playlists = Playlist.objects.all().order_by('-created_on')
        user=request.query_params.get('user', None)
        if user is not None:
            playlists = playlists.filter(user=user)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Create a new product for the current user's store"""
        user=request.auth.user
        serializer = CreatePlaylistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk):
        """_summary_"""
        playlist = Playlist.objects.get(pk=pk)
        serializer = CreatePlaylistSerializer(playlist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # playlist.categories.remove(*playlist.categories.all())
        # playlist.categories.add(*request.data['categories'])
        playlist.tracks.remove(*playlist.tracks.all())
        playlist.tracks.add(*request.data['tracks'])

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """_summary_"""
        playlist = Playlist.objects.get(pk=pk)
        playlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    