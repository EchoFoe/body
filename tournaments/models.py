from django.db import models

from members.models import Member
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow

class TournamentsCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название дисциплины")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория турнира'
        verbose_name_plural = 'Категории турниров'


class TournamentsFederation(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название федерации")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Федерация'
        verbose_name_plural = 'Федерации'


class TournamentsRecord(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название рекорда")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Уровень рекорда'
        verbose_name_plural = 'Уровень рекордов'

class TournamentsDivision(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название дивизиона")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизион'

class TournamentsStatus(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название статуса")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория статуса'
        verbose_name_plural = 'Категории статусов'

class Tournaments(models.Model):
    tournaments_name = models.TextField(max_length=512, null=True, default=True, verbose_name='Название турнира')
    tournaments_name_short = models.CharField(max_length=32, blank=True, null=True, verbose_name='Сокращенное название соревнований для рекордов')
    tournaments_region = models.CharField(max_length=64, default=True, verbose_name='Регион')
    tournaments_town = models.CharField(max_length=64, default=True, verbose_name='Город')
    tournaments_time_begin = models.DateTimeField(default=None, verbose_name='Дата начала турнира')
    tournaments_time_end = models.DateTimeField(default=None, verbose_name='Дата окончания турнира')
    tournaments_categories = models.ManyToManyField(TournamentsCategory, blank=True, default=True,verbose_name='Дисциплины')
    tournaments_federations = models.ManyToManyField(TournamentsFederation, blank=True, default=True, verbose_name='Федерации')
    tournaments_records = models.ForeignKey(TournamentsRecord, null=True, default=True, on_delete=models.CASCADE, verbose_name='Уровень рекордов')
    tournaments_divisions = models.ManyToManyField(TournamentsDivision, blank=True, default=True, verbose_name='Дивизионы')
    tournaments_status = models.ForeignKey(TournamentsStatus, blank=True, default=True, on_delete=models.CASCADE, verbose_name='Статус')
    tournaments_sponsors = models.CharField(max_length=512, null=True, blank=True, default=None, verbose_name='Спонсоры')
    tournaments_description = models.TextField(max_length=512, blank=True, default=None, verbose_name='Описание турнира')
    tournaments_provisions_dk = models.FileField(upload_to="tournaments_files_provisions_dk", blank=True, default=None, null=None, verbose_name='Положения на турнир с допинг-контролем')
    tournaments_provisions_bezdk = models.FileField(upload_to="tournaments_files_provisions_bezdk", blank=True, default=None, null=None,
verbose_name='Положения на турнир без допинг-контроля')
    tournaments_nominations = models.FileField(upload_to="tournaments_files_nominations", blank=True, default=None, null=None,
verbose_name='Номинации на турнир')
    tournaments_is_active = models.BooleanField(default=True, verbose_name='Актуальность турнира')
    tournaments_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания турнира')
    tournaments_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования турнира')

    @property
    def Турнир(self):
        return truncatechars(self.tournaments_name, 80)

    @property
    def tournaments_description_short(self):
        return truncatechars(self.tournaments_description, 20)

    @property
    def Дисциплины(self):
        return "\n".join([p.name for p in self.tournaments_categories.all()])

    @property
    def Дивизионы(self):
        return "\n".join([p.name for p in self.tournaments_divisions.all()])

    def __str__(self):
        return "%s" % self.tournaments_name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

    def save(self, *args, **kwargs):
        super(Tournaments, self).save(*args, **kwargs)

class MemberInTournaments(models.Model):
    tournament = models.ForeignKey(Tournaments, blank=True, null=True, default=None, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Участник')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s %s, почта: %s, телефон: %s, вес по заявке: %s, горород: %s " % (self.member.first_name, self.member.last_name, self.member.email, self.member.phone, self.member.weight, self.member.town)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

# class TournamentsImage(models.Model):
#     Tournaments = models.ForeignKey(Tournaments, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Турнир')
#     tournaments_image = models.ImageField(upload_to='tournaments_images/', verbose_name='Фотография турнира')
#     tournaments_image_is_main = models.BooleanField(default=False, verbose_name='Главная')
#     tournaments_image_is_active = models.BooleanField(default=True, verbose_name='Актуально')
#     tournaments_image_created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки фото')
#     tournaments_image_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования фото')
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'Фотография турнира'
#         verbose_name_plural = 'Фотографии турниров'