# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3', '0009_auto_20170522_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='attestation',
            field=models.TextField(max_length=255, verbose_name='Форма промежуточной аттестации'),
        ),
        migrations.AlterField(
            model_name='program',
            name='intensity',
            field=models.CharField(max_length=10, verbose_name='Общая трудоемкость дисциплины'),
        ),
    ]