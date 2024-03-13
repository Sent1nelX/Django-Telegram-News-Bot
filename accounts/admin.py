from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import CustomUser, News


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'country', 'city', 'address', 'phone_number', 'user_id', 'language_code', 'is_bot', 'latitude', 'longitude')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'image_tag')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='125px'>")
        else:
            return "No Image"
    image_tag.short_description = 'Image'


@admin.register(News)  # Регистрируем модель News в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'popular', 'date', 'time', 'created_at')  # Отображаемые поля в списке
    search_fields = ['title', 'info']  # Поля для поиска
    list_filter = ['date', 'created_at', 'popular']  # Фильтры для списка
    readonly_fields = ('created_at', 'date')  # Только для чтения
    
    fieldsets = (
        (None, {
            'fields': ('title', 'info', 'url', 'popular', 'time', 'date')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Свернуть этот блок по умолчанию
        }),
    )


