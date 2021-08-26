from django.db import models
from django.utils import timezone
from . import Room
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_meesages',
        on_delete=models.CASCADE
    )
    
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)