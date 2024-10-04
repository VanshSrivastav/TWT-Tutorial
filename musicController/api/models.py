from django.db import models
import string
import random

# Create your models here.

def generateUniqueCode():

    length = 6
    while True:
        # Generates a random code that is all uppercase of length 6. 
        # the function works as follows:
        # random.choices(string.ascii_uppercase), k = length returns an ARRAY of 6 RANDOM chars. 
        # Then we join them into a single string, then we check if that code is present in our DB. 
        # If it is not then we return it else generate again

        code = "".join(random.choices(string.ascii_uppercase),k=length)
        if Room.objects.filter(code = code).count() == 0:
            break
    
    return code


class Room(models.Model):
    """
    Our Columns in the DB
    Code - The code that is used for the room
    Host - The host of the room
    guestCanPause - if a guest has permission to pause the song
    voteToSkip - Number of votes to skip
    createdAT - Date Time field to show room creation
    """
    # our columns in the DB
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guestCanPause = models.BooleanField(null=False, default=False)
    voteToSkip = models.IntegerField(null=False, default=2)
    createdAt = models.DateTimeField(auto_now_add=True)


