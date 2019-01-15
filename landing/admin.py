from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['email', 'last_name']
    search_fields = ['email', 'last_name']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
