from django.db import models
from django.utils import timezone


class Zayavka_sudia(models.Model):
    email = models.EmailField(max_length=64, default=True, verbose_name='Емейл')
    first_name = models.CharField(max_length=64, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=64, default=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=64, default=True, verbose_name='Отчество')
    phone = models.CharField(max_length=18, default=True, verbose_name='Номер телефона')
    age = models.DecimalField(max_digits=2, decimal_places=0, default=True, verbose_name='Возраст')
    country = models.CharField(max_length=32, default=True, verbose_name='Страна')
    region = models.CharField(max_length=64, default=True, verbose_name='Область/Регион')
    town = models.CharField(max_length=32, default=True, verbose_name='Город')
    message = models.TextField(max_length=512, null=True, default=True, verbose_name='Сообщение')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата заявления')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Судья: %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Он-лайн заявка на судейство'
        verbose_name_plural = 'Он-лайн заявки на судейства'