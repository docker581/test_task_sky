from django.contrib import admin

from .models import Patient, Case, Document, Body


class PatientAdmin(admin.ModelAdmin):
    list_display = ['fio', 'birth_date', 'gender', 'id']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'date_begin', 'date_end', 'result']


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'patient', 'case', 'date', 'id']


class BodyAdmin(admin.ModelAdmin):
    list_display = ['document', 'content', 'id']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Body, BodyAdmin)
