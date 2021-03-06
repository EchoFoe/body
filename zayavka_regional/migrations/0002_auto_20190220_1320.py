# Generated by Django 2.1.4 on 2019-02-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayavka_regional', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zayavka_regional',
            name='weight',
        ),
        migrations.AddField(
            model_name='zayavka_regional',
            name='country',
            field=models.CharField(default=True, max_length=32, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='zayavka_regional',
            name='region',
            field=models.CharField(default=True, max_length=64, verbose_name='Область/Регион'),
        ),
        migrations.AlterField(
            model_name='zayavka_regional',
            name='email',
            field=models.EmailField(default=True, max_length=64, verbose_name='Емейл'),
        ),
        migrations.AlterField(
            model_name='zayavka_regional',
            name='first_name',
            field=models.CharField(default=True, max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='zayavka_regional',
            name='last_name',
            field=models.CharField(default=True, max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='zayavka_regional',
            name='message',
            field=models.TextField(default=True, max_length=128, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='zayavka_regional',
            name='middle_name',
            field=models.CharField(default=True, max_length=64, verbose_name='Отчество'),
        ),
    ]
