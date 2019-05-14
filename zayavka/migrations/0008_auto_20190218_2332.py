# Generated by Django 2.1.4 on 2019-02-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayavka', '0007_auto_20190218_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='trener',
            field=models.CharField(blank=True, max_length=32, verbose_name='Тренер'),
        ),
    ]
