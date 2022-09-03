from django.urls import path
from .views import (
                        CourseList,
                        CourseDetail,
                        ThemeList,
                        ThemeDetail,
                        CourseThemeList,
                        CourseThemeDetail,
                        PurchaseList,
                        PurchaseDetail,
                        
                    )


app_name = 'courses'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('themes/', ThemeList.as_view(), name='theme-list'),
    path('themes/<int:pk>/', ThemeDetail.as_view(), name='theme-detail'),
    path('course-themes/', CourseThemeList.as_view(), name='course-theme-list'),
    path('course-themes/<int:pk>/', CourseThemeDetail.as_view(), name='course-theme-detail'),
    path('purchases/', PurchaseList.as_view(), name='purchase-list'),
    path('purchases/<int:pk>/', PurchaseDetail.as_view(), name='purchase-detail'),

]