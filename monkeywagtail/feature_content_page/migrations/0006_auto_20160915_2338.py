# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feature_content_page', '0005_auto_20160915_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorfeaturepagerelationship',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_feature_page_relationship', to='author.Author'),
        ),
    ]
