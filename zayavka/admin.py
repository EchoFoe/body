from django.contrib import admin
from .models import *


class ZayavkaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zayavka._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Zayavka


admin.site.register(Zayavka, ZayavkaAdmin)
