from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from livetapes_api.models.show import Show

from livetapes_api.models.track import Track
from livetapes_api.serializers.track_serializer import TrackSerializer,CreateTrackSerializer

class TrackView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            track=Track.objects.get(pk=pk)
            serializer = TrackSerializer(track)
            return Response(serializer.data)
        except track.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        tracks=Track.objects.all()
        show=request.query_params.get('show', None)
        if show is not None:
            tracks = tracks.filter(show_id=show).order_by('track_number')
        serializer=TrackSerializer(tracks, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        show = Show.objects.get(pk=request.data['show_id'])
        serializer = CreateTrackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(show=show)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        """_summary_"""
        track = Track.objects.get(pk=pk)
        track.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
        