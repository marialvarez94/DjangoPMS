# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-29 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prendas', '0009_auto_20181128_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='order',
        ),
    ]
