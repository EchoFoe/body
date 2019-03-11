from django.contrib import admin
from .models import *


class Zayavka_juneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zayavka_june._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Zayavka_june


admin.site.register(Zayavka_june, Zayavka_juneAdmin)
