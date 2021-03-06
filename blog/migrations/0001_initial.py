# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('article_content', models.CharField(max_length=300)),
                ('article_creationDate', models.DateTimeField()),
                ('article_image', models.CharField(max_length=100)),
                ('article_num_views', models.IntegerField()),
                ('article_isPublished', models.BooleanField(default=False)),
                ('article_isApproved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Banwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=100)),
                ('comment_creationDate', models.DateTimeField()),
                ('comment_isApproved', models.BooleanField(default=False)),
                ('article_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Articles')),
                ('parent_id', models.ForeignKey(default=id, on_delete=django.db.models.deletion.CASCADE, to='blog.Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Emotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_isLocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('articleTag', models.ManyToManyField(to='blog.Articles')),
            ],
        ),
    ]
