from django.contrib import admin
from django.utils.text import slugify
from .models import Category, Country, Region, Registration
# from .models import Registration
from django.contrib.auth.hashers import make_password


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'created_at', 'updated_at')
    list_filter = ('parent_category', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name', 'email']
    fields = [
        'first_name', 'last_name', 'email', 'password', 'password_confirmation',
        'phone', 'company', 'address1', 'address2', 'city', 'postal_code', 'country', 'region',
    ]
    readonly_fields = ['password_confirmation']  # Sadece görüntüleme, düzenlenemez

    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.save()


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Registration, RegistrationAdmin)
