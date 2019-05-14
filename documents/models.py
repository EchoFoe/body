from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
import PIL as pillow


class Documents(models.Model):
    documents_description = models.TextField(max_length=512, blank=True, default=None, verbose_name='Описание раздела')
    documents_soglashenie = models.FileField(upload_to="documents_soglashenie", blank=True, default=None, null=None, verbose_name='Соглашение законного представителя для участия в соревнованиях gfp НЕСОВЕРШЕННОЛЕТНЕГО спортсмена')
    documents_pravila = models.FileField(upload_to="documents_pravila", blank=True, default=None, null=None,
verbose_name='Правила gfp')
    documents_normativi = models.FileField(upload_to="documents_normativi", blank=True, default=None, null=None,
verbose_name='Нормативы gfp')
    documents_is_active = models.BooleanField(default=True, verbose_name='Актуальность документов')
    documents_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания записи/загрузки документов')
    documents_updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования записи/загрузки документов')

    def __str__(self):
        return "%s" % self.documents_description

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'