# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160918_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='totalc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='totalg',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
