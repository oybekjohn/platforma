from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'username', 'email', 'first_name', 'last_name', 'phone', 'joined_at')
    list_display_links = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    list_per_page = 25

