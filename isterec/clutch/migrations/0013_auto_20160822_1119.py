# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clutch', '0012_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clutchrecdata',
            name='reviewer_1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='clutchrecdata',
            name='reviewer_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='clutchrecdata',
            name='reviewer_3',
            field=models.TextField(default=''),
        ),
    ]
