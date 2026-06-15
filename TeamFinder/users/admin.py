from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User, FavoriteProject


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'surname', 'phone', 'is_active', 'is_staff', 'view_on_site')
    list_display_links = ('id', 'email')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'name', 'surname', 'phone')
    readonly_fields = ('date_joined', 'last_login', 'avatar_preview')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {
            'fields': ('name', 'surname', 'avatar', 'avatar_preview', 'phone', 'github_url', 'about')
        }),
        ('Статусы', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Права доступа', {
            'fields': ('groups', 'user_permissions')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'phone', 'password1', 'password2'),
        }),
    )
    
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.avatar.url)
        return format_html('<span style="color: gray;">Нет аватарки</span>')
    avatar_preview.short_description = 'Превью аватарки'
    
    def view_on_site(self, obj):
        return format_html('<a href="{}">Посмотреть на сайте</a>', f'/users/profile/{obj.id}/')
    view_on_site.short_description = 'Ссылка'
    
    def get_queryset(self, request):
        return super().get_queryset(request)


@admin.register(FavoriteProject)
class FavoriteProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__email', 'user__name', 'project__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'project')