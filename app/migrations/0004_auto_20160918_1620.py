# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-18 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160918_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s1_p_g',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s2_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s3_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s4_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s5_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s6_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s7_p_g',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]