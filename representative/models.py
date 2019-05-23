from django.db import models
from django.template.defaultfilters import truncatechars
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.utils import timezone
import PIL as pillow

class RepresentativeCategory(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Наименование категории новости")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория руководства'
        verbose_name_plural = 'Категории руководств'

class Representative(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=64, null=True, blank=True, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, default='info@gfp-russia.ru', verbose_name='Емейл')
    phone = models.CharField(max_length=18, null=True, blank=True, verbose_name='Телефон')
    position = models.TextField(max_length=512, blank=True, default=None, verbose_name='Должность')
    category = models.ForeignKey(RepresentativeCategory, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name='Категория')
    info = models.TextField(max_length=512, null=True, blank=True, default=None, verbose_name='Дополнительная информация')
    vk = models.URLField(max_length=128, blank=True, verbose_name='ВКонтакте')
    instagram = models.URLField(max_length=128, blank=True, verbose_name='Инстаграм')
    is_active = models.BooleanField(default=True, verbose_name='Актуально')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания новости')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования новости')

    @property
    def Должность(self):
        return truncatechars(self.position, 30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

class RepresentativeImage(models.Model):
    Representative = models.ForeignKey(Representative, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Руководство')
    image = models.ImageField(upload_to='news_images/', verbose_name='Фотография')
    image_is_main = models.BooleanField(default=False, verbose_name='Главная')
    image_is_active = models.BooleanField(default=True, verbose_name='Актуально')
    image_created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки фото')
    image_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования фото')

    def __str__(self):
            return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'