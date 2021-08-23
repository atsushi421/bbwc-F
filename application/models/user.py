from django.db import models
from django.contrib.auth.models import AbstractUser


# ユーザモデルの拡張
class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)  # unique=True は重複付加 & 入力必須
