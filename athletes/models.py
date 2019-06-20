from django.db import models
from django.template.defaultfilters import truncatechars
from tournaments.models import Tournaments
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус спортсмена'
        verbose_name_plural = 'Статусы спортсменов'

class Gender(models.Model):
    name = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Пол спортсмена'
        verbose_name_plural = 'Пол спортсменов'

class Line_up(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Лично/Командно'
        verbose_name_plural = 'Лично/Командно'

class Division(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название дивизиона")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизионы'

class Discipline(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Название дисциплины")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class Age_category(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Возрастная категория")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Возрастная категория'
        verbose_name_plural = 'Возрастные категории'

class Weight_category(models.Model):
    name = models.CharField(max_length=128, blank=True, default=True, verbose_name="Возрастная категория")
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Весовая категория'
        verbose_name_plural = 'Весовые категории'

class Athletes(models.Model):
    email = models.EmailField(max_length=128, default=True, verbose_name='Емейл')
    phone = models.CharField(max_length=18, default=True, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=128, default=True, verbose_name='Имя')
    last_name = models.CharField(max_length=128, default=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, default=True, verbose_name='Отчество')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Пол')
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=True, verbose_name='Вес')
    birthday = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рождения')
    age = models.DecimalField(max_digits=2, decimal_places=0, default=True, verbose_name='Возраст')
    age_category = models.ManyToManyField(Age_category, blank=True, default=True, verbose_name='Возраст. кат-рия')
    weight_category = models.ForeignKey(Weight_category, null=True, on_delete=models.CASCADE, verbose_name='Вес. категория')
    raised_weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=00.00, verbose_name='Поднятый вес (общий)')
    wilkes = models.DecimalField(max_digits=6, decimal_places=2, default=00.00, blank=True, null=True, verbose_name='Коэффициент Уилкса')
    country = models.CharField(max_length=32, default=True, verbose_name='Страна')
    region = models.CharField(max_length=32, default=True, verbose_name='Область/Регион')
    town = models.CharField(max_length=32, default=True, verbose_name='Город')
    line_up = models.ForeignKey(Line_up, on_delete=models.CASCADE, verbose_name='Команда/Лично')
    trainer = models.CharField(max_length=64, blank=True, verbose_name='Тренер')
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE, verbose_name='Турнир')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Дивизион')
    discipline = models.ManyToManyField(Discipline, blank=True, default=True, verbose_name='Дисциплины')
    message = models.TextField(max_length=128, blank=True, null=True, default=None, verbose_name='Сообщение')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=id(1), verbose_name='Статус')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата заявления')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования')

    @property
    def Турнир(self):
        return truncatechars(self.tournament, 50)

    @property
    def Сообщение(self):
        return truncatechars(self.message, 20)

    @property
    def Дивизион(self):
        return self.division

    @property
    def Дисциплины(self):
        return "\n".join([p.name for p in self.discipline.all()])

    @property
    def Возрастные_категории(self):
        return "\n".join([p.name for p in self.age_category.all()])

    def __str__(self):
        return "Спортсмен(ка): %s %s, почта: %s" % (self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'

    def save(self, *args, **kwargs):
        super(Athletes, self).save(*args, **kwargs)

class AthletesImage(models.Model):
    Athletes = models.ForeignKey(Athletes, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Спортсмен')
    image = models.ImageField(upload_to='athletes_images/', verbose_name='Фотография спортсмена')
    image_is_main = models.BooleanField(default=False, verbose_name='Главная')
    image_is_active = models.BooleanField(default=True, verbose_name='Актуально')
    image_created = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки фото')
    image_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования фото')

    def __str__(self):
            return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'