from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Paper(models.Model):
    name = models.CharField(
        max_length=255,
    )
    
    read_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )