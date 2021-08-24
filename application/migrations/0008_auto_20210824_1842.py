# Generated by Django 3.2.6 on 2021-08-24 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20210824_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
        migrations.AddField(
            model_name='room',
            name='part',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]