# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_favortie',
            field=models.BooleanField(default=False),
        ),
    ]
