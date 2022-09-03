from django.contrib import admin

from .models import Course, Theme, CourseTheme, CourseTeacher, CourseStudent, Purchase



class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_per_page = 25


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    list_per_page = 25


class CourseThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'theme', 'created_at', 'updated_at')
    list_display_links = ('id', 'course', 'theme')
    search_fields = ('course', 'theme')
    list_per_page = 25


class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'teacher', 'created_at', 'updated_at')
    list_display_links = ('id', 'course', 'teacher')
    search_fields = ('course', 'teacher')
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
admin.site.register(CourseTheme, CourseThemeAdmin)
admin.site.register(CourseTeacher, CourseTeacherAdmin)
admin.site.register(CourseStudent, CourseStudentAdmin)
admin.site.register(Purchase, PurchaseAdmin)
