from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_id = models.BigIntegerField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="ID пользователя",
        help_text="Уникальный идентификатор пользователя в Telegram.",
    )
    language_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Код языка",
        help_text="Код языка, используемый пользователем в Telegram.",
    )
    is_bot = models.BooleanField(
        default=False,
        verbose_name="Бот",
        help_text="Указывает, является ли пользователь ботом.",
    )
    country = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Страна",
        help_text="Страна пользователя в Telegram.",
    )
    city = models.CharField(
        max_length=120, 
        blank=True, 
        null=True, 
        verbose_name="Город", 
        help_text="Город пользователя в Telegram.",
    )
    latitude = models.CharField(
        max_length=120, 
        blank=True, 
        null=True, 
        verbose_name="Широта", 
        help_text="Широта пользователя в Telegram.",
    )
    longitude = models.CharField(
        max_length=120, 
        blank=True, 
        null=True, 
        verbose_name="Долгота", 
        help_text="Долгота пользователя в Telegram.",
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Адрес",
        help_text="Адрес пользователя в Telegram.",
    )
    image = models.ImageField(
        upload_to='users_images/', 
        null=True, 
        blank=True,
        verbose_name="Изображение",
        help_text="Изображение пользователя."
    )
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        verbose_name="Биография", 
        help_text="Краткая информация о пользователе."
    )
    phone_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True,
        verbose_name="Номер телефона", 
        help_text="Номер телефона пользователя."
    )
    
    def __str__(self) -> str:
        if self.username:
            return self.username
        return f"{self.id}: Anonymous User"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-date_joined"]
    

class News(models.Model):
    popular = models.BooleanField(
        default=False,
        verbose_name = "Популярная",
        help_text = "Указывает, является ли новость популярной."
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Заголовок новости."
    )
    info = models.TextField(
        verbose_name="Описание",
        help_text="Описание новости."
    )
    url = models.URLField(
        verbose_name="URL",
        help_text="URL новости."
    )
    time = models.CharField(
        max_length=255,
        verbose_name="Время",
        help_text="Время новости."
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата",
        help_text="Дата новости."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания новости."
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]
