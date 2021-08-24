# Generated by Django 3.2.6 on 2021-08-24 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_room_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.room')),
            ],
        ),
    ]
