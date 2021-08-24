from django.db import models
from . import Room

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