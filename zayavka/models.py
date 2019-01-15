from django.db import models
from django.utils import timezone


class Zayavka(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    first_name = models.CharField(max_length=128, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=128, default=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, default=True, verbose_name='Отчество')
    phone = models.CharField(max_length=18, default=True, verbose_name='Номер телефона')
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=True, verbose_name='Вес по заявке')
    message = models.TextField(max_length=128, blank=True, null=True, default=None, verbose_name='Сообщение')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата заявления')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Спортсмен(ка): %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Он-лайн заявка на участие в турнире'
        verbose_name_plural = 'Он-лайн заявки на участие в турнире'