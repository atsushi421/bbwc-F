# Generated by Django 3.2.6 on 2021-08-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_alter_room_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
