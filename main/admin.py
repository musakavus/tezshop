from django.contrib import admin
from django.utils.text import slugify
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'created_at', 'updated_at')
    list_filter = ('parent_category', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
