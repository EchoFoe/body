from django.contrib import admin
from .models import *


class Zayavka_regionalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zayavka_regional._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Zayavka_regional


admin.site.register(Zayavka_regional, Zayavka_regionalAdmin)
