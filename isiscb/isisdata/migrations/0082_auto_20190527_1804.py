# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-27 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isisdata', '0081_auto_20190527_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cachedtimeline',
            name='authority',
        ),
        migrations.AddField(
            model_name='cachedtimeline',
            name='authority_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
