import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    name = models.CharField(
        max_length=255,
        blank = False,
        null = False,
        unique = True,
    )
    
    part = models.ManyToManyField(
        User,
        blank = True,
        default = None,
    )
    
    def __str__(self):
        return self.name
