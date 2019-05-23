from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export import resources, widgets, fields
from django.db.models.fields.related import ForeignKey


class RepresentativeImageInline(admin.TabularInline):
    model = RepresentativeImage
    extra = 0

    class RepresentativeCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in RepresentativeCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = RepresentativeCategory

    admin.site.register(RepresentativeCategory, RepresentativeCategoryAdmin)

class RepresentativeAdmin(admin.ModelAdmin):
    inlines = [RepresentativeImageInline]
    list_display = ['first_name', 'last_name', 'category', 'phone', 'Должность']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Representative


admin.site.register(Representative, RepresentativeAdmin)

class RepresentativeImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RepresentativeImage._meta.fields]

    class Meta:
        model = RepresentativeImage


admin.site.register(RepresentativeImage, RepresentativeImageAdmin)
