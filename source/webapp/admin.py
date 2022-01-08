from django.contrib import admin

from .models import GuestBook
# Register your models here.

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'status']
    list_filter = ['author']
    search_field = ['author', 'status']
    readonly_fields = ['created_at', 'updated_at']
    fields = ['author', 'email', 'text', 'created_at', 'updated_at', 'status']

admin.site.register(GuestBook, GuestBookAdmin)