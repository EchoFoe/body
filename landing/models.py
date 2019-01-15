from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    first_name = models.CharField(max_length=128, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=128, default=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, default=True, verbose_name='Отчество')
    message = models.TextField(blank=True, null=True, default=None, verbose_name='Сообщение')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата подписки')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Пользователь: %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'