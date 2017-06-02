# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3', '0002_program_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='addlit',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень основной и дополнительной литературы. Дополнительная литература'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='aim',
            field=models.CharField(default=0, max_length=255, verbose_name='Цель дисциплины'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='attestation',
            field=models.CharField(default=0, max_length=255, verbose_name='Форма промежуточной аттестации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='fond',
            field=models.CharField(default=0, max_length=255, verbose_name='Фонд оценочных средств для проведения промежуточной аттестации обучающих-ся по дисциплине '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='goal',
            field=models.CharField(default=0, max_length=255, verbose_name='Задачи дисциплины'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='intensity',
            field=models.CharField(default=0, max_length=255, verbose_name='Общая трудоемкость дисциплины'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='internet',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень ресурсов информационно-телекоммуникационной сети «Интернет»'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='lectures',
            field=models.CharField(default=0, max_length=255, verbose_name='Темы лекций, их содержание, трудоемкость'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='listLit',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень учебно-методического обеспечения для самостоятельной работы обу-чающихся по дисциплине'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='listit',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень информационных технологий, используемых при осуществлении образовательного процесса по дисциплине, включая перечень программного обеспе-чения и информационных справочных систем'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='mainlit',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень основной и дополнительной литературы. Основная литература'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='method',
            field=models.CharField(default=0, max_length=255, verbose_name='Методические указания для обучающихся по освоению дисциплины'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='methodTable',
            field=models.CharField(default=0, max_length=255, verbose_name='Методическое обеспечение самостоятельной работы обучающихся'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='planResults',
            field=models.CharField(default=0, max_length=255, verbose_name='Перечень планируемых результатов обучения по дисциплине, соотнесенных с планиру-емыми результатами освоения образовательной программы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='pracs',
            field=models.CharField(default=0, max_length=255, verbose_name='Состав и объем практических занятий'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='prepex',
            field=models.CharField(default=0, max_length=255, verbose_name='Подготовка к экзамену'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='preplec',
            field=models.CharField(default=0, max_length=255, verbose_name='Подготовка к лекции'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='preprac',
            field=models.CharField(default=1, max_length=255, verbose_name='Подготовка к практическим занятиям'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='tableBase',
            field=models.CharField(default=0, max_length=255, verbose_name='Описание материально-технической базы, необходимой для осуществления образовательного процесса по дисциплине'),
            preserve_default=False,
        ),
    ]