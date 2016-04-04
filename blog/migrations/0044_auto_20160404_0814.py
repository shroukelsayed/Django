# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-04 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Articles'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='parent_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='blog.Comments'),
        ),
    ]