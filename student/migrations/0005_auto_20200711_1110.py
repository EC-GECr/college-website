# Generated by Django 3.0.7 on 2020-07-11 11:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0004_auto_20200711_1108'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Profile',
        ),
    ]