from django.db import models
from django.contrib.auth.models import AbstractUser
from .room import Room


# ユーザモデルの拡張
class User(AbstractUser):
    email = models.EmailField('email', unique=True)  # unique=True は重複付加 & 入力必須

    keyword1 = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
        default="",
    )
    
    keyword2 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    keyword3 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    keyword4 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    keyword5 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    score = models.IntegerField(
        default=0,
    )
    
    book = models.ManyToManyField(
        Room,
        blank=True
    )
    
    jourclub = models.ManyToManyField(
        Room,
        blank=True,
        related_name='jourclub'
    )