# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0010_business_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(upload_to='businesss/'),
        ),
    ]
