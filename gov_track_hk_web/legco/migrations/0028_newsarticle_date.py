# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legco', '0027_auto_20160908_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
