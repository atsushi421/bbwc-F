from django.db import models
from . import Room
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):
    file = models.FileField(
        upload_to='files/',
        blank=False,
        null=False,
    )
    
    upload_at = models.DateTimeField(auto_now_add=True),
        
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )