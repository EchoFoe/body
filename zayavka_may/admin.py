from django.contrib import admin
from .models import *


class Zayavka_mayAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Zayavka_may._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Zayavka_may


admin.site.register(Zayavka_may, Zayavka_mayAdmin)
