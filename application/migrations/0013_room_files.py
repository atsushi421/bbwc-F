# Generated by Django 3.2.6 on 2021-08-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_alter_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='files',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
