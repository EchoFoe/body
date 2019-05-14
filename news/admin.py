from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0

    class NewsCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in NewsCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = NewsCategory

    admin.site.register(NewsCategory, NewsCategoryAdmin)

# class NewsAdmin(admin.ModelAdmin):
#     inlines = [NewsImageInline]
#     list_display = ['news_name', 'news_town', 'news_category', 'news_summary_short', 'news_time', 'news_created']
#     list_filter = ['news_name', 'news_town', 'news_category']
#     search_fields = ['news_name', 'news_town', 'news_category']
#
#     class Meta:
#         model = News
#
#
# admin.site.register(News, NewsAdmin)

class NewsResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category',
                            widget=ForeignKeyWidget(NewsCategory, 'name'))

    class Meta:
        model = News
        # fields = [field.name for field in News._meta.fields if field.name != "id"]
        # exclude = ['id']
        # import_id_fields = ['uuid']


class NewsAdmin(ImportExportActionModelAdmin):
    resource_class = NewsResource
    # list_display = [field.name for field in News._meta.fields if field.name != "id"]
    list_display = ['news_name', 'news_town', 'news_summary_short', 'news_time']
    inlines = [NewsImageInline]
    list_filter = ['news_town', 'news_time', 'news_name']
    search_fields = ['news_name', 'news_town']

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)


class NewsImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NewsImage._meta.fields]

    class Meta:
        model = NewsImage


admin.site.register(NewsImage, NewsImageAdmin)
