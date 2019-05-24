from django.contrib import admin
from .models import *


class Zayavka_mayAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Zayavka_may._meta.fields]
    list_display = ['last_name', 'first_name', 'gender', 'age', 'birthday', 'sostav', 'message', 'weight', 'raised_weight', 'wilkes', 'created']
    list_filter = ['last_name', 'email', 'message']
    search_fields = ['last_name', 'first_name', 'message']

    class Meta:
        model = Zayavka_may


admin.site.register(Zayavka_may, Zayavka_mayAdmin)
