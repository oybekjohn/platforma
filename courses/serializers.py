from rest_framework import serializers
from .models import (   Course, 
                        Theme, 
                        CourseTheme, 
                        CourseTeacher, 
                        CourseStudent, 
                        Purchase,
                    )



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class CourseThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTheme
        fields = "__all__"


class CourseTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeacher
        fields = "__all__"


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"