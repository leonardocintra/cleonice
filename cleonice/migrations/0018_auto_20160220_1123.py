# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleonice', '0017_indexmediacarrousel_slide_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexmediacarrousel',
            old_name='carrousel',
            new_name='carrousel_image',
        ),
        migrations.RenameField(
            model_name='indexmediacircle',
            old_name='circle',
            new_name='circle_image',
        ),
        migrations.RenameField(
            model_name='indexmediaphotofeatured',
            old_name='photo_featured',
            new_name='photo_featured_image',
        ),
        migrations.AlterField(
            model_name='indexmediacarrousel',
            name='slide_active',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
    ]