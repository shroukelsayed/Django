# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20160402_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comments'),
        ),
    ]
