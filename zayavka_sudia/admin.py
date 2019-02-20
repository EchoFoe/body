from django.contrib import admin
from .models import *


class Zayavka_sudiaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zayavka_sudia._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Zayavka_sudia


admin.site.register(Zayavka_sudia, Zayavka_sudiaAdmin)
