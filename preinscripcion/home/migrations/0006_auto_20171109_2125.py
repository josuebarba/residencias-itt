# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20171108_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materiainfo',
            old_name='semestra',
            new_name='semestre',
        ),
    ]