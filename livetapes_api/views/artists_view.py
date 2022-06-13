from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from livetapes_api.models.artist import Artist
from livetapes_api.serializers.artist_serializer import ArtistSerializer
class ArtistView(ViewSet):
    def retrieve(self, request, pk):
        try:
            artist=Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        except artist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        artists = Artist.objects.all().order_by('name')
        serializer=ArtistSerializer(artists, many=True)
        return Response(serializer.data)