# Generated by Django 3.2.2 on 2021-05-12 20:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MessageModel',
            new_name='PrivateMessage',
        ),
    ]
