from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views  # Import JWT views


schema_view = get_schema_view(
    openapi.Info(
        title="Venue Booking API",
        default_version='v1',
        description="API for Venue Booking System",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

from rest_framework_simplejwt.views import TokenRefreshView
import logging

logger = logging.getLogger(__name__)

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        logger.info(f"Received refresh token: {request.data.get('refresh')}")
        return super().post(request, *args, **kwargs)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access and refresh token
    path('api/v1/token/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('api/v1/users/', include('apps.users.urls')),  # Users app URLs
    path('api/v1/book/', include('apps.book.urls')),  # Bookings app URLs (if used)
    path('api/v1/venues/', include('apps.venues.urls')),  # Venues app URLs (if used)
     path('api/v1/dashboard/', include('apps.dashboard.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



