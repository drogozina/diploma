# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3', '0003_auto_20170515_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='addlit',
            field=models.TextField(verbose_name='Перечень основной и дополнительной литературы. Дополнительная литература'),
        ),
        migrations.AlterField(
            model_name='group',
            name='aim',
            field=models.TextField(verbose_name='Цель дисциплины'),
        ),
        migrations.AlterField(
            model_name='group',
            name='attestation',
            field=models.TextField(verbose_name='Форма промежуточной аттестации'),
        ),
        migrations.AlterField(
            model_name='group',
            name='fond',
            field=models.TextField(verbose_name='Фонд оценочных средств для проведения промежуточной аттестации обучающих-ся по дисциплине '),
        ),
        migrations.AlterField(
            model_name='group',
            name='goal',
            field=models.TextField(verbose_name='Задачи дисциплины'),
        ),
        migrations.AlterField(
            model_name='group',
            name='intensity',
            field=models.TextField(verbose_name='Общая трудоемкость дисциплины'),
        ),
        migrations.AlterField(
            model_name='group',
            name='internet',
            field=models.TextField(verbose_name='Перечень ресурсов информационно-телекоммуникационной сети «Интернет»'),
        ),
        migrations.AlterField(
            model_name='group',
            name='lectures',
            field=models.TextField(verbose_name='Темы лекций, их содержание, трудоемкость'),
        ),
        migrations.AlterField(
            model_name='group',
            name='listLit',
            field=models.TextField(verbose_name='Перечень учебно-методического обеспечения для самостоятельной работы обу-чающихся по дисциплине'),
        ),
        migrations.AlterField(
            model_name='group',
            name='listit',
            field=models.TextField(verbose_name='Перечень информационных технологий, используемых при осуществлении образовательного процесса по дисциплине, включая перечень программного обеспе-чения и информационных справочных систем'),
        ),
        migrations.AlterField(
            model_name='group',
            name='mainlit',
            field=models.TextField(verbose_name='Перечень основной и дополнительной литературы. Основная литература'),
        ),
        migrations.AlterField(
            model_name='group',
            name='method',
            field=models.TextField(verbose_name='Методические указания для обучающихся по освоению дисциплины'),
        ),
        migrations.AlterField(
            model_name='group',
            name='methodTable',
            field=models.TextField(verbose_name='Методическое обеспечение самостоятельной работы обучающихся'),
        ),
        migrations.AlterField(
            model_name='group',
            name='planResults',
            field=models.TextField(verbose_name='Перечень планируемых результатов обучения по дисциплине, соотнесенных с планиру-емыми результатами освоения образовательной программы'),
        ),
        migrations.AlterField(
            model_name='group',
            name='pracs',
            field=models.TextField(verbose_name='Состав и объем практических занятий'),
        ),
        migrations.AlterField(
            model_name='group',
            name='prepex',
            field=models.TextField(verbose_name='Подготовка к экзамену'),
        ),
        migrations.AlterField(
            model_name='group',
            name='preplec',
            field=models.TextField(verbose_name='Подготовка к лекции'),
        ),
        migrations.AlterField(
            model_name='group',
            name='preprac',
            field=models.TextField(verbose_name='Подготовка к практическим занятиям'),
        ),
        migrations.AlterField(
            model_name='group',
            name='tableBase',
            field=models.TextField(verbose_name='Описание материально-технической базы, необходимой для осуществления образовательного процесса по дисциплине'),
        ),
    ]