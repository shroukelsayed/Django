# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20160403_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Comments'),
        ),
    ]
