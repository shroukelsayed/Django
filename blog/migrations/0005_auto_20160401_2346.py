# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160401_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='articales'),
        ),
    ]
