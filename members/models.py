from django.db import models
# from tournaments.models import Tournaments
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

class Member(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    first_name = models.CharField(max_length=128, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=128, default=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, default=True, verbose_name='Отчество')
    gender = models.CharField(max_length=1, choices=(('m', ('Муж.')), ('f', ('Жен.'))), blank=True, null=True, verbose_name='Пол')
    phone = models.CharField(max_length=18, default=True, verbose_name='Номер телефона')
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=True, verbose_name='Вес по заявке')
    age = models.DecimalField(max_digits=2, decimal_places=0, default=True, verbose_name='Возраст')
    country = models.CharField(max_length=32, default=True, verbose_name='Страна')
    region = models.CharField(max_length=32, default=True, verbose_name='Область/Регион')
    town = models.CharField(max_length=32, default=True, verbose_name='Город')
    sostav = models.CharField(max_length=32, default=True, verbose_name='Команда/Лично')
    trener = models.CharField(max_length=32, blank=True, verbose_name='Тренер')
    # tournament = models.ForeignKey(Tournaments.tournaments_name, on_delete=models.CASCADE)
    message = models.TextField(max_length=128, null=True, default=None, verbose_name='Сообщение')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата заявления')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    def __str__(self):
        return "Спортсмен(ка): %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Он-лайн заявка на участие в турнире'
        verbose_name_plural = 'Он-лайн заявки на участие в турнире'

    # def save(self, *args, **kwargs):
    #     super(Member, self).save(*args, **kwargs)