# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20160702_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='date_formed',
            field=models.DateField(blank=True, null=True, verbose_name='Date the artist started'),
        ),
    ]
