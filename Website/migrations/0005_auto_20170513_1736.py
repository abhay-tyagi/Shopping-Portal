# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_auto_20170513_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]