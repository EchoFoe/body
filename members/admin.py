from django.contrib import admin
from .models import *


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):  # класс заказадмин
    list_display = [field.name for field in Member._meta.fields]
    # inlines = [ProductInOrderInline]
    search_fields = ['name', 'id']

    class Meta:
        model = Member


admin.site.register(Member, OrderAdmin)
