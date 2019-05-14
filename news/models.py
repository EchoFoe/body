from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow

class NewsCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Наименование категории новости")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории турниров'

class News(models.Model):
    news_name = models.TextField(max_length=512, null=True, blank=True, default=True, verbose_name='Название новости')
    news_summary = models.TextField(max_length=512, blank=True, default=None, verbose_name='Что произошло?')
    news_town = models.CharField(max_length=64, blank=True, default=True, verbose_name='Населенный пункт к новости')
    news_category = models.ForeignKey(NewsCategory, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Категория новости')
    news_time = models.DateTimeField(default=None, verbose_name='Дата для новости')
    news_is_active = models.BooleanField(default=True, verbose_name='Актуально')
    news_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания новости')
    news_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования новости')

    @property
    def news_summary_short(self):
        return truncatechars(self.news_summary, 30)

    def __str__(self):
        return "%s" % self.news_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsImage(models.Model):
    News = models.ForeignKey(News, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Новость')
    news_image = models.ImageField(upload_to='news_images/', verbose_name='Фотография (АФИША)')
    news_image_is_main = models.BooleanField(default=False, verbose_name='Главная')
    mews_image_is_active = models.BooleanField(default=True, verbose_name='Актуально')
    news_image_created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки фото')
    news_image_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования фото')

    def __str__(self):
            return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография (АФИША)'
        verbose_name_plural = 'Фотографии (АФИШИ)'