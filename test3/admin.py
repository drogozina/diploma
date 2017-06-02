from django.contrib import admin

from .models import Group, Discipline, Program, Document
# Register your models here.

class NewDisp(admin.ModelAdmin):
    list_display = [field.name for field in Discipline._meta.fields]
    # change_form_template = 'createDis.html'
    fieldsets = [
        (None, {'fields': ['index']}),
        ('Date information', {'fields': ['department'], 'classes': ['']}),
    ]
    class Meta:
        model = Discipline

admin.site.register(Group)
admin.site.register(Discipline)
admin.site.register(Program)
admin.site.register(Document)
