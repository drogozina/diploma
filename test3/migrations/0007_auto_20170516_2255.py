# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3', '0006_auto_20170516_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='protocolnum',
            field=models.TextField(max_length=255, verbose_name='Номер протокола'),
        ),
    ]
