# Generated by Django 3.2.6 on 2021-08-24 10:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20210824_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='part',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
