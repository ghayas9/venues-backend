# # """
# # URL configuration for venues project.

# # The `urlpatterns` list routes URLs to views. For more information please see:
# #     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# # Examples:
# # Function views
# #     1. Add an import:  from my_app import views
# #     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# # Class-based views
# #     1. Add an import:  from other_app.views import Home
# #     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# # Including another URLconf
# #     1. Import the include() function: from django.urls import include, path
# #     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# # """
# # # from django.contrib import admin
# # # from django.urls import path, include

# # # urlpatterns = [
# # #     path('admin/', admin.site.urls),
# # #     path('api/users/', include('apps.users.urls')),
# # #     path('api/venues/', include('apps.venues.urls')),
# # # ]


# # # from django.contrib import admin
# # # from django.urls import path, include

# # # urlpatterns = [
# # #     path('admin/', admin.site.urls),
# # #     path('api/users/', include('users.urls')),
# # #     # path('api/venues/', include('venues.urls')),
# # # ]


# # from rest_framework import permissions
# # from drf_yasg.views import get_schema_view
# # from drf_yasg import openapi

# # # Configure API schema view
# # schema_view = get_schema_view(
# #    openapi.Info(
# #       title="Venues API",
# #       default_version='v1',
# #       description="API documentation for the Venues application",
# #       terms_of_service="https://www.google.com/policies/terms/",
# #       contact=openapi.Contact(email="contact@venues.local"),
# #       license=openapi.License(name="BSD License"),
# #    ),
# #    public=True,
# #    permission_classes=(permissions.IsAuthenticated,),
# # )

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/users/', include('apps.users.urls')),  # Your users API URLs
# #     path('swagger/', schema_view.as_view(), name='swagger-docs'),  # Swagger documentation
# # ]


# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# # Define the schema view for Swagger documentation
# schema_view = get_schema_view(
#    openapi.Info(
#       title="User Management API",
#       default_version='v1',
#       description="API documentation for user management (Registration, Login, etc.)",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="ghayasudin999@mail.com"),
#       license=openapi.License(name="MIT License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/users/', include('apps.users.urls')),  # Include the user-related APIs
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),  # Another view option
# ]



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
    path('api/users/', include('apps.users.urls')),  # Users app URLs
   #  path('api/bookings/', include('apps.bookings.urls')),  # Bookings app URLs (if used)
   #  path('api/venues/', include('apps.venues.urls')),  # Venues app URLs (if used)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
