# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20160402_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_id',
            field=models.ForeignKey(default=id, on_delete=django.db.models.deletion.CASCADE, to='blog.Comments'),
        ),
    ]