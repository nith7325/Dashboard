# Generated by Django 2.0.5 on 2018-06-13 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genre',
            new_name='alert',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_logo',
            new_name='alert_details',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_title',
            new_name='market',
        ),
    ]
