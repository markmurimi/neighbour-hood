# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20180526_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='user',
        ),
    ]
