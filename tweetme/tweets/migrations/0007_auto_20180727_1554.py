# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-27 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20180724_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp', 'content']},
        ),
    ]