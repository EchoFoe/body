from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget


class SportsmanImageInline(admin.TabularInline):
    model = SportsmanImage
    extra = 0

    class DisciplineAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Discipline._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Discipline

    admin.site.register(Discipline, DisciplineAdmin)

    class Weight_categoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Weight_category._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Weight_category

    admin.site.register(Weight_category, Weight_categoryAdmin)

    class Age_categoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Age_category._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Age_category

    admin.site.register(Age_category, Age_categoryAdmin)

    class DivisionAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Division._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Division

    admin.site.register(Division, DivisionAdmin)

    class StatusAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Status._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Status

    admin.site.register(Status, StatusAdmin)

    class GenderAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Gender._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Gender

    admin.site.register(Gender, GenderAdmin)

    class Line_upAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Line_up._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = Line_up

    admin.site.register(Line_up, Line_upAdmin)


class SportsmanAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ['age_category']
    inlines = [SportsmanImageInline]
    fields = [('last_name', 'first_name', 'middle_name', 'gender'), ('email', 'phone'), ('country', 'region', 'town'), ('age', 'birthday'), 'age_category', ('weight', 'weight_category'), ('raised_weight', 'wilkes'), ('division', 'discipline'), 'tournament', ('line_up', 'trainer'), ('status', 'is_active'), 'message', ('created', 'updated')]
    list_display = ['last_name', 'first_name', 'is_active', 'gender', 'age', 'Возрастные_категории', 'weight', 'weight_category',
                    'Дивизион', 'Дисциплина', 'Турнир', 'wilkes', 'created']
    list_filter = ['division', 'discipline', 'gender', 'age_category', 'weight_category', 'tournament', 'status',
                   'line_up', 'town', 'is_active']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Sportsman


admin.site.register(Sportsman, SportsmanAdmin)