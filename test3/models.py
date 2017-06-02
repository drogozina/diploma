from django.db import models

# Create your models here.

class Document(models.Model):
    minobrnayki = models.CharField(max_length=255, verbose_name='МИНОБРНАУКИ РОССИИ')
    fed = models.CharField(max_length=255, verbose_name='федеральное государственное бюджетное образовательное учреждение высшего образования')
    decan = models.CharField(max_length=255, verbose_name='Декан факультета')
    approve = models.CharField(max_length=255, verbose_name='Кто утверждает')
    approvePosition = models.CharField(max_length=255, verbose_name='Должность утверждающего')
    name = models.CharField(max_length=255, verbose_name='Название шаблона')

    def __str__(self):
        return "%s" % (self.name)

class Discipline(models.Model):
    index = models.CharField(max_length=255, primary_key=True, default='index', verbose_name='Индекс' )
    department = models.CharField(max_length=255, verbose_name='Кафедра')
    competention = models.CharField(max_length=255, verbose_name='Код компетенции')
    name = models.CharField(max_length=255, verbose_name='Название')
    part = models.CharField(max_length=255, verbose_name='Базовая/вариативная часть',
                            choices=[
                                ('Базовая часть', 'Базовая часть'),
                                ('Вариативная часть', 'Вариативная часть')])
    kindofdis = models.CharField(max_length=255, verbose_name='Обязательная дисциплина/дисциплина по выбору/факультатив',
                                 choices=[
                                     ('Обязательная дисциплина', 'Обязательная дисциплина'),
                                     ('Дисциплина по выбору', 'Дисциплина по выбору'),
                                     ('Факультатив', 'Факультатив')])
    weeks = models.IntegerField(default=0, verbose_name='Количество недель')
    lectures = models.IntegerField(default=0, verbose_name='Часов лекций')
    labs = models.IntegerField(default=0, verbose_name='Часов лабораторных')
    pracs = models.IntegerField(default=0, verbose_name='Часов практики')
    srs = models.IntegerField(default=0, verbose_name='Часов СРС')
    krprkt = models.IntegerField(default=0, verbose_name='КР/ПРКТ')
    izkr = models.IntegerField(default=0, verbose_name='ИЗ/КР')
    ctrl = models.CharField(max_length=255, verbose_name='Контроль')
    group_name = models.CharField(max_length=255, verbose_name='Дисциплина для группы')
    def __str__(self):
        return "%s %s" % (self.name, self.department)

class Group(models.Model):
    course = models.CharField(max_length=255, verbose_name='Имя группы', default='GroupName')
    form = models.CharField(max_length=255, verbose_name='Форма обучения')
    direction = models.CharField(max_length=255, verbose_name='Код направления подготовки')
    dirname = models.CharField(max_length=255, verbose_name='Направление подготовки')
    profile = models.CharField(max_length=255, verbose_name='Профиль подготовки')
    def __str__(self):
        return "%s %s" % (self.course, self.dirname)

class Program(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', null=True, blank=True, unique=False)
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', null=True, blank=True, unique=False)
    document = models.ForeignKey(Document, verbose_name='Оформление документа', null=True, blank=True, unique=False)
    author = models.CharField(max_length=255, verbose_name='Автор')
    degree = models.CharField(max_length=255, verbose_name='Ученая степень')
    dep = models.CharField(max_length=255, verbose_name='Кафедра')
    protocolnum = models.TextField(max_length=255, verbose_name='Номер протокола')
    date = models.CharField(max_length=255, verbose_name='Дата протокола')
    aim = models.TextField(verbose_name='Цель дисциплины', )
    goal = models.TextField(verbose_name='Задачи дисциплины')
    #is a table
    planResults = models.TextField(
        verbose_name='Перечень планируемых результатов обучения по дисциплине, соотнесенных с планиру-емыми результатами освоения образовательной программы')
    disciplineContent = models.TextField(verbose_name="Содержание дисциплины, структурированное по разделам, с указанием отведенного на них количества академических часов и видов учебных занятий")
    intensity = models.CharField(max_length=10, verbose_name='Общая трудоемкость дисциплины')
    attestation = models.CharField(max_length=255, verbose_name='Форма промежуточной аттестации')
    lectures = models.TextField(verbose_name='Темы лекций, их содержание, трудоемкость')
    pracs = models.TextField(verbose_name='Состав и объем практических занятий')
    labs = models.TextField(verbose_name='Состав и объем лаборартоных занятий')
    listLit = models.TextField(
        verbose_name='Перечень учебно-методического обеспечения для самостоятельной работы обучающихся по дисциплине')
    fond = models.TextField(
        verbose_name='Фонд оценочных средств для проведения промежуточной аттестации обучающихся по дисциплине ')
    mainlit = models.TextField(verbose_name='Перечень основной и дополнительной литературы. Основная литература')
    addlit = models.TextField(verbose_name='Перечень основной и дополнительной литературы. Дополнительная литература')
    internet = models.TextField(verbose_name='Перечень ресурсов информационно-телекоммуникационной сети «Интернет»')
    method = models.TextField(verbose_name='Методические указания для обучающихся по освоению дисциплины')
    methodTable = models.TextField(verbose_name='Методическое обеспечение самостоятельной работы обучающихся')
    preplec = models.TextField(verbose_name='Подготовка к лекции')
    preprac = models.TextField(verbose_name='Подготовка к практическим занятиям')
    prepex = models.TextField(verbose_name='Подготовка к экзамену')
    listit = models.TextField(
        verbose_name='Перечень информационных технологий, используемых при осуществлении образовательного процесса по дисциплине, включая перечень программного обеспечения и информационных справочных систем')
    tableBase = models.TextField(
        verbose_name='Описание материально-технической базы, необходимой для осуществления образовательного процесса по дисциплине')

    def __str__(self):
        return "%s %s %s" % (self.author, self.discipline, self.group)


