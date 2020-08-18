# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-26 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isisdata', '0087_auto_20200125_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='tracking_state',
            field=models.CharField(blank=True, choices=[(b'HS', b'HSTM Upload'), (b'PT', b'Printed'), (b'AU', b'Authorized'), (b'PD', b'Proofed'), (b'FU', b'Fully Entered'), (b'NO', b'None')], db_index=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcitation',
            name='tracking_state',
            field=models.CharField(blank=True, choices=[(b'HS', b'HSTM Upload'), (b'PT', b'Printed'), (b'AU', b'Authorized'), (b'PD', b'Proofed'), (b'FU', b'Fully Entered'), (b'NO', b'None')], db_index=True, max_length=2, null=True),
        ),
    ]
