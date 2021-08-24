from django.db import models
from django.contrib.auth.models import AbstractUser


# ユーザモデルの拡張
class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)  # unique=True は重複付加 & 入力必須

    key1 = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
        default=None,
    )
    
    key2 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    key3 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    key4 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )
    
    key5 = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        default="",
    )