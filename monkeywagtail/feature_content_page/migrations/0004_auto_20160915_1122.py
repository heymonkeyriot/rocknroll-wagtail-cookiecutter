# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feature_content_page', '0003_auto_20160911_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistfeaturepagerelationship',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_page_artist_relationship', to='artist.Artist'),
        ),
    ]