from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

class RoomView(generics.ListAPIView):
    """
    queryset - returns all room objects in the DB
    serializer_class calls on the serializer to display the DB items properly
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

