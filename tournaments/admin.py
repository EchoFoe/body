from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget


class MemberInTournamentsInline(admin.TabularInline):
    model = MemberInTournaments
    extra = 0

    class TournamentsCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in TournamentsCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = TournamentsCategory

    admin.site.register(TournamentsCategory, TournamentsCategoryAdmin)

    class TournamentsFederationAdmin(admin.ModelAdmin):
        list_display = [field.name for field in TournamentsFederation._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = TournamentsFederation

    admin.site.register(TournamentsFederation, TournamentsFederationAdmin)

    class TournamentsRecordAdmin(admin.ModelAdmin):
        list_display = [field.name for field in TournamentsRecord._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = TournamentsRecord

    admin.site.register(TournamentsRecord, TournamentsRecordAdmin)

    class TournamentsDivisionAdmin(admin.ModelAdmin):
        list_display = [field.name for field in TournamentsDivision._meta.fields]
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = TournamentsDivision

    admin.site.register(TournamentsDivision, TournamentsDivisionAdmin)

    class TournamentsStatusAdmin(admin.ModelAdmin):
        list_display = [field.name for field in TournamentsStatus._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = TournamentsStatus

    admin.site.register(TournamentsStatus, TournamentsStatusAdmin)


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

# class TournamentsResource(resources.ModelResource):
#     category = fields.Field(column_name='tournaments_categories', attribute='tournaments_categories',
#                             widget=ManyToManyWidget(TournamentsCategory, 'name'))
#     record = fields.Field(column_name='Уровень рекордов', attribute='tournaments_records',
#                             widget=ForeignKeyWidget(TournamentsCategory, 'name'))
#     division = fields.Field(column_name='tournaments_divisions', attribute='tournaments_divisions',
#                             widget=ManyToManyWidget(TournamentsDivision, 'name'))
#
#     class Meta:
#         model = Tournaments
        # fields = [field.name for field in Tournaments._meta.fields if field.name != "id"]
        # exclude = ['id']
        # import_id_fields = ['uuid']


# class TournamentsAdmin(ImportExportActionModelAdmin):
#     filter_horizontal = ('tournaments_divisions', 'tournaments_federations', 'tournaments_categories',)
#     resource_class = TournamentsResource
#     # list_display = [field.name for field in News._meta.fields if field.name != "id"]
#     # fields = ['tournaments_categories']
#     list_display = ['Турнир', 'Дивизионы', 'tournaments_records', 'tournaments_town', 'tournaments_time_begin', 'tournaments_time_end', 'tournaments_status']
#     inlines = [MemberInTournamentsInline]
#     list_filter = ['tournaments_name', 'tournaments_town', 'tournaments_categories', 'tournaments_status']
#     search_fields = ['tournaments_name', 'tournaments_town', 'tournaments_categories', 'tournaments_status']
#
#     class Meta:
#         model = Tournaments
#
#
# admin.site.register(Tournaments, TournamentsAdmin)

class TournamentsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tournaments_divisions', 'tournaments_federations', 'tournaments_categories',)
    # resource_class = TournamentsResource
    # list_display = [field.name for field in News._meta.fields if field.name != "id"]
    # fields = ['tournaments_categories']
    list_display = ['Турнир', 'Дивизионы', 'tournaments_records', 'tournaments_town', 'tournaments_time_begin', 'tournaments_time_end', 'tournaments_status']
    inlines = [MemberInTournamentsInline]
    list_filter = ['tournaments_name', 'tournaments_town', 'tournaments_categories', 'tournaments_status']
    search_fields = ['tournaments_name', 'tournaments_town', 'tournaments_categories', 'tournaments_status']

    class Meta:
        model = Tournaments


admin.site.register(Tournaments, TournamentsAdmin)

class TournamentsMemberAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in MemberInTournaments._meta.fields]
    list_display = ['email']

    class Meta:
        model = MemberInTournaments