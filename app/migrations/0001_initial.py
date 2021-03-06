# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-18 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sap_id', models.IntegerField()),
                ('s1_name', models.CharField(max_length=50)),
                ('s1_t_c', models.IntegerField()),
                ('s1_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s1_l', models.IntegerField()),
                ('s1_p', models.IntegerField()),
                ('s1_t', models.IntegerField()),
                ('s2_name', models.CharField(max_length=50)),
                ('s2_t_c', models.IntegerField()),
                ('s2_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s2_l', models.IntegerField()),
                ('s2_p', models.IntegerField()),
                ('s2_t', models.IntegerField()),
                ('s3_name', models.CharField(max_length=50)),
                ('s3_t_c', models.IntegerField()),
                ('s3_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s3_l', models.IntegerField()),
                ('s3_p', models.IntegerField()),
                ('s3_t', models.IntegerField()),
                ('s4_name', models.CharField(max_length=50)),
                ('s4_t_c', models.IntegerField()),
                ('s4_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s4_l', models.IntegerField()),
                ('s4_p', models.IntegerField()),
                ('s4_t', models.IntegerField()),
                ('s5_name', models.CharField(max_length=50)),
                ('s5_t_c', models.IntegerField()),
                ('s5_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s5_l', models.IntegerField()),
                ('s5_p', models.IntegerField()),
                ('s5_t', models.IntegerField()),
                ('s6_name', models.CharField(max_length=50)),
                ('s6_t_c', models.IntegerField()),
                ('s6_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s6_l', models.IntegerField()),
                ('s6_p', models.IntegerField()),
                ('s6_t', models.IntegerField()),
                ('s7_name', models.CharField(max_length=50)),
                ('s7_t_c', models.IntegerField()),
                ('s7_p_c', models.DecimalField(decimal_places=1, max_digits=11)),
                ('s7_l', models.IntegerField()),
                ('s7_p', models.IntegerField()),
                ('s7_t', models.IntegerField()),
            ],
        ),
    ]
