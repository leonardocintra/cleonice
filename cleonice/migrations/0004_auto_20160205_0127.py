# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleonice', '0003_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('BO', 'Bolo'), ('BI', 'Biscoito')], default='BO', max_length=2),
        ),
    ]