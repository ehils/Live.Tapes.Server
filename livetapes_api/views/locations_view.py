from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from livetapes_api.models.location import Location
from livetapes_api.serializers.location_serializer import LocationSerializer
class LocationView(ViewSet):
    def retrieve(self, request, pk):
        try:
            location=Location.objects.get(pk=pk)
            serializer = LocationSerializer(location)
            return Response(serializer.data)
        except location.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        locations = Location.objects.all().order_by('location')
        serializer=LocationSerializer(locations, many=True)
        return Response(serializer.data)