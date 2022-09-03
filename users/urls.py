from django.urls import path

from .views import UserList, UserDetail



app_name = 'users'

urlpatterns = [
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),

]