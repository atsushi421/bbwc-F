# Generated by Django 3.2.6 on 2021-08-26 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0023_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='key1',
            new_name='keyword1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='key2',
            new_name='keyword2',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='key3',
            new_name='keyword3',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='key4',
            new_name='keyword4',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='key5',
            new_name='keyword5',
        ),
    ]
