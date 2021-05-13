# Generated by Django 3.2.2 on 2021-05-12 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_channel_channelmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelmessage',
            name='publication_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
