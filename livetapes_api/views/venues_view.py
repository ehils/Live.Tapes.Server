from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from livetapes_api.models.venue import Venue
from livetapes_api.serializers.venue_serializer import VenueSerializer
class VenueView(ViewSet):
    def retrieve(self, request, pk):
        try:
            venue=Venue.objects.get(pk=pk)
            serializer = VenueSerializer(venue)
            return Response(serializer.data)
        except venue.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        venues = Venue.objects.all().order_by('venue')
        serializer=VenueSerializer(venues, many=True)
        return Response(serializer.data)