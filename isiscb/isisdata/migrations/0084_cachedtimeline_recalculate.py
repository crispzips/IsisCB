# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-31 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isisdata', '0083_merge_20190624_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachedtimeline',
            name='recalculate',
            field=models.BooleanField(default=False),
        ),
    ]
