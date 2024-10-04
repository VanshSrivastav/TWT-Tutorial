from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    """
    Our Serializer class, this maps the data from the DB into python objects
    Fields:
    id - Room Number
    code - Code for Room
    host - Host of room
    guestCanPause - If the guest can pause song
    voteToSkip - votes to skip song
    createdAt - date and time of room creation
    """
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guestCanPause', 'voteToSkip', 'createdAt')

