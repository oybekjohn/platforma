from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Platforma API",
      default_version='v1',
      description="Platforma API",
      contact=openapi.Contact(email="test@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path("admin/", admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('api/',
        include([
            path('', include('users.urls', namespace='users')),
            path('', include('courses.urls', namespace='courses')),
        ])
    ),
    path('api-auth/', include('rest_framework.urls')),
]