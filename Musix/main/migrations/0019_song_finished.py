# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_song_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]