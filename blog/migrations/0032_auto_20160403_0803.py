# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20160403_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Comments'),
        ),
    ]
