from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_published', 'featured')
    list_filter = ('is_published', 'featured', 'publish_date')
    search_fields = ('title', 'description', 'content')
    readonly_fields = ('slug', 'publish_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('📝 Basic Information', {
            'fields': ('title', 'slug', 'author', 'publish_date', 'updated_date')
        }),
        ('📄 Content', {
            'fields': ('description', 'content'),
            'classes': ('wide',)
        }),
        ('🖼️ Media', {
            'fields': ('image',)
        }),
        ('🔍 SEO', {
            'fields': ('meta_title', 'meta_description', 'tags'),
            'classes': ('collapse',)
        }),
        ('📱 Open Graph', {
            'fields': ('og_title', 'og_description'),
            'classes': ('collapse',),
            'description': 'Fields for social media sharing (image is same as main image)'
        }),
        ('📌 Publishing', {
            'fields': ('is_published', 'featured')
        }),
    )
