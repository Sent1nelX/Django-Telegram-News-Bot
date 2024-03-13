# Generated by Django 5.0.2 on 2024-02-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, help_text='Адрес пользователя в Telegram.', max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, help_text='Город пользователя в Telegram.', max_length=120, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, help_text='Страна пользователя в Telegram.', max_length=120, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_bot',
            field=models.BooleanField(default=False, help_text='Указывает, является ли пользователь ботом.', verbose_name='Бот'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language_code',
            field=models.CharField(blank=True, help_text='Код языка, используемый пользователем в Telegram.', max_length=10, null=True, verbose_name='Код языка'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='latitude',
            field=models.FloatField(blank=True, help_text='Широта пользователя в Telegram.', null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='longitude',
            field=models.FloatField(blank=True, help_text='Долгота пользователя в Telegram.', null=True, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.BigIntegerField(blank=True, help_text='Уникальный идентификатор пользователя в Telegram.', null=True, unique=True, verbose_name='ID пользователя'),
        ),
    ]
