# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160626_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='advert_url',
            field=models.URLField(blank=True, verbose_name='External link for advert'),
        ),
    ]
