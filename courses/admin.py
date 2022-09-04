from django.contrib import admin

from .models import Course, Theme, CourseStudent, Purchase



class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_per_page = 25


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'course', 'title', )
    search_fields = ('course', 'title', )
    list_per_page = 25


class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'student', 'created_at', 'updated_at')
    list_display_links = ('id', 'course', 'student')
    search_fields = ('course', 'student')
    list_per_page = 25


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'course')
    search_fields = ('user', 'course')
    list_per_page = 25


admin.site.register(Course, CourseAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(CourseStudent, CourseStudentAdmin)
admin.site.register(Purchase, PurchaseAdmin)
