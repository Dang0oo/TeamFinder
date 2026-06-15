from django.contrib import admin
from django.utils.html import format_html
from .models import Project
from constants import ADMIN_LIST_PER_PAGE


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'status', 'created_at', 'view_on_site')
    list_display_links = ('id', 'name')
    list_filter = ('status', 'created_at', 'owner')
    search_fields = ('name', 'description', 'owner__email', 'owner__name')
    readonly_fields = ('created_at',)
    list_per_page = ADMIN_LIST_PER_PAGE
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'status')
        }),
        ('Автор и участники', {
            'fields': ('owner', 'participants')
        }),
        ('GitHub', {
            'fields': ('github_url',),
            'classes': ('collapse',)
        }),
        ('Дата создания', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner').prefetch_related('participants')
    
    def view_on_site(self, obj):
        return format_html('<a href="{}">Посмотреть на сайте</a>', obj.get_absolute_url())
    view_on_site.short_description = 'Ссылка'