from django.db.models import CharField
from django import forms
from django.forms import ModelForm

from test3.models import Group, Program

class programForm(ModelForm):
    class Meta:
        model = Program
        exclude = ('group', 'discipline', 'author', 'degree', 'dep', 'protocolnum', 'date', 'planResults', 'disciplineContent', 'methodTable', 'tableBase')

