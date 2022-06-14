from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from livetapes_api.models import Show, Track, Artist, Location, Venue
from livetapes_api.serializers.show_serializer import CreateShowSerializer, ShowSerializer
class ShowView(ViewSet):
    def retrieve(self, request, pk):
        """_summary_"""
        try:
            show = Show.objects.get(pk=pk)
            serializer = ShowSerializer(show)
            return Response(serializer.data)
        except Show.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        shows = Show.objects.all()
        
        user=request.query_params.get('user', None)
        artist = request.query_params.get('artist', None)
        venue = request.query_params.get('venue', None)
        location = request.query_params.get('location', None)
        date = request.query_params.get('date', None)
        
        search_term = request.query_params.get('search_term', None)
        
        if search_term is not None:
            shows = shows.filter(
                Q(artist__name__contains=search_term) | Q(tracks__title__contains= search_term)
            )
        if user is not None:
            shows = shows.filter(user=user)
        if artist is not None:
            shows= shows.filter(artist=artist)
        if venue is not None:
            shows= shows.filter(venue=venue)
        if location is not None:
            shows= shows.filter(location=location)
        if date is not None:
            shows = shows.filter(date__contains=date)
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)
    def create(self,request):
        user = request.auth.user
        # don't send id from front end, send input of text
        artist, _ = Artist.objects.get_or_create(name=request.data['artist'])
        venue, _ = Venue.objects.get_or_create(venue=request.data['venue'])
        location, _ = Location.objects.get_or_create(location=request.data['location'])
        serializer = CreateShowSerializer(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, artist=artist, venue=venue, location=location)
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    def destroy(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    