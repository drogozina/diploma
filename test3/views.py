# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import programForm
from .models import Group, Discipline, Program, Document
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


class createEverything():
    groupObj = Group.objects.create()
    programObj = Program.objects.create()

    htmls = [
        'http://fkn.univer.omsk.su/academics/bakalavr.htm',
        'http://fkn.univer.omsk.su/academics/master.htm'
    ]
    departments = {}
    groups = {'10.05.01': 'СБС',
              '10.03.01': 'СББ',
              '09.03.01': 'СИБ',
              '09.03.03': 'СПБ',
              '39.03.01': 'ССБ',
              '09.04.01': 'СИМ',
              '10.04.01': 'СБМ',
              '39.04.01': 'ССМ',
              '02.03.01': 'СМБ'}
    shortdeps = {'Кафедра кибернетики': 'ФС.ККБ',
                 'Кафедра компьютерных технологий и сетей': 'ФС.ККТС',
                 'Кафедра информационной безопасности': 'ФС.КИБ',
                 'Кафедра социологии': 'ФС.КС'}

    def getDeps(self):
        url = 'http://fkn.univer.omsk.su/people/kafedri.htm'
        array = []
        html_doc = urlopen(url).read()
        kek = BeautifulSoup(html_doc)
        for a in kek.findAll('li'):
            for f in a.findAll('font'):
                array.append(f.contents[0] + '\n')
                self.departments[f.contents[0]] = 'http://fkn.univer.omsk.su' + a.a.get('href')[2:]
        return array

    def getTeacher(self, department):
        url = self.departments.get(department)
        array = []

        html_doc = urlopen(url).read()
        kek = BeautifulSoup(html_doc)
        for f in kek.findAll('font'):
            nameanddegree = ""
            if f.get('size') == '4':
                nameanddegree += str(f.b.string)
            if f.get('size') == '3':
                nameanddegree += " - " + str(f.contents[1]) + '\n'
            array.append(nameanddegree)
        return array

    def getCourses(self, direction, url):
        array = []
        html_doc = urlopen(url).read()
        kek = BeautifulSoup(html_doc)
        template = re.compile(self.groups[direction])
        divs = kek.findAll('div', "field-body")
        for div in divs:
            for a in div.findAll('a'):
                try:
                    if template.search(a.contents[0]):
                        tmp = a.string.split(", ")
                        array.append(tmp[1] + "\n")
                except Exception:
                    pass

        return array

    def getDegree(self, forma, url):
        array = []
        html_doc = urlopen(url).read()
        kek = BeautifulSoup(html_doc)
        template = re.compile("Форм[аы] обучения:")
        profile = re.compile("(Профиль)|(Специализация)")
        prformag = re.compile("(Магистерская)")
        spec = ""
        divs = kek.findAll('div', "field-body")
        for div in divs:
            for ul in div.findAll('ul'):
                for li in ul.findAll('li'):

                    try:
                        for i in range(0,20):
                            br = str(li.contents[i])
                            if profile.search(br):
                                spec = br.split(": ")[1]
                            if prformag.search(br):
                                spec = str(li.contents[i+1].string)
                            if template.search(br):
                                if forma.search(br):
                                    tmp = ""
                                    if li.b.string is None:
                                        tmp += li.b.contents[0] + li.b.contents[1].string + li.b.contents[2] + " - " + spec
                                    else:
                                        tmp += str(li.b.string) + " - " + spec + '\n'

                                    array.append(tmp)
                                    break
                                break
                    except IndexError:
                        pass
        return array

    def gettingStarted(self, forma):
        if forma == "Очная":
            forma = re.compile(" очная")
        if forma == "Заочная":
            forma = re.compile(" заочная[\.\,]")

        result = []
        for html in self.htmls:
            result += self.getDegree(forma, html)

        return result

    def getDisp(self, dep):
        discipline = Discipline.objects.filter(department=self.shortdeps[dep], group_name__contains=self.groups[self.groupObj.direction])
        array = []
        for disp in discipline:
            array.append(disp.name + '\n')
        return array

    @csrf_exempt
    def getStudyForm(self, request):

        form = request.POST.get('forma')
        dir = request.POST.get('dir')
        course = request.POST.get('course')
        dep = request.POST.get('department')
        author = request.POST.get('author')
        protocol = request.POST.get('protocol')
        date = request.POST.get('date')
        disp = request.POST.get('discipline')
        content = None
        if form:
            self.groupObj.form = form
            content = self.gettingStarted(self.groupObj.form)
            self.groupObj.save()
        if dir:
            direction = dir.split(" ")
            self.groupObj.direction = direction[0]
            direction = dir.split(" - ")
            self.groupObj.dirname = direction[1]
            self.groupObj.profile = direction[2]
            courseUrl = "http://fkn.univer.omsk.su/academics/Rab_Plani/rup.htm"
            if self.groupObj.form == "Заочная":
                courseUrl = "http://fkn.univer.omsk.su/academics/Rab_Plani/rup_z.htm"
            content = self.getCourses(self.groupObj.direction, courseUrl)
            self.groupObj.save()
        if course:
            try:
                self.groupObj = Group.objects.get(course=course)
            except:
                self.groupObj.course = course

            content = self.getDeps()
            self.groupObj.save()
        if dep:
            self.programObj.dep = dep
            content = self.getTeacher(dep)
        if author:
            str = author.split(" - ")
            self.programObj.author = str[0]
            self.programObj.degree = str[1]
            self.programObj.group = self.groupObj
            content = self.getDisp(self.programObj.dep)
            self.programObj.save()
        if protocol:
            self.programObj.protocolnum = protocol
            self.programObj.save()
        if date:
            self.programObj.date = date
            self.programObj.save()
        if disp:
            self.programObj.discipline = Discipline.objects.get(name=disp)
            self.programObj.document = Document.objects.get(name='Template')
            content = self.fillTable()
            self.programObj.save()

        response = HttpResponse(content=content)
        return response

    def fillTable(self):
        array = []
        array.append(self.groupObj.dirname + '\n')
        array.append(self.groupObj.direction + '\n')
        array.append(self.groupObj.profile + '\n')
        array.append(self.programObj.discipline.part + '\n')
        array.append(self.programObj.discipline.kindofdis + '\n')
        return array

page = createEverything()

@csrf_exempt
def root(request):
    global page
    return render(request, '1.html', {'pk': page.programObj.id})

@csrf_exempt
def info(request):
    global page
    if request.method == 'POST':
        return page.getStudyForm(request)


@csrf_exempt
def create(request, pk):
    program = Program.objects.get(id=pk)
    if request.method == "POST":
        form = programForm(request.POST, instance=program)
        str = request.POST.get('content')
        methodTable = request.POST.get('methodTable')
        tableBase = request.POST.get('tableBase')
        tablehours = request.POST.get('arrayOfHours')
        if str:
            program.planResults = str
            program.save()
        if tablehours:
            program.disciplineContent = tablehours
            program.save()
        if methodTable:
            program.methodTable = methodTable
            program.save()
        if tableBase:
            program.tableBase = tableBase
            program.save()
        if form.is_valid():
            program = form.save()
            program.save()
            return render(request, '3.html', {'pk': pk})
    else:
        form = programForm()
    return render(request, '2.html', {'form': form, 'pk': pk, 'program': program})


from test3.makedoc import make
import codecs
@csrf_exempt
def fileDown(request, pk):
    program = Program.objects.get(id=pk)
    return make(program)
@csrf_exempt
def finish(request, pk):
    if request.method == 'POST':
        program = Program.objects.get(id=pk)
        return make(program)
    else:
        return render(request, '3.html', {'pk':pk})