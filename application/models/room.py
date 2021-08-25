import uuid
from django.db import models

class Room(models.Model):
    name = models.CharField(
        max_length=255,
        blank = False,
        null = False,
        unique = True,
    )
    
    files = models.FileField(
        blank = True,
        upload_to= 'files/'
    )
    
    def __str__(self):
        return self.name
