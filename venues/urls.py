from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Venue Booking API",
        default_version='v1',
        description="API for Venue Booking System",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),  # Users app URLs
   #  path('api/bookings/', include('apps.bookings.urls')),  # Bookings app URLs (if used)
    path('api/v1/venues/', include('apps.venues.urls')),  # Venues app URLs (if used)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
