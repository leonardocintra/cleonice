# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleonice', '0007_auto_20160208_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]