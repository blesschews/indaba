# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-17 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markitup.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abstract', markitup.fields.MarkupField(help_text='Describe your talk in one or twoparagraphs, mentioning your target audience & whatthey will get out of your talkYou are free to use markdown syntax', no_rendered_field=True)),
                ('title', models.CharField(max_length=1024)),
                ('_abstract_rendered', models.TextField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talk_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('S', 'Short_Talk'), ('L', 'Long_Talk'), ('T', 'Tutorial')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='talk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.Talk_Type'),
        ),
    ]
