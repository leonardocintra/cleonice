# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleonice', '0018_auto_20160220_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexmediacarrousel',
            name='order_slide',
        ),
        migrations.RemoveField(
            model_name='indexmediacarrousel',
            name='slide_active',
        ),
    ]
