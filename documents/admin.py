from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *

class DocumentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Documents._meta.fields]
    list_filter = ['documents_description']
    search_fields = ['documents_description']

    class Meta:
        model = Documents


admin.site.register(Documents, DocumentsAdmin)