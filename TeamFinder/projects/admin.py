from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'description', 'author__username', 'author__email')
    readonly_fields = ('created_at',)
    list_per_page = 20
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'status')
        }),
        ('Автор и участники', {
            'fields': ('author', 'participants')
        }),
        ('Дата создания', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author').prefetch_related('participants')